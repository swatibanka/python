
import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.sathyatech.com/")
bs = BeautifulSoup(response.text,"html.parser")

result = bs.find("h2",{"class":"vc_custom_heading"}).text
print(result)

result_2 = bs.find_all("h4",{"class":"eltdf-cli-title entry-title"})
for x in result_2:
    print(x.text)

