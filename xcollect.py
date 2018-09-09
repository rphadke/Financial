#! /usr/bin/env python3.6

### EXP-1 import pandas_datareader.data as web
### EXP-1 import datetime    
### EXP-1 
### EXP-1 start = datetime.datetime(2018, 1, 1)
### EXP-1 end = datetime.datetime.now()
### EXP-1 df = web.DataReader("GOOGL", 'yahoo', start, end)
### EXP-1 
### EXP-1 dates =[]
### EXP-1 for x in range(len(df)):
### EXP-1     newdate = str(df.index[x])
### EXP-1     newdate = newdate[0:10]
### EXP-1     dates.append(newdate)
### EXP-1 
### EXP-1 df['dates'] = dates
### EXP-1 
### EXP-1 print df.head()
### EXP-1 print df.tail()
### EXP-1 

import pandas as pd
from pandas.io.data import DataReader

symbols_list = ['ORCL', 'TSLA', 'IBM','YELP', 'MSFT']
d = {}
for ticker in symbols_list:
    d[ticker] = DataReader(ticker, "yahoo", '2014-12-01')
pan = pd.Panel(d)
df1 = pan.minor_xs('Adj Close')
print(df1)

