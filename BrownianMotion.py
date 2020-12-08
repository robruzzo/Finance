# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:47:44 2020
Brownian Motion Simulation
@author: robru
"""

import scipy
import matplotlib.pyplot as plt

def bronian_motion(dt=0.1,X0=0,N=1000):    
    #Initialize W(t) with zeroes
    W=scipy.zeros(N+1)
    
    #We create N+1 Timesteps: T=0,1,2,3,4,5,...N
    t = scipy.linspace(0,N,N+1)
    
    #We have to use cumulative sum: on every step the additional value is 
    #drawn from a normal distributions with mean 0 and variance of dt.... N(0,dt)
    W[1:N+1]=scipy.cumsum(scipy.random.normal(X0,dt,N))

    return t,W

def plot_brownian_motion(t,W):
    plt.plot(t,W)
    plt.xlabel('Time (t)')
    plt.ylabel('Wiener-Process W(t)')
    plt.title('Wiener-Process')
    plt.show()    


if __name__=="__main__":
    t,W = bronian_motion()
    plot_brownian_motion(t,W)