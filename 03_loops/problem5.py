input_str = "teeter"

for char in input_str:
  print(char)
  if input_str.count(char) == 1:
    print("Char is: ", char)
    break
  # the break willl stops the loop when it gets the result we want