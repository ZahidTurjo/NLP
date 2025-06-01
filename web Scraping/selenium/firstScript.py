from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser=webdriver.Chrome()
browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print("Open Browser")
time.sleep(3)
title=browser.title
print(title)

usernmae=browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
usernmae.send_keys("Admin")
userpass=browser.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
userpass.send_keys("admin123")
time.sleep(7)