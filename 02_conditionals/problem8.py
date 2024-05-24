password_check = input("Enter password to check strength: ")

if len(password_check) < 6:
  strength = "Weak"
elif len(password_check) < 10:
  strength = "medium"
else:
  strength = "strong"

print("your password strength is:", strength)
