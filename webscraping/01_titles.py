import requests
from bs4 import BeautifulSoup
import lxml
import csv
url="https://books.toscrape.com/"    
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, "lxml")
books = soup.find_all('article', class_='product_pod')# y dekho har book ek article tag mein hai or uski class 'product_pod'
with open("webscraping/books.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price"])
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        writer.writerow([title, price])