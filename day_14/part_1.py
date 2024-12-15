import re
from typing import Dict, Tuple


def load_data(file_path: str) -> list:
    regex = r"p=(.*),(.*) v=(.*),(.*)"

    robots = []

    with open(file_path, "r") as file:
       for line in file:
            match = re.match(regex, line)
            
            robot = {
                "p": (int(match.group(2)), int(match.group(1))),
                "v": (int(match.group(4)), int(match.group(3)))
            }

            robots.append(robot)
    return robots


def move_robot(robot: Dict, bounds: Tuple) -> dict:
    p = robot["p"]
    v = robot["v"]

    new_p = (
        (p[0] + v[0]) % bounds[0], 
        (p[1] + v[1]) % bounds[1]
    )

    return  new_p


def main():
    robots = load_data("input.txt")

    cols = 101
    rows = 103

    for i in range(100):
        for r in robots:
            r["p"] = move_robot(r, (rows, cols))


    q_count = [0, 0, 0, 0]
    for r in robots:

        if r["p"][0] == rows // 2 or r["p"][1] == cols // 2:
            continue
        
        # Q1 top left
        if r["p"][0] < rows // 2 and r["p"][1] < cols // 2:
            q_count[0] += 1
            continue

        # Q2 top right
        if r["p"][0] < rows // 2 and r["p"][1] > cols // 2:
            q_count[1] += 1
            continue

        # Q3 bottom left
        if r["p"][0] > rows // 2 and r["p"][1] < cols // 2:
            q_count[2] += 1
            continue

        # Q4 bottom right
        if r["p"][0] > rows // 2 and r["p"][1] > cols // 2:
            q_count[3] += 1
            continue

    print(q_count)
    print(q_count[0] * q_count[1] * q_count[2] * q_count[3])


if __name__ == "__main__":
    main()