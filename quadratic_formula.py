#問１
def solve(a, b, c):
        x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
        x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
        print(x1, end=" ")
        print(x2)

solve(1, -6, 9)
solve(1, 2, -8)
solve(8, -6, -35)
solve(1, 0, 1)
