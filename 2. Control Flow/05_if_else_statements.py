# Conditional statements example
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# Nested if example
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
    if age >= 21:
        print("You are also eligible to drink alcohol (in most countries).")
else:
    print("You are not eligible to vote.")
