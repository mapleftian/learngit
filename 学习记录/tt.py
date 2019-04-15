#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     tt.py
   Author:        fynn-PC
   date:          2019/4/11 22:28
   Software:      PyCharm
-------------------------------------------------
"""

import re
import requests
import pandas as pd
import json


def retrieve_quotes_historical(stock_code):
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' %(stock_code,stock_code)
    r = requests.get(url)
    #由于网页本身内容是规范的，所以通过json格式解析内容
    patter = 'HistoricalPriceStore":{"prices":(.*?),"isPending"'
    data = re.findall(patter,r.text)
    #由于多了一个[]，系统默认是二维列表，所以选取list[0]
    quotes = data[0]
    datas = json.loads(quotes)
    #返回最原始信息
    datas = datas[::-1]
    print(datas[1].keys())
    #这里不能直接返回datas
    return [item for item in datas if not 'type' in item]

if __name__ == '__main__':
    quotes = retrieve_quotes_historical('AXP')
    column = ['Date','Open','High','Low','Close','Adj Close**','Volume']
    quotesDf = pd.DataFrame(quotes)
    print(quotesDf)
