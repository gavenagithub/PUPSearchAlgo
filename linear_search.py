import timeit

def linear_search(arr, target):
    for i, element in enumerate(arr):
        print("i=",i ,"element=",element)
        if element == target:
            return i

    return -1

def linear_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)



#def binary_search
numbers = range(1, 101)
test_data = ", ".join(map(str, numbers))
# print("test_data=",test_data)
target = 100
# arr = list(map(int, test_data.split(",")))
arr =[100,20,4,10,-9,1000,89,43,24,6,8]
print("array dataset=",arr)
result =linear_search( arr, target)
print(f"Result found in index: {result} ")