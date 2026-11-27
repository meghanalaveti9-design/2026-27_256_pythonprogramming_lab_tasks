student = {
    "name": "Meghana",
    "age": 18,
    "course": "CSE"
}

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))

student.update({"age": 19})
print(student)

student.pop("course")
print(student)