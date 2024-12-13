import re
from math import ceil

with open('input.txt', 'r') as file:
    machines = re.findall(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)", file.read())
    total = 0

    for info in machines:
        ax, ay, bx, by, px, py = map(int, info)
        px += 10000000000000
        py += 10000000000000

        found = False
        determinant = ax * by - ay * bx

        if determinant != 0:
            a_float = (px * by - py * bx) / determinant
            b_float = (py * ax - px * ay) / determinant

            a_min = ceil(max(0, a_float))
            b_min = ceil(max(0, b_float))

            a = a_min
            b = b_min

            x = a * ax + b * bx
            y = a * ay + b * by

            if x == px and y == py:
                tokens = (a * 3) + b
                total += tokens

    print(f"total tokens: {total}")