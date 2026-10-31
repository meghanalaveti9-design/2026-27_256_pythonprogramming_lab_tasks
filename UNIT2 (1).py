a = int(input("Enter a first angle:"))
b = int(input("Enter a second angle:"))
c = int(input("Enter a third angle:"))
if a > 0 and b > 0 and c > 0 and a + b + c == 180:
    print("The triangle is valid")
else:
    print("The triangle is not valid")