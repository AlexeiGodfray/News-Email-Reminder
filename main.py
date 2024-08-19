from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless=new") # for Chrome >= 109
driver = webdriver.Chrome(options=chrome_options)

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
    
    headline_info = "NPR:"+ "\n" + Headline1.text +"\n" + link1 + "\n" + Headline2.text +"\n" + link2 + "\n" + Headline3.text +"\n" + link3 
    print(headline_info)

main()
driver.quit()