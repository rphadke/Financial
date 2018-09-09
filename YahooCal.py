#! /usr/bin/env python3

import requests, sys, lxml.html
import getpass
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import re

max_column = 10
row = ""

class tee(object):
	def __init__(self, fn='/tmp/foo.txt'):
		self.o = sys.stdout
		self.f = open(fn, 'w')
	def write(self, s):
		self.o.write(s)
		self.f.write(s)


s = requests.Session()

#page to scrape
### RSP response = s.get('https://finance.yahoo.com/calendar/earnings?from=2018-06-24&to=2018-06-30&day=2018-06-27')
response = s.get('https://finance.yahoo.com/calendar/earnings')
response = s.get('https://finance.yahoo.com/quote/IBM/options?p=IBM')

if response.status_code != requests.codes.ok :
	print ( response.status_code )
else:
	print( 'Success (GET): ' + str(response.status_code))

### RSP print (response.text) #redirected to the login page

soup = BeautifulSoup(response.text,"html.parser")
sys.stdout = tee()
print(soup.prettify())
### sys.stdout = tee()
column = 0
for tag in soup.find_all(re.compile("td")):
	row += tag.string
	if column < max_column :
		row += str(" | ")
		column += 1
	else :
		print (row)
		column = 0
		row = ""




	





