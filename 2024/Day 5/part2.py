import re

with open("input.txt", "r") as file:
    lines = [line.rstrip() for line in file.readlines()]
    rules = re.findall(r"(\d+)\|(\d+)", str(lines))
    updates = [line.split(",") for line in lines if "," in line and line]
    unordered_updates = []
    file.close()

for update in updates:
    unordered = False
    for rule1, rule2 in rules:
        if rule1 in update and rule2 in update:
            page1 = update.index(rule1)
            page2 = update.index(rule2)
            if page1 > page2:
                unordered = True
                break
    if unordered:
        unordered_updates.append(update)

for update in unordered_updates:
    swapped = True
    while swapped:
        swapped = False
        for rule1, rule2 in rules:
            if rule1 in update and rule2 in update:
                page1 = update.index(rule1)
                page2 = update.index(rule2)
                if page1 > page2:
                    update[page1], update[page2] = update[page2], update[page1]
                    swapped = True

total = sum([int(update[len(update) // 2]) for update in unordered_updates])
print(f"total: {total}")