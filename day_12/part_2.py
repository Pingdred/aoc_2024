from typing import Tuple, List


def load_data(file_path) -> Tuple[Tuple[str]]:
    garden = tuple()
    with open(file_path, 'r') as file:
        for line in file:
            cells = tuple([c for c in line.strip()])
            garden += (cells,)
    return garden


def get_neighbors(pos: Tuple[int]) -> List[Tuple[int]]:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    neighbors = []
    for direction in directions:
        i = pos[0] + direction[0]
        j = pos[1] + direction[1]
        neighbors.append((i, j))

    return neighbors


def get_region(garden, pos, explored) ->  List[Tuple[int]]:
    region = []

    region.append(pos)
    explored.add(pos)

    neighbors = get_neighbors(pos)
    
    for cell in neighbors:
        if cell in explored:
            continue

        # Check if cell is out of bounds
        if cell[0] < 0 or cell[0] >= len(garden) or cell[1] < 0 or cell[1] >= len(garden[0]):
            continue

        if garden[cell[0]][cell[1]] == garden[pos[0]][pos[1]]:
            region += get_region(garden, cell, explored)

    return region


def get_missing_corner(cell: Tuple[int, int], neighbors: List[Tuple[int, int]]) -> Tuple[int]:
    cell_row, cell_col = cell
    neighbor1_row, neighbor1_col = neighbors[0]
    neighbor2_row, neighbor2_col = neighbors[1]

    # Get the direction of the neighbors
    neighbor1_direction = (neighbor1_row - cell_row, neighbor1_col - cell_col)
    neighbor2_direction = (neighbor2_row - cell_row, neighbor2_col - cell_col)

    # Get the direction of the missing corner
    missing_corner_direction = (
        neighbor1_direction[0] + neighbor2_direction[0],
          neighbor1_direction[1] + neighbor2_direction[1]
    )

    # Move the cell to the missing corner 
    missing_corner = (
        cell_row + missing_corner_direction[0],
        cell_col + missing_corner_direction[1]
    )

    return missing_corner

def count_cell_vertices(cell, region) -> int:

    neighbors = get_neighbors(cell)
    neighbors = [n for n in neighbors if n in region]
    num_neighbors = len(neighbors)

    # If the cell has 0 in-region neighbors, the number of vertices is 4
    # because the cell is isolated
    if num_neighbors == 0:
        return 4
    
    # If the cell has 1 in-region neighbor, the number of vertices is 2
    # because the cell is on the edge of the region
    if num_neighbors == 1:
        return  2
    
    if num_neighbors == 2:
        # Check if neighbors are in the same row or column
        same_row = neighbors[0][0] == neighbors[1][0]
        same_col = neighbors[0][1] == neighbors[1][1]
        if same_col or same_row:
            return 0

        missing_corner = get_missing_corner(cell, neighbors)
        if missing_corner not in region:
            return 2
        
        return 1

    if num_neighbors == 3:
        corners = []
        for i in range(3):
            for j in range(i+1, 3):
                # Check if neighbors are in the same row or column
                same_row = neighbors[i][0] == neighbors[j][0]
                same_col = neighbors[i][1] == neighbors[j][1]
                if same_col or same_row:
                    continue

                missing_corner = get_missing_corner(cell, [neighbors[i], neighbors[j]])
                if missing_corner in region:
                    corners.append(missing_corner)
        
        return 2 - len(corners)
        

    # If the cell has 4 neighbors, the number of vertices is 
    # the number of diagonal spots that are not in the region
    diagonal_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    diagonal_neighbors = []
    for d in diagonal_directions:
        i = cell[0] + d[0]
        j = cell[1] + d[1]
        if (i, j) in region:
            diagonal_neighbors.append((i, j))

    return 4 - len(diagonal_neighbors)


def count_vertices(region) -> int:
    vertices = 0
    for cell in region:
        vertices += count_cell_vertices(cell, region)
    return vertices


def main():
    garden = load_data('input.txt')

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
    for _, region in regions.items():
        area = len(region)
        vertices = count_vertices(region)
        total_price += area * vertices

    print(total_price)


if __name__ == '__main__':
    main()