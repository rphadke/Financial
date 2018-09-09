#! /usr/bin/env python3.6

### from pandas_datareader import Options
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
import datetime

### tickers = ['AAPL', 'MSFT']

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = datetime.datetime(2018,1,1)
end_date = datetime.datetime(2018,8,1)
data_source='yahoo'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
# panel_data = data.DataReader(tickers, data_source, start_date, end_date)
# print(panel_data)

