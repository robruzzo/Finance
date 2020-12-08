# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:51:30 2020

@author: robru
"""
import numpy as np
from scipy import stats

def blackscholes_call(S,E,T,rf,sigma):
    #First we have to calculate d1,d2 parameters
    d1 = (np.log(S/E)+(rf+sigma*sigma/2.0)*T)/(sigma*np.sqrt(T))
    d2 = d1-sigma*np.sqrt(T)
    
    #We need N(x) normal distribution function
    return S*stats.norm.cdf(d1)-E*np.exp(-rf*T)*stats.norm.cdf(d2)

def blackscholes_put(S,E,T,rf,sigma):
    #First we have to calculate d1,d2 parameters
    d1 = (np.log(S/E)+(rf+sigma*sigma/2.0)*T)/(sigma*np.sqrt(T))
    d2 = d1-sigma*np.sqrt(T)
    
    #We need N(x) normal distribution function
    return -S*stats.norm.cdf(-d1)+E*np.exp(-rf*T)*stats.norm.cdf(-d2)


if __name__=="__main__":
    S0=100                      #underlying stock price at t=0
    E=100                       #strike price
    T=1                         #Expiry = 1 year -365 days
    rf=0.05                     #risk-free rate
    sigma=0.2                   #Volatility of the underlying stock
    
    print("Call option price according to Black-Scholes Model: ",blackscholes_call(S0,E,T,rf,sigma))
    print("Put option price according to Black-Scholes Model: ", blackscholes_put(S0,E,T,rf,sigma))