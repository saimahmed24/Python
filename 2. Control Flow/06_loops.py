# For loop example
print("For loop example:")
for i in range(1, 6):
    print(f"Iteration {i}")

# While loop example
print("\nWhile loop example:")
counter = 5
while counter > 0:
    print(f"Countdown: {counter}")
    counter -= 1

# Break example
print("\nBreak example:")
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    print(i)

# Continue example
print("\nContinue example:")
for i in range(1, 10):
    if i % 2 == 0: 
        continue
    print(i)

# Loop with else
print("\nLoop with else:")
for i in range(1, 5):
    print(i)
else:
    print("Loop completed without a break.")
