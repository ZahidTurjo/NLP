
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/select-menu.php")
time.sleep(2)

box=driver.find_element(By.CSS_SELECTOR,"#mbsc-control-0 > div > label > span.mbsc-ios.mbsc-ltr.mbsc-textfield-inner.mbsc-textfield-inner-outline.mbsc-textfield-inner-stacked.mbsc-textarea-inner.mbsc-textfield-tags-inner > span.mbsc-textfield-tags.mbsc-ios.mbsc-ltr.mbsc-textfield.mbsc-textfield-outline.mbsc-select.mbsc-textfield-stacked.mbsc-textfield-outline-stacked.mbsc-textarea")
box.click()
element1=driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[41]")
element1.click()
time.sleep(3)
element2=driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[42]")
element2.click()
time.sleep(3)