# Introduction to Lists
fruits = ["apple","banana","cherry"]

# Accessing elements
print("First fruit:", fruits[0])

# Adding elements
fruits.append("orange")
print("After append:", fruits)

# Removing elements
fruits.remove("banana")
print("After remove:", fruits)

# Slicing
print("Sliced list:", fruits[1:])

# Iterating through a list
print("Iterating through the list:")
for fruit in fruits:
    print(fruit)