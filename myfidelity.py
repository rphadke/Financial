#! /usr/bin/env python3

import requests, sys, lxml.html
import getpass

s = requests.Session()
login_url = 'https://login.fidelity.com/ftgw/Fas/Fidelity/RtlCust/Login/'

username = input("USERNAME: ")
password = getpass.getpass('PASSWORD')

payload = {
    'ssn' : username,
    'pin' : password
}

response = s.post(login_url, data=payload, headers=dict(referer='https://login.fidelity.com'))
if response.status_code != requests.codes.ok :
	print('Failure(POST): ' + str(response.status_code))
else:
	print('Success(POST): ' + str(response.status_code))
print(response.text)

#page to scrape
response = s.get('https://fixedincome.fidelity.com/ftgw/fi/FIBondDetails?requestType=&displayFormat=TABLE&cusip=30382LDK1&ordersystem=TORD&preferenceName=')

if response.status_code != requests.codes.ok :
	print ( response.status_code )
else:
	print( 'Success (GET): ' + str(response.status_code))

print (response.text) #redirected to the login page
