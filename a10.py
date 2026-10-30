items = ["Idli", "Dosa", "Juice"]
prices = [30, 50, 25]
stock = [20, 15, 10]
sales = 0
n = int(input("Number of order lines: "))
for i in range(n):
    print("Menu:", list(enumerate(items, start=1)))
    item_no = int(input("Choose item number: "))
    qty = int(input("Quantity: "))
    index = item_no-1
    if index < 0 or index >= len(items) or qty <= 0:
        print("Invalid order")
    elif qty > stock[index]:
        print("Not enough stock")
    else:
        bill = prices[index] * qty
        sales += bill
        stock[index]-= qty
        print("Order bill:", bill)
print("Total sales:", sales)
print("Remaining stock:")
for i in range(len(items)):
    print(items[i], stock[i])
