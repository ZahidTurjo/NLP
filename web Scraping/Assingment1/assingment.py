from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
book_name1 = []
author_name1 = []
category1 = []
ratings1 = []
price1 = []

description=[]

options = Options()
options.add_argument("--headless=new")  
options.add_argument("user-agent=Mozilla/5.0")
driver = webdriver.Chrome(options=options)

url="https://www.rokomari.com/book/authors?ref=sm_p0&page=1"
driver.get(url)
time.sleep(3)

# count page number
page_num=driver.find_element(By.XPATH,'//*[@id="author-list"]/div[3]/section/div[3]/div/a[11]').text
print(page_num)


author_url=[]

# collect all the author_url

# for i in range(1,page_num+1):
#     url=f"https://www.rokomari.com/book/authors?ref=sm_p0&page={i}"
#     WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//div[@class='authorListItem']//a"))
# )
#     authors=driver.find_elements(By.XPATH,"//div[@class='authorListItem']//a")
#     for au in authors:
#         author_url.append(au.get_attribute('href'))



# collect single page author url


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='authorListItem']//a"))
)
authors=driver.find_elements(By.XPATH,"//div[@class='authorListItem']//a")
for au in authors:
    author_url.append(au.get_attribute('href'))
# print(author_url)
time.sleep(5)

# collect books url
book_url = set()

for i, auth in enumerate(author_url):
    print(i)
    driver.get(auth)
    time.sleep(3)
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.books-wrapper__item a')))
    books = driver.find_elements(By.CSS_SELECTOR, '.books-wrapper__item a')
    for book in books:
        url = book.get_attribute('href')
        
        book_url.add(url)


book_url = list(book_url)

from selenium.common.exceptions import TimeoutException
wait = WebDriverWait(driver, 10)

for i, boi in enumerate(book_url):
    print(f"Scraping book {i+1}: {boi}")
    driver.get(boi)
    time.sleep(5)
# book name
    try:
        book_tag = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[@class='bookTitle_bookName__B4CEH ']"))
        )
        book_name1.append(book_tag.text)
    except TimeoutException:
        book_name1.append('-')
   
# writer name
    try:        
        author_tag = driver.find_element(By.XPATH, "//p[@class='bookTitle_authorName__HoSND']//a")
        author_name1.append(author_tag.text)
    except NoSuchElementException:
        author_name1.append('-')
    
# category
    try:
        cat_tag=driver.find_element(By.XPATH,"//p[@class='bookCategory_category__giRM1']//a")
        category1.append(cat_tag.text)
               
    except NoSuchElementException:
        category1.append('-')   
 

# rating
    try:
        rat_tag=driver.find_element(By.XPATH,"//div[@class='detailsBookContainer_detailsContentRating__pBLi4 mt-3']//span")
        ratings1.append(rat_tag.text)
    except NoSuchElementException:
        ratings1.append('-')
  
        
# price        
    try:
        price_tag=driver.find_element(By.XPATH,"//div[@class='priceDetails_priceAndDiscount__oEFMK']//span")
        price1.append(price_tag.text)
    except NoSuchElementException:
        price1.append('-')
        
    time.sleep(1)


# description
    # try:
    #     c=driver.find_element(By.XPATH,"//button[@class='text-primary inline']")
    #     c.click()
    #     time.sleep(3)
    #     descriptions=driver.find_element(By.XPATH,'//*[@id="ts--desktop-details-book-main-info"]/div[6]/div/div/div/div[2]/div/div')
    #     description.append(descriptions.text)
    # except NoSuchElementException:
    #     description.append('-')

    print("ok!")
        
import pandas as pd    
df = pd.DataFrame({
    "Book Name": book_name1,
    "Author Name": author_name1,
    "Category": category1,
    "Rating": ratings1,
    "Price": price1
})
df.to_csv("books_data.csv", index=False, encoding='utf-8-sig')
df
print("data saved!!")
