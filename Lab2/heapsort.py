import matplotlib.pyplot as plt
import time
import random

def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1 
    r = 2 * i + 2  

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)

def measure_time(arr):
    start_time = time.time()
    heapSort(arr)
    end_time = time.time()
    return end_time - start_time

array_sizes = [10, 100, 1000, 5000, 10000]
sorting_times = []
for size in array_sizes:
    data = [random.randint(-1000, 1000) for _ in range(size)]
    sorting_time = measure_time(data)
    sorting_times.append(sorting_time)

plt.plot(array_sizes, sorting_times, marker='o')
plt.title('HeapSort Performance')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()
