
def check_safety(values) -> bool:

    if  values[0] == values[1]:
        return False

    all_decreasing = values[0] > values[1]    

    print(f"all_decreasing: {all_decreasing}")

    for i in range( len(values) -1 ):
        if all_decreasing:
            if values[i] <= values[i+1]:
                return False
        else:
            if values[i] >= values[i+1]:
                return False
            
        # Check if the difference between the two values is between 1 and 3
        print(f"{values[i]}, {values[i+1]}: {abs(values[i] - values[i+1])}")

        if abs(values[i] - values[i+1]) < 1 or abs(values[i] - values[i+1]) > 3:
            return False

    return True
        

safe_reports_count = 0

# load input from file
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        values = line.split()
        if check_safety([int(a) for a in values]):
            print(f"Safe: {values}")
            safe_reports_count += 1

print(safe_reports_count)