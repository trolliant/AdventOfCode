import re

with open("input.txt", "r") as file:
    lines = re.findall(r"(\d+):\s(.+)", file.read())
    lines = [[line[0], line[1].split()] for line in lines]
    total = 0

    for line in lines:
        target = int(line[0])
        nums = [int(num) for num in line[1]]
        operator_num = len(nums) - 1

        for i in range(3 ** operator_num):
            operators = []
            temp = i
            for j in range(operator_num):
                if temp % 3 == 0:
                    operators.append("+")
                elif temp % 3 == 1:
                    operators.append("*")
                else:
                    operators.append("||")
                temp //= 3

            result = nums[0]
            valid = True
            for j in range(len(operators)):
                if operators[j] == "+":
                    result += nums[j+1]
                elif operators[j] == '*':
                    result *= nums[j+1]
                elif operators[j] == '||':
                    result = int(str(result) + str(nums[j+1]))
                else:
                    valid = False
                    break

            if valid and result == target:
                expr = str(nums[0])

                for j in range(len(operators)):
                    expr += operators[j] + str(nums[j+1])

                total += target
                break

print(f"total calibration result: {total}")