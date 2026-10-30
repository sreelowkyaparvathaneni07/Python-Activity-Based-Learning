marks = []
for i in range(3):
    m = int(input("Enter subject mark: "))
    if m < 0 or m > 100:
        print("Invalid mark")
        break
    marks.append(m)
else:
    failed = [i for i in range(3) if marks[i] < 35]
    if len(failed) == 1 and 35 - marks[failed[0]] <= 5:
        marks[failed[0]] = 35
        print("Grace marks applied")
    total = sum(marks)
    print("Final marks:", marks)
    print("Total:", total)
    print("Percentage:", total / 3, "%")
    if all(m >= 35 for m in marks):
        print("Result: PASS")
    else:
        print("Result: FAIL")
