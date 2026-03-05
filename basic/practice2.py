class Account:
    def __init__(self,name,balance,account_number):
        self.name=name
        self.balance=balance
        self.account_number=account_number
        
    def debit(self,money):
        self.money=money
        self.balance-=self.money
        print(f"Rs.{self.money} was debited from {self.account_number}")
        print(f"Balance: {round(self.balance,2)}")
        
    def credit(self,money):
        self.money=money
        self.balance+=self.money
        print(f"Rs.{self.money} was credited from {self.account_number}")
        print(f"Balance: {self.balance}")
        
    
user1=Account("Nischal",20.24,"4213325496434324")
user1.debit(5)
user1.credit(100)