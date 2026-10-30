attended = int(input("Classes attended: "))
total = int(input("Total classes held: "))
if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance data")
else:
    percent = attended / total * 100
    future = 0
    while (attended + future) / (total + future) * 100 < 75:
        future += 1
        print("Current attendance:", round(percent, 2), "%")
        if percent >= 75:
            print("Already eligible")
        else:
            print("Consecutive classes to attend:", future)
