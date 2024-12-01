import bisect
totalDist = 0
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

for i, num1 in enumerate(leftList):
    num2 = rightList[i]
    if num1 > num2:
        dist = num1 - num2
    else:
        dist = num2 - num1
    totalDist += dist
print(f"final distance: {totalDist}")