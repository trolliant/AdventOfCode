import re

with open('input.txt', 'r') as file:
    machines = re.findall(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)", file.read())
    total = 0

    for info in machines:
        ax, ay, bx, by, px, py = map(int, info)
        found = False

        for a in range(101):
            if found:
                break
            for b in range(101):
                x = a * ax + b * bx
                y = a * ay + b * by
                if x == px and y == py:
                    tokens = (a * 3) + b
                    total += tokens
                    found = True
                    break

    print(f"total tokens: {total}")