class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def display_account_details(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance}")


class SavingsAccount(BankAccount):
    WITHDRAWAL_LIMIT = 500

    def withdraw(self, amount):
        if amount > self.WITHDRAWAL_LIMIT:
            print(f"Cannot withdraw more than ${self.WITHDRAWAL_LIMIT} in a single transaction.")
        else:
            super().withdraw(amount)


class PremiumSavingsAccount(SavingsAccount):
    WITHDRAWAL_LIMIT = 2000


# Testing the accounts
if __name__ == "__main__":
    # Create a regular bank account
    account1 = BankAccount("001", 1000)
    account1.deposit(500)
    account1.withdraw(200)
    account1.display_account_details()

    # Create a savings account
    account2 = SavingsAccount("002", 1000)
    account2.deposit(500)
    account2.withdraw(600)  # Should not be allowed
    account2.withdraw(400)  # Should be allowed
    account2.display_account_details()

    # Create a premium savings account
    account3 = PremiumSavingsAccount("003", 5000)
    account3.deposit(1000)
    account3.withdraw(1500)  # Should be allowed
    account3.withdraw(2500)  # Should not be allowed
    account3.display_account_details()