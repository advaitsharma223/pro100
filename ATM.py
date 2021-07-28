class ATM:
    def __init__(self, cardNumber, pinNumber, balance):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.balance = balance
    
    def cashWithdrawal(self):
        Q1 = input("How much money would you like to withdraw: ")
        print(Q1)

    def balanceEnquiry(self):
        print("The balance in your card is Ruppees "+ user.balance)

user = ATM(1234, 1234, 400)

print(user.cardNumber)
user.cashWithdrawal()