import os, math, random, copy
path_input = os.getcwd() + "/Module_1_Week4_Assignment_Input.txt"

min_cut = math.inf
num_iterations = 50


def remove_self_references(full_adj_list):
    for k, adj_vertices in full_adj_list.items():
        adj_vertices = [n for n in adj_vertices if n != k]
        full_adj_list[k] = adj_vertices


def run_karger(curr_adj_list: dict) :
    while len(curr_adj_list) > 2:
        # same as list(curr_adj_list.keys())
        contraction_vertex = random.choice(list(curr_adj_list))
        contraction_target = random.choice(curr_adj_list[contraction_vertex])
        # print(f"Removing edge [{contraction_vertex},{contraction_target}]")

        list_orig_edges = curr_adj_list[contraction_target]
        curr_adj_list[contraction_vertex] += list_orig_edges
        # replace all instances of contracted vertex in all connected edges
        for node in list_orig_edges:
            curr_adj_list[node] = [contraction_vertex if i == contraction_target else i for i in curr_adj_list[node]]

        curr_adj_list.pop(contraction_target)
        remove_self_references(curr_adj_list)


if __name__ == '__main__':
    orig_adj_list = dict()
    with open(path_input, "r") as f:
        for line in f:
            line_vertices = [int(x) for x in line.split()]
            leading_vertex = line_vertices[0]
            orig_adj_list[leading_vertex] = line_vertices[1:]

    remove_self_references(orig_adj_list)

    test_case = {1: [2, 3, 4, 7], 2: [1, 3, 4], 3: [1, 2, 4], 4: [1, 2, 3, 5], 5: [4, 6, 7, 8],
                 6: [5, 7, 8], 7: [1, 5, 6, 8], 8: [5, 6, 7]}

    min_list = None
    curr_min = math.inf
    for i in range(num_iterations):
        # seeding necessary?
        adj_list = copy.deepcopy(orig_adj_list)
        # adj_list = copy.deepcopy(test_case)
        run_karger(adj_list)
        length = len(adj_list[list(adj_list)[0]])
        if length < curr_min:
            curr_min = length
            min_list = adj_list
            print(f"Result: {curr_min}")

