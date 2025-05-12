import os
from networkx.utils.union_find import UnionFind
from collections import defaultdict
from itertools import combinations

path_input = os.getcwd() + "/Module_3_Week2_Assignment_Input.txt"
path_input_ex = os.getcwd() + "/Module_3_Week2_Assignment_Input_ex.txt"
path_input_ex_2 = os.getcwd() + "/Module_3_Week2_Assignment_Input_ex_2.txt"
path_input_2 = os.getcwd() + "/Module_3_Week2_Assignment_Input_b.txt"


def union_find_explicit(filename, k):
    with open(filename, "r") as f:
        num_edges = int(f.readline())
        edges = [[int(y) for y in x.split()] for x in f.readlines()]  # weight length
    # sort edges by dist
    edges.sort(key=lambda x: x[2])

    clusters = UnionFind(range(1, num_edges+1))
    num_clusters = num_edges
    i_edge = 0
    while True:
        edge_to_fuse = edges[i_edge]
        clusters.union(clusters[edge_to_fuse[0]], clusters[edge_to_fuse[1]])
        num_clusters = len(list(clusters.to_sets()))
        if num_clusters < k:
            break
        i_edge += 1

    print("Solution question 1:", edges[i_edge][2])

def union_find_implicit(filename):
    with open(filename, "r") as f:
        x = f.readline().split()
        num_nodes, length = int(x[0]), int(x[1])
        nodes = [int(x.replace(" ", ""), 2) for x in f.readlines()]
    node_map = defaultdict(list)
    for i in range(num_nodes):
        node_map[nodes[i]].append(i)
    # generate bitshift maps for comparison
    # Idea: instead of comparing the nodes with o(n²), generate for each all candidate nodes with dist 0, 1 and 2
    # and check if those are in the dict. If yes, unionize them
    bitmasks = list()
    bitmasks.extend([1 << n for n in range(length)])
    for x, y in combinations(bitmasks, 2):
        bitmasks.append(x ^ y)
    bitmasks.append(0)

    clusters = UnionFind(range(0, num_nodes))
    for node_int, node_list in node_map.items():
        for dist in bitmasks:
            pot_node_int = node_int ^ dist
            if pot_node_int in node_map.keys():
                # unionize
                for n in node_list:
                    clusters.union(node_list[0], n)
                for m in node_map[pot_node_int]:
                    clusters.union(node_list[0], m)

    # get number of clusters
    print("Solution question 2:", len(list(clusters.to_sets())))

if __name__ == '__main__':
    # union_find_explicit(path_input_ex, 2)
    # union_find_explicit(path_input_ex, 3)
    union_find_explicit(path_input, 4)
    # union_find_implicit(path_input_ex_2)  # should be 990
    union_find_implicit(path_input_2)


