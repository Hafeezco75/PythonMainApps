
class Account:

    def init__(self, name:str, balance:int, pin: str):
        self.balance: int = balance
        pass

    def check_balance(self, pin:str) -> int:
        return self.balance

    def deposit(self, amount:int):
        self.balance = self.balance + amount

    def withdraw(self, amount:int, pin:str):
        pin_is_valid_and_balance_is_sufficient = self.pin._eq_(pin) and amount <= self.balance
        if pin_is_valid_and_balance_is_sufficient:
            self.balance = self.balance - amount
