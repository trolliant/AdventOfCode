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
    return diff and (inc or dec)

safe_reports = sum(1 for x in reports if safecheck(x))
print(f"{safe_reports} safe reports")