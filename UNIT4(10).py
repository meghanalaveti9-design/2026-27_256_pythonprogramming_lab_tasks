students = [
    {"name": "Meghana", "marks": 90},
    {"name": "Ram", "marks": 75},
    {"name": "Sita", "marks": 85}
]

ascending = sorted(students, key=lambda x: x["marks"])
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

print("Ascending:", ascending)
print("Descending:", descending)