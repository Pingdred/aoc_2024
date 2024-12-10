from typing import List

from tqdm import tqdm


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
    free_spots: List[List] = []

    for i in range(len(disk)):

        if disk[i] !=  '.':
             
            # New file found
            if disk[i] >= len(files):
                files.append([])
            
            files[disk[i]].append(i)
        else:

            # New free spot found
            if i > 0 and disk[i-1] != '.': 
                free_spots.append([])

            free_spots[len(free_spots) -1].append(i)

    for id in tqdm(range(len(files)-1, 0, -1)):
        for fs_i in range(len(free_spots)):

            fs = free_spots[fs_i]

            # Check if the free spot has enough space for the file
            # and if the free spot is before the file
            if len(fs) >= len(files[id]) and files[id][0] > fs[0]:

                # Move the file to the free spot
                for i in range(len(files[id])):
                    disk[fs[i]] = id
                    disk[files[id][i]] = '.'
                
                # Update the free spot
                free_spots[fs_i] = fs[len(files[id]):] 
                break  

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
    print(f"Checksum part 2: {checksum}")
