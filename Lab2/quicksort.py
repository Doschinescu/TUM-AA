import matplotlib.pyplot as plt
import time
import random

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

def measure_time(arr):
    start_time = time.time()
    quickSort(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

array_sizes = [10, 100, 1000, 5000, 10000]
sorting_times = []
for size in array_sizes:
    data = [random.randint(-1000, 1000) for _ in range(size)]
    sorting_time = measure_time(data)
    sorting_times.append(sorting_time)

plt.plot(array_sizes, sorting_times, marker='o')
plt.title('QuickSort Performance')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()
