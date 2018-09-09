#! /usr/bin/env python3.6

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
### from pandas.io import data, wb

style.use('ggplot')

start = dt.datetime(2018,1,1)
end = dt.datetime.now()

df = web.DataReader("TSLA", 'morningstar', start, end)
