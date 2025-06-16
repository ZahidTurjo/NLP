
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")
time.sleep(2)
driver.find_element(By.ID,"user-name").send_keys("problem_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//a[@id='logout_sidebar_link']").click()
time.sleep(3)