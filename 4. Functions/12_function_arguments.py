# Function with default arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Default argument
greet("Saim")   # Positional argument

def introduce(name, age):
    print(f"I am {name} and I am {age} years old.")

introduce(age=21, name="Saim")