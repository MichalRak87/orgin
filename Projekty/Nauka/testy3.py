

class Bank:
    def __init__(self):
        self.amount = 0

    def add_money(self,money):
        self.amount += money
        return money

    def sub_money(self,money):
        self.amount -= money
        return money

class TestBank:
    def test_create_bank(self):
        bank = Bank()
        assert bank.amount == 0
        assert isinstance(bank,Bank)

    def test_add_money(self):
        bank = Bank()
        bank.add_money(100)
        bank.add_money(100)
        money = bank.add_money(100)
        assert bank.amount == 300
        assert money == 100

    def test_sub_money(self):
        bank = Bank()
        bank.add_money(100)
        money = bank.sub_money(100)
        assert money == 100
        assert bank.amount == 0