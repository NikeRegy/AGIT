'''
Welcme Screen
Ask for the account number
Enter 4-digit PIN
Display transaction options to perform
Withdrawal/Deposit/Check Balance/Exit
'''


full_name = "Morenike Oyediran"
account_no = 9011730152
PIN = 3546
current_balance = 400000


# Splash Screen
print("Welcome to Morenike's Bank")

account = int(input("Enter account number \n>> "))

if account == account_no:
    passcode = int(input("Enter your 4-digit PIN \n>>"))
    if int(passcode) == PIN:
        print(f"Welcome {full_name}!")
        
        print("What do you want to do today? \n 1. Deposit \n 2. Withdrawal \n 3. Check Balance \n 4. Exit")

        transaction = input(">> ")
        
        if int(transaction) == 1 or transaction.strip().lower() == "Deposit":
            deposit_amount = int(input("Enter Amount"))

            new_balance = deposit_amount + current_balance
            print(f"Your new balance is {new_balance}")

            print(f"Thanks for banking with us {full_name}. Hope to see you soon!")
 
        elif int(transaction) == 2 or transaction.strip().lower() == "Withdrawal":
            withdrawal_amount = int(input("Enter Amount: "))

            if withdrawal_amount > current_balance:
                print("Insufficient Funds! Try again later")
            else:
                
                new_balance = current_balance - withdrawal_amount

                print("Kindly take your cash")
                print(f"Your new balance is {new_balance}")
                print(f"Thanks for banking with us {full_name}. Hope to see you soon!")
            
        elif int(transaction) == 3 or transaction.strip().lower() == "Check Balance":
            print(f"Your current balance is {current_balance}")
            print(f"Thanks for banking with us {full_name}. Hope to see you soon!")

        elif int(transaction) == 4 or transaction.strip().lower() == "Exit":
           
             print(f"Thanks for banking with us {full_name}. Hope to see you soon!")
     
            
        



        
    else:
        print("Incorrect PIN, Try again!")
else:
    print("User does not exist")

        
