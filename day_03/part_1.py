import re
from typing import List

def read_input(file_path) -> str:
    with open(file_path) as f:
        lines = f.readlines()
        return "".join(lines)
    

def filter_input(data: str) -> List[int]:
    results = []
    should_process = True
    
    # Define regex patterns
    pattern = r"""
        (?P<dont>don't\(\))|
        (?P<do>do\(\))|
        (?P<mul>mul\((?P<x>\d{1,3}),(?P<y>\d{1,3})\))
    """
    
    for match in re.finditer(pattern, data, re.VERBOSE):
        if match.group('dont'):
            should_process = False
            continue

        if match.group('do'):
            should_process = True
            continue

        if match.group('mul') and should_process:
            x = int(match.group('x'))
            y = int(match.group('y'))
            results.append(x*y)
                
    return results


if __name__ == "__main__":
    data = read_input('input.txt')
    filtered_data = filter_input(data)

    print(sum(filtered_data))