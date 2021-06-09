
import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
bs = BeautifulSoup(response.text,"html.parser")
result = bs.find_all("div",{"class":"_4rR01T"})
for data in result:
    print(data.text)
