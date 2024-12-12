from collections import Counter

with open("input.txt", "r") as file:
    stones = Counter(map(int, file.read().split()))

for i in range(10000):
    new_stones = Counter()
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
        else:
            stone_str = str(stone)
            if len(stone_str) % 2 == 0:
                mid = len(stone_str) // 2
                new_stones[int(stone_str[:mid])] += count
                new_stones[int(stone_str[mid:])] += count
            else:
                new_stones[stone * 2024] += count
    stones = new_stones
    print(f"loop {i+1} completed, current num of stones: {sum(new_stones.values())}")

print(f"total stones: {sum(stones.values())}")