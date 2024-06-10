import random
import unittest
from bankAccount import BankAccount

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.bank = BankAccount()
        self.bank.update_account()


    def test_that_account_can_be_created(self):
        self.bank = BankAccount(bank_name="FirstBank", account_name="Philip Emagweali", account_number=random.randint(100000000, 999999999), phone_number="09035311210", account_type="Savings", account_balance=0.00)
        self.assertEqual(self.bank.account_name, "Philip Emagweali")
        self.assertEqual(self.bank.phone_number, "09035311210")

    def test_that_account_can_be_updated(self):
        self.bank = BankAccount(bank_name="FirstBank", account_name="Philip Emagweali", account_number=random.randint(100000000, 999999999), phone_number="09035311210", account_type="Savings", account_balance=0.00)
        self.assertEqual(self.bank.update_account(), "ZenithBank")


if __name__ == '__main__':
    unittest.main()
