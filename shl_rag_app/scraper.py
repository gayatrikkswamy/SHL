
import requests
from bs4 import BeautifulSoup

def scrape_shl():
    url = "https://www.shl.com/products/product-catalog/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text,"html.parser")

    data = []

    products = soup.find_all("a")

    for p in products:
        text = p.get_text(strip=True)
        if len(text) > 10:
            data.append(text)

    return data
