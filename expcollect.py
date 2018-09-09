#! /usr/bin/env python3.6

### import pandas as pd
from pandas_datareader import data, wb

import datetime as dt

ticker = ['ORCL','TSLA','IBM','MSFT']

start = dt.datetime(2018,1,1)
end = dt.datetime.now()

df = data.DataReader('IBM', 'morningstar', start, end)
print(df)
