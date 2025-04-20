from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://google.com'
driver.get(url)
time.sleep(2)
search = driver.find_element(By.CLASS_NAME,'gLFyf')
time.sleep(1)
search.send_keys('午')
time.sleep(2)
search.send_keys('餐')
time.sleep(3)
search.send_keys(Keys.ENTER)
time.sleep(20)