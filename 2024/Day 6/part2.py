from copy import deepcopy

with open("input.txt", "r") as file:
    area = [list(line.strip()) for line in file]
    directions = {0: [-1,0], 1: [0,1], 2: [1,0], 3: [0,-1]}
    loops = 0
    rows = len(area)
    columns = len(area[0])
    for row in range(rows):
        for column in range(columns):
            if area[row][column] == "^":
                start_row, start_column = row, column

    for row in range(rows):
        for column in range(columns):
            obstruction = deepcopy(area)
            print(f"[{row}][{column}]")
            if obstruction[row][column] == ".":
                obstruction[row][column] = "O"
                position = [start_row, start_column]
                direction = 0
                prev_states = set()

                while True:
                    state = (tuple(position), direction)

                    if state in prev_states:
                        loops += 1
                        break

                    prev_states.add(state)
                    a, b = position
                    x, y = directions[direction]

                    if a+x >= rows or b+y >= columns or a+x < 0 or b+y < 0:
                        break

                    if obstruction[a+x][b+y] in ["#", "O"]:
                        old_direction = direction
                        if direction != 3:
                            direction += 1
                        else:
                            direction = 0
                    else:
                        position[0] += x
                        position[1] += y

print(f"loops: {loops}")