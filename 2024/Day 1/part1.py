import bisect

left_list = []
right_list = []

with open("input.txt", "r") as file:
    for num_list in file:
        num_list = (num_list.split("   "))
        num1 = int(num_list[0])
        num2 = int(num_list[1].rstrip())
        bisect.insort(left_list, num1)
        bisect.insort(right_list, num2)
    file.close()

total_dist = sum(abs(num1 - right_list[i]) for i, num1 in enumerate(left_list))
print(f"final distance: {total_dist}")