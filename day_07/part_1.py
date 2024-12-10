

def load_input(file_path):
    values = {}

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            test_value, ops = line.split(':')

            values[int(test_value)] = [int(o) for o in ops.strip().split(' ')]

    return values

def evaluate(operands, operators):
    result = operands[0]

    for i in range(1, len(operands)):
        if operators[i - 1] == '+':
            result += operands[i]
        elif operators[i - 1] == '*':
            result *= operands[i]

    return result

def generate_operators_combinations(n):
    operators = ['+', '*']
    result = []

    for i in range(2 ** n):
        combination = []
        for j in range(n):
            if i & (1 << j):
                combination.append(operators[0])
            else:
                combination.append(operators[1])
        result.append(combination)

    return result

if __name__ == '__main__':
    input = load_input('input.txt')

    print(input)

    total_calibration_results = 0

    for test_value, ops in input.items():
        operators_combinations = generate_operators_combinations(len(ops) - 1)

        for operators in operators_combinations:
            result = evaluate(ops, operators)

            if result == test_value:
                total_calibration_results += test_value    
                break

    print(total_calibration_results)
