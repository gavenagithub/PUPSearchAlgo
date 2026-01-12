import timeit

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        print("position=",pos)
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

def interpolation_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)


numbers = range(1, 1001,4)
test_data = ", ".join(map(str, numbers))
# print(test_data)
target = 13
# arr = list(map(int, test_data.split(",")))
arr = [1, 13, 25, 27, 39, 311, 313, 415, 517, 519, 521, 623, 625, 727, 729, 831, 833, 835, 937, 939, 941]
# target = 833
result =interpolation_search(arr, target)
print(f"Result found in index: {result} ")


# def interpolation_search_recursive(arr, target, low, high):
#     if low <= high and target >= arr[low] and target <= arr[high]:
#         if low == high:
#             if arr[low] == target:
#                 return low
#             return -1

#         pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

#         if arr[pos] == target:
#             return pos
#         elif arr[pos] < target:
#             return interpolation_search_recursive(arr, target, pos + 1, high)
#         else:
#             return interpolation_search_recursive(arr, target, low, pos - 1)

#     return -1
