import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


options = Options()
driver = webdriver.Firefox(options=options)
driver.get("https://www.google.com/maps/search/laptop+shop+near+me/@22.877761,91.0840244,13.25z?entry=ttu&g_ep=EgoyMDI1MDUyOC4wIKXMDSoASAFQAw%3D%3D")


time.sleep(5)


try:
    scrollable_div = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]')
except:
    print("Could not find the sidebar")
    driver.quit()
    exit()

for _ in range(50):
    scrollable_div.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

divs=driver.find_elements(By.CLASS_NAME,"hfpxzc")
data=[]

for div in divs:
    name = div.get_attribute('aria-label')
    if name:
        name = name.split("·")[0].strip()
    else:
        name = div.text.strip()
    
    url = div.get_attribute('href')

    if name and url:
        data.append({
            'restaurant_name': name,
            'location_url': url
        })

import pandas as pd
df=pd.DataFrame(data)
df.to_csv("laptopShop_in_noakhali.csv")


print(df.shape)
