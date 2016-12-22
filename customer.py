##customer: deposit, withdrawal, balance
class customer(object):
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        
    def set_balance(self, balance=0.0):
        self.balance = balance

    def set_name(self, name):
        self.name = name
        
    def withdraw(self, amount):
        if amount > self.balance:
            #raise RuntimeError("You have a low balance")
            return "You don't have enough funds"
        self.balance -=  amount
        return self.balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
        
joel = customer("Joel",10000.0)
joel.set_balance(200000)
joel.set_name("Alex")
print joel.withdraw(50000)


        
