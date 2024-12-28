# Introduction to Tuples
coordinates = (10, 20)

# Accessing elements
print("X-coordinate:", coordinates[0])
print("Y-coordinate:", coordinates[1])

#Immutability example       
try:             
    coordinates[0] = 15
except TypeError as e:
    print("Error:", e)

# Tuples for multiple assignment
x, y = coordinates
print(f"x:{x} y:{y}")