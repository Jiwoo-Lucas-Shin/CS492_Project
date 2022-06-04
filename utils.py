import yahoo_fin.stock_info as si
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def get_com_list(company_list):
    if company_list == 'SnP500':
        return si.tickers_sp500()
    elif company_list == 'DOW':
        return si.tickers_dow()

def get_price_changes(com_list, market_index, start_date, end_date):
    com_price_changes = pd.DataFrame()
    for com_name in com_list:
        com_price_changes[com_name] = pd.Series(price_change(com_name, start_date, end_date))
        # new_column = pd.DataFrame({com_name: price_change(com_name, start_date, end_date)})
        # com_price_changes = pd.concat([com_price_changes, new_column], axis=1)
    
    # delete companies which have NaN
    com_price_changes.dropna(axis=1, inplace=True)

    # concate market price change
    if market_index == 'SnP500':
        market_stock = 'SPY'
        market_name = 'S&P500'
    elif market_index == 'Nasdaq':
        market_stock = '^IXIC'
        market_name = 'Nasdaq'
    # market_col = pd.DataFrame({market_name: price_change(market_stock, start_date, end_date)})
    # com_price_changes = pd.concat([com_price_changes, market_col], axis=1)
    com_price_changes[market_name] = pd.Series(price_change(market_stock, start_date, end_date))

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

def get_adjacency_matrix(com_price_changes, cor_type, threshold, tot_list):
    sim_vectors = cosine_similarity(com_price_changes.T)
    # make adjacency matrix
    adj_matrix = pd.DataFrame()
    for i in range(len(sim_vectors)):
        temp_adj = np.zeros(len(sim_vectors))
        cnt = 0
        for num in sim_vectors[i]:
            if cor_type == 'both':
                if num >= threshold or num <= -1 * threshold:
                    temp_adj[cnt] = 1
            elif cor_type == 'positive':
                if num >= threshold:
                    temp_adj[cnt] = 1
            elif cor_type == 'negative':
                if num <= -1 * threshold:
                    temp_adj[cnt] = 1   
            cnt += 1
        adj_matrix[tot_list[i]] = pd.Series(temp_adj)
        # new_column = pd.DataFrame({tot_list[i]: temp_adj})
        # adj_matrix = pd.concat([adj_matrix, new_column], axis=1)
        
    adj_matrix.set_index(keys=tot_list, inplace=True)
    return adj_matrix

def save_cosine_ranking(com_price_changes, save_path):
    tot_list = com_price_changes.keys()
    sim_vectors = cosine_similarity(com_price_changes.T)
    rank_matrix = pd.DataFrame()

    for i in range(len(tot_list)):
        rank = tot_list[(-1*sim_vectors[i]).argsort()[1:11]]
        rank_matrix[tot_list[i]] = pd.Series(rank)

    path = save_path + '/cosine_ranking_matrix.csv'
    rank_matrix.to_csv(path)
