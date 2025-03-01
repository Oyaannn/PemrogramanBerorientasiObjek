class BankAccount:
    def __init__(self, owner_name, balance=0, pin=1234):
        self.owner_name = owner_name
        self._balance = balance
        self.__pin = pin

    def deposit(self, amount, pin):
        if pin == self.__pin:
            self._balance += amount
            print(f"{self.owner_name} deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid PIN!")

    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if amount <= self._balance:
                self._balance -= amount
                print(f"{self.owner_name} withdrew ${amount}. New balance: ${self._balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Invalid PIN!")

def main_menu():
    accounts = {}
    while True:
        print("\nBank Menu:")
        print("1. List Accounts")
        print("2. Create Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        menu = input("Enter your menu: ")

        if menu == '1':
            for account_id, account in accounts.items():
                print(f"ID: {account_id}, Owner: {account.owner_name}, Balance: ${account._balance}")

        elif menu == '2':
            owner_name = input("Enter the owner name: ")
            balance = int(input("Enter balance: "))
            pin = int(input("Set the PIN: "))
            account_id = len(accounts) + 1
            accounts[account_id] = BankAccount(owner_name, balance, pin)
            print(f"Account created with ID: {account_id}, Owner: {owner_name}, Balance: ${balance}")
            
        elif menu == '3':
            account_id = int(input("Enter the account ID: "))
            if account_id in accounts:
                pin = int(input("Enter your PIN: "))
                amount = int(input("Enter amount to deposit: "))
                accounts[account_id].deposit(amount, pin)
            else:
                print("Invalid account ID.")

        elif menu == '4':
            account_id = int(input("Enter the account ID: "))
            if account_id in accounts:
                pin = int(input("Enter your PIN: "))
                amount = int(input("Enter amount to withdraw: "))
                accounts[account_id].withdraw(amount, pin)
            else:
                print("Invalid account ID.")

        elif menu == '5':
            print("Exiting the menu.")
            break

        else:
            print("Invalid menu. Please try again.")

if __name__ == "__main__":
    main_menu()
