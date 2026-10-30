height = int(input("Enter pattern height (1-9): "))
if height < 1 or height > 9:
    print("Invalid height")
else:
    for row in range(1, height + 1):
        print(" " * (height - row), end="")
    for number in range(1, row + 1):
        print(number, end="")
    print()
