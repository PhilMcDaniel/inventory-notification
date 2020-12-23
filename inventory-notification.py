from twilio.rest import Client
import config
import requests
from bs4 import BeautifulSoup
import re

# twilio authentication
account_sid = config.account_sid
auth_token = config.auth_token
client = Client(account_sid, auth_token)

urls = []
urls.append('https://www.microcenter.com/product/628318/asus-geforce-rtx-3080-tuf-gaming-overclocked-triple-fan-10gb-gddr6x-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/630201/msi-geforce-rtx-3070-gaming-x-trio-triple-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/628346/evga-geforce-rtx-3080-ftw3-ultra-gaming-triple-fan-10gb-gddr6x-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/628303/asus-geforce-rtx-3080-tuf-gaming-triple-fan-10gb-gddr6x-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/630684/asus-geforce-rtx-3070-tuf-overclocked-triple-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/628686/asus-geforce-rtx-3080-strix-overclocked-triple-fan-10gb-gddr6x-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/631469/asus-geforce-rtx-3060-ti-tuf-gaming-overclocked-triple-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/628330/msi-geforce-rtx-3080-gaming-x-trio-triple-fan-10gb-gddr6x-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/631321/asus-geforce-rtx-3070-ko-overclocked-dual-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/630578/evga-geforce-rtx-3070-xc3-ultra-gaming-triple-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/630577/evga-geforce-rtx-3070-ftw3-ultra-gaming-triple-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/630686/asus-geforce-rtx-3070-rog-strix-overclocked-dual-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/628344/evga-geforce-rtx-3080-xc3-ultra-gaming-triple-fan-10gb-gddr6x-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/630682/asus-geforce-rtx-3070-dual-overclocked-dual-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/631319/gigabyte-geforce-rtx-3070-aorus-master-overclocked-triple-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/628331/msi-geforce-rtx-3080-ventus-3x-overclocked-triple-fan-10gb-gddr6x-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/631473/asus-geforce-rtx-3060-ti-dual-overclocked-dual-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/629693/gigabyte-geforce-rtx-3080-vision-overclocked-triple-fan-10gb-gddr6x-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/628609/zotac-geforce-rtx-3080-trinity-overclocked-triple-fan-10gb-gddr6x-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/631532/msi-geforce-rtx-3060-ti-ventus-2x-overclocked-dual-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/630680/asus-geforce-rtx-3070-dual-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/630033/gigabyte-geforce-rtx-3070-gaming-overclocked-triple-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/630034/gigabyte-geforce-rtx-3070-eagle-overclocked-triple-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/631533/msi-geforce-rtx-3080-suprim-x-overclocked-triple-fan-10gb-gddr6x-pcie-40-graphics-car?storeid=045d')
urls.append('https://www.microcenter.com/product/631474/asus-geforce-rtx-3060-ti-ko-overclocked-dual-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/631741/gigabyte-geforce-rtx-3060-ti-gaming-pro-overclocked-triple-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/629691/gigabyte-geforce-rtx-3080-aorus-m-overclocked-triple-fan-10gb-gddr6x-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/631742/gigabyte-geforce-rtx-3060-ti-gaming-overclocked-triple-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/630202/msi-geforce-rtx-3070-ventus-3x-overclocked-triple-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/630203/msi-geforce-rtx-3070-ventus-2x-overclocked-dual-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/631927/evga-geforce-rtx-3060-ti-xc-gaming-dual-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/631531/msi-geforce-rtx-3060-ti-gaming-x-trio-triple-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/630806/asus-geforce-rtx-2060-rog-strix-evo-overclocked-triple-fan-6gb-gddr6-pcie-30-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/632001/asus-nvidia-geforce-rtx-3070-rog-strix-white-overclocked-triple-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/631926/evga-geforce-rtx-3060-ti-ftw-ultra-gaming-triple-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
urls.append('https://www.microcenter.com/product/628342/gigabyte-geforce-rtx-3080-gaming-overclocked-triple-fan-10gb-gddr6x-pcie-40-graphics-card?storeid=045')

#test that is definitely instock locally
#urls.append('https://www.microcenter.com/product/618532/asus-radeon-rx-5700-xt-rog-strix-overclocked-triple-fan-8gb-gddr6-pcie-40-graphics-card?storeid=045')
#url = urls[0]

instock = False
for url in urls:
    page = requests.get(url)
    #page

    soup = BeautifulSoup(page.text, 'html.parser')
    # print out pretty version of html
    # print(soup.prettify())

    #this location is a datalayer json that contains information about the product
    data = soup.find_all(type="text/javascript")[3]
    dstring = data.string
    #print(dstring)

    #get title for more detailed SMS and print
    title = soup.title.text
    title = title.replace("\r","").replace("\n","").replace("\t","")

    #this checks to see if the item is in-stock
    match = re.search("'inStock':'True'",dstring)
    if match:
        instock = True
        #print(instock)
        print(f"In stock: {title}")
        message = client.messages \
                    .create(
                        body=f"In stock: {title}\r\n {url}",
                        from_= config.from_number,
                        to = config.to_number
                    )
    else:
        print(f"Not in stock: {title}")
        #print(instock)

#send text if all were checked and none were instock
#print(instock)
#if instock == False:
#    message = client.messages \
#                    .create(
#                        body=f"None of the listed items are in stock",
#                        from_= config.from_number,
#                        to = config.to_number
#                    )