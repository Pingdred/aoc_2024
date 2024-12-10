from typing import List, Tuple

def load_input(file_path: str) -> List[List]:
    map = []
    with open(file_path, 'r') as file:
       for line in file:
           map.append([int(x) for x in line.strip()])

    return map


def find_trailhead(map: List[List]):
    trailheads = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                trailheads.append((i, j))

    return trailheads


def explore(map: List[List], start: Tuple[int, int], path: List[Tuple]) -> int:

    height = map[start[0]][start[1]]
    
    if height == 9:
        # print(f'Found trailroad at {start}')

        # map_copy = [x.copy() for x in map]

        # for i in range(len(map_copy)):
        #     for j in range(len(map_copy[i])):
        #         if (i,j ) not in path:
        #             map_copy[i][j] = '.'
        #         else:
        #             map_copy[i][j] = str(map_copy[i][j])

        # for line in map_copy:
        #     print(line)
        return [start]

    trailroads = []
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    next_positions = []

    for dir in dirs:

        np = (start[0] + dir[0], start[1] + dir[1])

        if np[0] < 0 or np[0] >= len(map) or np[1] < 0 or np[1] >= len(map[0]):
            #print(f'Out of bounds at {np}')
            continue

        if np in path:
            #print(f'Skipping {np} as it is the previous position')
            continue
        
        if map[np[0]][np[1]] - height != 1:
            #print(f'Skipping {np} as it is too high')
            continue

        next_positions.append((start[0] + dir[0], start[1] + dir[1]))
    
    path.extend(next_positions)
    for np in next_positions:
        #print(f'Exploring {np} from {start}') 
         
        #path.append(start)       
        trailroads.extend(explore(map, np, path.copy()))

    return trailroads


if __name__ == '__main__':

    map = load_input('input.txt')
    # for line in map:
    #     print(line)
    
    trailheads = find_trailhead(map)

    part_1 = sum([len(set(explore(map, t, []))) for t in trailheads])
    print(part_1)

    par_2 = sum([len(explore(map, t, [])) for t in trailheads])
    print(par_2)
