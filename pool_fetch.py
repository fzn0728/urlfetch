# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:21:06 2016

@author: ZFang
"""

from multiprocessing.pool import ThreadPool
import time
import os
import pandas as pd
from urllib.request import urlopen


os.chdir('C:\\Users\\ZFang\\Desktop\\TeamCo\\URLfetch\\urlfetch')

start = time.time()


ticker = pd.ExcelFile('tickerlist.xlsx')
ticker_df = ticker.parse(str(ticker.sheet_names[0]))
ticker_list = list(ticker_df['Ticker'])[0:10]




def fetch(ticker):
    result = []
    url = 'http://finance.yahoo.com/quote/' + ticker
    result.append(ticker)
    result.append(urlopen(url).read())
    print(url+' fetching...... ' + str(time.time()-start))
    return result







pool = ThreadPool(processes=10)


result = pool.apply_async(fetch, (ticker_list))
return_val = result.get()