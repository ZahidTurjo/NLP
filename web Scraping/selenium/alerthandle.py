from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
import time


url="https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)
time.sleep(3)
# alert=driver.find_element(By.CSS_SELECTOR,"#content > div > ul > li:nth-child(1) > button")
# alert.click()
# time.sleep(3)
# alert_driver=driver.switch_to.alert

# print(alert_driver.text)
# time.sleep(3)
# alert_driver.accept()

# alert_btn=driver.find_element(By.CSS_SELECTOR,"#content > div > ul > li:nth-child(2) > button")
# alert_btn.click()
# time.sleep(3)
# alert=driver.switch_to.alert

# print(alert.text)
# time.sleep(3)
# alert.dismiss()

# time.sleep(3)

alert_btn=driver.find_element(By.CSS_SELECTOR,"#content > div > ul > li:nth-child(3) > button")
alert_btn.click()
time.sleep(3)

alert=driver.switch_to.alert

print(alert.text)
time.sleep(2)
alert.send_keys("Yes turjo is the boss")
time.sleep(5)
alert.accept()
time.sleep(3)
