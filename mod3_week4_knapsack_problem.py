import os
from numba import jit
import numpy as np

path_input = os.getcwd() + "/Module_3_Week4_Assignment_Input.txt"
path_input_ex = os.getcwd() + "/Module_3_Week4_Assignment_Input_ex.txt"
path_input_2 = os.getcwd() + "/Module_3_Week4_Assignment_Input_b.txt"


@jit(nopython=True)
def knapsack_calc(items, total_weight):
    vals = [0] * (total_weight + 1)
    for i in range(len(items)):
        for j in range(total_weight, items[i][1] - 1, -1):
            curr_item = items[i]
            vals[j] = max(vals[j], vals[j - curr_item[1]] + curr_item[0])
    return max(vals)


def knapsack(filename):
    with open(filename, "r") as f:
        total_weight = int(f.readline().split()[0])
        items = [[int(y) for y in x.split(" ")] for x in f.readlines()]   # value, weight

    print(f"Solution optimal value: {knapsack_calc(np.array(items), total_weight)}")


if __name__ == '__main__':
    knapsack(path_input_ex)  # should be 8
    knapsack(path_input)  # 2493893
    knapsack(path_input_2)
