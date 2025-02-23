class BankAccount:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner_name} deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner_name} withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

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
                print(f"ID: {account_id}, Owner: {account.owner_name}, Balance: ${account.balance}")

        elif menu == '2':
            owner_name = input("Enter the owner name: ")
            balance = int(input("Enter balance: "))
            account_id = len(accounts) + 1
            accounts[account_id] = BankAccount(owner_name, balance)
            print(f"Account created with ID: {account_id}, Owner: {owner_name}, Balance: ${balance}")
            
        elif menu == '3':
            account_id = int(input("Enter the account ID: "))
            if account_id in accounts:
                amount = int(input("Enter amount to deposit: "))
                accounts[account_id].deposit(amount)
            else:
                print("Invalid account ID.")

        elif menu == '4':
            account_id = int(input("Enter the account ID: "))
            if account_id in accounts:
                amount = int(input("Enter amount to withdraw: "))
                accounts[account_id].withdraw(amount)
            else:
                print("Invalid account ID.")

        elif menu == '5':
            print("Exiting the menu.")
            break

        else:
            print("Invalid menu. Please try again.")


if __name__ == "__main__":
    main_menu()
