from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.daraz.com.bd/routers/cudy-124177424/')

driver.maximize_window()
title=driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/a').text
image=driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div[1]/div/div/div[1]/div/a/div/img').get_attribute('src')

print(title)
print(image)

response=requests.get(image)
if response.status_code == 200:
    with open("image.jpg","wb") as f:
        f.write(response.content)
else:
    print(f"error:-:{response.status_code}")

time.sleep(6)