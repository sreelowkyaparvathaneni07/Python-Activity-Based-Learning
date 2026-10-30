names = []
prices = []
quantities = []
n = int(input("Number of products: "))
for i in range(n):
    name = input("Product name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    names.append(name)
    prices.append(price)
    quantities.append(qty)
total = 0
for i in range(n):
    line = prices[i] * quantities[i]
    total += line
    print(names[i], "=", line)
budget = 1500
print("Basket total:", total)
if total <= budget:
    print("Budget remaining:", budget- total)
else:
    print("Over budget by:", total- budget)
