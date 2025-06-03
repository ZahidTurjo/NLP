from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
url="https://the-internet.herokuapp.com/drag_and_drop"
driver.get(url)
driver.maximize_window()
time.sleep(3)

source=driver.find_element(By.ID,"column-a")
destination=driver.find_element(By.ID,"column-b")

action=ActionChains(driver)
action.drag_and_drop(source,destination).perform()

time.sleep(3)