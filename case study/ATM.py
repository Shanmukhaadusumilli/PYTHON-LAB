import sys

correct_pin="1234"

balance=5000


pin=input("Enter your ATM PIN:")
if pin !=correct_pin:
    print("Invalid PIN.Exiting...")
    sys.exit()

withdraw = float(input("Enter amopunt to withdraw:"))



if withdraw<=0:
    print("Invalid amount!")
elif withdraw>balance:
    print("Insufficient balance!")
else:
    balance-=withdraw
    print("Withdrawl sucessful.Remaining balance:", balance)
        
          
