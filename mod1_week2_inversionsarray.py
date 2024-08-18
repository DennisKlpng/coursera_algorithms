import os
path_input = os.getcwd() + "/Module_1_Week2_Assignment_Input.txt"

brute_force_solution = 2407905288

test_array = [1, 3, 5, 2, 4, 6]
test_array_inversions = 3

test_array_2 = [4, 1, 3, 2, 6, 5]


def brute_force(arr):
    count = 0
    n = len(arr)
    for i in range(n - 1):  # only iterate until second to last
        for j in range(i + 1, n):  # start one after i, go to end
            if arr[i] > arr[j]:
                count += 1
    return count


def cross_calc_merge(l_arr, r_arr):
    merged_array = []
    ct = 0
    l_index, r_index = 0, 0
    len_l = len(l_arr)
    len_r = len(r_arr)
    while True:
        if l_index == len_l:
            merged_array.extend(r_arr[r_index:])
            return merged_array, ct
        if r_index == len_r:
            merged_array.extend((l_arr[l_index:]))
            return merged_array, ct
        if l_arr[l_index] < r_arr[r_index]:
            merged_array.append(l_arr[l_index])
            l_index += 1
        else:  # l_arr[l_index] > r_arr[r_index]
            merged_array.append(r_arr[r_index])
            r_index += 1
            ct += (len_l - l_index)
    return merged_array, ct


def recursive(arr):
    n = len(arr)
    if n == 1:
        return arr, 0
    if n == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]], 1
        return arr, 0
    divider = int(n/2)
    l_sorted, l_ct = recursive(arr[:divider])
    r_sorted, r_ct = recursive(arr[divider:])
    c_sorted, c_ct = cross_calc_merge(l_sorted, r_sorted)
    return c_sorted, l_ct + r_ct + c_ct


if __name__ == '__main__':
    array = []
    with open(path_input, "r") as f:
        array = [int(x) for x in f.read().splitlines()]
    # print(f"Brute force solution: {brute_force(array)}")
    print(f"Brute force cached solution: {brute_force_solution}")
    # print(f"Recursive Test: {recursive(test_array)[1]}")
    print(f"Recursive solution: {recursive(array)[1]}")

    # print(f"Brute force Test 2: {brute_force(test_array_2)}")
    # print(f"Recursive Test 2: {recursive(test_array_2)[1]}")

