from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()

driver.get('https://www.daraz.pk/invisible-unisex-fashion-3/')

driver.maximize_window()
titles=[]
for j in range(1,71):
    driver.get(f'https://www.daraz.pk/invisible-unisex-fashion-3/?page={j}')
    print(f"page num->{j}")
    for i in range(1,41):
        num=str(i)
        title=driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+num+']/div/div/div[2]/div[2]/a').text
        titles.append(title)
        # print(f"{i}->{title}")
        # print()
print(len(titles))

