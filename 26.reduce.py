import functools
def max_in_list(numbers):
    return functools.reduce(max, numbers)

print (max_in_list([5,30,29,31,200]))
