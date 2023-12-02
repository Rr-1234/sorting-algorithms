import random
import time
import sys
# Sorting Algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
# Test Data Generation
def generate_test_data(size, data_type='random'):
    if data_type == 'random':
        return [random.randint(1, 1000) for _ in range(size)]
    elif data_type == 'sorted':
        return sorted([random.randint(1, 1000) for _ in range(size)])
    elif data_type == 'reverse':
        return sorted([random.randint(1, 1000) for _ in range(size)], reverse=True)
    elif data_type == 'partially':
        arr = [random.randint(1, 1000) for _ in range(size)]
        arr[:size//2] = sorted(arr[:size//2])
        return arr
# Measure Execution Time
def measure_time(func, arr):
    start = time.perf_counter()
    func(arr.copy())
    end = time.perf_counter()
    return end - start
# Running Tests with reduced input sizes
input_sizes = [10, 1000, 10000] 
data_types = ['random', 'sorted', 'reverse', 'partially']
sorting_algorithms = [bubble_sort, selection_sort, insertion_sort]
for data_type in data_types:
    print(f"Input type: {data_type.capitalize()}")
    for size in input_sizes:
        print(f"Input size: {size}")
        arr = generate_test_data(size, data_type)
        for sort_func in sorting_algorithms:
            time_taken = measure_time(sort_func, arr)
            space_complexity = sys.getsizeof(arr)
            print(f"{sort_func.__name__} : Time = [{time_taken:.5f}]seconds, Space = [{space_complexity}] bytes")
        print("--------------------------------------------------------------")
