import pytest


class CheckAmount(Exception):
    pass


class Bank:
    def __init__(self):
        self.amount = 0

    def add_money(self, money):
        self.amount += money
        return money

    def sub_money(self, money):
        if money > self.amount:
            raise CheckAmount('Nie ma kasy')
        self.amount -= money
        return money


class TestBank:
    def test_check_balance(self):
        with pytest.raises(CheckAmount):
            bank = Bank()
            bank.sub_money(100)
