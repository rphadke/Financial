#!/usr/bin/env python3.6

import urllib
from bs4 import BeautifulSoup

page=urllib.request.urlopen("https://finance.yahoo.com/quote/%5EGSPC?p=^GSPC")
content = page.read().decode('utf-8')
soup = BeautifulSoup(content, 'html.parser')
valsp = soup.find("span", {"data-reactid": "36"}).decode_contents(formatter="html")
print(valsp)
