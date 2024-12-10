

from typing import List


def load_input():
    m = []
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            m.append([c for c in line.strip()])
    return m

def check_xmas(m, x, y):
    if x < 0 or x >= len(m) or y < 0 or y >= len(m[0]):
        return 0

    strings: List[str] = []
    # get string from the matrix starting form x and y for each direction

    # up string if available included x, y
    strings.append(''.join(m[i][y] for i in range(x, max(x-4, -1), -1)))
    
    # down string if available
    strings.append(''.join(m[i][y] for i in range(x, min(x+4, len(m)))))

    # right string if available
    strings.append(''.join(m[x][i] for i in range(y, min(y+4, len(m[0])))))
                   
    # left string if available
    strings.append(''.join(m[x][i] for i in range(y, max(y-4, -1), -1)))

    # up-left string if available
    strings.append(''.join(m[x-i][y-i] for i in range(min(4, x+1, y+1))))  
    
    # down-right string if available
    strings.append(''.join(m[x+i][y+i] for i in range(min(4, len(m)-x, len(m[0])-y))))

    # up-right string if available
    strings.append(''.join(m[x-i][y+i] for i in range(min(4, x+1, len(m[0])-y))))

    # down-left string if available
    strings.append(''.join(m[x+i][y-i] for i in range(min(4, len(m)-x, y+1))))


    print(f"{x}, {y}: {strings}")

    c = 0
    for i, s in enumerate(strings):
        if s.startswith('XMAS'):           
            c += 1

    return c


def count_xmas(m):
    count = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 'X':
                count += check_xmas(m, i, j)
    return count


m = load_input()
for i in m:
    print(i)

print(count_xmas(m))
