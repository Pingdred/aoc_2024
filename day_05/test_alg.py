import time
import matplotlib.pyplot as plt
from part_2 import load_input, check_ordering_rules, topological_sort
from functools import cmp_to_key

MIN, MAX = 10, 100

def compare(a, b, ordering_rules):
    if (a, b) in ordering_rules:
        return -1
    elif (b, a) in ordering_rules:
        return 1
    else:
        return 0

def run_sorting_algorithm(ordering_rules, updates, algorithm):
    for update in updates:
        if check_ordering_rules(ordering_rules, update):
            continue

        if algorithm == "topological_sort":
            topological_sort(ordering_rules, update)
        elif algorithm == "sorted":
            sorted(update, key=cmp_to_key(lambda a, b: compare(a, b, ordering_rules)))

def measure_time(ordering_rules, updates, algorithm):
    times = []
    for i in range(MIN, MAX):
        start_time = time.time()
        
        run_sorting_algorithm(ordering_rules, updates[:i], algorithm)

        end_time = time.time()
        times.append(end_time - start_time)
    return times

def plot_results(times_topological, times_sorted):
    plt.figure(figsize=(10, 5))
    plt.plot(range(MIN, MAX), times_topological, label='Topological Sort')
    plt.plot(range(MIN, MAX), times_sorted, label='Sorted with cmp_to_key')
    plt.xlabel('Number of Updates')
    plt.ylabel('Time (seconds)')
    plt.title('Algorithm Performance Comparison')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    ordering_rules, updates = load_input("input.txt")

    times_topological = measure_time(ordering_rules, updates, "topological_sort")
    times_sorted = measure_time(ordering_rules, updates, "sorted")

    plot_results(times_topological, times_sorted)