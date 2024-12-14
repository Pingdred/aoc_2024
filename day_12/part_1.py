from typing import Tuple, List

def load_data(file_path):
    garden = tuple()
    with open(file_path, 'r') as file:
        for line in file:
            cells = tuple([c for c in line.strip()])
            garden += (cells,)
    return garden

def get_neighbors(garden: Tuple[Tuple], pos: Tuple[int]) -> List[Tuple[int]]:
    # Only orizontal and vertical directions are needed
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    adjacent_cells = []

    for direction in directions:
        i = pos[0] + direction[0]
        j = pos[1] + direction[1]
        if 0 <= i < len(garden) and 0 <= j < len(garden[0]):
            adjacent_cells.append((i, j))
    return adjacent_cells


def get_region(garden, pos, explored):  
    region = []

    region.append(pos)
    explored.add(pos)

    if len(explored) == 0:
        region.add(pos)
        explored.add(pos)

    neighbors = get_neighbors(garden, pos)
    
    for cell in neighbors:
        if cell in explored:
            continue

        if garden[cell[0]][cell[1]] == garden[pos[0]][pos[1]]:
            region += get_region(garden, cell, explored)

    return region

def get_perimeter(garden: Tuple[Tuple], region: List) -> int:
    perimeter = 0
    for cell in region:
        adjacent_cells = get_neighbors(garden, cell)
        perimeter += 4 - len(adjacent_cells)
        for adjacent_cell in adjacent_cells:
            if adjacent_cell not in region:
                perimeter += 1
    return perimeter
    

if __name__ == '__main__':
    garden = load_data('input.txt')
    # for row in garden:
    #     print(row)

    explored = set()
    regions = {}

    # Get all regions in the garden
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if (i, j) in explored:
                continue

            region = get_region(garden, (i, j), explored)
            for cell in region:
                explored.add(cell)
            regions[(garden[i][j],(i, j))] = region

    total_price = 0
    for k, v in regions.items():
        area = len(v)
        perimeter = get_perimeter(garden, v)

        #print(f'{k[0]}: {area} {perimeter}')
        total_price += area * perimeter

    print(total_price)