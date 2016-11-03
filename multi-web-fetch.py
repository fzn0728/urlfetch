# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:46:51 2016

@author: ZFang
"""
'''
import time
import threading
import queue
from urllib.request import urlopen
import time
import pandas as pd


start = time.time()



def fetch(ticker):
    url = 'http://finance.yahoo.com/quote/' + ticker
    result[i] = urlopen(url).read()
    
ticker = pd.ExcelFile('tickerlist.xlsx')
ticker_df = ticker.parse(str(ticker.sheet_names[0]))
ticker_list = list(ticker_df['Ticker'])[0:10]



result = [None] * 10
process = [None] * 10
# utility - spawn a thread to execute target for each args
for i in range(len(ticker_list)):
    process[i] = threading.Thread(target=fetch, args=[ticker_list[i]])
    process[i].start()

for i in range(len(process)):
    process[i].join()
    
    
    
    
print("Elapsed Time: %ss" % (time.time() - start))
'''


import time
import threading
import queue
from urllib.request import urlopen

# utility - spawn a thread to execute target for each args
def run_parallel_in_threads(target, args_list):
    result = queue.Queue()
    # wrapper to collect return value in a Queue
    def task_wrapper(args):
        result.put(target(args))
    threads = [threading.Thread(target=task_wrapper, args=[args]) for args in args_list]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return result

# below is the application code
urls = [
    ('http://www.google.com/',),
    ('http://www.lycos.com/',),
    ('http://www.bing.com/',),
    ('http://www.altavista.com/',),
    ('http://achewood.com/',),
]

l = [None] * 5


def fetch(url):
    l[i] = urlopen(url, timeout=60).read()

result = run_parallel_in_threads(fetch, urls)


# for i in urls:
#     print(i)