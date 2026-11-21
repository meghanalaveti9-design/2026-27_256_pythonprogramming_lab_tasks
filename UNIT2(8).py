n = int(input("Enter a number: "))

if n <= 1:
    print(n, "is not a Prime Number")
else:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        print(n, "is a Prime Number")
    else:
        print(n, "is not a Prime Number")