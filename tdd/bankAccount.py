import random
class BankAccount:

    def __init__(self, bank_name, account_name, account_number, phone_number, account_type, account_balance):
        self.bank = []
        self.bank_name = "FirstBank"
        self.account_name = "Philip Emagweali"
        self.account_number = random.randint(100000000, 999999999)
        self.phone_number = "09035311210"
        self.account_type = "Savings"
        self.account_balance = 0.00

    def create_account(self):
        self.bank_name = self.bank_name
        self.account_name = self.account_name
        self.account_number = random.randint(100000000, 999999999)
        self.phone_number = self.phone_number
        self.account_type = "Current"
        self.account_balance = 0.00


    def update_account(self):
        self.bank.append(self.bank_name)
        self.bank.append(self.account_name)
        self.account_number = random.randint(100000000, 999999999)
        self.phone_number = self.phone_number
        self.account_type = "Savings"
        self.account_balance = 0.00
        return self.bank.append(self.bank_name)


    def deposit(self, amount):
        amount = 3000
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        if amount < self.account_balance:
            self.account_balance -= amount
        else:
            print("Insufficient funds")
        return self.account_balance

    bank = {
    }
