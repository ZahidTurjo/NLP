
from bs4 import BeautifulSoup
import requests



url="https://www.amazon.in/Apple-Headphones-Cancellation-Transparency-Personalised/dp/B0DGJ7S59D/ref=sr_1_4?crid=RBARZ970AYJI&dib=eyJ2IjoiMSJ9.y08pMqaeTlUXGU64oyMGlx8v2Sx78yzGgsFfSLyufaCZhsU6s-KsHLVTWzO21l030BNAPdSwF1uvk-xP2xiYHOrOsuJoyUXTbtnLlKohg0PDfeDV2ow3KJTID02CZHFHe8BElHxz0Qx9AFS7cgOtkIB0SiGqovUlX53vpFMVfDlFCxKDYYyYS0xwojJ1zvN8J-uZuRvzI8Bf-RrBv58giQ5qGy-67sptz4v75mHE4Wo.tSxthxJx5H1i4-8rVzEb4sSrmXDaiOyiNDov_Gs8y5U&dib_tag=se&keywords=apple%2Bairpods%2Bpro%2Bmax&nsdOptOutParam=true&qid=1736429886&sprefix=%2Caps%2C209&sr=8-4&th=1"

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}

response=requests.get(url,headers=headers)


if response.status_code==200:
    html_content=response.text
else:
    print(f'error-->{response.status_code}')


# print(html_content)

soup=BeautifulSoup(html_content,'lxml')
# print(soup.prettify())

product_title=soup.find("span",id="productTitle").text.strip()

product_price=soup.find("span",class_="a-price-whole").text.strip()

product_rating=soup.find("span",class_="a-size-base a-color-base").text.strip()
product_bp=soup.find("ul",class_="a-unordered-list a-vertical a-spacing-mini").text.strip()
product_des=soup.find("div",id="productDescription").text.strip()
reviews=soup.find("ul",id="cm-cr-dp-review-list").text.strip()

# print(reviews)

import csv
# with open("amazon_headPhn data.csv",mode='w',newline='', encoding="utf-8")as f:
#     writer=csv.writer(f)
#     writer.writerow(["product_title", "product_price", "product_rating", "product_bp", "product_description", "reviews"])

#     writer.writerow([product_title, product_price, product_rating, product_bp, product_des, reviews])


print("All Ok!")