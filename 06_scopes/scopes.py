username = "chaiaurcode"

def func():
  username = "chai"
  print(username)

print(username)
func()

x = 99

def chaicoder(num):
  def actual(x):
    return x ** num
  return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(3), g(3))