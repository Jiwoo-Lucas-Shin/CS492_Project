import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from node2vec import Node2Vec
from sklearn.preprocessing import MinMaxScaler
from sklearn.mixture import GaussianMixture

def get_graph(adj_matrix, tot_list):
    # adjacency matrix -> dateframe
    graph_df = pd.DataFrame(columns=['head', 'similarity', 'tail'])
    
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if i < j:
                if adj_matrix[tot_list[i]][j] == 1:
                    head = tot_list[i]
                    # sim = adj_matrix[i][j]
                    sim = 1
                    tail = tot_list[j]
                    graph_df = graph_df.append({'head': head, 'similarity': sim, 'tail': tail}, ignore_index=True)

    return nx.from_pandas_edgelist(graph_df, "head", "tail", edge_attr=True, edge_key="similarity", create_using=nx.Graph())


def save_graph_png(G, save_path):
    node_list = list(G.nodes())
    # TOP10, Top11-20 companies in S&P 500 (2022-03-18)
    Top10 = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'GOOG', 'TSLA', 'BRK.B', 'NVDA', 'FB', 'UNH']
    # Top11_20 = ['JNJ', 'JPM', 'PG', 'V', 'HD', 'XOM', 'BAC', 'CVX', 'PFE', 'MA']

    node_color = []
    for i in range(len(node_list)):
        if node_list[i] == 'S&P500' or node_list[i] == 'Nasdaq':
            node_color.append('red')
        elif node_list[i] in Top10:
            node_color.append('yellow')
        # elif node_list[i] in Top11_20:
        #     node_color.append('black')
        else:
            node_color.append('blue')
    
    plt.figure(figsize=(50, 50))
    # degree centrality
    d = dict(G.degree)
    nx.draw(G, with_labels=True, node_color = node_color,
            node_size = [v * 30 for v in d.values()], font_size=15)

    path = save_path + '/degree_centrality.png'
    plt.savefig(path)

def apply_node2vec(G):
    node2vec = Node2Vec(graph=G, # target graph
                        dimensions=50, # embedding dimension
                        walk_length=10, # number of nodes in each walks 
                        p = 1,
                        q = 2,
                        weight_key='similarity', # weighted node2vec
                        num_walks=1000, 
                        workers=1)
    
    return node2vec.fit(window=10)

def save_ranking(node_vecs, save_path):
    node_list = list(node_vecs.wv.vocab)

    rank_matrix = pd.DataFrame()
    rank_matrix = pd.DataFrame()

    for com_name in node_list:
        sim_list = []
        for sim_com, _ in node_vecs.most_similar(com_name):
            sim_list.append(sim_com)
        rank_matrix[com_name] = pd.Series(sim_list)
    
    path = save_path + '/ranking_matrix.csv'
    rank_matrix.to_csv(path)
    
def save_cluster_result(G, node_vecs, save_path):
    gm = GaussianMixture(n_components=5, random_state=0).fit(node_vecs.wv.vectors)

    for n, label in zip(node_vecs.wv.index2entity, gm.predict(node_vecs.wv.vectors)):
        G.nodes[n]['label'] = label

    plt.figure(figsize=(30, 30))
    nx.draw_networkx(G, pos=nx.layout.spring_layout(G), 
                    node_color=[n[1]['label'] for n in G.nodes(data=True)], 
                    cmap=plt.cm.rainbow
                    )
    plt.axis('off')
    
    path = save_path + '/graph_cluster_result.png'
    plt.savefig(path)