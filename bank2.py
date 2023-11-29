class BankAccount:
    def __init__ (self, balance, account_number):
        self.__balance=balance
        self.__account_number=account_number
    
    def deposit(self):
        deposit = float(input("How much do you want to deposit "))
        self.__balance += deposit
        print ("your amount is ", deposit)
        print ("your amount is ", self.__balance)
    def withdraw(self):
        withdraw = float(input("How much do you want to withdraw "))
        self.__balance -= withdraw
        print ("your amount is ", withdraw)
        print ("your amount is ", self.__balance)
        
    def display(self):
        print("Balance {} \n Account_number {}".format(self.__balance, self.__account_number))
    
pr=BankAccount(1000,"12345")
pr.deposit()
pr.withdraw()
pr.display()
    
    
    
    
