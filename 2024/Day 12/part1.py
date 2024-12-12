with open('input.txt', 'r') as file:
    map_data = [list(line.strip()) for line in file]

visited = set()
total_price = 0

for x in range(len(map_data)):
    for y in range(len(map_data[0])):
        if (x, y) not in visited:
            stack = [(x, y)]
            region = []
            plant_type = map_data[x][y]

            while stack:
                cx, cy = stack.pop()
                if (cx, cy) not in visited:
                    visited.add((cx, cy))
                    region.append((cx, cy))
                    neighbours = []
                    if cx > 0:
                        neighbours.append((cx - 1, cy))
                    if cx < len(map_data) - 1:
                        neighbours.append((cx + 1, cy))
                    if cy > 0:
                        neighbours.append((cx, cy - 1))
                    if cy < len(map_data[0]) - 1:
                        neighbours.append((cx, cy + 1))
                    for nx, ny in neighbours:
                        if map_data[nx][ny] == plant_type and (nx, ny) not in visited:
                            stack.append((nx, ny))

            area = len(region)
            perimeter = 0
            for rx, ry in region:
                if rx == 0 or map_data[rx-1][ry] != plant_type:
                    perimeter += 1
                if rx == len(map_data)-1 or map_data[rx+1][ry] != plant_type:
                    perimeter += 1
                if ry == 0 or map_data[rx][ry-1] != plant_type:
                    perimeter += 1
                if ry == len(map_data[0])-1 or map_data[rx][ry+1] != plant_type:
                    perimeter += 1

            total_price += area * perimeter

print(f"total fence price: {total_price}")