principle = float(input())
rate = float(input())
time = float(input())
amount = principle * (1 + rate / 100) ** time
ci = amount - principle
print(ci)
