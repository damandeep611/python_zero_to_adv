class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def full_name(self):
    return f"{self.brand} {self.model}"

my_car = Car(input("Enter car brand:"), input("Enter Car Model:"))
print("Car Brand:", my_car.brand)
print("Car Model:", my_car.model)
print(my_car.full_name())

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)