#! /usr/bin/env python3.6

import urllib3
from bs4 import BeautifulSoup
from html.parser import HTMLParser
url='http://www.google.com'
http=urllib3.PoolManager()
response=http.request('GET',url)
###soup=BeautifulSoup(response.data)
soup=BeautifulSoup(response.data,"html.parser")
print(soup.title)
### print(soup)
###RSP soup=BeautifulSoup(response.data,"html_parser")
###RSP soup=BeautifulSoup(response.data)
###RSP print(soup)
###RSP class MyHTMLParser(HTMLParser):
###RSP     def handle_starttag(self, tag, attrs):
###RSP         print("Start tag:", tag)
###RSP         for attr in attrs:
###RSP             print("     attr:", attr)
###RSP     def handle_endtag(self, tag):
###RSP         print("End tag  :", tag)
###RSP     def handle_data(self, data):
###RSP         print("Data     :", data)
###RSP     def handle_comment(self, data):
###RSP         print("Comment  :", data)
###RSP     def handle_entityref(self, name):
###RSP         c = chr(name2codepoint[name])
###RSP         print("Named ent:", c)
###RSP     def handle_charref(self, name):
###RSP         if name.startswith('x'):
###RSP             c = chr(int(name[1:], 16))
###RSP         else:
###RSP             c = chr(int(name))
###RSP         print("Num ent  :", c)
###RSP     def handle_decl(self, data):
###RSP         print("Decl     :", data)
###RSP parser = MyHTMLParser()
###RSP soup=BeautifulSoup(response.data)
###RSP print(soup)
###RSP print(soup.parser)
###RSP print(soup.feed)
###RSP from urllib.parse import urlparse
###RSP print(soup.prettify())
###RSP print title
###RSP print soup.p
###RSP print (soup.p)
###RSP print (soup.title)
###RSP url='https://finance.yahoo.com/quote/GOOG?p=GOOG'
###RSP html=urllib3.urlopen(url)
###RSP html=urllib.urlopen(url)
###RSP html=urllib2.urlopen(url)
###RSP import urllib2
###RSP html=urllib2.urlopen(url)
###RSP http=urllib3.PoolManager()
###RSP response=http.request('GET',url)
###RSP soup=BeautifulSoup(response.data)
###RSP print(soup.prettify())
###RSP print (soup.script)
###RSP print (soup.quote)
###RSP print (soup.quotes)
###RSP quit
###RSP quit()
###RSP from googlefinance import getQuotes
###RSP import json
###RSP print json.dumps(getQuotes('AAPL'), indent=2)
###RSP print (json.dumps(getQuotes('AAPL'), indent=2))
###RSP quit
###RSP quit()
###RSP from googlefinance import getQuotes
###RSP import json
###RSP print (json.dumps(getQuotes('AAPL'), indent=2))
###RSP import urllib3
###RSP print (json.dumps(getQuotes('AAPL'), indent=2))
###RSP import urllib
###RSP print (json.dumps(getQuotes('AAPL'), indent=2))
###RSP quit()
###RSP from googlefinance import getQuotes
###RSP import json
###RSP print json.dumps(getQuotes('AAPL'), indent=2)
###RSP print (json.dumps(getQuotes('AAPL'), indent=2))
###RSP quit
###RSP quit()
###RSP from bs4 import BeautifulSoup
###RSP import urllib2
###RSP url = 'http://www.thefamouspeople.com/singers.php'
###RSP html = urllib2.urlopen(url)
###RSP soup = BeautifulSoup(html)
###RSP html = urllib.urlopen(url)
###RSP html = urllib3.urlopen(url)
###RSP quit()
###RSP from bs4 import BeautifulSoup
###RSP import urllib2
###RSP url = 'http://www.thefamouspeople.com/singers.php'
###RSP html = urllib2.urlopen(url)
###RSP soup = BeautifulSoup(html)
###RSP html = urllib.urlopen(url)
###RSP html = urllib3.urlopen(url)
###RSP import urllib3
###RSP html = urllib3.urlopen(url)
###RSP from urllib import urlopen
###RSP from bs4 import BeautifulSoup
###RSP import urllib3
###RSP http = urllib3.PoolManager()
###RSP url = 'http://www.thefamouspeople.com/singers.php'
###RSP response = http.request('GET', url)
###RSP soup = BeautifulSoup(response.data);
###RSP import urllib3
###RSP from bs4 import BeautifulSoup
###RSP url = 'http://www.thefamouspeople.com/singers.php'
###RSP http = urllib3.PoolManager()
###RSP response = http.request('GET', url)
###RSP soup = BeautifulSoup(response.data.decode('utf-8'))
###RSP print (soup)
###RSP url = 'https://finance.yahoo.com/quote/GOOG?p=GOOG'
###RSP http = urllib3.PoolManager()
###RSP response = http.request('GET', url)
###RSP soup = BeautifulSoup(response.data.decode('utf-8'))
###RSP print (soup)
###RSP print (soup);
###RSP quit
###RSP quit()
###RSP import urllib3
###RSP from bs4 import BeautifulSoup
###RSP url = 'http://www.thefamouspeople.com/singers.php'
###RSP http = urllib3.PoolManager()
###RSP quit()
###RSP from bs4 import BeautifulSoup
###RSP import urllib2
###RSP import urllib3
###RSP url = "http://www.pythonforbeginners.com"
###RSP content = urllib2.urlopen(url).read()
###RSP content = urllib3.urlopen(url).read()
###RSP import urllib3
###RSP content = urllib3.urlopen(url).read()
###RSP import urllib3
###RSP http = urllib3.PoolManager()
###RSP url = 'http://www.thefamouspeople.com/singers.php'
###RSP response = http.request('GET', url)
###RSP soup = BeautifulSoup(response.data)
###RSP soup = BeautifulSoup(response.data,'html.parser'))
###RSP soup = BeautifulSoup(response.data,'html.parser')
###RSP print(soup)
###RSP url = 'http://finance.yahoo.com/TSLA?p=TSLA'
###RSP response = http.request('GET', url)
###RSP soup = BeautifulSoup(response.data,'html.parser')
###RSP ====================
###RSP print(soup)
###RSP url = 'http://finance.yahoo.com/quote/TSLA?p=TSLA'
###RSP soup = BeautifulSoup(response.data,'html.parser')
###RSP print(soup)
###RSP url = 'https://finance.yahoo.com/quote/TSLA?p=TSLA'
###RSP soup = BeautifulSoup(response.data,'html.parser')
###RSP print(soup)
###RSP mport requests
###RSP import requests
###RSP import requests from urllib3 import urlopen
###RSP import requests
###RSP from urllib3 import urlopen
###RSP import urllib3
###RSP import csv
###RSP import pandas as pd
###RSP quit
###RSP quit()
