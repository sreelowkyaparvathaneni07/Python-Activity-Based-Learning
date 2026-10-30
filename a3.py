balance = 1000
deposits = 0
withdrawals = 0
n = int(input("Number of transactions: "))
for i in range(n):
    kind = input("D for deposit, W for withdrawal: ").upper()
    amount = float(input("Amount: "))
    if amount <= 0:
        print("Rejected: amount must be positive")
    elif kind == "D":
        balance += amount
        deposits += 1
    elif kind == "W" and amount <= balance:
        balance -= amount
        withdrawals += 1
    else:
        print("Rejected: invalid type or insufficient balance")
print("Final balance:", balance)
print("Successful deposits:", deposits)
print("Successful withdrawals:", withdrawals)