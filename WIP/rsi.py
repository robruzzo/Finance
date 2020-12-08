# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 21:40:43 2020

@author: robru
"""
import pandas as pd

n = 14 #RSI Period
sma=True
ema=False
wilders=False
ticker='AAPL'
data_directory='E:/Datasets/Stocks/'
ticker_sub_directory='sp500/'
AvgUp=[]
AvgD=[]
dat=pd.DataFrame()

def RSI_CALC(n,sma,ema,wilders,ticker):
    data = pd.read_csv(data_directory+ticker_sub_directory+ticker+'.csv',parse_dates=True)
    close=data['Close']
    
        
    return data


dat=RSI_CALC(10,False,False,False,'AAPL')
