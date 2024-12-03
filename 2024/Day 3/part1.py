import re
with open("input.txt", "r") as file:
    corrupt_memory = file.read()
    file.close()

matches = re.findall(r"mul\((\d+),(\d+)\)", corrupt_memory)
total = 0

for x in matches:
    total += int(x[0]) * int(x[1])
print(f"total is {total}")