class UserAuthentication:
    def login (self):
        return "User has logged in"
    
class Email(UserAuthentication):
    def login(self):
        return "User has logged in using email"
    
class Google(UserAuthentication):
    def login(self):
        return "User has logged in using Google"
    
class FingerPrint(UserAuthentication):
    def login(self):
        return "User has logged in using Fingerprint"
    
user = [UserAuthentication(), Email(), Google(), FingerPrint()]
for users in user:
    print(users.login())