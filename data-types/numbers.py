# basic arithmatic operations 


#1. write a program that takes two numbers as input and performs addition, subtraction, multiplication and division on them

# first we will take two numbers from the user as input
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

# now we will perform arithmatic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1	* num2
division = num1  / num2 if num2 != 0 else "undefined"

# to display the results 
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")

# 2. Generate first 20 numbers of fibonacci sequence



