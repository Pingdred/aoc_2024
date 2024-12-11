from typing import List
from tqdm import tqdm
from functools import lru_cache


def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().split(" ")
        return [int(num) for num in data]
    
    
@lru_cache(maxsize=None)
def apply_rules(stone: int, depth: int) -> List:

    if depth == 0:
        return 1

    new_stones = []

    stone_str = str(stone)
    stone_len = len(stone_str)

    if stone == 0:
        new_stones.append(1)
    elif stone_len % 2 == 0:
        left = stone_str[:stone_len//2]
        right = stone_str[stone_len//2:]
        new_stones += [int(left), int(right)]
    else:
        new_stones.append(stone*2024)

    tot = 0
    for s in new_stones:
        tot += apply_rules(s, depth-1)

    return tot


if __name__ == "__main__":
    stones = load_data("input.txt")
    print(stones)

    final_stones = 0
    for stone in tqdm(stones):
        final_stones += apply_rules(stone, 75)

    print(final_stones)