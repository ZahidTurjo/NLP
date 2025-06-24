import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options

options = Options()
driver=webdriver.Firefox(options=options)
url="https://www.tutorialspoint.com/selenium/practice/frames.php"
driver.get(url)
iframe=driver.find_elements(By.TAG_NAME,"iframe")
total=len(iframe)
print(total)