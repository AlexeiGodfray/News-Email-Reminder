from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
import datetime
from smtp import email_logic  # Importing the email logic from smtp.py

# Setup for Selenium and WebDriver
date = datetime.datetime.now()
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--headless=new")  # For Chrome >= 109
driver = webdriver.Chrome(options=chrome_options)

def main():
    print(f"The News for {date}")
    
    # Collecting all scraped data
    scraped_info = []
    scraped_info.extend(npr_info())
    scraped_info.extend(BBC_info())
    scraped_info.extend(Yahoo())
    
    # Sending the collected info via email
    email_logic(scraped_info)

    # Quitting the driver
    driver.quit()

def npr_info():
    urls = [
        "https://www.npr.org/sections/",
        "https://www.npr.org/sections/politics/",
        "https://www.npr.org/sections/world/"
    ]
    headlines = []
    
    for url in urls:
        try:
            driver.get(url)
            Headline1 = driver.find_element(By.XPATH, '//*[@id="featured"]/div/article[1]/div[2]/div/h2/a')
            Headline2 = driver.find_element(By.XPATH, '//*[@id="featured"]/div/article[2]/div[2]/div/h2/a')
            Headline3 = driver.find_element(By.XPATH, '//*[@id="featured"]/div/article[3]/div[2]/div/h2/a')
            
            # Storing the headlines and links
            headlines.append(f"NPR Headline 1: {Headline1.text} - {Headline1.get_attribute('href')}")
            headlines.append(f"NPR Headline 2: {Headline2.text} - {Headline2.get_attribute('href')}")
            headlines.append(f"NPR Headline 3: {Headline3.text} - {Headline3.get_attribute('href')}")
            
            return headlines  # Exit once successful
        except (NoSuchElementException, TimeoutException, WebDriverException):
            continue  # Try the next URL if the current one fails
    
    headlines.append("There seems to be a problem accessing NPR at the moment.")
    return headlines

def BBC_info():
    url = "https://www.bbc.com/news"
    headlines = []
    
    try:
        driver.get(url)
        Headline1 = driver.find_element(By.XPATH, '//*[@id="main-content"]/article/section[1]/div/div/div[1]/div/div/div[1]/a/div/div[2]/div[1]/div/h2')
        link1 = driver.find_element(By.XPATH, '//*[@id="main-content"]/article/section[1]/div/div/div[1]/div/div/div[1]/a').get_attribute("href")
        headlines.append(f"BBC Headline 1: {Headline1.text} - {link1}")
    except (NoSuchElementException, TimeoutException, WebDriverException):
        headlines.append(f"Front Page Article from {url} can't be loaded")

    try:
        Headline2 = driver.find_element(By.XPATH, '//*[@id="main-content"]/article/section[1]/div/div/div[2]/div/div/a/div/div[2]/div[1]/div/h2')
        link2 = driver.find_element(By.XPATH, '//*[@id="main-content"]/article/section[1]/div/div/div[2]/div/div/a').get_attribute("href")
        headlines.append(f"BBC Headline 2: {Headline2.text} - {link2}")
        
        Headline3 = driver.find_element(By.XPATH, '//*[@id="main-content"]/article/section[1]/div/div/div[4]/div[1]/div/a/div/div/div[1]/div/h2')
        link3 = driver.find_element(By.XPATH, '//*[@id="main-content"]/article/section[1]/div/div/div[4]/div[1]/div/a').get_attribute("href")
        headlines.append(f"BBC Headline 3: {Headline3.text} - {link3}")
    except (NoSuchElementException, TimeoutException, WebDriverException):
        headlines.append("There was an error accessing the two side articles")

    return headlines

def Yahoo():
    headlines = []
    
    try:
        driver.get('https://finance.yahoo.com/quote/%5EGSPC/')
        indexName500 = driver.find_element(By.XPATH, '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[1]/div/section/h1')
        marketPrice500 = driver.find_element(By.XPATH, '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/fin-streamer[1]/span')
        indexChange500 = driver.find_element(By.XPATH, '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/fin-streamer[2]/span')
        marketPercentage = driver.find_element(By.XPATH, '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/fin-streamer[3]')
        marketPercentageValue = marketPercentage.get_attribute("data-value")
        
        headlines.append(f"{indexName500.text}: {marketPrice500.text} ({indexChange500.text}, {marketPercentageValue}%)")
        
        driver.get('https://finance.yahoo.com/quote/%5EIXIC/')
        indexNameNas = driver.find_element(By.XPATH, '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[1]/div/section/h1')
        marketPriceNas = driver.find_element(By.XPATH, '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/fin-streamer[1]/span')
        indexChangeNas = driver.find_element(By.XPATH, '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/fin-streamer[2]/span')
        marketPercentageNas = driver.find_element(By.XPATH, '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/fin-streamer[3]')
        marketPercentageValueNas = marketPercentageNas.get_attribute("data-value")
        
        headlines.append(f"{indexNameNas.text}: {marketPriceNas.text} ({indexChangeNas.text}, {marketPercentageValueNas}%)")
    except (NoSuchElementException, TimeoutException, WebDriverException):
        headlines.append("The S&P 500 or NASDAQ cannot be accessed from Yahoo Finance.")

    return headlines

# Run the main function
main()
