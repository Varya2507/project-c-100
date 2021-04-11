class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber= cardnumber
        self.pin= pin

    def withdrawal(self, amount):
        new_amount=5000-amount
        print("Your new balance is "+str(new_amount))

    def check_balance(self):
        print("Your balance is 5000 Rupees") 

def main():
    card_number=input("Insert your card number here!")
    pin_number=input("Please insert your pin!")
    new_user=Atm(card_number, pin_number)
    print("Choose your option")
    print("1. Balance Enquiry  2. Withdrawal")
    activity=int(input("enter activity number: "))

    if(activity==1):
        new_user.check_balance()
    elif(activity==2):
        amount=int(input("Enter the amount"))
        new_user.withdrawal(amount)

    else: print("Enter a valid number") 
main()           


    