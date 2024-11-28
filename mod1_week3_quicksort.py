import os, math, statistics, copy
path_input = os.getcwd() + "/Module_1_Week3_Assignment_Input.txt"


def calc_pivot_first(input_array, l, r):
    return input_array[l]


def calc_pivot_last(input_array, l, r):
    input_array[l], input_array[r] = input_array[r], input_array[l]
    return input_array[l]


def calc_pivot_median(input_array, l, r):
    vals = [input_array[l], input_array[r], input_array[int((r+l)/2)]]
    median = statistics.median(vals)
    index_median = input_array.index(median)
    input_array[l], input_array[index_median] = input_array[index_median], input_array[l]
    return median


def recursive_sort(sorting_array, l, r, pivot_calc):
    global rec_num_comps
    #print(f"l: {l}, r: {r}, array to analyze: {sorting_array[l:r+1]}")
    if (r - l) < 1:
        return
    rec_num_comps += (r - l)
    p = pivot_calc(sorting_array, l, r)
    #print(f"pivot: {p}")
    i = l + 1  # i is the index of the first element in the upper array
    for j in range(l + 1, r + 1):  # r+1 since range excludes the upper bound
        if sorting_array[j] < p:
            sorting_array[j], sorting_array[i] = sorting_array[i], sorting_array[j]
            i += 1
    sorting_array[l], sorting_array[i-1] = sorting_array[i-1], sorting_array[l]
    recursive_sort(sorting_array, l, i - 2, pivot_calc)
    recursive_sort(sorting_array, i, r, pivot_calc)


if __name__ == '__main__':
    array = []
    with open(path_input, "r") as f:
        array = [int(x) for x in f.read().splitlines()]

    # pivot = calc_pivot_first(test_array)
    # print(pivot, " ", test_array)
    #
    # test_array_copy = copy.deepcopy(test_array)
    # pivot = calc_pivot_last(test_array_copy)
    # print(pivot, " ", test_array_copy)
    #
    # test_array_copy = copy.deepcopy(test_array)
    # pivot = calc_pivot_median(test_array_copy)
    # print(pivot, " ", test_array_copy)

    recursive_sort(array, 0, len(array) - 1, calc_pivot_median)
    print(rec_num_comps)

# first: 162085
# last: 164123
# median: 138382
