import os
import bisect

path_input = os.getcwd() + "/Module_2_Week4_Assignment_Input.txt"


def solve(numbers: list, borders: tuple):
    t_min, t_max = borders
    adds = set()
    numbers.sort()
    for i in numbers:
        j_min = t_min - i
        j_max = t_max - i
        for k in range(bisect.bisect_left(numbers, j_min), bisect.bisect_right(numbers, j_max)):
            j = numbers[k]
            if i == j:
                continue
            sum_ij = i + j
            if t_min <= sum_ij <= t_max:
                adds.add(sum_ij)

    return len(adds)


if __name__ == '__main__':
    with open(path_input, "r") as f:
        numbers_assignment = list(set([int(line) for line in f]))
    borders_assignment = (-10000, 10000)
    numbers_test_1 = [-3, -1, 1, 2, 9, 11, 7, 6, 2]
    borders_test_1 = (3, 10)
    assert 8 == solve(numbers_test_1, borders_test_1)

    print(f"assignment res: {solve(numbers_assignment, borders_assignment)}")