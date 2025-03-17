class Vehicle:
    def move(self):
        return "The vehicle is moving."

class Car(Vehicle):
    def move(self):
        return "The car is driving on the road."

class Bicycle(Vehicle):
    def move(self):
        return "The bicycle is cycling on the road."

class Boat(Vehicle):
    def move(self):
        return "The boat is sailing on the water."
    
vehicle = [Vehicle(), Car(), Bicycle(), Boat()]
for vehicles in vehicle:
    print(vehicles.move())
    
    class UserAuthentication:
        def login(self):
            raise NotImplementedError("Subclasses should implement this method.")

    class EmailPasswordAuthentication(UserAuthentication):
        def login(self, email, password):
            return f"Logging in with email: {email} and password: {password}"

    class GoogleAuthentication(UserAuthentication):
        def login(self, google_id):
            return f"Logging in with Google ID: {google_id}"

    class FingerprintAuthentication(UserAuthentication):
        def login(self, fingerprint_data):
            return f"Logging in with fingerprint data: {fingerprint_data}"

    auth_methods = [
        EmailPasswordAuthentication(),
        GoogleAuthentication(),
        FingerprintAuthentication()
    ]

    for auth in auth_methods:
        if isinstance(auth, EmailPasswordAuthentication):
            print(auth.login("user@example.com", "password123"))
        elif isinstance(auth, GoogleAuthentication):
            print(auth.login("google-id-12345"))
        elif isinstance(auth, FingerprintAuthentication):
            print(auth.login("fingerprint-data-xyz"))