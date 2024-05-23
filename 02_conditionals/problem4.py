fruit =  input("enter the fruit name")
color = input("Enter color of fruit to check ripeness: ")

if fruit == "Banana":
  if color == "green":
    print("unripe")
  elif color == "yellow":
   print("ripe")
  elif color == "brown":
    print("overripe")