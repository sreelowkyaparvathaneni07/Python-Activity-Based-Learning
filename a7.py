password = input("Enter sample password: ")
has_upper = False
has_lower = False
has_digit = False
for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True
print("Length >= 8:", len(password) >= 8)
print("Has uppercase:", has_upper)
print("Has lowercase:", has_lower)
print("Has digit:", has_digit)
if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("Sample password meets the rules")
else:
    print("Sample password does not meet all rules")