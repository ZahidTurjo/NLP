from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
import time


url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
time.sleep(3)

driver.switch_to.new_window()
time.sleep(2)
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(3)

total_tabs=len(driver.window_handles)
print(total_tabs)