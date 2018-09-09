#! /usr/bin/env python

import urllib
import re

def get_quote(symbol):
	# base_url = 'http://finance.google.com/finance?q='
	base_url = 'https://finance.yahoo.com/quote/'
	content = urllib.urlopen(base_url + symbol + '?p=' + symbol).read()
	print (content)
	m = re.search('id="re_694653_l".*?>(.*)<', content)
	if m:
		quote = m.group(1)
	else:
		quote = 'no quote available for: ' + symbol
	return quote

import stockquote
print (stockquote.get_quote('goog'))

