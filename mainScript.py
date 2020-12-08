'''
This script will be employed to run all of the other scripts to calculate portfolio values and risk
and write a report in a format to be determined. HTML?
'''

import tickerdatautil as td
#import portfoliocalc as pc
#import capm

#Allow for csv or pickle
period ="1y" #Default Initial Yahoo Finance Download Period
delay=0.5	 #Default Delay between downloads in seconds
data_directory='E:/Datasets/Stocks/' #Include the trailing '/'
fileName ="sp500tickers.pickle" #Default File Name For updating
ticker_sub_directory ='SP500'
start_date='2010-01-01'
end_date='2017-01-01'
interval='1d'

#Update Tickers
#td.update_ticker_prices_fromLast(data_directory,ticker_sub_directory,fileName,delay)

#Purge Tickers and Redownload
td.get_data_from_yahoo(data_directory,ticker_sub_directory,fileName,period,False,True,delay)

