import timeit
import math

def jump_search(arr, target):
    n = len(arr)
    jump = int(math.sqrt(n))
    print("jump=",jump)
    left, right = 0, 0

    while right < n and arr[right] < target:
        left = right
        right += jump
        print("left=",left,"right=",right)

    for i in range(left, min(right, n)):
        if arr[i] == target:
            return i

    return -1

def jump_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)

numbers = range(1, 1001)
test_data = ", ".join(map(str, numbers))
target = 990
arr = list(map(int, test_data.split(",")))

result = jump_search(arr, target)
print(f"Result found in index: {result} ")