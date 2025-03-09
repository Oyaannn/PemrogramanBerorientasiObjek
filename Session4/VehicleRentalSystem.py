class Vehicle:
    def __init__(self, brand, model, rental_rate):
        self.brand = brand
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        return self.rental_rate * days


class Car(Vehicle):
    def open_trunk(self):
        return "Trunk is now open."


class Bike(Vehicle):
    def kickstart(self):
        return "Bike is now kickstarted."


class LuxuryFeatures:
    def enable_gps(self):
        return "GPS is now enabled."

    def enable_heated_seats(self):
        return "Heated seats are now enabled."


class LuxuryCar(Car, LuxuryFeatures):
    def __init__(self, brand, model, rental_rate, luxury_charge):
        super().__init__(brand, model, rental_rate)
        self.luxury_charge = luxury_charge

    def calculate_rental(self, days):
        base_rental = super().calculate_rental(days)
        return base_rental + (self.luxury_charge * days)


# Example usage:
if __name__ == "__main__":
    car = Car("Toyota", "Camry", 50)
    bike = Bike("Yamaha", "MT-07", 30)
    luxury_car = LuxuryCar("BMW", "7 Series", 100, 20)

    print(car.calculate_rental(3))  # Output: 150
    print(bike.calculate_rental(3))  # Output: 90
    print(luxury_car.calculate_rental(3))  # Output: 360

    print(car.open_trunk())  # Output: Trunk is now open.
    print(bike.kickstart())  # Output: Bike is now kickstarted.
    print(luxury_car.enable_gps())  # Output: GPS is now enabled.
    print(luxury_car.enable_heated_seats())  # Output: Heated seats are now enabled.