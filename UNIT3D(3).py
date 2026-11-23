def calculate(a, b, c):
    total = a + b + c
    average = total / 3
    return total, average

m1 = 80
m2 = 90
m3 = 70

t, avg = calculate(m1, m2, m3)

print("Total:", t)
print("Average:", avg)