import sys
from tqdm import tqdm

def load_input(file_path):
    values = {}

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            test_value, ops = line.split(':')

            values[int(test_value)] = [int(o) for o in ops.strip().split(' ')]

    return values

def evaluate(operands, operators):
    result = 0

    while len(operands) > 1:
        if operators[0] == '+':
            result = operands[0] + operands[1]
        elif operators[0] == '*':
            result = operands[0] * operands[1]
        elif operators[0] == '||':
            result= int(str(operands[0]) + str(operands[1]))

        # Update operands and operators
        operands = [result] + operands[2:]
        operators = operators[1:]

    return result

def generate_operators_combinations(n):
    operators = ['+', '*', '||']
    result = []

    for i in range(3 ** n):
        combination = []
        for j in range(n):
            combination.append(operators[i // 3 ** j % 3])

        result.append(combination)
       

    return result

if __name__ == '__main__':
    sys.set_int_max_str_digits(10**9)
    input = load_input('input.txt')

    print(input)

    total_calibration_results = 0

    for test_value, ops in tqdm(input.items(), desc='Calibrating'):
        operators_combinations = generate_operators_combinations(len(ops) - 1)

        for operators in operators_combinations:
            result = evaluate(ops, operators)

            if result == test_value:
                total_calibration_results += test_value    
                break

    print(total_calibration_results)
