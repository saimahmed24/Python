# Introduction to Sets
numbers = {1, 2, 3, 4, 5}

# Adding and removing elements
numbers.add(6)
numbers.remove(3)
print(f"Set after operations: {numbers}")

# Set operations
even_numbers = {2, 4, 6, 8}
print(f"Union: {numbers | even_numbers}")
print(f"Intersection: {numbers & even_numbers}")
print(f"Difference: {numbers - even_numbers}")

# Checking membership
print(f"Is 4 in the set? {4 in numbers}")
print(f"Is 10 in the set? {10 in numbers}")