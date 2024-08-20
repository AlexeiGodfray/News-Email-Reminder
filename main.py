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
            return #exists once successful 
        except (NoSuchElementException, TimeoutException, WebDriverException):
            #print(f"Trouble accessing {url}, trying next link.")
            pass
    
    print("There seems to be a problem accessing NPR at the moment.")

def BBC_info():
    #we need a try catch statement since the BBC may use a live link, or a internal link for the first few articles
    driver.get("https://www.bbc.com/news")
    Headline1 = driver.find_element("xpath", '//*[@id="main-content"]/article/section[1]/div/div/div[1]/div/div/div[1]/a/div/div[2]/div[1]/div/h2')
    Headline2 =  
    print(Headline1.text)
main()
driver.quit()