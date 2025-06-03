from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from selenium.webdriver import ActionChains

driver=webdriver.Firefox()
url="https://qa-automation-practice.netlify.app/radiobuttons"
driver.get(url)
time.sleep(3)
driver.find_element(By.ID,"radio-button1").click()
time.sleep(3)