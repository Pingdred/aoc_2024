import re
from typing import List
from functools import cmp_to_key

def load_input(file_path):
    ordering_rules = set()
    updates = []

    with open(file_path) as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            if not line:
                continue

            if re.match(r"\d+\|\d+", line):
                a, b = line.split('|')
                ordering_rules.add((int(a), int(b)))
            else:
                updates.append([int(i) for i in line.split(',')])

    return ordering_rules, updates

def check_ordering_rules(ordering_rules, update):

    for i in range(1, len(update)):
        if (update[i-1], update[i]) not in ordering_rules:
            return False

    # Same as above but slower
    # for i in range(len(update)):
    #     after_rules = [rule[1] for rule in ordering_rules if rule[0] == update[i] and rule[0] in update and rule[1] in update]
    #     before_rules = [rule[0] for rule in ordering_rules if rule[1] == update[i] and rule[0] in update and rule[1] in update]

    #     right = update[i+1:]
    #     left = update[:i]

    #     for r in right:
    #        if r not in after_rules:
    #            return False
           
    #     for l in left:
    #         if l not in before_rules:
    #             return False

    return True

# Topological sort
def topological_sort(ordering_rules, update):
    after_values = {}
    before_values = {}
    for u in update:
        after_values[u] = [rule[1] for rule in ordering_rules if rule[0] == u and rule[0] in update and rule[1] in update]
        before_values[u] = [rule[0] for rule in ordering_rules if rule[1] == u and rule[0] in update and rule[1] in update]

    queue = []
    relations = {}
    for k, v in before_values.items():
        if len(v) == 0:
            queue.append(k)
        else:
            relations[k] = len(v)

    if len(queue) == 0:
        return None
    
    valid_updates = []
    while queue:
        node = queue.pop(0)
        valid_updates.append(node)

        for v in after_values[node]:
            relations[v] -= 1
            if relations[v] == 0:
                queue.append(v)

    if len(valid_updates) != len(update):
        return None
        
    return valid_updates    


if __name__ == "__main__":

    ordering_rules, updates = load_input("input.txt")

    invalid_updates: List[List[int]] = []
    for u in updates:
        if not check_ordering_rules(ordering_rules, u):
            invalid_updates.append(u)

    def compare(a, b):
        if (a,b) in ordering_rules:
            return -1
        elif (b,a) in ordering_rules:
            return 1
        else:
            return 0

    corrected_updates = []
    for u in invalid_updates:
        print(f"Correcting update: {u}")

        # # Slow
        # ordered_update = topological_sort(ordering_rules, u)
        # if ordered_update:
        #     print(f"\tCorrected update: {ordered_update}")
        #     corrected_updates.append(ordered_update)
            

        ordered_update = sorted(u, key=cmp_to_key(compare))
        if ordered_update != u:
            print(f"\tCorrected update: {ordered_update}")
            corrected_updates.append(ordered_update)

    print(sum([v[len(v)//2] for v in corrected_updates]))