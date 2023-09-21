def is_monotonic(arr):
    monotonic = False
    is_growing = check_growing(arr, 0)
    for i in range(len(arr) - 1):
        if not is_growing:
            if arr[i] >= arr[i + 1]:
                monotonic = True
            else:
                monotonic = False
                break
        else:
            if arr[i] <= arr[i + 1]:
                monotonic = True
            else:
                monotonic = False
                break
    return monotonic


def check_growing(arr, i):
    is_growing = False
    if i != len(arr) - 1:
        if arr[i] > arr[i + 1]:
            is_growing = False
        elif arr[i] < arr[i + 1]:
            is_growing = True
        else:
            check_growing(arr, i + 1)
    else:
        is_growing = True
    return is_growing


arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]
arr3 = [1, 2, 2, 3, 2, 4]
arr4 = [1, 2, 2, 3, 4]

print(is_monotonic(arr1))
print(is_monotonic(arr2))
print(is_monotonic(arr3))
print(is_monotonic(arr4))
