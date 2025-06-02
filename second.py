

class Bank():
    def __init__(self , balance = 0 ):
        self.balance = balance

    def Checkbalance(self):
        return f"your current balance is {self.balance}"
    
    def Deposit(self , Amount):

            return f"your  balnce is {self.balance == Amount + self.balance} after you deposit {Amount}"
    
    def Witdraw(self , Amount):
         return f"your balance is {self.balance - Amount} after you withdraw {Amount}"
    

Person = Bank(500)
print(Person.Checkbalance())
print(Person.Deposit(1000))
print(Person.Checkbalance())
print(Person.Witdraw(200))
print(Person)



     