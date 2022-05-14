import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from node2vec import Node2Vec
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

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
    node_color = ['red' if node_list[i]=='S&P500' else 'blue' for i in range(len(node_list))]
    
    plt.figure(figsize=(20, 20))
    # degree centrality
    d = dict(G.degree)
    nx.draw(G, with_labels=True, node_color = node_color,
            node_size = [v * 70 for v in d.values()], font_size=30)

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

def save_cluster_result(node_vecs, save_path):
    node_list = list(node_vecs.wv.vocab)
    com_vector_list = [node_vecs.wv[com] for com in node_list]
    
    # sacling usnig MinMaxScaler
    scaler = MinMaxScaler()
    node_scale = scaler.fit_transform(com_vector_list)
    
    # K-means clustering
    kmeans = KMeans(n_clusters = 2).fit(com_vector_list)
    com_cluster = kmeans.fit_predict(node_scale)
    
    # use pca to visualize
    pca = PCA(n_components=2)
    node_pca = pca.fit_transform(com_vector_list)
    pca_df = pd.DataFrame(data = node_pca, columns = ['pc1', 'pc2'])
    
    # color list (*maximum # of cluster: 6)
    color_list = []
    for i in range(len(com_cluster)):
        if com_cluster[i] == 0:
            color_list.append('blue')
        elif com_cluster[i] == 1:
            color_list.append('red')
        elif com_cluster[i] == 2:
            color_list.append('yellow')
        elif com_cluster[i] == 3:
            color_list.append('black')
        elif com_cluster[i] == 4:
            color_list.append('pink')
        elif com_cluster[i] == 5:
            color_list.append('purple')
        else:
            color_list.append('orange')

    plt.figure(figsize=(13,7))
    plt.xlabel("PC1", size=15)
    plt.ylabel("PC2", size=15)
    plt.title("Company Embedding Space", size=20)
    plt.scatter(pca_df['pc1'],pca_df['pc2'], linewidths=5, color=color_list)
    
    vocab=list(node_list)
    for i, word in enumerate(vocab):
        plt.annotate(word, xy=(pca_df['pc1'][i], pca_df['pc2'][i]))
        
    path = save_path + '/k-means_reslut.png'
    plt.savefig(path)