class BankAccount:
    def __init__(self,account_holder,balance):
        self.name=account_holder
        self._balance=balance
    @property
    def get_balance(self):
        print(f"Dear {self.name}, your balance is {self._balance}")
        
    @property
    def deposite(self):
        return self._balance
    
    @deposite.setter
    def deposite(self,deposite_amount):
        if deposite_amount>0:
            self._balance+=deposite_amount
            print(f"New balance:{self._balance}")
    @property    
    def withdraw(self):
        return self._balance
    @withdraw.setter
    def withdraw(self,withdraw_amount):
        if withdraw_amount>0:
            self._balance-=withdraw_amount
            print(f"New balance:{self._balance}")

        
acc1=BankAccount("Nischal",0)
acc1.get_balance
acc1.deposite=200
acc1.withdraw=100


    
    
        