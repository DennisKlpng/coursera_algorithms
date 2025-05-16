import os
import numpy
import math
from numba import jit

path_input_a = os.getcwd() + "/Module_4_Week1_Assignment_Input_a.txt"
path_input_b = os.getcwd() + "/Module_4_Week1_Assignment_Input_b.txt"
path_input_c = os.getcwd() + "/Module_4_Week1_Assignment_Input_c.txt"

path_input_test = os.getcwd() + "/Module_4_Week1_Assignment_Input_test.txt"


@jit(nopython=True)
def floyd_warshall(matrix):
    dim = len(matrix)
    # Using floyd-warshall algorithm to calculate the distances between all vertices
    for k in range(dim):
        for i in range(dim):
            for j in range(dim):
                if matrix[i, j] > matrix[i, k] + matrix[k, j]:
                    matrix[i, j] = matrix[i, k] + matrix[k, j]
    return matrix


def floyd_warshall_solve(filename):
    with open(filename, "r") as f:
        num_vertices = int(f.readline().split()[0])
        shortest_paths = numpy.full((num_vertices, num_vertices), math.inf)
        for i in range(num_vertices):
            shortest_paths[i, i] = 0
        for line in f.readlines():
            tail, head, weight = [int(y) for y in line.split()]
            shortest_paths[tail-1, head-1] = weight

        floyd_warshall(shortest_paths)

        # check if any diagonal element is < 0 => negative cycle
        if numpy.trace(shortest_paths) < 0:
            return None
        else:
            return numpy.min(shortest_paths[numpy.nonzero(shortest_paths)])


if __name__ == '__main__':
    print(floyd_warshall_solve(path_input_a))
    print(floyd_warshall_solve(path_input_b))
    print(floyd_warshall_solve(path_input_c))
    # print(floyd_warshall_solve(path_input_test))
