import random
import timeit
import matplotlib.pyplot as plt

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Сортування злиттям
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

# Генерація випадкових даних
def generate_data(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Обгортки
def time_insertion(arr): insertion_sort(arr.copy())
def time_merge(arr): merge_sort(arr.copy())
def time_timsort(arr): sorted(arr)

# Основна частина
if __name__ == "__main__":
    sizes = [100, 1000, 5000]
    insertion_times = []
    merge_times = []
    timsort_times = []

    for size in sizes:
        data = generate_data(size)
        print(f"\n🔎 Dataset size: {size}")

        insertion_time = timeit.timeit(lambda: time_insertion(data), number=5)
        merge_time = timeit.timeit(lambda: time_merge(data), number=5)
        timsort_time = timeit.timeit(lambda: time_timsort(data), number=5)

        insertion_times.append(insertion_time)
        merge_times.append(merge_time)
        timsort_times.append(timsort_time)

        print(f"Insertion Sort: {insertion_time:.6f} seconds")
        print(f"Merge Sort: {merge_time:.6f} seconds")
        print(f"Timsort (built-in): {timsort_time:.6f} seconds")

    # Побудова графіка
    plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
    plt.plot(sizes, merge_times, label='Merge Sort', marker='o')
    plt.plot(sizes, timsort_times, label='Timsort (built-in)', marker='o')
    plt.xlabel('Dataset size')
    plt.ylabel('Time (seconds for 5 runs)')
    plt.title('Performance of Sorting Algorithms')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
