students = {
    1: {"name": "Meghana", "marks": 90},
    2: {"name": "Ram", "marks": 85},
    3: {"name": "Sita", "marks": 95}
}

for student in students.values():
    print("Name:", student["name"])
    print("Marks:", student["marks"])