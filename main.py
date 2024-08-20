from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless=new") # for Chrome >= 109
driver = webdriver.Chrome(options=chrome_options)

def main():
    npr_info()
    BBC_info()

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
        return
    except (NoSuchElementException, TimeoutException, WebDriverException):
        print("There was an error accessing the two side articles")

main()
driver.quit()