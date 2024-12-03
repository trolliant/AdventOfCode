import re

with open("input.txt", "r") as file:
    corrupt_memory = file.read()
    file.close()

matches = re.findall(r"mul\((\d+),(\d+)\)", corrupt_memory)
total = sum(int(x[0]) * int(x[1]) for x in matches)
print(f"total: {total}")