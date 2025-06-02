from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()

url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver.get(url)

time.sleep(3)

driver.find_element(By.CSS_SELECTOR,"#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.orangehrm-login-forgot > p").click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)

driver.close()