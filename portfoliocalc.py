import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt
import pickle
import time

'''
NOTE IT WAS FOUND THAT THE OPTIMAL HAS FALLEN ON NO DATA POINT FOR THE MyWatchList
'''

data_directory='E:/Datasets/Stocks/' #Include the trailing '/'
ticker_sub_directory ='MyWatchList/'
fileName='MyWatchList.pickle'
simulations=10000 #default value for monte carlo simulations
data=pd.DataFrame(index=['Date'])
script_start=time.time()
output_portfolio_name=fileName[:-7]+"_optimum_portfolio.pickle"

def get_tickers(fileName):
    with open(data_directory + fileName,"rb") as f:
            tickers=pickle.load(f)
    return tickers

def show_data(data):
    data.plot(figsize=(10,5))
    plt.show()

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

def calc_daily_returns(data):
    returns=np.log(data/data.shift(1))
    return returns;

def plot_daily_returns(data):
    returns.plot(figsize=(10,5))
    plt.show()

def show_statistics(returns):
    print("\nAverage Returns:")
    print(returns.mean()*252)
    print("\nCovariance Matrix:")
    print(returns.cov()*252)

'''
Function Name: init_weights()
Purpose: This function randomly initializes the weights of the
         stocks as it relates to their weight in the portfolio
'''
def init_weights():
    weights =np.random.random(len(tickers))
    weights /= np.sum(weights)
    return weights

'''
Function Name: calc_portfolio_return(returns, weights)
Purpose: This function will calculate the overall estimated return of
         the portfolio based on the average returns of the stocks.
'''
def calc_portfolio_return(returns, weights):
    portfolio_return=np.sum(returns.mean()*weights)*252
    print("Expected portfolio return: ", portfolio_return)
    return portfolio_return

'''
Function Name: calculate portfolio_variance(returns, weights)
Purpose: Calculate the variance in the portfolio, or average risk
'''
def calc_portfolio_variance(returns, weights):
    portfolio_variance = np.sqrt(np.dot(weights.T,np.dot(returns.cov()*252, weights)))
    print("Expected portfolio variance: ",portfolio_variance)
    return portfolio_variance

def create_portfolios(weights,returns, simulations=simulations):
    print("\nCreating Portfolios... Time:",time.time()-script_start)
    preturns=[]
    pvariances=[]
    #Monte Carlo Simulation
    for i in range(simulations):
        weights = np.random.random(len(tickers))
        weights/=np.sum(weights)
        preturns.append(np.sum(returns.mean()*weights)*252)
        pvariances.append(np.sqrt(np.dot(weights.T,np.dot(returns.cov()*252, weights))))
    preturns=np.array(preturns)
    pvariances=np.array(pvariances)
    #print("Elapsed Time: ",time.time()-start_time)
    return preturns, pvariances

def plot_portfolios(returns,variances):
    plt.figure_size=(10,6)
    plt.scatter(variances, returns,c=returns/variances,marker='o')
    plt.grid(True)
    plt.xlabel("Expected Volatility")
    plt.ylabel("Expected Return")
    plt.colorbar(label='Sharpe Ratio')
    plt.show()


def statistics(weights,returns):
    portfolio_return=np.sum(returns.mean()*weights)*252
    portfolio_volatility=np.sqrt(np.dot(weights.T,np.dot(returns.cov()*252,weights)))
    return np.array([portfolio_return,portfolio_volatility,portfolio_return/portfolio_volatility])

def min_sharpe(weights,returns):
    return -statistics(weights,returns)[2]

def optimize_portfolio(weights,returns):
    print("\nOptimizing Portfolio... Time: ",time.time()-script_start)
    constraints=({'type':'eq','fun':lambda x: np.sum(x)-1}) #constrain the weights to a sum of 1
    bounds = tuple((0,1) for x in range(len(tickers)))
    optimum=opt.minimize(fun=min_sharpe, x0=weights, args=returns, method='SLSQP',bounds=bounds, constraints=constraints)
    return optimum

def print_optimial_portfolio(optimum, returns):
    print("Optimal Weights: ", optimum['x'].round(3))
    print("Expected Return:, volatility and Sharpe Ratio:", statistics(optimum['x'].round(3),returns))

'''
def save_optimial_portfolio(optimum, returns):
    print("Optimal Weights: ", optimum['x'].round(3))
    print("Expected Return:, volatility and Sharpe Ratio:", statistics(optimum['x'].round(3),returns))
    print("Saving Optimum Portfolio")
    with open(data_directory + output_portfolio_name,"wb") as f:
        pickle.dump(optimum['x'].round(3),f)
'''

def save_optimial_portfolio_pickle(optimum, returns):
    x=0
    port=[]
    print("Saving Optimum Portfolio")
    for ticker in tickers:
        if optimum['x'][x].round(3) > 0.0:
            print("Ticker: ",ticker, "\tWeight: ",optimum['x'][x].round(3))
            port.append([tickers,optimum['x'][x].round(3)])
        x+=1
    with open(data_directory + output_portfolio_name,"wb") as f:
        pickle.dump(port,f)



def show_optimal_portfolio(optimum,returns,preturns,pvariances):
    plt.figure(figsize=(10,6))
    plt.scatter(pvariances,preturns,c=preturns/pvariances,marker='o')
    plt.grid(True)
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')
    plt.colorbar(label='Sharpe Ratio')
    plt.plot(statistics(optimum['x'],returns)[1],statistics(optimum['x'], returns)[0], 'g*',markersize=20.0)
    plt.show()



if __name__=="__main__":
    tickers=get_tickers(fileName)
    data=load_data(tickers,data)
    show_data(data)
    returns=calc_daily_returns(data)
    plot_daily_returns(returns)
    show_statistics(returns)
    weights=init_weights()
    calc_portfolio_return(returns,weights)
    calc_portfolio_variance(returns,weights)
    preturns,pvariances=create_portfolios(weights,returns,simulations)
    plot_portfolios(preturns,pvariances)
    optimum=optimize_portfolio(weights,returns)
    print_optimial_portfolio(optimum,returns)
    save_optimial_portfolio_pickle(optimum,returns)
    show_optimal_portfolio(optimum,returns,preturns,pvariances)
    print("Elapsed Time: ",time.time()-script_start)
