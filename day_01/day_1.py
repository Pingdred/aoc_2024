

list_a = []
list_b = []

list_a_count = {}
list_b_count = {}

# load input from file
with open('day_1/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        a, b = line.split()
        a, b = int(a), int(b)

        list_a.append(a)
        list_b.append(b)

        list_a_count[a] = list_a_count.get(a, 0) + 1
        list_b_count[b] = list_b_count.get(b, 0) + 1
       
# sorted_list_a = sorted(list_a)
# sorted_list_b = sorted(list_b)

total_distance  = sum([a*list_b_count.get(a, 0) for a in list_a])

print(total_distance)