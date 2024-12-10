from typing import List


def load_input():
    m = []
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            m.append([c for c in line.strip()])
    return m

def check_xmas(m, x, y):

    # sottomatrice 3x3 di m centrata in x, y, se possibile
    submatrix = []
    for i in range(x-1, x+2):
        row = []
        for j in range(y-1, y+2):
            if i >= 0 and i < len(m) and j >= 0 and j < len(m[0]):
                row.append(m[i][j])

        if len(row) == 3:
            submatrix.append(row)

    if len(submatrix) != 3:
        return 0
    else:
        #print("Submatrix centred in ", x, y)
        # for i in submatrix:
        #     print(i)

        # check if the submatrix is XMAS
        right_diagonal_str = ''.join(submatrix[i][i] for i in range(3))
        left_diagonal_str = ''.join(submatrix[i][2-i] for i in range(3))

        if right_diagonal_str in ("MAS", "SAM") and left_diagonal_str in ("MAS", "SAM"):
            #print("Found XMAS in submatrix centred in ", x, y)
            return 1
        
    return 0

def count_xmas(m):
    count = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 'A':
                count += check_xmas(m, i, j)
    return count


m = load_input()
# for i in m:
#     print(i)

print(count_xmas(m))
