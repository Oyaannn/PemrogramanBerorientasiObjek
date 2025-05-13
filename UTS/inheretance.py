class Vehicle:
    def speak(self):
        return "Some Sound"
    
class Car(Vehicle):
    def speak(self):
        return "Brummm Brummm"
    
cars = Car()
print(cars.speak())