import bisect

left_list = []
right_list = []

with open("input.txt", "r") as file:
    for num_list in file:
        num_list = (num_list.split("   "))
        bisect.insort(left_list, int(num_list[1].rstrip()))
        bisect.insort(right_list, int(num_list[0]))
    file.close()

total_dist = sum(abs(num - right_list[i]) for i, num in enumerate(left_list))
print(f"final distance: {total_dist}")