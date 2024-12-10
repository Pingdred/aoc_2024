from typing import List, Union
from tqdm import tqdm


DIRECTIONS = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

def load_input(path):
    m = []
    with open(path) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):

            pos = line.find('^')
            if pos != -1:
                guard_pos = (i, pos)

            m.append([c for c in line.strip()])

    return m, guard_pos

def go_forward(board, pos, current_direction, draw_path=True) -> Union[List, bool]:

    x, y = pos
    direction_vector = DIRECTIONS[current_direction]

    if draw_path:
        board[x][y] = 'X'

    next_x = x
    next_y = y
    path = []
    while True:
        next_x += direction_vector[0]
        next_y += direction_vector[1]

        if next_x< 0 or next_x >= len(board) or next_y < 0 or next_y >= len(board[0]):
            if draw_path:
                board[x][y] = 'X'
            return path, True

        if board[next_x][next_y] == '#':
            if draw_path:
                board[x][y] = current_direction
            break

        if draw_path:
            board[x][y] = 'X'

        path.append((next_x, next_y))
        x = next_x
        y = next_y

    return path, False

def turn_right(direction):
    directions = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^'
    }

    return directions[direction]
    
def follow_path(board, start_pos, start_direction, stop_if_loop=False, drow_path=True):

    guard_direction = start_direction
    guard_pos = start_pos

    turn_points = []
    full_path = []

    while True:

        # calculate next guard position
        path, end = go_forward(board, guard_pos, guard_direction, draw_path=drow_path)

        if len(path) > 0:
            new_guard_pos = path[-1]
        else:
            new_guard_pos = guard_pos

        # Save the explore positions
        full_path.extend(path)

        # Check if the guard exit the board
        if end:
            break

        if len(turn_points) > 3 and stop_if_loop and (new_guard_pos, guard_direction) in turn_points:
            return full_path, turn_points, True

        # Save the guard position and direction when encounter an obstacle
        turn_points.append((new_guard_pos, guard_direction))

        # Turn the guard to the right
        guard_direction = turn_right(guard_direction)
    
        guard_pos = new_guard_pos

    return full_path, turn_points, False

def find_loops(board, start_position, full_path, turn_points):
    potential_loops = []

    guard_direction = board[start_position[0]][start_position[1]]

    for step_index in tqdm(range(len(full_path))):

        if full_path[step_index] == start_position:
            continue

        board_copy = [r.copy() for r in board]

        # Add the obstacle
        board_copy[full_path[step_index][0]][full_path[step_index][1]] = '#'
       
        _, _, loop = follow_path(board_copy, start_position, guard_direction, stop_if_loop=True, drow_path=True)

        # print("AFTER")
        # for i in board_copy:
        #     print(i)

        if loop:
            potential_loops.append(full_path[step_index])

    return potential_loops

if __name__ == "__main__":
    board, guard_pos = load_input("input.txt")
    for i in board:
        print(i)

    print(f"Guard start poosition: {guard_pos}")

    full_path, turn_points, _ = follow_path(board, guard_pos, '^', drow_path=False)

    loops = find_loops(board, guard_pos, full_path, turn_points)

    # for l in loops:
    #     board[l[0]][l[1]] = 'O'

    # for i in board:
    #     print(i) 

    print(f"Explored positions: {len(set(full_path))}")

    print(f"Potential loops: {len(set(loops))}")
    