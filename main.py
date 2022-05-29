import argparse
import os
from utils import get_com_list, get_price_changes, price_change, get_adjacency_matrix
from graph_function import get_graph, save_graph_png, apply_node2vec, save_ranking, save_cluster_result

parser = argparse.ArgumentParser(description='CS492 Project')
parser.add_argument('--start', default='2022-04-25', type=str)
parser.add_argument('--end', default='2022-05-23', type=str)
parser.add_argument('--p', default=1, type=float)
parser.add_argument('--q', default=2, type=float)
parser.add_argument('--cor_type', default='both', type=str, help='positive, negative, both')
parser.add_argument('--threshold', default=0.8, type=float)
parser.add_argument('--market_index', default='SnP500', type=str, help='Nasdaq or SnP500')
parser.add_argument('--company_list', default='SnP500', type=str, help='SnP500 or DOW')
parser.add_argument('--save_folder', default='results', type=str)

def main():
    args = parser.parse_args()
    
    path = os.getcwd()
    save_path = path + '/' + args.save_folder
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    
    com_list = get_com_list(args.company_list)

    # conpany price change + market index price change matrix
    com_price_changes = get_price_changes(com_list, args.market_index, args.start, args.end)

    # total_list
    tot_list = com_price_changes.keys()
    
    # get adjacency matrix
    adj_matrix = get_adjacency_matrix(com_price_changes, args.cor_type, args.threshold, tot_list)

    # get graph using adjacency matrix
    G = get_graph(adj_matrix, tot_list)
    
    # save graph as png (* node size: degree centrality)
    save_graph_png(G, save_path)

    # get node vectors
    node_vecs = apply_node2vec(G, args.p, args.q)
    
    # save ranking matrix as csv
    save_ranking(node_vecs, save_path)

    # save cluster result as png
    save_cluster_result(G, node_vecs, save_path)
    
    print('main.py: finished successfully')
    
if __name__ == '__main__':
    main()
