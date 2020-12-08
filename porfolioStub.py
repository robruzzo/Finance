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
sample=0.05


def get_tickers(fileName=fileName,sample=sample,subset=False):
	tickers=pd.read_pickle(data_directory+fileName)
	if subset:
		subset=tickers.sample(frac=sample)
		print("Number of tickers selected:" len(subset))


def load_data(tickers, data):
	for ticker in tickers:
		ticker_data = pd.read_csv(data_directory+ticker_sub_directory+ticker+'.csv',parse_dates=True)
		ticker_data['Date']=pd.to_datetime(ticker_data['Date'])
		ticker_data['Date']=ticker_data['Date'].dt.strftime('%m/%d/%Y')
		ticker_data.set_index(['Date'],inplace=True)
		ticker_data=ticker_data[['Close']]
		ticker_data.rename(columns={'Close':"{}".format(ticker)}, inplace=True)
		data = pd.concat([data, ticker_data], axis=1, sort=False)
		data=data.dropna()
	return data

get_tickers(fileName,sample,subset=True)