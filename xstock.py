#! /usr/bin/env python3.6

import urllib3
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/GOOG?p=GOOG'
http = urllib3.PoolManager()
response=http.request('GET', url)
soup = BeautifulSoup(response.data)
print (soup.prettify())

# print (soup.html)
# print (soup.p)
# print (soup.find_all(id="link2"))
# print (soup.find_all(["a","b"]))
# for tag in soup.find_all(True):
# 	print("TAG: tag", tag.name())

print(soup.get_text())
