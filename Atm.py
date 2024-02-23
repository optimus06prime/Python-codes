#Welcome
i=2
print("Welcome to the ATM, what transaction would you like to perform?")
#Costumer verification
person1 = "Clifford devoe"
person2 = "Elon Musk"
correct_account_number1 = 7048782107
correct_account_number2 = 7012878407
correct_pin1 = 00000
correct_pin2 = 11111
balance1 = 50000
balance2 = 75600
account_number = int(input("Enter your account number: "))
if account_number != correct_account_number2:
    print("Wrong account number")
elif account_number == correct_account_number2:
   print("")       
   user_pin = int(input("Enter your pin number "))
   if user_pin != correct_pin2:
      print("Wrong user pin number")
   elif len (str(user_pin)) != len(str(correct_pin2)):
      print("Your user pin number has five digits")
   elif user_pin == correct_pin2:
      while True:
         print("Welcome, " , person2)    
         
         #Transactions processses ...
         print("Main menu")
         print("    1 - View my balance")  
         print("    2 - Withdraw cash")
         print("    3 - Deposit funds")
         print("    4 - Exit")
         print("Enter a choice")

         user_choice = int(input(" "))
         #Account balance 
         if user_choice == 1:
            print("Your account balance is #" , balance2)
         #Making withdrawals    
         if user_choice == 2:
            print("Withrawal menu")
            print("   1 - #1000   4 - #10000")
            print("   2 - #2000   5 - #20000")
            print("   3 - #5000   6 - Cancel transaction")
            print("choose a withrawal amount")

            withdrawal_choice = int(input(" "))
            if withdrawal_choice == 1:
               print("Your withdrawal was sucessfull, you have #", balance2 - 1000 , " left in your account")
               balance2 -=1000
            if withdrawal_choice == 2:
               print("Your withdraw was succesfull, you have #" , balance2 - 2000, " left in your account")
               balance2-=2000
            if withdrawal_choice == 3:
               print("Your withdraw was succesfull, you have #" , balance2 - 5000, " left in your account")
               balance2-=5000
            if withdrawal_choice == 4:
               print("Your withdraw was succesfull, you have #" , balance2 - 10000, " left in your account")
               balance2-=10000
            if withdrawal_choice == 5:
               print("Your withdraw was succesfull, you have #" , balance2 - 20000, " left in your account")
               balance2-=20000
            if withdrawal_choice == 6:
               print("Withdrawal transaction cancelled")
         #fund deposit
         if user_choice == 3:                                
            print("How much would you like to deposit?")
            deposit = int(input( ))
            print("Deposit sucessfull      ", "Current balance = " , balance2 + deposit)
         #Exiting the Atm    
         if user_choice == 4:
            print("")
            user_answer = input("Are you sure you want to exit? (type yes/no): ")
            if user_answer == "yes":
               print("Goodbye!")
               break
            if user_answer == "no":
               print("Continue transactions...")
               continue
            else:
               print("Please, re-type your answer")

         