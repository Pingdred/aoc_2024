def load_data(file_path):
    grid = []
    antennas = {}

    with open(file_path, 'r') as file:
        for line in file:
            grid.append([c for c in line.strip()])

    for line in range(len(grid)):
        for col in range(len(grid[line])):
            if grid[line][col] != '.':
                if grid[line][col] not in antennas:
                    antennas[grid[line][col]] = []
                antennas[grid[line][col]].append((line, col))
       

    return grid, antennas


def find_antinodes(p1, p2):

    antinodes = set([p1, p2])

    if p1 == p2:
        return antinodes
    
    # Calculate direction vector from p1 to p2
    diff = (p2[0] - p1[0], p2[1] - p1[1])

    # Move from p1 in the opposite direction of the vector
    antinode_1 = (p1[0] - diff[0], p1[1] - diff[1])

    while in_grid(grid, antinode_1):
        antinodes.add(antinode_1)
        antinode_1 = (antinode_1[0] - diff[0], antinode_1[1] - diff[1])

    # Move from p2 in the direction of the vector
    antinode_2 = (p2[0] + diff[0], p2[1] + diff[1])
    while in_grid(grid, antinode_2):
        antinodes.add(antinode_2)
        antinode_2 = (antinode_2[0] + diff[0], antinode_2[1] + diff[1])

    return antinodes
  

def in_grid(grid, pos):
    return pos[0] >= 0 and pos[0] < len(grid) and pos[1] >= 0 and pos[1] < len(grid[0])
  

if __name__ == "__main__":
    grid, antennas = load_data('input.txt')

    cols = [str(i) for i in range(len(grid[0]))]
    # print(f"  - {cols}")
    # for i in range(len(grid)):
    #     print(f"{i} - {grid[i]}")

    #print(antennas)

    antinodes = set()
    for ant, pos in antennas.items():
        
        for p1 in pos[:(len(pos) // 2) + 1]: # Slice the list to avoid double checking the same pair
            for p2 in pos:
                if p1 == p2:
                    continue
                
                new_antinodes = find_antinodes(p1, p2)
                antinodes.update(new_antinodes)

    # for antinode in antinodes:
    #     grid[antinode[0]][antinode[1]] = '#'

    # for row in grid:
    #     print(row)
    print(len(antinodes))


