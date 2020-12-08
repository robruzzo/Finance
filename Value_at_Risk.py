# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 23:27:10 2020

@author: robru
"""


import numpy as np
from scipy.stats import norm
import yfinance as yf
import datetime

#we want to calculate VaR in n days time
#we have to consider that the mean and standard deviation will change
#mu = mu*n and sigma=sigma*sqrt(n) we have to use transformations

def value_at_risk_long(position,c,mu,sigma,n):
    alpha=norm.ppf(1-c)
    var=position*(mu*n-sigma*alpha*np.sqrt(n))
    return var

if __name__=="__main__":
    #historical data to approximate mean and standard deviation
    start_date=datetime.datetime(2014,1,1)
    end_date = datetime.datetime(2017,10,15)
    
    #download stock related data from Yahoo Finance

    
    tick=yf.Ticker('C')
    citi=tick.history(start=start_date,end=end_date)
    
    citi['returns']=citi['Close'].pct_change()
    
    S=1e6           #This is the investment (position)
    c=0.99          #This is the confidence level
    
    #We can assume daily returns to be normally distributed: means and variance (std dev)
    mu = np.mean(citi['returns'])
    sigma = np.std(citi['returns'])
    
    print('Value at risk is: $%0.2f' % value_at_risk_long(S,c,mu,sigma,1))
    