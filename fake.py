def binary_search(arr, low, high, key):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return low

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        index = binary_search(arr, 0, j, key)
        while j >= index:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    arr = [2, 4, 7, 2, 1, 5, 6, 9, 10, 24, 4, 6, 30, 12, 7]
    print("Original array:", arr)
    binary_insertion_sort(arr)
    print("Sorted array:", arr)
    key = 3
    index = binary_search(arr, 0, len(arr) - 1, key)
    arr.insert(index, key)
    print("Array after inserting", key, ":", arr)

if __name__ == "__main__":
    main()
