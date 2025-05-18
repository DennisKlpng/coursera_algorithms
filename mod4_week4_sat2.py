import time
from z3 import *

path_inputs = [os.getcwd() + f"/Module_4_Week4_Assignment_Input_{i+1}.txt" for i in range(6)]

path_input_test = os.getcwd() + "/Module_4_Week4_Assignment_Input_test.txt"
path_input_test_2 = os.getcwd() + "/Module_4_Week4_Assignment_Input_test_2.txt"


def z3_or_direct(input_cond):
    ctx = input_cond[0].ctx
    _es = (Ast * 2)()
    _es[0] = input_cond[0].as_ast()
    _es[1] = input_cond[1].as_ast()
    return BoolRef(Z3_mk_or(ctx.ref(), 2, _es), ctx)


def sat_solve(filename):
    s = Solver()
    with open(filename, "r") as f:
        start_time = time.time()
        num_vars = int(f.readline())
        sat_vars = ["0"]
        for i in range(1, num_vars+1):
            var = Bool(f"{i}")
            sat_vars.append(var)
        print(f"Time vor variable init: {time.time() - start_time}")
        start_time = time.time()
        for line in f.readlines():
            var1, var2 = [int(x) for x in line.split()]
            sat_var1, sat_var2 = sat_vars[abs(var1)], sat_vars[abs(var2)]
            if var1 < 0:
                sat_var1 = Not(sat_var1)
            if var2 < 0:
                sat_var2 = Not(sat_var2)
            clause = z3_or_direct([sat_var1, sat_var2])
            # clause = Or([sat_var1, sat_var2])
            s.add(clause)
        print(f"Time vor reading and parsing input: {time.time() - start_time}")

    print("Checking")
    result = s.check()
    print(f"Solved sat2 with {num_vars} variables with result: {result}")
    if result == sat:
        return "1"
    return "0"


if __name__ == '__main__':
    res = ""
    # print(sat_solve(path_input_test))
    # print(sat_solve(path_input_test_2))
    for input_path in path_inputs:
        res += sat_solve(input_path)
    print(res)
    

