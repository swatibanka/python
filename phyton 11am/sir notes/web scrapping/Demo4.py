from bs4 import BeautifulSoup
html_string = '''<html>
    <head></head>
    <body>
        <h1 class="my_bg_color" id="first">Welcome to HTML</h1>
        <h1 class="one" id="second">Welcome to Web Scrapping</h1>
        <h1 class="my_bg_color" id="three">Welcome to Both</h1>
    </body>
</html>'''
bs = BeautifulSoup(html_string,"html.parser")

result = bs.find("h1",{"id":"three"}).text

print(result)