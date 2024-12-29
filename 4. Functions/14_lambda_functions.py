# Lambda function
square = lambda x: x ** 2
print("Square of 5:", square(5))

# Lambda function with filter
numbers = [1,2,3,4,5,6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)