import yahoo_fin.stock_info as si
import yfinance as yf

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def get_com_list(list_name):
    if list_name == 'S&P500':
        return si.tickers_sp500()
    elif list_name == 'DOW':
        return si.tickers_dow()

def get_price_change(com_list, start_date, end_date):
    com_price_changes = pd.DataFrame()
    for com_name in com_list:
        com_price_changes[com_name] = pd.Series(price_change(com_name, start_date, end_date))
    # delete companies which have NaN
    com_price_changes.dropna(axis=1, inplace=True)
    return com_price_changes

def price_change(com_name, start_date, end_date):
    price_df = yf.download(com_name, 
                start = start_date, 
                end = end_date, 
                progress=False)
    # adjusted close price
    adj_close_df = price_df['Adj Close']
    # calculate daily price change(%)
    price_change_rate = np.zeros(len(adj_close_df) - 1)
    for i in range(1, len(adj_close_df)):
        price_change_rate[i-1] = 100 * (adj_close_df[i] - adj_close_df[i-1]) / adj_close_df[i-1]
    return price_change_rate
    

def get_adjacency_matrix(com_price_changes, threshold, tot_list):
    sim_vectors = cosine_similarity(com_price_changes.T)
    # make adjacency matrix
    adj_matrix = pd.DataFrame()
    for i in range(len(sim_vectors)):
        temp_adj = np.zeros(len(sim_vectors))
        cnt = 0
        for num in sim_vectors[i]:
            if num >= threshold or num <= -1 * threshold:
                temp_adj[cnt] = 1
            cnt += 1
        adj_matrix[tot_list[i]] = pd.Series(temp_adj)
    adj_matrix.set_index(keys=tot_list, inplace=True)
    return adj_matrix