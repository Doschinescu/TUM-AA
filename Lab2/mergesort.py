import matplotlib.pyplot as plt
import time
import random

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0   
    k = l     
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

def measure_time(arr):
    start_time = time.time()
    mergeSort(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

array_sizes = [10, 100, 1000, 5000, 10000]
sorting_times = []
for size in array_sizes:
    data = [random.randint(-1000, 1000) for _ in range(size)]
    sorting_time = measure_time(data)
    sorting_times.append(sorting_time)

plt.plot(array_sizes, sorting_times, marker='o')
plt.title('MergeSort Performance')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()
