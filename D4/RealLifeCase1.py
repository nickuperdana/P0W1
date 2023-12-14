class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.__account_number = account_number
        self.__balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
        
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Your balance is insufficient.")
            # withdrawAmount = amount
        # return print(withdrawAmount)
        
    def check_balance(self):
        return self.__balance
    
    
account = BankAccount("1234567890", 5000, "12/12/12", "ADAMS")

account.deposit(2000)
account.withdraw(12000)

print(f"Current account balance: {account.check_balance()}. Withdraw request:")