from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
def main():
    npr_info()
    
def npr_info():
    driver.get("https://www.npr.org/sections/news/")
    Headline1 = driver.find_element("xpath",'//*[@id="featured"]/div/article[1]/div[2]/div/h2/a')
    Headline2 = driver.find_element("xpath", '//*[@id="featured"]/div/article[2]/div[2]/div/h2/a')
    Headline3 = driver.find_element("xpath", '//*[@id="featured"]/div/article[3]/div[2]/div/h2/a')

    link1 = Headline1.get_attribute('href')
    link2 = Headline2.get_attribute('href')
    link3 = Headline3.get_attribute('href')
    
    headline_info = Headline1.text + "\n" + Headline2.text  + "\n" + Headline3.text
    print(headline_info)

main()
driver.quit()