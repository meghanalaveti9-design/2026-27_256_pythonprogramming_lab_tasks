def rectangle(l, b):
    area = l * b
    perimeter = 2 * (l + b)
    return area, perimeter

l = 5
b = 3

a, p = rectangle(l, b)

print("Area:", a)
print("Perimeter:", p)