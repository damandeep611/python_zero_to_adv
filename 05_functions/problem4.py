import math

def circle_stats(radius):
  area = round(math.pi * radius ** 2, 2)
  # in the above code i used round( code , 2) so that values are round off to 2 decimal places and 2 represents 2 decimals places 
  circumference = round(2 * math.pi * radius, 2)
  return area, circumference
  
a, c = circle_stats(3)
print("Area: ", a, "Circumference: ", c)