import os
import heapq
from collections import defaultdict
import sys

path_input = os.getcwd() + "/Module_2_Week2_Assignment_Input.txt"


def solve():
    edges = dict()  # key: node, val: pair of node + weight

    with open(path_input, "r") as f:
        for line in f:
            split = line.split()
            edges[int(split[0])] = [[int(y) for y in x.split(",")] for x in split[1:]]
    visited = set()
    endpos = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    distances = defaultdict(lambda: sys.maxsize)
    queue = [(0, 1)]  # weight, node
    heapq.heapify(queue)
    while len(queue) != 0:
        weight, node = heapq.heappop(queue)
        visited.add(node)
        for nb in edges[node]:
            new_weight = nb[1] + weight
            if nb[1] not in visited and new_weight < distances[nb[0]]:
                heapq.heappush(queue, (new_weight, nb[0]))
                distances[nb[0]] = new_weight
    print(",".join([str(distances[pos]) for pos in endpos]))


if __name__ == '__main__':
    solve()
