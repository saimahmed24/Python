# Global and local variables
x = 10 # Global variable

def print_x():
    x = 5       # Local variable
    print("Inside function:", x)

print_x()
print("Outside function:", x)

# Using global keyword
def modify_global():
    global x
    x = 20

modify_global()
print("After modification:", x)