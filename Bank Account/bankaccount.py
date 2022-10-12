class BankAccount:
    # Its work as a constructor
    def __init__(self, holder, number, balance=0):
        print("Bank Account Created")
        self.holder  = holder
        self.number  = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount    

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('Not Enough Balance')    
    
    # Its Print the value is text format
    def __str__(self):
        return f"Bank Account {self.holder},{self.number}, {self.balance}"         