import timeit

def ternary_search(arr, target, left, right):
    if left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        print("mid1=",mid1,"mid2=",mid2)
        
        if arr[mid1] == target:
            return mid1
        elif arr[mid2] == target:
            return mid2
        elif target < arr[mid1]:
            return ternary_search(arr, target, left, mid1 - 1)
        elif target > arr[mid2]:
            return ternary_search(arr, target, mid2 + 1, right)
        else:
            return ternary_search(arr, target, mid1 + 1, mid2 - 1)

    return -1


def ternary_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)

numbers = range(1, 101)
test_data = ", ".join(map(str, numbers))
target = -11
arr = list(map(int, test_data.split(",")))
left, right = 0, len(arr) - 1
result =ternary_search(arr, target, left, right)
print(f"Result found in index: {result} ")