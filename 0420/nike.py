from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url ='https://www.nike.com/tw/w/mens-shoes-nik1zy7ok'

driver = webdriver.Chrome()

driver.get(url)

n = 0
while n < 3:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight - 1000)')
    time.sleep(3)
    n += 1

titles = driver.find_elements(By.CLASS_NAME,'product-card__title')
# titles = driver.find_elements(By.CSS_SELECTOR,'.product-card__title')


time.sleep(3)

for title in titles:
    print(title.text)


