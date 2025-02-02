import os
from functools import cmp_to_key

path_input = os.getcwd() + "/Module_3_Week1_Assignment_Input.txt"
path_input_mst = os.getcwd() + "/Module_3_Week1_Assignment_Input_b.txt"


def compare_diff(a, b):
    if (a[0] - a[1]) > (b[0] - b[1]):
        return -1
    elif (a[0] - a[1]) < (b[0] - b[1]):
        return 1
    elif a[0] > b[0]:
        return -1
    return 1


def compare_ratio(a, b):
    if (a[0] / a[1]) >= (b[0] / b[1]):
        return -1
    return 1


def get_sum(sorted_jobs):
    compl_time = 0
    res = 0
    for job in sorted_jobs:
        compl_time += job[1]
        res += compl_time * job[0]
    return res


if __name__ == '__main__':
    with open(path_input, "r") as f:
        num_jobs = f.readline()
        jobs = [[int(y) for y in x.split()] for x in f.readlines()]  # weight length
    jobs = sorted(jobs, key=cmp_to_key(compare_diff))
    print(f"res 1: {get_sum(jobs)}")
    jobs = sorted(jobs, key=cmp_to_key(compare_ratio))
    print(f"res 2: {get_sum(jobs)}")

    with open(path_input_mst, "r") as f:
        (num_vertices, num_edges) = f.readline().split()
        edges = [[int(y) for y in x.split()] for x in f.readlines()]  # vert_1 vert_2 cost
    edges = sorted(edges, key=lambda x: x[2])
    # initialize
    X = {edges[0][0]}
    total_cost = 0
    while len(X) != int(num_vertices):
        for edge in edges:
            if edge[0] in X and edge[1] not in X:
                total_cost += edge[2]
                X.add(edge[1])
                break
            elif edge[1] in X and edge[0] not in X:
                total_cost += edge[2]
                X.add(edge[0])
                break
            else:
                continue
    print(f"res 3: {total_cost}")

    