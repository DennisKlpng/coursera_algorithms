import os
import heapq
import anytree

path_input = os.getcwd() + "/Module_3_Week3_Assignment_Input.txt"
path_input_ex = os.getcwd() + "/Module_3_Week3_Assignment_Input_ex.txt"
path_input_2 = os.getcwd() + "/Module_3_Week3_Assignment_Input_b.txt"
path_input_ex_2 = os.getcwd() + "/Module_3_Week3_Assignment_Input_ex_b.txt"


class HuffmanNode(anytree.NodeMixin):
    def __init__(self, weight, basic=True, parent=None, children=None):
        self.weight = weight
        self.basic = basic
        self.parent = parent
        if children:  # set children only if given
            self.children = children

    def __lt__(self, nxt):
        return self.weight < nxt.weight


def huffman(filename):
    with open(filename, "r") as f:
        num_symbols = int(f.readline())
        symbol_weights = [HuffmanNode(int(x)) for x in f.readlines()]  # weight
    heapq.heapify(symbol_weights)
    while len(symbol_weights) > 1:
        left = heapq.heappop(symbol_weights)
        right = heapq.heappop(symbol_weights)
        heapq.heappush(symbol_weights, HuffmanNode(left.weight + right.weight, False, None, [left, right]))
    max_depth = 0
    min_depth = num_symbols
    for pre, fill, node in anytree.RenderTree(symbol_weights.pop()):
        if node.basic:
            if node.depth < min_depth:
                min_depth = node.depth
            if node.depth > max_depth:
                max_depth = node.depth

    print(f"Solution question 1 max: {max_depth}, min: {min_depth}")


def max_weight_independent(filename):
    with open(filename, "r") as f:
        num_vertices = int(f.readline())
        vertex_weights = [int(x) for x in f.readlines()]  # weight

    # fill array
    max_weight_sets = [0, vertex_weights[0]]
    for i in range(2, num_vertices + 1):
        max_weight_sets.append(max(max_weight_sets[i - 1], max_weight_sets[i - 2] + vertex_weights[i - 1]))

    # reconstruct path
    path = []
    j = num_vertices
    while j >= 1:
        if max_weight_sets[j - 1] >= max_weight_sets[j - 2] + vertex_weights[j - 1]:
            j -= 1
        else:
            path.append(j)
            j -= 2

    # print(path)
    res_bits = ""
    for k in [1, 2, 3, 4, 17, 117, 517, 997]:
        if k in path:
            res_bits += "1"
        else:
            res_bits += "0"

    print("Solution question 2:", res_bits)


if __name__ == '__main__':
    huffman(path_input)  # max 19, min 9
    huffman(path_input_ex)  # should be max 4, min 2
    max_weight_independent(path_input_2)
    # max_weight_independent(path_input_ex_2)  # should be 990
    max_weight_independent(path_input)  # should be 10010010


