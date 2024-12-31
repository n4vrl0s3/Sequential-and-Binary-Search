def sequential_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Testing
array = ['d', 'c', 'g', 'h', 'b', 'a', 'f', 'i', 'e', 'c']

print("Element 'a' found at index", sequential_search(array, 'a'), "using sequential search")
print("Element 'a' found at index", binary_search(array, 'a'), "using binary search")