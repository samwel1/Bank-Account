#Python program to create a Bankaccount class
#With both deposit() and withdraw() function


# BankAccount class
class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Hello and welcome to the Madollar ATM Your Balance is:", self.balance)
        
    #A function to deposit amount
    def deposit(self):
        amount = float(input("Enter the amount to deposit:"))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    #A function to withdraw the amount
    def withdraw(self):
        amount = float(input("Enter the amout you wish to withdraw:"))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You withdrew", amount)
        else:
            print("Insufficient balance")
        
    #Function to display the balance
    def display(self):
        print("\n Available Balance is:", self.balance)


#Driver code

#Creating an object for the class

s = BankAccount()

#Calling functions with that clss object
s.deposit()
s.withdraw()
s.display()
