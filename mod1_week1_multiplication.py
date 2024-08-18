num_1 = 3141592653589793238462643383279502884197169399375105820974944592
num_2 = 2718281828459045235360287471352662497757247093699959574966967627

res_correct = num_1*num_2


def recursive_multiplication(num_a, num_b):
    num_length = max(len(str(num_a)), len(str(num_b)))
    if num_length == 1:
        return num_a * num_b
    if num_length % 2 != 0:
        num_length += 1

    num_a_str = str(num_a).zfill(num_length)
    num_b_str = str(num_b).zfill(num_length)

    half_length = int(num_length / 2)

    x_1 = int(num_a_str[:half_length])
    x_2 = int(num_a_str[half_length:])
    y_1 = int(num_b_str[:half_length])
    y_2 = int(num_b_str[half_length:])
    p1 = recursive_multiplication(x_1, y_1)
    p2 = recursive_multiplication(x_2, y_2)
    p3 = recursive_multiplication(x_1 + x_2, y_1 + y_2)

    return p1 * pow(10, num_length) + (p3 - p1 - p2) * pow(10, half_length) + p2


print(f"python internal multiplication: {res_correct}")
print(f"recursive multiplication: {recursive_multiplication(num_1, num_2)}")
print(f"diff: {res_correct - recursive_multiplication(num_1, num_2)}")
