from unittest import TestCase

from test import Account

class TestAccount(TestCase):

    def test_create_account_balance_is_zero(self):
        janet_account = Account(name="name",balance:0, pin:"pin")
        self.assertEqual(first:0, janet_account.check_balance("pin"))

    def test_deposit_2k_balance_is_2k(self):
        janet_account = Account(name: "name", balance:0, pin: "pin")
        self.assertEqual(first:2, janet_account.check_balance("pin"))
        janet_account.deposit(2000)
        self.assertEqual(first:2000, janet_account.check_balance("pin"))
