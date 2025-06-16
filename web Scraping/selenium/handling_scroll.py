
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.maveryx.com/maveryx/")
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(3)

driver.execute_script("window.scrollTo(0,0)")
time.sleep(3)