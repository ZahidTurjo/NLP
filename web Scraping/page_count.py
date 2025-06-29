import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.daraz.com.bd/catalog/?spm=a2a0e.searchlist.search.d_go.5a1924055AA4qF&q=laptop")

last_height = driver.execute_script("return document.body.scrollHeight")
print(f"last_height--->{last_height}")
time.sleep(3)
while True:
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3) 

    new_height = driver.execute_script("return document.body.scrollHeight")
    print(f"new_height-->{new_height}")
    if new_height == last_height:
        break
    last_height = new_height

time.sleep(4)
elements=driver.find_elements(By.CSS_SELECTOR,'a[href*="&page="]')

time.sleep(3)
page_num=[]
for element in elements:
    ele=element.text
    try:
        number = int(ele)
        page_num.append(number)
    except ValueError:
        print(f"Not a number: {ele}")


print(max(page_num))
 