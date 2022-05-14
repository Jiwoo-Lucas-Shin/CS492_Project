import argparse
import os
from utils import get_com_list, get_price_change, price_change, get_adjacency_matrix
from graph_function import get_graph, save_graph_png, apply_node2vec, save_cluster_result

parser = argparse.ArgumentParser(description='CS492 Project')
parser.add_argument('--start', default='2022-04-01', type=str)
parser.add_argument('--end', default='2022-04-30', type=str)
parser.add_argument('--threshold', default=0.5, type=float)
parser.add_argument('--list_name', default='DOW', type=str)
parser.add_argument('--save_folder', default='graph_png', type=str)

def main():
    args = parser.parse_args()
    
    path = os.getcwd()
    save_path = path + '/' + args.save_folder
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    
    com_list = get_com_list(args.list_name)
    com_price_changes = get_price_change(com_list, args.start, args.end)
    snp_change = price_change('SPY', args.start, args.end)
    
    # Add S&P500_change_rate to com_price_changes
    com_price_changes['S&P500'] = snp_change

    # total_list
    tot_list = com_price_changes.keys()
    
    # get adjacency matrix
    adj_matrix = get_adjacency_matrix(com_price_changes, args.threshold, tot_list)

    # get graph using adjacency matrix
    G = get_graph(adj_matrix, tot_list)
    
    # save graph as png (* node size: degree centrality)
    save_graph_png(G, save_path)
    
    # get node vectors
    node_vecs = apply_node2vec(G)
    
    # save cluster result as png
    save_cluster_result(node_vecs, save_path)
    
    print('main.py: finished successfully')
    
if __name__ == '__main__':
    main()