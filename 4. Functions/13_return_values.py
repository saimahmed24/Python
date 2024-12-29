# Function returning a value
def add(a,b):
    return a+b

result = add(5,3)
print("Sum:", result)

# Returning multiple values
def arithmetic_operations(a,b):
    return a + b, a - b, a * b, a / b

add, sub, mul, div = arithmetic_operations(10,2)
print("Results:", add, sub, mul, div)