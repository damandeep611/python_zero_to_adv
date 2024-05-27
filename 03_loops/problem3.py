number = int(input("Enter number you want to see table of: "))

for i in range(1, 11):
  if i == 5:
    continue
  # using contiinue breaks only one iteration unlike break() which stops all the iterations at once
  print(number, 'x', i, '=', number * i)



