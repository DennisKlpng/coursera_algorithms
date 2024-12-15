import os
from collections import defaultdict
import sys
import threading

sys.setrecursionlimit(800000)
threading.stack_size(67108864)
path_input = os.getcwd() + "/Module_2_Week1_Assignment_Input.txt"


def dfs_first_pass(graph: dict, node, visited: defaultdict, visited_order: list):
    visited[node] = True
    # print(f"parsing node {node}")
    for nb in graph[node]:
        if not visited[nb]:
            dfs_first_pass(graph, nb, visited, visited_order)
    # print(f"no neighbours left, saving index for node {node}")
    visited_order.append(node)


def dfs_second_pass(graph: dict, node, visited: defaultdict, scc: set):
    visited[node] = True
    scc.add(node)
    for nb in graph[node]:
        if not visited[nb]:
            dfs_second_pass(graph, nb, visited, scc)


def solve():
    orig_graph = defaultdict(list)
    inverted_graph = defaultdict(list)
    all_nodes = set()

    with open(path_input, "r") as f:
        for line in f:
            line_vertices = [int(x) for x in line.split()]
            orig_graph[line_vertices[0]].append(line_vertices[1])
            inverted_graph[line_vertices[1]].append(line_vertices[0])
            all_nodes.add(line_vertices[0])

    test_case = {1: [7], 2: [5], 3: [9], 4: [1], 5: [8],
                 6: [3, 8], 7: [4, 9], 8: [2], 9: [6]}
    test_case_inv = {1: [4], 2: [8], 3: [6], 4: [7], 5: [2],
                     6: [9], 7: [1], 8: [5, 6], 9: [3, 7]}

    visited_nodes = defaultdict(lambda: False)
    assoc_node_2_visited = list()
    # start_node = 10  # FOR TEST
    start_node = max(all_nodes)
    while start_node > 1:
        start_node -= 1
        if visited_nodes[start_node]:
            continue
        # dfs_first_pass(test_case, start_node, visited_nodes, assoc_node_2_visited)
        dfs_first_pass(orig_graph, start_node, visited_nodes, assoc_node_2_visited)
    # print(assoc_node_2_visited)

    visited_nodes.clear()
    scc_list = list()
    assoc_node_2_visited.reverse()
    for start_node in assoc_node_2_visited:
        if visited_nodes[start_node]:
            continue
        curr_scc = set()
        # dfs_second_pass(test_case_inv, start_node, visited_nodes, curr_scc)
        dfs_second_pass(inverted_graph, start_node, visited_nodes, curr_scc)
        scc_list.append(curr_scc)
    # print(scc_list)
    sizes = [len(x) for x in scc_list]
    sizes.sort(reverse=True)
    print(f"{sizes[0]},{sizes[1]},{sizes[2]},{sizes[3]},{sizes[4]}")


if __name__ == '__main__':
    thread = threading.Thread(target=solve)
    thread.start()
