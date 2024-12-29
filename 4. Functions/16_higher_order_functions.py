# Passing functions as arguments
def square(x):
    return x ** 2

def apply_function(func, value):
    return func(value)

print("Result:", apply_function(square, 5))

# Using map, filter and reduce
from functools import reduce

numbers = [1,2,3,4,5]

squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared)

filtered = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", filtered)

summed = reduce(lambda x, y :x + y, numbers)
print("Sum of numbers:", summed)