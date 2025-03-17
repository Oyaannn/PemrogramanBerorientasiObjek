class Vehicle:
    def move(self):
        return "The vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "The car is driving on the road"

class Bicycle(Vehicle):
    def move(self):
        return "The bicycle is cycling on the road"

class Boat(Vehicle):
    def move(self):
        return "The boat is sailing on the water"
    
vehicle = [Vehicle(), Car(), Bicycle(), Boat()]
for vehicles in vehicle:
    print(vehicles.move())