from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()

url="https://the-internet.herokuapp.com/dropdown"
driver.get(url)

# select option by visible text
dropdown=driver.find_element(By.ID,"dropdown")

select=Select(dropdown)
# select.select_by_visible_text("Option 1")

# # select by value
# select.select_by_value("2")

# select by index
select.select_by_index(1)

time.sleep(4)