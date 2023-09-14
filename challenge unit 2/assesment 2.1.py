class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if self.__account_balance >= amount:
            self.__account_balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Balance: ${self.__account_balance:.2f}")


# Test the BankAccount class
account = BankAccount("123456789", "John Doe", 1000.00)
account.display_balance()

account.deposit(500.00)
account.display_balance()

account.withdraw(200.00)
account.display_balance()

account.withdraw(1500.00)  # This will print "Insufficient funds"
account.display_balance()
