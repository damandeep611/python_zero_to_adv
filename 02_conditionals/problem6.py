#  Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = int(input("Enter the distance to travel: "))

if distance <= 3 :
  mode = "walk"
elif distance <= 15:
  mode = "bike"
else:
  mode = "Car"

print("Ai recommend you the travel transport of", mode)

