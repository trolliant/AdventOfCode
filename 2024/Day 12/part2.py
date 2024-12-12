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
            edges = set()

            for rx, ry in region:
                if rx == 0 or map_data[rx-1][ry] != plant_type:
                    edges.add((rx, ry, 'top'))
                if rx == len(map_data)-1 or map_data[rx+1][ry] != plant_type:
                    edges.add((rx, ry, 'bottom'))
                if ry == 0 or map_data[rx][ry-1] != plant_type:
                    edges.add((rx, ry, 'left'))
                if ry == len(map_data[0])-1 or map_data[rx][ry+1] != plant_type:
                    edges.add((rx, ry, 'right'))

            sides = 0
            for direction in ['top', 'bottom', 'left', 'right']:
                direction_edges = {(x, y) for x, y, d in edges if d == direction}
                while direction_edges:
                    current_side = set()
                    start = direction_edges.pop()
                    current_side.add(start)
                    start_x, start_y = start

                    if direction in ['top', 'bottom']:
                        check_y = start_y - 1
                        while (start_x, check_y) in direction_edges:
                            current_side.add((start_x, check_y))
                            direction_edges.remove((start_x, check_y))
                            check_y -= 1

                        check_y = start_y + 1
                        while (start_x, check_y) in direction_edges:
                            current_side.add((start_x, check_y))
                            direction_edges.remove((start_x, check_y))
                            check_y += 1
                    else:
                        check_x = start_x - 1
                        while (check_x, start_y) in direction_edges:
                            current_side.add((check_x, start_y))
                            direction_edges.remove((check_x, start_y))
                            check_x -= 1

                        check_x = start_x + 1
                        while (check_x, start_y) in direction_edges:
                            current_side.add((check_x, start_y))
                            direction_edges.remove((check_x, start_y))
                            check_x += 1

                    sides += 1

            total_price += area * sides

print(f"total fence price: {total_price}")