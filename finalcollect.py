# !/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from pandas_datareader import data, wb
import datetime as dt

startdate = dt.datetime(2018,8,1)
enddate = dt.datetime.now()

ticker_list = ['IBM','IQ','ALGN','MSFT']

### data1 = data.DataReader(ticker,'yahoo',startdate,enddate)
for symbol in ticker_list:
	# data1 = data.DataReader(symbol,'yahoo',startdate,enddate)
	data1 = data.DataReader(symbol,'yahoo',startdate,enddate)
	print ("=========>>>" + symbol)
	data1.ix['2018-8-10']
	### print(data1.head)
	print(data1)
### data1.reset_index(inplace=True)
### data1.set_index("Date", inplace=True)
# data1 = data1.drop("Symbol", axis=1)

### print(data1.head())
#### print(data1)

