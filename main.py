from bank import BankAccount, SavingsAccount

acc = BankAccount("Ali")
acc.deposit(100)
print(acc.get_balance())

s = SavingsAccount("Ali", 1000)
s.add_interest(10)
print(s.get_balance())
