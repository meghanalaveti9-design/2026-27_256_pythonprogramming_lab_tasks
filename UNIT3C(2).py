s = {10, 20, 30, 40}

print("Set:", s)

# Membership testing
print(20 in s)
print(50 in s)

# Add
s.add(50)
print("After add:", s)

# Remove
s.remove(20)
print("After remove:", s)

# Discard
s.discard(100)
print("After discard:", s)