import sys
import math

from chemical_class import Equation


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# unbalanced = input()
unbalanced = "H2 + O2 -> H2O"

equation = Equation(unbalanced)
equation.parse_seq()
solution = equation.solve()

if solution == "2H2 + O2 -> 2H2O":
    print("You dit it :)")
else:
    print("ERROR: Wrong solution "+format(solution))

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# print(solution)
