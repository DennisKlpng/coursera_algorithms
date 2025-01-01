import os
import heapq

path_input = os.getcwd() + "/Module_2_Week3_Assignment_Input.txt"


def solve(numbers: list):
    curr_median = 0
    heap_low, heap_high = [], []

    for num in numbers:
        if len(heap_high) == 0 or num > heap_high[0]:
            heapq.heappush(heap_high, num)
        else:
            heapq.heappush(heap_low, num * -1)
        if len(heap_high) > (1 + len(heap_low)):
            # take smallest element from heap high and stuff it into heap low
            heapq.heappush(heap_low, -1 * heapq.heappop(heap_high))
        elif len(heap_low) > (1 + len(heap_high)):
            heapq.heappush(heap_high, -1 * heapq.heappop(heap_low))
        if len(heap_high) > len(heap_low):
            curr_median += heap_high[0]
        elif len(heap_high) < len(heap_low):
            curr_median += heap_low[0]*-1
        else:
            curr_median += heap_low[0]*-1
        curr_median = curr_median % 10000

    return curr_median


if __name__ == '__main__':
    with open(path_input, "r") as f:
        numbers_assignment = [int(line) for line in f]
    numbers_test_1 = [1, 666, 10, 667, 100, 2, 3]
    assert 142 == solve(numbers_test_1)
    numbers_test_2 = [6331, 2793, 1640, 9290, 225, 625, 6195, 2303, 5685, 1354]
    assert 9335 == solve(numbers_test_2)

    print(f"assignment res: {solve(numbers_assignment)}")