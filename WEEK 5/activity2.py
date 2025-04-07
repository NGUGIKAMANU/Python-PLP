# Activity 2: Polymorphism Challenge

# Parent Class: Vehicle
class Vehicle:
    def move(self):
        pass  # Placeholder method, to be overridden by subclasses

# Subclasses with polymorphic move methods
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water 🚤")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road 🚴‍♂️")

class Robot(Vehicle):
    def move(self):
        print("Moving based on instructions 🤖")

# Creating instances of different vehicles
vehicles = [Car(), Boat(), Plane(), Bicycle(), Robot()]

# Calling move() method for each vehicle
for vehicle in vehicles:
    vehicle.move()
