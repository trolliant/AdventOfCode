import re

with open("input.txt", "r") as file:
    lines = [line.rstrip() for line in file.readlines()]
    rules = re.findall(r"(\d+)\|(\d+)", str(lines))
    updates = [line.split(",") for line in lines if "," in line and line]
    ordered_updates = []
    file.close()

for update in updates:
    ordered = True
    for rule1, rule2 in rules:
        if rule1 in update and rule2 in update:
            page1 = update.index(rule1)
            page2 = update.index(rule2)
            if page1 > page2:
                ordered = False
                break
    if ordered:
        ordered_updates.append(update)

total = sum([int(update[len(update) // 2]) for update in ordered_updates])
print(f"total: {total}")