def simple_interest(p, t, r=5):
    si = (p * t * r) / 100
    return si

# Using default rate
print("Simple Interest (default rate):", simple_interest(1000, 2))

# Using explicit rate
print("Simple Interest (explicit rate):", simple_interest(1000, 2, 10))