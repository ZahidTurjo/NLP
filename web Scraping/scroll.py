from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get('https://www.daraz.com.bd/products/-i345148524-s1687348589.html')

driver.maximize_window()

driver.refresh()

height=driver.execute_script('return document.body.scrollHeight')

print(height)

for i in range(0,height+1100,60):
    driver.execute_script(f'window.scrollTo(0,{i})')
    time.sleep(2)

comments=driver.find_elements(By.CLASS_NAME,'content')

commentList=[]

for comment in comments:
    commentList.append(comment.text)
    print(f'->{comment.text}')
    print()
print(len(commentList))
time.sleep(10)