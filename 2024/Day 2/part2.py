with open("input.txt", "r") as file:
    reports = [list(map(int, line.strip().split())) for line in file]
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
    for level in range(len(checkline)):
        loopline = checkline[:level] + checkline[level+1:]
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

safe_reports = sum(1 for x in reports if safecheck(x))
print(f"{safe_reports} safe reports")