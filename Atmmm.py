import sys

#Welcome
print("Welcome to Auto-TM...")
 #Costumer verification
person1 = "Clifford Devoe"
person2 = "Elon Musk"
account_number1 = 7048782107
account_number2 = 7012878407
correct_pin1 = 00000
correct_pin2 = 12345
balance1 = 50000
balance2 = 75600

Number_of_trials = 0
while Number_of_trials < 3:
    account_number = int(input("Enter your account number: "))
    print(account_number)
    if account_number != account_number1 and account_number != account_number2:
        print("Incorrect account number!")
        Number_of_trials += 1
    else:
        PIN = int(input("Enter your PIN: "))
        if PIN != correct_pin1 and PIN != correct_pin2:
            print("Incorrect PIN!")
            Number_of_trials += 1
        elif PIN == correct_pin1:
            global Balance
            global Name
            global Account_number
            Balance = balance1
            Name = person1
            Account_number = account_number1
            print("Welcome, " , person1)    
            print("Main menu")
            print("    1 - View my balance")  
            print("    2 - Withdraw cash")
            print("    3 - Deposit funds")
            print("    4 - Exit")
            print("Enter a choice")

            user_choice = int(input(" "))
            #Account balance 
            if user_choice == 1:
               print("Your account balance is #" , balance1)
      #Making withdrawals    
            if user_choice == 2:
               print("Withrawal menu")
               print("   1 - #1000      4 - #10000")
               print("   2 - #2000   5 - #20000")
               print("   3 - #5000   6 - Cancel transaction")
               print("choose a withrawal amount")

            withdrawal_choice = int(input(" "))
            if withdrawal_choice == 1:
               print("Your withdrawal was sucessfull, you have #", balance1 - 1000 , " left in your account")
            if withdrawal_choice == 2:
               print("Your withdraw was succesful, you have #" , balance1 - 2000, " left in your account")
            if withdrawal_choice == 3:
               print("Your withdraw was succesful, you have #" , balance1 - 5000, " left in your account")
            if withdrawal_choice == 4:
               print("Your withdraw was succesful, you have #" , balance1 - 10000, " left in your account")
            if withdrawal_choice == 5:
               print("Your withdraw was succesful, you have #" , balance1 - 20000, " left in your account")
            if withdrawal_choice == 6:
               print("Withdrawal transaction cancelled")
      #fund deposit
            if user_choice == 3:                                
               print("How much would you like to deposit?")
               deposit = int(input( ))
               print("Deposit sucessfull      ", "Current balance = " , balance1 + deposit)
      #Exiting the Atm    
            if user_choice == 4:
               print("Are you sure you want to exit?   " , "(type yes/no)")
               user_answer = input( )
               if user_answer == "yes":
                   print("Goodbye!")
               elif user_answer == "no":
                   print("Resrart transaction")
                
                   
        elif PIN == correct_pin2:          
            
            Balance = balance1
            Name = person1
            Account_number = account_number1
            print("Welcome, " , person2)       
            print("Main menu")
            print("    1 - View my balance")  
            print("    2 - Withdraw cash")
            print("    3 - Deposit funds")
            print("    4 - Exit")
            print("Enter a choice")

            user2_choice = int(input(" "))
            #Account balance 
            if user2_choice == 1:
                print("Your account balance is #" , balance2)
               #Making withdrawals    
            if user2_choice == 2:
                print("Withrawal menu")
                print("   1 - #1000      4 - #10000")
                print("   2 - #2000   5 - #20000")
                print("   3 - #5000   6 - Cancel transaction")
                print("choose a withrawal amount")
                withdrawal_choice = int(input(" "))
                if withdrawal_choice == 1:
                  print("Your withdrawal was sucessful, you have #", balance2 - 1000 , " left in your account")
                if withdrawal_choice == 2:
                  print("Your withdraw was succesful, you have #" , balance2 - 2000, " left in your account")
                if withdrawal_choice == 3:
                  print("Your withdraw was succesful, you have #" , balance2 - 5000, " left in your account")
                if withdrawal_choice == 4:
                  print("Your withdraw was succesful, you have #" , balance2 - 10000, " left in your account")
                if withdrawal_choice == 5:
                  print("Your withdraw was succesful, you have #" , balance2 - 20000, " left in your account")
                if withdrawal_choice == 6:
                  print("Withdrawal transaction cancelled")
      #fund deposit
            if user2_choice == 3:                                
                print("How much would you like to deposit?")
                deposit = int(input( ))
                print("Deposit sucessfull      ", "Current balance = " , balance2 + deposit)
      #Exiting the Atm    
            if user2_choice == 4:
                print("Are you sure you want to exit?   " , "(type yes/no)")
            user2_answer = input( )
            if user2_answer == "yes":
                print("Goodbye!")
            elif user2_answer == "no":
                print("Continue transactions...")


else:
    print("You have run out of trials!")
    sys.exit()


