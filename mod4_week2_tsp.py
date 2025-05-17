import os
import numpy as np
import itertools
import math

path_input = os.getcwd() + "/Module_4_Week2_Assignment_Input.txt"


def tsp(dists, num_cities):
    # Solving with Held-Karp algorithm
    # Memoization array, initialize with initial distances from starting node (0 here, 1 in material)
    A = dict()
    for k in range(1, num_cities):
        A[(1 << k, k)] = dists[0, k]

    for size in range(2, num_cities):
        for subset in itertools.combinations(range(1, num_cities), size):
            # calculate bitmask for subset
            mask = 0
            for entry in subset:
                mask |= 1 << entry
            for k in subset:
                mask_wo_k = mask & ~(1 << k)
                arr = []
                for m in subset:
                    if m == k:
                        continue
                    arr.append(A[(mask_wo_k, m)] + dists[m, k])
                A[(mask, k)] = min(arr)

    # Find optimum by adding way back to start vertex
    arr = []
    # 2 ** n is 1 and n 0-s, substract 1 to get full bitmask, aka 25*1. Unset start pos by substracting 1
    bits_all_but_start = 2 ** num_cities - 1 - 1
    for k in range(1, num_cities):
        arr.append(A[(bits_all_but_start, k)] + dists[k, 0])
    return min(arr)


def calculate_dists(coords):
    num_cities = len(coords)
    dists = np.full((num_cities, num_cities), 0.0)
    for i in range(num_cities):
        for j in range(num_cities):
            dists[i, j] = math.sqrt(pow(coords[i][0] - coords[j][0], 2)
                                    + pow(coords[i][1] - coords[j][1], 2))
    return dists

def tsp_solve(filename):
    with open(filename, "r") as f:
        num_cities = int(f.readline())
        city_coords = [[float(y) for y in x.split()] for x in f.readlines()]
        # Heuristic: there's a bottleneck betwen nodes 11 and 12 (when starting at 0)
        # => split into two graphs both including 11 and 12, add paths, substract dist between 11 and 12 twice
        city_coords_lower = city_coords[:13]
        city_coords_upper = city_coords[11:]

        # calculate all distances
        dists_lower = calculate_dists(city_coords_lower)
        num_lower = len(city_coords_lower)

        dists_upper = calculate_dists(city_coords_upper)
        num_upper = len(city_coords_upper)

    # print(int(tsp(dists, num_cities)))  # goes out of memory
    res = tsp(dists_lower, num_lower) + tsp(dists_upper, num_upper)
    res -= 2 * dists_lower[11, 12]
    print(int(res))


if __name__ == '__main__':
    tsp_solve(path_input)
