class Car:
  total_car = 0


  def __init__(self, brand, model):
    self.brand = brand
    self.__model = model
    Car.total_car += 1

  def get_brand(self):
    return self.brand +  "!"

  def full_name(self):
    return f"{self.brand} {self.__model}"

  def fuel_type(self):
    return "Petrol or Diesel"
  
  @staticmethod
  def general_info():
    return "Cars are fucking amazing"
  
  @property
  def model(self):
    return self.__model

class ElectricCar(Car):
  def __init__(self, brand, model, battery_size):
    super().__init__(brand, model)
    self.battery_size = battery_size

  def fuel_type(self):
    return "Electric Charge"

# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.brand)
# print(my_tesla.fuel_type())

# my_car = Car("Tata", "Safari")
# # my_car.model = "City"
# Car("Tata", "Nexon")

# print(my_car.general_info())
# print(my_car.model)

# my_car = Car(input("Enter car brand:"), input("Enter Car Model:"))
# print("Car Brand:", my_car.brand)
# print("Car Model:", my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model)


class Battery:
  def battery_info(self):
    return "This is Battery"

class Engine:
  def engine_data(self):
    return "Here is Your Freaking Engine"

class ElectricCarTwo(Battery, Engine, Car):
  pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_data())
print(my_new_tesla.battery_info())
