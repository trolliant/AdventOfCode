import re

with open("input.txt", "r") as file:
    lines = re.findall(r"(\d+):\s(.+)", file.read())
    lines = [[line[0], line[1].split()] for line in lines]
    total = 0

    for line in lines:
        target = int(line[0])
        nums = [int(num) for num in line[1]]
        operator_num = len(nums) - 1

        for i in range(2 ** operator_num):
            operators = []
            temp = i
            for j in range(operator_num):
                if temp % 2 == 0:
                    operators.append("+")
                else:
                    operators.append("*")
                temp //= 2

            result = nums[0]
            for j in range(len(operators)):
                if operators[j] == "+":
                    result += nums[j+1]
                else:
                    result *= nums[j+1]

            if result == target:
                expr = str(nums[0])

                for j in range(len(operators)):
                    expr += operators[j] + str(nums[j+1])

                total += target
                break

print(f"total calibration result: {total}")