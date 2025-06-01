from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.amazon.com/s?k=laptop%22&ref=nb_sb_noss')
driver.maximize_window()
title=driver.find_element(By.XPATH,'//*[@id="7b7b757c-c9bb-4804-a140-ade670f2d616"]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/a/h2/span').text

print(title)
time.sleep(15)
