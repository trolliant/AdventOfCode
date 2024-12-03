import re
with open("input.txt", "r") as file:
    corrupt_memory = file.read()
    file.close()

matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", corrupt_memory)
enabled = True
total = 0

for x in matches:
    if x == "do()":
        enabled = True
    elif x == "don't()":
        enabled = False
    elif enabled:
        x = re.sub(r"mul\((\d+),(\d+)\)", r"\1 \2", x).split()
        total += int(x[0]) * int(x[1])

print(f"total is {total}")
