from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
import time

# double click

# double_click_btn=driver.find_element(By.ID,"doubleClickBtn")

# driver.execute_script("arguments[0].scrollIntoView()",double_click_btn)

# actions.double_click(double_click_btn).perform()
# time.sleep(3)

# right click

url="https://demoqa.com/buttons"
driver.get(url)
time.sleep(3)
actions=ActionChains(driver)


right_click=driver.find_element(By.ID,"rightClickBtn")

driver.execute_script("arguments[0].scrollIntoView()",right_click)

actions.context_click(right_click).perform()

time.sleep(3)