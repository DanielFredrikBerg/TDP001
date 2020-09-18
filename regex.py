import re
import urllib.request

with open('index.html', 'r') as web_page:
    html_text = web_page.read()
    print(html_text)
