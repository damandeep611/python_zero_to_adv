number = int(input("Enter the digit you want factorial of: "))
factorial = 1

while number > 0:
  factorial = factorial  * number
  number = number -1
  # or we can write it in more efficient manner like
  # factorial *= number
  # number -= 1

print("Factorial value of given number is: ",factorial)