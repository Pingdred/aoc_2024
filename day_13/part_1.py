import re

def load_data(file_name: str):
    regex_button_a = r'(?<=Button A: )X\+(\d+), Y\+(\d+)'
    regex_button_b = r'(?<=Button B: )X\+(\d+), Y\+(\d+)'
    regex_prize = r'(?<=Prize: )X\=(\d+), Y\=(\d+)'

    machines = []
    with open(file_name, 'r') as file:
        data = file.read().split('\n\n')
        for d in data:
            machine = {
                'button_a': tuple(map(int, re.findall(regex_button_a, d)[0])),
                'button_b': tuple(map(int, re.findall(regex_button_b, d)[0])),
                'prize':    tuple(map(int, re.findall(regex_prize, d)[0]))
            }
            machines.append(machine)

    return machines


def cramers(button_a, button_b, prize):
    det = (button_a[0] * button_b[1]) - (button_a[1] * button_b[0])
    det_x = (prize[0] * button_b[1]) - (prize[1] * button_b[0])
    det_y = (button_a[0] * prize[1]) - (button_a[1] * prize[0])
    
    # Check if the prize is reachable
    if det_x % det != 0 or det_y % det != 0:
        return None

    return (det_x // det, det_y // det)


def main():
    machines = load_data('input.txt')
    
    tot_a = 0
    tot_b = 0
    for machine in machines:
        presses = cramers(machine['button_a'], machine['button_b'], machine['prize'])
        if not presses:
            print('No solution found')
            continue
        
        tot_a += presses[0]
        tot_b += presses[1]
        print(f'Button A: {presses[0]}, Button B: {presses[1]}')

    total_tokens = (tot_a * 3) + tot_b

    print(f'Total tokens: {total_tokens}')


if __name__ == '__main__':
    main()