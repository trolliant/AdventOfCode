with open("input.txt", "r") as file:
    wordsearch = [list(line.strip()) for line in file]
    file.close()

rows = len(wordsearch)
columns = len(wordsearch[0])
occurrences = 0

for row in range(1, rows - 1):
    for column in range(1, columns - 1):
        if wordsearch[row][column] != "A":
            continue
        try:
            diagonal1 = ((wordsearch[row - 1][column - 1] == "M" and wordsearch[row + 1][column + 1] == "S") or (wordsearch[row - 1][column - 1] == "S" and wordsearch[row + 1][column + 1] == "M"))
            diagonal2 = ((wordsearch[row - 1][column + 1] == "M" and wordsearch[row + 1][column - 1] == "S") or (wordsearch[row - 1][column + 1] == "S" and wordsearch[row + 1][column - 1] == "M"))
            if diagonal1 and diagonal2:
                occurrences += 1
        except IndexError:
            continue

print(f"{occurrences} X-MASes found :)")