import requests
import urllib3
import csv
import pandas as pd
from pandas import DataFrame
import datetime
import pandas.io.data

YahooUrl = 'http://ichart.yahoo.com/table.csv?s='
start_month = 1 - 1
start_day = 1
start_year = 2010

end_month = 12 - 1
end_day = 31
end_year = 2014

Start_ApiMonth = '&a=%s' %(start_month)
Start_ApiDay = '&b=%s' %(start_day)
Start_ApiYear = '&c=%s' %(start_year)

End_ApiMonth = '&d=%s' %(end_month)
End_ApiDay = '&e=%s' %(end_day)
End_ApiYear = '&f=%s' %(end_year)

interval = 'm'

ApiInterval = '&g=%s' %(interval)

ApiStatic = '&ignore=.csv'

Ticker = input("What is the ticker > ")

myURL = YahooUrl + Ticker + Start_ApiMonth + Start_ApiDay +         Start_ApiYear + End_ApiMonth + End_ApiDay + End_ApiYear + ApiInterval +  ApiStatic

http = urllib3.PoolManager()
### soup = BeautifulSoup(response.data.'html.parser')

Website = http.request('GET', myURL)
Info = Website.read()

output = open('output.csv','wb')
wr = csv.writer(output, dialect='excel')
for item in Info:
    wr.writerow(item)
print Info

