#! /usr/bin/python

import sys
import urllib as url

symbol = 'TSLA'
urlocation = 'https://finance.yahoo.com/' + symbol + '?p=' + symbol

print urlocation

response = url.urlopen('http://finance.yahoo.com/TSLA?p=TSLA')
# response = url.urlopen(urlocation)

html = response.read()

print html

