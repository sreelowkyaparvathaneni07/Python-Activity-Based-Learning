products = [("Pen", 10, 20), ("Notebook", 60, 3), ("Folder", 25, 8)]
for name, price, stock in products:
    value = price * stock
    print("Product:", name)
    print("Inventory value:", value)
    if stock < 5:
        print("Replenishment required")
