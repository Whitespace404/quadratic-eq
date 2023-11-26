import random
import time


def generate_quadratic_equation():
    a = random.choice([random.randint(-15, -1), random.randint(1, 15)])
    b = random.randint(-15, 15)
    c = random.randint(-15, 15)

    equation = f"{a}x^2 + {b}x + {c} = 0"

    return equation


start = time.time()
equation = generate_quadratic_equation()
input(equation)
end = time.time()

print(f"{round(end - start, 2)} s")
