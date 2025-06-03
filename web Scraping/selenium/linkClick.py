from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
url="https://demo.guru99.com/"
driver.get(url)
driver.maximize_window()
time.sleep(3)
link=driver.find_element(By.LINK_TEXT,"Bank Project")

link.click()

time.sleep(3)
