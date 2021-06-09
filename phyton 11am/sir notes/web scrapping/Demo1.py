
from bs4 import BeautifulSoup

html_string = '''<html>
    <head></head>
    <body>
        <h1>Welcome to HTML</h1>
        <h1>Welcome to Web Scrapping</h1>
        <h1>Welcome to Both</h1>
    </body>
</html>'''

bs = BeautifulSoup(html_string,"html.parser")
result = bs.find("h1").text
print(result)
result1 = bs.find("h1").text
print(result1)