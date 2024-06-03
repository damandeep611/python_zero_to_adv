file = open('youtube.txt', 'w')

try:
  file.write('The martian')
finally:
  file.close()

with open('youtube.txt', 'w') as file:
  file.write('Martian and python')