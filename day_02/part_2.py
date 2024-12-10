
def check_safety(values):

    if values[0] == values[1]:
        return False
    
    all_decreasing = values[0] > values[1]    

    for i in range( len(values) -1 ):
        diff = values[i] - values[i + 1]
        #print(f"Values: {values[i]} {values[i+1]}")

        if not (1 <= abs(diff) <= 3):
            print(f"\tDifference out of range [{values[i]}, {values[i+1]}]: {diff}")
            return False

        current_decreasing = (diff > 0)
        if all_decreasing != current_decreasing:
            print(f"\tOrder mismatch: {all_decreasing} != {current_decreasing}")
            return False

    return True
        

safe_reports_count = 0

# load input from file
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        values = line.split()
        values = [int(a) for a in values]

        print(f"Values: {values}")

        if check_safety(values):
            print(f"Safe: {values}")
            safe_reports_count += 1
        else:
            print(f"Unsafe: {values}")
            print("Checking subsets:")
            for i in range(len(values)):
                subset = values[:i] + values[i+1:]
                if check_safety(subset):
                    print(f"\tSafe: {subset}")
                    safe_reports_count += 1
                    break
                else:
                    print(f"\tUnsafe: {subset}")

print(safe_reports_count)