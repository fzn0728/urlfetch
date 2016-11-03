# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:46:51 2016

@author: ZFang
"""

import time
import threading
import queue
from urllib.request import urlopen
import time
import pandas as pd


ticker = pd.ExcelFile('tickerlist.xlsx')
ticker_df = ticker.parse(str(ticker.sheet_names[0]))
ticker_list = list(ticker_df['Ticker'])

start = time.time()

result = []
def fetch(ticker):
    url = 'http://finance.yahoo.com/quote/' + ticker
    text = urlopen(url).read()
    result.append([ticker,text])
    # result[i] = urlopen(url).read()
    print(url+' fetching...... ' + str(time.time()-start))
    

process = [None] * len(ticker_list)
# utility - spawn a thread to execute target for each args
for i in range(len(ticker_list)):
    process[i] = threading.Thread(target=fetch, args=[ticker_list[i]])
    process[i].start()

# time.sleep()
for i in range(len(ticker_list)):    
    process[i].join()


print("Elapsed Time: %ss" % (time.time() - start))

