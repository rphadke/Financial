#!/usr/bin/python

import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

req = urllib.request.Request('https://finance.yahoo.com/quote/TSLA?p=TSLA')
response = urllib.request.urlopen(req)

# try: response = urllib.request.urlopen(req)
html = response.read()

print (html)

