class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def check_balance(self):
        print("balance is 500") 
    def withdrawl(self,amount):
        new_amount=500-amount
        print("withdrawl amount"+str(amount)+"remaining balance"+str(new_amount))
def main():
        Card_number=input("insert your card")
        pin_number=input("enter your pin")
        new_user=Atm(Card_number,pin_number)
        print("choose activity")
        print("1.balance 2.withdrawl")
        activity=int(input("enter activity number"))
        if(activity==1):
            new_user.check_balance()
        elif(activity==2):
            amount=int(input("Enter Amount"))
            new_user.withdrawl(amount)
        else:
            print("Enter Valid Number")    
if __name__=="__main__":
        main()
            

    

        
        