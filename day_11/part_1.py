from typing import List
from functools import lru_cache


def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().split(" ")
        return [int(num) for num in data]


@lru_cache(maxsize=None)
def apply_rules(stone: int) -> List:
    stone_str = str(stone)
    stone_len = len(stone_str)

    if stone == 0:
        return [1]

    if stone_len % 2 == 0:
        left =stone_str[:stone_len//2]
        right =stone_str[stone_len//2:]

        return [int(left), int(right)]
        
    return [stone*2024]


def blink(stones: List):
    new_stones = []
    for s in stones:
        new_stones += apply_rules(s)
        
    return new_stones


if __name__ == "__main__":
    stones = load_data("input.txt")
    print(stones)

    for i in range(25):
        stones = blink(stones)

    print(len(stones))

    

