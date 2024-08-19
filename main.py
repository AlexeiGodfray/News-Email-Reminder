from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://www.npr.org/sections/news/")
Headline1 = driver.find_element("xpath",'//*[@id="featured"]/div/article[1]/div[2]/div/h2/a')
Headline2 = driver.find_element("xpath", '//*[@id="featured"]/div/article[2]/div[2]/div/h2/a')

aTag1 = driver.find_element("xpath", '//*[@id="featured"]/div/article[1]/div[2]/div/h2/a')
aTag2 = driver.find_element("xpath", )
link1 = aTag1.get_attribute('href')


print(Headline2.text)

driver.quit()