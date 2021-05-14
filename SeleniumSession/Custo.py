import sys

class Customer:
    bankName = 'Dutchbank'

    def __init__(self, name, balance=0):
        self.balance = balance
        self.name = name

    def deposite(self, amt):
        self.balance = self.balance + amt
        print('after deposite balance:', self.balance)

    def withdraw(self, amt):
        if amt > self.balance:
            print('insufficiant fund...cannot perform any operation')
            sys.exit()
        self.balance = self.balance - amt
        print('after withdraw balance:', self.balance)


print('Welcome to bank:', Customer.bankName)

name = input('Enter your name:')

c = Customer(name)
while True:
    print('d-Deposite\nw-Withdrawn\ne-Exit')
    option = input('Enter your option:')
    if option == 'd' or option == 'D':
        amt = float(input('Enter amount to deposit:'))
        c.deposite(amt)
    elif option == 'w' or option == 'W':
        amt = float(input('Enter amount to Withdrawn:'))
        c.withdraw(amt)
    elif option.lower() == 'e':
        print('Thanks for banking with us')
        sys.exit()
    else:
        print('Invalid option...chose correct option')


