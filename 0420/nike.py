from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url ='https://www.nike.com/tw/w/mens-apparel-6ymx6znik1'

driver = webdriver.Chrome()

driver.get(url)

titles = driver.find_elements(By.CLASS_NAME,'product-card__title')
# titles = driver.find_elements(By.CSS_SELECTOR,'.product-card__title')

for title in titles:
    print(title.text)


