# Encapsulation

class BankAccount:
    
    def __init__(self):
        self._balance=0.0
    @property
    def balance(self):
        return (f"Balance:${self._balance}")
    
    def deposite(self,amount):
        if amount <=0:
            raise ValueError("Deposite amount must be positive")
        self._balance+=amount
    
    def withdraw(self,amount):
        if amount<=0:
            raise ValueError("Withdraw amount must be positive")
        if amount>self._balance:
            raise ValueError("Insufficient amount")
        self._balance-=amount

acc1=BankAccount()
print(acc1.balance)
acc1.deposite(300)
print(acc1.balance)
acc1.withdraw(400)
print(acc1.balance)