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
    print(f"{checkline} is {"safe" if diff and (inc or dec) else "unsafe"}")
    return diff and (inc or dec)

safeReports = 0
for x in reports:
    if safecheck(x):
        safeReports += 1
print(f"{safeReports} safe reports")