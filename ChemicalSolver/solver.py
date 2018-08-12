import sys
import math

from chemical_class import Equation


NB_TRY = 10


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

with open("test_equations.txt") as f:
    for line in f.readlines():
        print('solving {} {} times...'.format(line.rstrip(), NB_TRY))
        # get equation and solution from test file
        unbalanced, balanced = line.rstrip().split(' => ')

        # parse equation
        equation = Equation(unbalanced)
        equation.parse_seq()

        # find a solution and assert it is correct (a lot of times)
        for i in range(NB_TRY):
            solution = equation.solve()

            assert solution == balanced, "ERROR: Wrong solution {}".format(solution)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# print(solution)
