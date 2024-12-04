with open("input.txt", "r") as file:
    wordsearch = [list(line.strip()) for line in file]
    word = "XMAS"
    file.close()

rows = len(wordsearch)
columns = len(wordsearch[0])
directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
occurrences = 0

for row in range(rows):
    for column in range(columns):
        if wordsearch[row][column] == word[0]:
            for dx, dy in directions:
                if not (0 <= row + dx*(len(word)-1) < rows and 0 <= column + dy*(len(word)-1) < columns):
                    continue
                found = True
                for i in range(len(word)):
                    if wordsearch[row + dx*i][column + dy*i] != word[i]:
                        found = False
                        break
                if found:
                    occurrences += 1

print(f"{occurrences} instances of {word}")