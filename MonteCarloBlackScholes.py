# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 22:17:07 2020

@author: robru
"""


import numpy as np


class OptionPricing:
    def __init__(self,S0,E,T,rf,sigma,iterations):
        self.S0=S0
        self.E=E
        self.T=T
        self.rf=rf
        self.sigma=sigma
        self.iterations=iterations
        
    def call_option_simulation(self):
        #we have 2 columns: first with 0s the second column will store the payoff
        #we need the first column of 0s: payoff function is max(0,S-E) for call option
        option_data = np.zeros([self.iterations,2])
        
        #dimensions: 1 dimensional array with as many items as the iterations
        rand = np.random.normal(0,1,[1,self.iterations])
        
        #equations for the S(t) stock price
        stock_price = self.S0*np.exp(self.T*(self.rf - 0.5*self.sigma**2)+self.sigma*np.sqrt(self.T)*rand)
        
        #we need S-E because we have to calculate the max (S-E,0)
        option_data[:,1]=stock_price-self.E
        
        #average for the Monte_carlo Method
        average = np.sum(np.amax(option_data,axis=1))/float(self.iterations)
        
        #we need to use the discount factor (value if money was in bank)
        return np.exp(-1.0*self.rf*self.T)*average
    
    
    def put_option_simulation(self):
        #we have 2 columns: first with 0s the second column will store the payoff
        #we need the first column of 0s: payoff function is max(0,S-E) for call option
        option_data = np.zeros([self.iterations,2])
        
        #dimensions: 1 dimensional array with as many items as the iterations
        rand = np.random.normal(0,1,[1,self.iterations])
        
        #equations for the S(t) stock price
        stock_price = self.S0*np.exp(self.T*(self.rf - 0.5*self.sigma**2)+self.sigma*np.sqrt(self.T)*rand)
        
        #we need S-E because we have to calculate the max (S-E,0)
        option_data[:,1]=self.E - stock_price
        
        #average for the Monte_carlo Method
        average = np.sum(np.amax(option_data,axis=1))/float(self.iterations)
        
        #we need to use the discount factor (value if money was in bank)
        return np.exp(-1.0*self.rf*self.T)*average    
    
'''
if __name__ == "__main__":
    S0=100                      #underlying stock price at t=0
    E=100                       #strike price
    T=1                         #Expiry = 1 year -365 days
    rf=0.05                     #risk-free rate
    sigma=0.2                   #Volatility of the underlying stock
    iterations = 10000000       #Number of iterations in the monte carlo simulation
    
    model = OptionPricing(S0,E,T,rf,sigma,iterations)
    
    
    
    print("Call option price according to Black-Scholes Model: ",model.call_option_simulation())
    print("Put option price according to Black-Scholes Model: ", model.put_option_simulation())
    
'''