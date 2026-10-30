subjects = ["Python", "Maths", "English"]
first = [55, 38, 70]
second = [68, 35, 70]
for i in range(len(subjects)):
    change = second[i] - first[i]
    if change > 0:
        trend = "Improved"
    elif change < 0:
        trend = "Declined"
    else:
        trend = "No change"
        print(subjects[i], "change:", change, "-", trend)
    if second[i] < 40:
        print(" Needs attention")
