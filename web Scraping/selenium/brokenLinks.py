from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
import time
import requests


url="https://jquery.com/"
driver.get(url)
time.sleep(3)
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))

for link in links:
    l=link.get_attribute('href')
    response=requests.get(l)
    if response.status_code>=400:
        print(f'broken links->{l}')
