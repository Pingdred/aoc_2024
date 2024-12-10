import re

def load_input(file_path):
    ordering_rules = []
    updates = []

    with open(file_path) as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            if not line:
                continue

            if re.match(r"\d+\|\d+", line):
                a, b = line.split('|')
                ordering_rules.append((int(a),int(b)))
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


if __name__ == "__main__":

    ordering_rules, updates = load_input("input.txt")

    valid_updates = []
    for u in updates:
        if check_ordering_rules(ordering_rules, u):
            valid_updates.append(u)


    for v in valid_updates:
        print(v)

    print(sum([v[len(v)//2] for v in valid_updates]))