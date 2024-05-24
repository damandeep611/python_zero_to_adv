coffee_size = input("Enter the coffee size you want: ")
extra_shot = True

if extra_shot:
  coffee = coffee_size + "Coffee with extra shot"
else:
  coffee = coffee_size + "Coffee"

print("Order:", coffee)