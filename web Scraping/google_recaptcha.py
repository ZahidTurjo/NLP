from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()

url="https://practicetestautomation.com/practice-test-login/"

driver.get(url)
print("Open Browser")

title=driver.title
print(title)
driver.maximize_window()
username=driver.find_element(By.NAME,"username")
username.send_keys("student")

userpass=driver.find_element(By.NAME,"password")
userpass.send_keys("Password123")

submit=driver.find_element(By.ID,"submit")
submit.click()

logOut=driver.find_element(By.LINK_TEXT,"Log out")
logOut_text=logOut.text

Expected_text="Log out"

if(logOut_text==Expected_text):
    print("Successfully logged in")
else:
    print("Error")

time.sleep(10)