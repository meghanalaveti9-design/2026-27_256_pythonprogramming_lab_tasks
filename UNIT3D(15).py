from functools import reduce

a = [1, 2, 3, 4, 5]

# map()
print("Squares:", list(map(lambda x: x*x, a)))

# filter()
print("Even numbers:", list(filter(lambda x: x%2==0, a)))

# reduce()
print("Sum:", reduce(lambda x, y: x+y, a))