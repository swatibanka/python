from bs4 import BeautifulSoup
html_string = '''<html>
    <head></head>
    <body>
        <h1 class="my_bg_color">Welcome to HTML</h1>
        <h1 class="one">Welcome to Web Scrapping</h1>
        <h1 class="my_bg_color">Welcome to Both</h1>
    </body>
</html>'''
bs = BeautifulSoup(html_string,"html.parser")

result = bs.find("h1",{"class":"one"}).text

print(result)