# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:46:51 2016

@author: ZFang
"""

import time
import threading
import queue
from urllib.request import urlopen
import pandas as pd


ticker = pd.ExcelFile('short_tickerlist.xlsx')
ticker_df = ticker.parse(str(ticker.sheet_names[0]))
ticker_list = list(ticker_df['Ticker'])

start = time.time()

result = []
def fetch(ticker):
    url = ('http://www.nasdaq.com/symbol/' + ticker + '/real-time')
    print('Visit ' + url)
    text = str(urlopen(url).read())
    result.append([ticker,text])
    print(url +' fetching...... ' + str(time.time()-start))
    

        
process = [None] * len(ticker_list)
# utility - spawn a thread to execute target for each args
for i in range(len(ticker_list)):
    process[i] = threading.Thread(target=fetch, args=[ticker_list[i]])
    
for i in range(len(ticker_list)):    
    print('Start_' + str(i))
    process[i].start()
    # print('Join_' + str(i))    
    # process[i].join()
# time.sleep()




# for i in range(len(ticker_list)):
#     print('Join_' + str(i))    
#     process[i].join()

print("Elapsed Time: %ss" % (time.time() - start))

# text = str(urlopen('http://www.nasdaq.com/symbol/aapl/real-time').read())

# text.getheaders()