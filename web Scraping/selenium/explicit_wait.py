import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options

options = Options()
driver=webdriver.Firefox(options=options)
url="https://bstackdemo.com/"
driver.get(url)

driver.find_element(By.XPATH,"//div[@id='3']//div[@class='shelf-item__buy-btn'][normalize-space()='Add to cart']").click()

element=WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,"//div[@class='buy-btn']"))
)
time.sleep(3)
element.click()

time.sleep(4)
driver.quit()