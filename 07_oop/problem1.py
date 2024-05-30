class Car:
  total_car = 0


  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    Car.total_car += 1

  def get_brand(self):
    return self.brand +  "!"

  def full_name(self):
    return f"{self.brand} {self.model}"

  def fuel_type(self):
    return "Petrol or Diesel"
  
  @staticmethod
  def general_info():
    return "Cars are fucking amazing"

class ElectricCar(Car):
  def __init__(self, brand, model, battery_size):
    super().__init__(brand, model)
    self.battery_size = battery_size

  def fuel_type(self):
    return "Electric Charge"

# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.brand)
# print(my_tesla.fuel_type())

my_car = Car("Tata", "Safari")

Car("Tata", "Nexon")

# print(my_car.general_info())
print(Car.general_info())

# my_car = Car(input("Enter car brand:"), input("Enter Car Model:"))
# print("Car Brand:", my_car.brand)
# print("Car Model:", my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)