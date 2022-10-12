from bankaccount import BankAccount

acc1 = BankAccount('Rakib', 1)
print(acc1)
print("Balance = ", acc1.balance)

acc1.deposit(10)
print("Balance After Add= ", acc1.balance)
acc1.withdraw(1)
print("Balance After Remove= ", acc1.balance)


acc1.withdraw(10)
print("Balance After Remove= ", acc1.balance)

# acc1 = BankAccount('RaR', 2, 50000)
# print(acc1.holder ,' has the number ', acc1.number)
# print("Balance = ", acc1.balance)