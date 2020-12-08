import pandas_datareader as pdr
from pandas_datareader import data, wb
from datetime import date
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import TickerDataUtil


data_directory='E:/Datasets/Stocks/' #Include the trailing '/'
fileName ="sp500tickers.pickle" #Default File Name For updating
ticker_sub_directory ='SP500'
risk_free_rate = 0.05 # put in a function to grab this information from somewhere
reference_stock ='^GSPC' #S&P 500 Index
ticker='IBM'
start_date='2010-01-01'
end_date='2017-01-01'
period ="1y" #Default Initial Yahoo Finance Download Period
delay=0.5	 #Default Delay between downloads in seconds
interval='1d'

def capm(start_date, end_date, ticker, reference_stock=reference_stock):
    
	#we prefer monthly returns instead of daily returns
	ticker_data = ticker_data.resample('M').last()
	reference_data = reference_stock.resample('M').last()

	#creating a dataFrame from the data - Adjusted Closing Price is used as usual
	data = pd.DataFrame({'s_adjclose' : ticker_data['Adj Close'], 'm_adjclose' : reference_data['Adj Close']}, index=ticker_data.index)
	#natural logarithm of the returns
	data[['s_returns', 'm_returns']] = np.log(data[['s_adjclose','m_adjclose']]/data[['s_adjclose','m_adjclose']].shift(1))
	#no need for NaN/missing values values so let's get rid of them
	data = data.dropna()

	#covariance matrix: the diagonal items are the vairances - off diagonals are the covariances
	#the matrix is symmetric: cov[0,1] = cov[1,0] !!!
	covmat = np.cov(data["s_returns"], data["m_returns"])
	print(covmat)
	
	#calculating beta according to the formula
	beta = covmat[0,1]/covmat[1,1]
	print("Beta from formula:", beta)

	#using linear regression to fit a line to the data [stock_returns, market_returns] - slope is the beta
	beta,alpha = np.polyfit(data["m_returns"], data['s_returns'], deg=1)
	print("Beta from regression:", beta)
	
	#plot
	fig,axis = plt.subplots(1,figsize=(20,10))
	axis.scatter(data["m_returns"], data['s_returns'], label="Data points")
	axis.plot(data["m_returns"], beta*data["m_returns"] + alpha, color='red', label="CAPM Line")
	plt.title('Capital Asset Pricing Model, finding alphas and betas')
	plt.xlabel('Market return $R_m$', fontsize=18)
	plt.ylabel('Stock return $R_a$')
	plt.text(0.08, 0.05, r'$R_a = \beta * R_m + \alpha$', fontsize=18)
	plt.legend()
	plt.grid(True)
	plt.show()
	
	#calculate the expected return according to the CAPM formula
	expected_return = risk_free_rate + beta*(data["m_returns"].mean()*12-risk_free_rate)
	print("Expected return:", expected_return)

if __name__ == "__main__":
	#using historical data 2010-2017: the market is the S&P500 !!!
	capm('2010-01-01', '2017-01-01','IBM', '^GSPC')
	
