from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
import time

chrome_options = Options()
#ad block may influence the site interaction
chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless=new") # for Chrome >= 109
driver = webdriver.Chrome(options=chrome_options)

def main():
    print("The News for ")
    npr_info()
    BBC_info()
    Yahoo()

def npr_info():
    urls = [
        "https://www.npr.org/sections/",
        "https://www.npr.org/sections/politics/",
        "https://www.npr.org/sections/world/"
    ]

    for url in urls:
        try:
            driver.get(url)
            Headline1 = driver.find_element("xpath", '//*[@id="featured"]/div/article[1]/div[2]/div/h2/a')
            Headline2 = driver.find_element("xpath", '//*[@id="featured"]/div/article[2]/div[2]/div/h2/a')
            Headline3 = driver.find_element("xpath", '//*[@id="featured"]/div/article[3]/div[2]/div/h2/a')
            # Print or return the headlines if successful
            print(f"Headlines from {url}:")
            print(Headline1.text)
            link1 = Headline1.get_attribute('href')
            print(link1)
            print(Headline2.text)
            link2 = Headline2.get_attribute('href')
            print(link2)
            print(Headline3.text)
            link3 = Headline3.get_attribute('href')
            print(link3)
            print("\n")
            return #exists once successful 
        except (NoSuchElementException, TimeoutException, WebDriverException):
            #print(f"Trouble accessing {url}, trying next link.")
            pass
    print("There seems to be a problem accessing NPR at the moment.")

#Web Scrapping Portion for The BBC
def BBC_info():
    url = "https://www.bbc.com/news"
    #we need a try catch statement for the main story as sometimes it maybe a live link, which changes the structure of the DOM
    try:
        driver.get(url)
        Headline1 = driver.find_element("xpath", '//*[@id="main-content"]/article/section[1]/div/div/div[1]/div/div/div[1]/a/div/div[2]/div[1]/div/h2')
        link1 = driver.find_element("xpath", '//*[@id="main-content"]/article/section[1]/div/div/div[1]/div/div/div[1]/a')
        link1 = link1.get_attribute("href")
        print(Headline1.text)
        print(link1)
    except (NoSuchElementException, TimeoutException, WebDriverException):
        print(f"Front Page Article from {url}, can't be loaded")

    #try catch for the Side Stories
    try:
        driver.get(url)
        Headline2 = driver.find_element("xpath", '//*[@id="main-content"]/article/section[1]/div/div/div[2]/div/div/a/div/div[2]/div[1]/div/h2')
        link2 = driver.find_element("xpath", '//*[@id="main-content"]/article/section[1]/div/div/div[2]/div/div/a')
        link2 = link2.get_attribute("href")
        print(Headline2.text)
        print(link2)
        Headline3 = driver.find_element("xpath", '//*[@id="main-content"]/article/section[1]/div/div/div[4]/div[1]/div/a/div/div/div[1]/div/h2')
        link3 = driver.find_element("xpath", '//*[@id="main-content"]/article/section[1]/div/div/div[4]/div[1]/div/a')
        link3 = link3.get_attribute("href")
        print(Headline3.text)
        print(link3)
    except (NoSuchElementException, TimeoutException, WebDriverException):
        print("There was an error accessing the two side articles")

    print("\n" + "\n")

#Yahoo stock markt Information 
def Yahoo():
    driver.get('https://finance.yahoo.com/quote/%5EGSPC/')
    try:
        indexName500 = driver.find_element("xpath", '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[1]/div/section/h1')
        print(indexName500.text)
        marketPrice500 = driver.find_element("xpath", '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/fin-streamer[1]/span')
        print(marketPrice500.text)
        indexChange500 = driver.find_element("xpath", '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/fin-streamer[2]/span')
        print(indexChange500.text)
        marketPercentage = driver.find_element("xpath", '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/fin-streamer[3]')
        marketPercentageValue = marketPercentage.get_attribute("data-value")
        print(marketPercentageValue)
        print("\n" + "\n")

        driver.get('https://finance.yahoo.com/quote/%5EIXIC/')
        indexNameNas = driver.find_element("xpath", '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[1]/div/section/h1')
        print(indexNameNas.text)
        marketPriceNas = driver.find_element("xpath", '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/fin-streamer[1]/span')
        print(marketPriceNas.text)
        indexChangeNas = driver.find_element("xpath", '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/fin-streamer[2]/span')
        print(indexChangeNas.text)
        marketPercentageNas = driver.find_element("xpath", '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section/div[1]/fin-streamer[3]')
        marketPercentageValueNas = marketPercentageNas.get_attribute("data-value")
        print(marketPercentageValueNas)
    except:
        print("The S&P 500 can not be accessed from Yahoo Finance.")

main()
driver.quit()