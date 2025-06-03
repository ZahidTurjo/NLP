from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
url="https://seleniumbase.io/demo_page"
driver.get(url)
time.sleep(3)
element=driver.find_element(By.TAG_NAME,"h1")
element.screenshot(".\\screenshot.png")
time.sleep(2)
driver.get_screenshot_as_file(".\\screenshot1.png")
time.sleep(3)