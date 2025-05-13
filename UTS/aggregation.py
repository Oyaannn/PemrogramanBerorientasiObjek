class Engine:
    def start(self):
        return "Engine Started"	
    
class Car:
    def __init__ (self, engine):
        self.engine = engine
        
    def start(self):
        return self.engine.start()
    
engine = Engine()
car = Car(engine)
print(car.start())