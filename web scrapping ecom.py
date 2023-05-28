import requests
from bs4 import BeautifulSoup
import pandas as pd

# proxies = {
#     "http": "http://customer-rcodewithharry-cc-us:UCl3NtE2jXcf@pr.oxylabs.io:7777",
#     "https": "http://customer-rcodewithharry-cc-us:UCl3NtE2jXcf@pr.oxylabs.io:7777"
# }

data = {'title':[], 'price':[]}

url = "https://www.amazon.in/s?k=iphone&crid=3MD7V0OFF2COT&sprefix=iphon%2Caps%2C351&ref=nb_sb_noss_2"

# r = requests.get(url, proxies=proxies)
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price-whole")
for span in spans:
    print(span.string)
    data['title'].append(span.string)
    
symbol = soup.find(class_="a-price-symbol")

for price in prices:
    print(price.string)
    data['price'].append(symbol.string + price.string)
    if(len(data["price"]) == len(data["title"])):
        break
df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv", index=False)
# df.to_excel("data.xlsx", index=False)