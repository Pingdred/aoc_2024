from typing import List


def load_data(file_path):
    disk_map = []
    with open(file_path, 'r') as file:
        data = file.read().strip()
        disk_map = [int(x) for x in data]

    return disk_map


def expand_disk_map(disk_map):
    disk = []
    files_id = {}
    file_id = 0
    is_file = True
    for d in disk_map:
        if is_file:
            disk.extend([file_id] * d)

            files_id[file_id] = d
            file_id += 1
                
            is_file = False
        else:
            disk.extend(['.'] * d)
            is_file = True

    return disk, files_id


def compact_files(disk: list):
        
    # List of indexes for each file
    files: List[List] = []

    # List of indexes for each free spot
    free_space: List[List] = []

    for i in range(len(disk)):
        if disk[i] !=  '.':
            files.append(i)
        else:
            free_space.append(i)

    while True:
        last_file = files.pop()
        first_free_space = free_space.pop(0)

        if last_file < first_free_space:
            break

        disk[first_free_space] = disk[last_file]
        disk[last_file] = '.'
        
    return disk


def checksum(disk):
    checksum = 0
    for i in range(len(disk)):
        if disk[i] == '.':
            continue

        checksum += (i*disk[i])

    return checksum
       

if __name__ == '__main__':
    disk_map = load_data('input.txt')
    print(disk_map)

    expanded_disk, files_id = expand_disk_map(disk_map)
    print(expanded_disk)

    compacted_disk =  compact_files(expanded_disk)
    checksum = checksum(compacted_disk)
    print(f"Checksum part 1: {checksum}")