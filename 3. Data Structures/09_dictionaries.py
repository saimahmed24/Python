# Introduction to Dictionaries
student = {
    "name": "Saim",
    "age": 22,
    "major": "Cybersecurity"       
    }

# Accessing values
print("Name:", student["name"])
print("Age:", student.get("age"))

# Adding and updating values
student["grade"] = "A"
student["age"] = 22
print("Updated dictionary:", student)

# Iterating through keys and values
print("Dictionary items:")
for key, value in student.items():
    print(f"{key}: {value}")

# Removing a key-value pair
del student["grade"]
print("After deletion:", student)