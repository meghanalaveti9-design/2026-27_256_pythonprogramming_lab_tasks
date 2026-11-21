# Creating a string
text = "  Hello Python Programming  "

# upper()
print("Uppercase:", text.upper())

# lower()
print("Lowercase:", text.lower())

# strip()
print("Strip:", text.strip())

# split()
words = text.strip().split()
print("Split:", words)

# join()
print("Join:", "-".join(words))

# replace()
print("Replace:", text.replace("Python", "Java"))

# find()
print("Find:", text.find("Python"))