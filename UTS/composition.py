class Engine:
    def start(self):
        return "Engine Started"
    
class Car:
    def __init__ (self):
        self.engine = Engine()
        
    def start(self):
        return self.engine.start()
    
cars = Car()
print(cars.start())  