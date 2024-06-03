# def basic_operation(a,b, operation):
#   if operation == 'addition':
#     return a +b
#   elif operation == 'subtraction':
#     return a -b
#   elif operation == 'multiplication':
#     return a * b
#   elif operation == 'division':
#     return a/b
#   else:
#     return 'invalid operation'
  
# result = basic_operation(10,5, 'division')
# print(result)


# problem 2*********************

# def number_properties(n):
#   properties = {
#     'even': n % 2 == 0,
#     'positive': n > 0,
#     'prime': n > 1 and all(n % i !=0 for i in range(2, int(n**0.5) +1))

#   }

#   return properties

# print(number_properties(9))

# problem 3************************

# def factorial(n):
#   if n == 0:
#     return 1
#   else:
#     return n * factorial(n-1)
  
# print(factorial(5))

# problem 4 ********************

def fibonacci(n):
  fib_seq = [0,1]
  for i in range(2,n):
    fib_seq.append(fib_seq[-1]+ fib_seq[-2])
    return fib_seq[:n]
  
print(fibonacci(999))
  

# problem 5 **************

def gcd(a,b):
  while b:
    a,b = b, a % b 
    return a
  
print(gcd(48,18))

# problemo 6 *************
def sum_of_digits(n):
  return sum(int(digit) for digit in str(n))

print(sum_of_digits(12345))

# problemo 7 ********check for palindrome number

def is_palindrome(n):
  s = str(n)
  return s == s[::-1]

print(is_palindrome(12321))


# problemo 8******check for armstrong number

def is_armstrong(n):
  digits = str(n)
  power = len(digits)
  return n == sum(int(d) ** power for d in digits)

print(is_armstrong(153))


# problemo 9********************** decimal to binary conversion

def decimal_to_binary(n):
  return bin(n)[2:]

print(decimal_to_binary(10))




