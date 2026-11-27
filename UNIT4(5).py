subjects = {
    "Python": 90,
    "Java": 85,
    "Maths": 95
}

print("Keys:")
for key in subjects:
    print(key)

print("Values:")
for value in subjects.values():
    print(value)

print("Items:")
for key, value in subjects.items():
    print(key, value)