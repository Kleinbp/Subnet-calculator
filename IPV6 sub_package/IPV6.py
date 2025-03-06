def solve_equations(a, b, c, d, e, f):
    for x in range(-10, 11):
        for y in range(-10, 11):
            if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
                print(f"Solution found: X = {x}, Y = {y}")
                return
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter constant c: "))
d = int(input("Enter coefficient d: "))
e = int(input("Enter coefficient e: "))
f = int(input("Enter constant f: "))
solve_equations(a, b, c, d, e, f)
