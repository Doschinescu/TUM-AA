import random
import time
import matplotlib.pyplot as plt

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def timsort(arr):
    arr.sort()

def measure_time(data, sort_function):
    start_time = time.time()
    sort_function(data.copy())
    end_time = time.time()
    return end_time - start_time

array_sizes = [10, 100, 1000, 5000, 10000]
sorting_times_quick = []
sorting_times_heap = []
sorting_times_merge = []
sorting_times_timsort = []

for size in array_sizes:
    data = [random.randint(-1000, 1000) for _ in range(size)]
    sorting_times_quick.append(measure_time(data, quick_sort))
    sorting_times_heap.append(measure_time(data, heap_sort))
    sorting_times_merge.append(measure_time(data, merge_sort))
    sorting_times_timsort.append(measure_time(data, timsort))

plt.figure(figsize=(10, 6))
plt.plot(array_sizes, sorting_times_quick, marker='o', label='Quick Sort')
plt.plot(array_sizes, sorting_times_heap, marker='s', label='Heap Sort')
plt.plot(array_sizes, sorting_times_merge, marker='^', label='Merge Sort')
plt.plot(array_sizes, sorting_times_timsort, marker='x', label='Timsort')
plt.xscale('log')  # Use a logarithmic scale on the x-axis
plt.xlabel('Array Size (log scale)')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.show()
