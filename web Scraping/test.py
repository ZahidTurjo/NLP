from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.daraz.com.bd/routers/cudy-124177424/')
driver.maximize_window()
title=driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/a').text
link=driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/a').get_attribute('href')
print(title,link)
time.sleep(7)