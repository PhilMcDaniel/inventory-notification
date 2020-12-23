import twilio
import requests
from bs4 import BeautifulSoup
import re

#always in stock
url = 'https://www.microcenter.com/product/472489/asus-phoenix-geforce-gtx-1050-ti-single-fan-4gb-gddr5-pcie-video-card'

#not in stock
#url = 'https://www.microcenter.com/product/630684/asus-geforce-rtx-3070-tuf-overclocked-triple-fan-8gb-gddr6-pcie-40-graphics-card'
page = requests.get(url)
#page

soup = BeautifulSoup(page.text, 'html.parser')
# print out pretty version of html
# print(soup.prettify())


data = soup.find_all(type="text/javascript")[3]
dstring = data.string

match = re.search("'inStock':'True'",dstring)
if match:
    print("In stock")
else:
    print("Not in stock")