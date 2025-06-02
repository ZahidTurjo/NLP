from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
import time

url="https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php"
driver.get(url)

checkbox=driver.find_element(By.ID,'hobbies')
time.sleep(3)
if not checkbox.is_selected():
    checkbox.click()
    time.sleep(5)