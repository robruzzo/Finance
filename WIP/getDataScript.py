# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 00:28:14 2020

@author: robru
"""
import pandas as pd
import tickerdatautil as td

#Global variables
data_directory='E:/Datasets/Stocks/'
ticker_sub_directory='indexes/'
csv_file ='indexes.csv'
output_pickle=csv_file[:-4]+".pickle"
period='5y'


df = pd.DataFrame(data=['AAPL','IBM','OLED'], columns=['Ticker']) 

'''
td.convert_tickers_csv_to_pickle(data_directory, csv_file)
td.get_data_from_yahoo(data_directory, ticker_sub_directory, output_pickle, period, False,True,0.5)
'''

'''
td.convert_tickers_df_to_pickle(data_directory,'mythree',df)
td.get_data_from_yahoo(data_directory, 'mythree/', 'mythree.pickle', period, False, False, 0.5)
'''
