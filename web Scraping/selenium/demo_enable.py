from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
url="https://training.openspan.com/login"
driver.get(url)
element1=driver.find_element(By.ID,"login_button").is_enabled()
print(element1)
time.sleep(3)
usernm=driver.find_element(By.ID,"user_name")
usernm.send_keys("abcd")
userpas=driver.find_element(By.ID,"user_pass")
userpas.send_keys(1223421)

element2=driver.find_element(By.ID,"login_button").is_enabled()
print(element2)
time.sleep(2)
btn=driver.find_element(By.ID,"login_button")
btn.click()
time.sleep(2)