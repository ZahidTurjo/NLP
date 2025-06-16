import time

from selenium import webdriver
options=webdriver.FirefoxOptions()
options.add_argument("--headless")
driver=webdriver.Firefox(options=options)
url='https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php'
driver.get(url)
time.sleep(3)
title=driver.title
print(title)
time.sleep(2)