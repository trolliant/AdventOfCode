import bisect
totalSimilarity = 0
leftList = []
rightList = []

with open("input.txt", "r") as file:
    for numList in file:
        numList = (numList.split("   "))

        num1 = int(numList[0])
        num2 = int(numList[1].rstrip())

        bisect.insort(leftList, num1)
        bisect.insort(rightList, num2)
    file.close()

for i in leftList:
    similarity = 0
    for j in rightList:
        if i == j:
            similarity += 1
    totalSimilarity += similarity * i
print(totalSimilarity)