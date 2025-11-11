import math

def discriminant(a, b, c):
    return b**2 - 4*a*c

def quadratic_roots(a, b, c):
    D = discriminant(a, b, c)
    print(f"Discriminant: {D}")

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"Two roots: x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = -b / (2*a)
        print(f"One root: x = {x}")
    else:
        print("No real roots")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

quadratic_roots(a, b, c)
