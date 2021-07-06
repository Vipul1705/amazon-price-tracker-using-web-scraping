import requests
from bs4 import BeautifulSoup
url="https://www.amazon.in/AMD-YD2600BBAFBOX-3-9GHz-Socket-Processor/dp/B07B41WS48/ref=mp_s_a_1_1?dchild=1&keywords=ryzen+5&qid=1625394459&sr=8-1"
# url=""
def get_converted_price(price):
    stripped_price = price.strip("₹ ,")
    replaced_price = stripped_price.replace(",", "")
    find_dot = replaced_price.find(".")
    to_convert_price = replaced_price[0:find_dot]
    converted_price = int(to_convert_price)

    return converted_price

def get_link_data(url):
    headers = {
    "User-Agent" :"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Accept-Language":"en",
    }
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")
    deal = True
    name = soup.find(id="productTitle").get_text()
    name = name.strip()

    price = soup.find(id="priceblock_dealprice")
    if price is None:
            price = soup.find(id="priceblock_ourprice")
            deal = False
    price = get_converted_price(price.get_text())
    
    image_url = soup.find(id="landingImage")
    image_url =image_url.get('src')

    return name, price, image_url, deal

print(get_link_data(url))