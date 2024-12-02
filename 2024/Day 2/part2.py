with open("input.txt", "r") as file:
    reports = []
    lines = file.readlines()
    for line in lines:
        line = line.rstrip()
        line = line.split(" ")
        line = [int(num) for num in line]
        reports.append(line)
    file.close()

def safecheck(checkline):
    diff = inc = dec = True
    for level in range(1, len(checkline)):
        if checkline[level] < checkline[level-1]: # increase check
            inc = False
        if checkline[level] > checkline[level-1]: # decrease check
            dec = False
        if abs(checkline[level] - checkline[level-1]) not in range(1,4): # difference check
            diff = False
    if not (diff and (inc or dec)):
        return dampencheck(checkline)
    else:
        return True

def dampencheck(checkline):
    diff = inc = dec = True
    for level in range(len(checkline)):
        loopline = checkline[:level] + checkline[level+1:] # originally used loopline.remove(loopline[level-1]), this would cause issues with duplicate values as it removes only the first occurrence of the number, not the one at the correct index, which resulted in 470 safe instead
        print(loopline)
        diff = inc = dec = True
        for looplevel in range(1, len(loopline)):
            if loopline[looplevel] < loopline[looplevel-1]:
                inc = False
            if loopline[looplevel] > loopline[looplevel-1]:
                dec = False
            if abs(loopline[looplevel] - loopline[looplevel-1]) not in range(1,4):
                diff = False
        if diff and (inc or dec):
            return True
    return False

safeReports = 0
for x in reports:
    if safecheck(x):
        safeReports += 1
print(f"{safeReports} safe reports")