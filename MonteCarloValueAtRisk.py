# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 23:52:22 2020

@author: robru
"""


import yfinance as yf
import datetime
import numpy as np


class ValueAtRiskMonteCarlo:
    
    def __init__(self, S, mu, sigma, c, n, iterations):
        self.S=S
        self.mu=mu
        self.sigma=sigma
        self.c = c
        self.n=n
        self.iterations=iterations
        
    def simulation(self):
        
        rand = np.random.normal(0,1,[1,self.iterations])
        
        #equation for the S(t) stock price
        stock_price = self.S*np.exp(self.n*(self.mu - 0.5*self.sigma**2)+self.sigma*np.sqrt(self.n)*rand)
        
        # we have to sort the stock prices to determine the percentile
        stock_price = np.sort(stock_price)
        
        #it depends on the confidence level 95->5 and 99->1
        percentile = np.percentile(stock_price,(1-self.c)*100)
        
        return self.S-percentile
    
if __name__=="__main__":
    
    S=1e6                   #the position
    c=0.99                  #the confidence level
    n=1                     #number of days
    iterations = 1000000   #of simulations
    
    #historical data to approximate mean and standard deviation
    start_date=datetime.datetime(2014,1,1)
    end_date = datetime.datetime(2017,10,15)
    
    #download stock related data from Yahoo Finance

    
    tick=yf.Ticker('C')
    citi=tick.history(start=start_date,end=end_date)
    
    citi['returns']=citi['Close'].pct_change()
    
    #We can assume daily returns to be normally distributed: means and variance (std dev)
    mu = np.mean(citi['returns'])
    sigma = np.std(citi['returns'])
    
    model = ValueAtRiskMonteCarlo(S,mu,sigma,c,n,iterations)
    
    
    print("Value At Risk Monte Carlo $%.2f: "% model.simulation())
   