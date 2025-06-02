from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
import time


url="https://the-internet.herokuapp.com/jqueryui/menu"
driver.get(url)
time.sleep(3)
hover=driver.find_element(By.CSS_SELECTOR,"#ui-id-3 > a")
menu=driver.find_element(By.CSS_SELECTOR,"#ui-id-8 > a")
time.sleep(3)
action=ActionChains(driver)
action.move_to_element(hover)
action.perform()
time.sleep(3)
menu=driver.find_element(By.CSS_SELECTOR,"#ui-id-8 > a")
menu.click()
time.sleep(3)