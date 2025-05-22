class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.__balance:
            return "Insufficient funds."
        self.__balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.__balance}"

    def get_balance(self):
        return f"Current balance: ${self.__balance}"

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            return f"Balance set to ${self.__balance}"
        else:
            return "Balance cannot be negative."

    def account_summary(self):
        return f"Account owner: {self.owner}, Balance: ${self.__balance}"


account1 = BankAccount("Alice", 1000)
print(account1.account_summary())
print(account1.deposit(500))
print(account1.withdraw(200))
print(account1.get_balance())
print(account1.set_balance(-100))
print(account1.set_balance(3000))
print(account1.get_balance())

try:
    print(account1.__balance)
except AttributeError as e:
    print("Error:", e)

print("Accessing with name mangling:", account1._BankAccount__balance)
