age = int(input("Enter your age to get ticket price: "))
day = input("Enter day to check discount: ")

price = 12 if age >= 18 else 8

if day == "Wednesday":
  price = price - 2
  # or you can use  price -= 2 it is a shorthand property
else:
  print("Discount available only on wedesday")

print("Ticket price for you is $", price)

