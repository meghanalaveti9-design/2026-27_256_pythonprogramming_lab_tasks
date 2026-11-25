balance = 1000

def deposit(amount):
    global balance
    balance += amount

def display():
    balance = 500
    print("Local Balance:", balance)

deposit(500)
display()

print("Account Balance:", balance)