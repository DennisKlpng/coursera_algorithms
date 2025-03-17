import os
from networkx.utils.union_find import UnionFind

path_input = os.getcwd() + "/Module_3_Week2_Assignment_Input.txt"
path_input_ex = os.getcwd() + "/Module_3_Week2_Assignment_Input_ex.txt"
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


if __name__ == '__main__':
    union_find_explicit(path_input_ex, 2)
    union_find_explicit(path_input_ex, 3)
    union_find_explicit(path_input, 4)
