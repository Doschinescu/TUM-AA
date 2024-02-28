import time
import random
import matplotlib.pyplot as plt

MIN_MERGE = 32

def calcMinRun(n): 
    r = 0
    while n >= MIN_MERGE: 
        r |= n & 1
        n >>= 1
    return n + r 

def insertionSort(arr, left, right): 
    for i in range(left + 1, right + 1): 
        j = i 
        while j > left and arr[j] < arr[j - 1]: 
            arr[j], arr[j - 1] = arr[j - 1], arr[j] 
            j -= 1

def merge(arr, l, m, r): 
    len1, len2 = m - l + 1, r - m 
    left, right = [], [] 
    for i in range(0, len1): 
        left.append(arr[l + i]) 
    for i in range(0, len2): 
        right.append(arr[m + 1 + i]) 

    i, j, k = 0, 0, l 

    while i < len1 and j < len2: 
        if left[i] <= right[j]: 
            arr[k] = left[i] 
            i += 1
        else: 
            arr[k] = right[j] 
            j += 1
        k += 1

    while i < len1: 
        arr[k] = left[i] 
        k += 1
        i += 1

    while j < len2: 
        arr[k] = right[j] 
        k += 1
        j += 1

def timSort(arr): 
    n = len(arr) 
    minRun = calcMinRun(n) 

    for start in range(0, n, minRun): 
        end = min(start + minRun - 1, n - 1) 
        insertionSort(arr, start, end) 

    size = minRun 
    while size < n: 
        for left in range(0, n, 2 * size): 
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
            if mid < right: 
                merge(arr, left, mid, right) 
        size = 2 * size 

def measure_time(arr):
    start_time = time.time()
    timSort(arr)
    end_time = time.time()
    return end_time - start_time

array_sizes = [10, 100, 1000, 5000, 10000]
sorting_times = []
for size in array_sizes:
    data = [random.randint(-1000, 1000) for _ in range(size)]
    sorting_time = measure_time(data)
    sorting_times.append(sorting_time)

plt.plot(array_sizes, sorting_times, marker='o')
plt.title('Sorting Time Complexity of TimSort')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()