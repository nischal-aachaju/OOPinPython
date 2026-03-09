class BankAccount:
    MIN_BALANCE=100
    
    def __init__(self,owner,amount):
        self.owner=owner
        self._amount=amount

    def deposite(self,amount):
        if amount>0:
            self._amount+=amount
            print(f"{self.owner}'s new balance : ${self._amount}")
        else:
            print("Amount must be greater then 0")
    
    @staticmethod
    def is_valid_interest_rate(rate):
        return rate>=0 and rate<=5
            
            
account1=BankAccount("Nischal",1000)
account2=BankAccount("Norman",300)
account1.deposite=200
account2.deposite=4000

print(BankAccount.is_valid_interest_rate(2))
print(account1.is_valid_interest_rate(6))
        