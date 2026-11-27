dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}

result = dict1.copy()
result.update(dict2)

print("First Dictionary:", dict1)
print("Merged Dictionary:", result)