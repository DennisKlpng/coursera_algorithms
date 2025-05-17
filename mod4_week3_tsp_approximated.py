import os
import math

path_input = os.getcwd() + "/Module_4_Week3_Assignment_Input.txt"

order_visited = [1]


def get_nearest(index: int, cities_list: list, already_visited: set):
    min_dist = math.inf
    nearest_index = 0
    _, x_src, y_src = cities_list[index]

    for i in range(index, -1, -1):  # iterate to the left
        if i in already_visited:
            continue
        _, x_dst, y_dst = cities_list[i]
        if pow(x_dst - x_src, 2) > min_dist:
            break  # exit early if the x-dist is already greater than the current min, since cities are sorted by x
        dist = pow(x_dst - x_src, 2) + pow(y_dst - y_src, 2)
        if dist == min_dist:
            # if we iterate left we have to deal with ties
            nearest_index = i
        elif dist < min_dist:
            min_dist = dist
            nearest_index = i

    for i in range(index, len(cities_list)):  # iterate to the right
        if i in already_visited:
            continue
        _, x_dst, y_dst = cities_list[i]
        if pow(x_dst - x_src, 2) > min_dist:
            break  # exit early if the x-dist is already greater than the current min, since cities are sorted by x
        dist = pow(x_dst - x_src, 2) + pow(y_dst - y_src, 2)
        if dist < min_dist:
            min_dist = dist
            nearest_index = i

    if min_dist > 1000000000:
        print("ERROR")
    already_visited.add(nearest_index)
    order_visited.append(nearest_index+1)
    return math.sqrt(min_dist), nearest_index


def tsp_solve(filename):
    with open(filename, "r") as f:
        num_cities = int(f.readline())
        city_coords = [[float(y) for y in x.split()] for x in f.readlines()]

        # dbg
        # city_coords = city_coords[:50]
        # num_cities = 50

        visited_cities = set()
        visited_cities.add(0)
        curr_index = 0
        total_dist = 0.0
        while len(visited_cities) != num_cities:
            new_dist, curr_index = get_nearest(curr_index, city_coords, visited_cities)
            total_dist += new_dist

        # add way back to start city:
        _, x_dst, y_dst = city_coords[0]
        _, x_src, y_src = city_coords[curr_index]
        total_dist += math.sqrt(pow(x_dst - x_src, 2) + pow(y_dst - y_src, 2))
        print(int(total_dist))
        # print(order_visited)


if __name__ == '__main__':
    tsp_solve(path_input)
