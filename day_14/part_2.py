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

    with open("output.txt", "w") as file:
        for i in range(10000):
            grid = [['.' for _ in range(cols)] for _ in range(rows)]
            for r in robots:
                r["p"] = move_robot(r, (rows, cols))
                grid[r["p"][0]][r["p"][1]] = "#"


            file.write(f"Time: {i}\n")
            for row in grid:
                file.write(''.join(row) + "\n")
            file.write("\n")


if __name__ == "__main__":
    main()