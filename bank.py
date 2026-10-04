class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Amount must be greater than 0")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than 0")
        elif amount > self.__balance:
            print("Not enough money")
        else:
            self.__balance -= amount


class SavingsAccount(BankAccount):
    def add_interest(self, percent):
        balance = self.get_balance()
        interest = balance * percent / 100
        self.deposit(interest)
