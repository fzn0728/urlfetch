# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 09:02:05 2016

@author: ZFang
"""

from multiprocessing import Pool
import requests
# from bs4 import BeautifulSoup
import pandas as pd
import os
import time

os.chdir('C:\\Users\\ZFang\\Desktop\\TeamCo\\URLfetch\\urlfetch')

start = time.time()

def fetch_url(x):
    myurl = ("http://finance.yahoo.com/q/cp?s=%s" % x)
    html = requests.get(myurl).content
    #soup = BeautifulSoup(html,'lxml')
    listOut = [x, str(html)]
    return listOut

tickDF = pd.read_excel('short_tickerlist.xlsx')
li = tickDF['Ticker'].tolist()



if __name__ == '__main__':
    p = Pool(7)
    output = p.map_async(fetch_url,li,chunksize=10)
    while not output.ready():
        print("Number of ticker left {0}".format((output._number_left)*10))
        time.sleep(1)
    result = output.get()
    p.close()
    p.join()
    print("Time is %ss" %(time.time()-start))
