with open("input.txt", "r") as file:
    stones = list(map(int, file.read().split()))

for i in range(25):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            new_stones.append(str(stone)[:mid])
            new_stones.append(str(stone)[mid:])
        else:
            new_stones.append(stone*2024)
    stones = list(map(int, new_stones))
    print(f"loop {i+1} completed, current num of stones: {len(stones)}")

print(f"total stones: {len(stones)}")