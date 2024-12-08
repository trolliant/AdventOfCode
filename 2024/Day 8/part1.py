from collections import defaultdict

with open("input.txt", "r") as file:
    grid = [line.strip() for line in file.readlines()]

width = len(grid[0])
height = len(grid)

antennas = defaultdict(list)
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell.isalnum():
            antennas[cell].append((x, y))

antinodes = set()

for freq, positions in antennas.items():
    for i in range(len(positions)):
        for j in range(len(positions)):
            if i != j:
                a = positions[i]
                b = positions[j]
                dx, dy = b[0] - a[0], b[1] - a[1]
                nx, ny = b[0] + dx, b[1] + dy

                if 0 <= nx < width and 0 <= ny < height:
                    antinodes.add((nx, ny))

print(f"total: {len(antinodes)}")