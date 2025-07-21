from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://books.toscrape.com/catalogue/page-1.html"

response = requests.get(url)

if response.status_code == 200:
    with open("page_1.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("✅ Page 1 saved as 'page_1.html'")
else:
    print(f"❌ Failed to fetch the page. Status code: {response.status_code}")

