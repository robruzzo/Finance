import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import scipy.optimize as opt
import pickle
import time

data_directory='E:/Datasets/Stocks/' #Include the trailing '/'
ticker_sub_directory ='sp500/'
fileName='sp500tickers.pickle'
portfolioFile='optimum_test.pickle'


tickers = pd.DataFrame()



def get_tickers(fileName=fileName):
	tickers=pd.read_pickle(data_directory+fileName)
	print("Ticker Count:",len(tickers))
	return tickers

def show_portfolio_weights(tickers,portfolioFile=portfolioFile):
	portfolio=pd.read_pickle(data_directory+portfolioFile)
	print("Portfolio Size:" ,len(portfolio))
	print(portfolio)
	return portfolio

tickers=get_tickers()
portfolio=show_portfolio_weights(tickers,portfolioFile)
'''
n=0
weightTotal=0
for ticker in tickers:
	if portfolio[n]>0:
		print("Ticker: ",ticker,"\tWeight: ",portfolio[n])
	n+=1
print("Total of weights: ",weightTotal)
'''