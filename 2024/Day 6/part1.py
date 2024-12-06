with open("input.txt", "r") as file:
    area = [list(line.strip()) for line in file]
    direction = 0
    directions = {0: [-1,0], 1: [0,1], 2: [1,0], 3: [0,-1]}
    visited = set()
    rows = len(area)
    columns = len(area[0])
    for row in range(rows):
        for column in range(columns):
            if area[row][column] == "^":
                position = [row,column]
                visited.add((row, column))

    while True:
        a, b = position
        x, y = directions[direction]

        if a+x >= rows or b+y >= columns or a+x < 0 or b+y < 0:
            break

        if area[a+x][b+y] == "#":
            if direction != 3:
                direction += 1
            else:
                direction = 0
        else:
            position[0] += x
            position[1] += y
            visited.add((position[0], position[1]))

print(f"total: {len(visited)}")