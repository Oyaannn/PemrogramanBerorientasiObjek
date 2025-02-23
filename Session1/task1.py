class car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print('the car brand is:', self.brand)
        print('the car model is:', self.model)
        print('the car year is:', self.year)
        print('-'*30)

# create object base on the car class
car1 = car('Lamborgini','Huracan',2018)
car1.display_info()
car2 = car('Ferrari','Toyota',2019)
car2.display_info()
car3 = car('Civic','Honda',2020)
car3.display_info()