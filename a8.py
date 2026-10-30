marks = [[78, 85, 90], [88, 76, 92], [67, 80, 74]]
best_total = -1
best_student = 0
for i in range(len(marks)):
    total = sum(marks[i])
    average = total / len(marks[i])
    print("Student", i + 1, "total:", total, "average:", round(average, 2))
    if total > best_total:
        best_total = total
        best_student = i + 1
print("Highest total:", best_total)
print("Top student:", best_student)
