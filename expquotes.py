#! /usr/bin/env python3.6

import urllib3
from bs4 import BeautifulSoup

# url = 'https://finance.yahoo.com/quote/GOOG?p=GOOG'
url = 'https://finance.yahoo.com/quote/GOOG/options?p=GOOG'

http = urllib3.PoolManager()

response = http.request('GET', url)

soup = BeautifulSoup(response.data.decode('utf-8'))

print (soup)

