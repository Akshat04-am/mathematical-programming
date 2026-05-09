import math
def vertex_and_roots(a,b,c):
    #prints the equation
    print(f"Equation: {a}x^2 + {b}x + {c}")

    vertex_x = -b/(2*a)
    vertex_y = a*(vertex_x**2) + b*vertex_x + c
    print(f"Vertexes: {vertex_x},{vertex_y}")

    d = b**2 - 4*a*c
    if d > 0:
        root_1 = (-b + math.sqrt(d))/(2*a)
        root_2 = (-b - math.sqrt(d))/(2*a)
        print(f"Root 1 and 2: {root_1},{root_2}")
    else:
        print("No real roots.")

vertex_and_roots(1,4,1)