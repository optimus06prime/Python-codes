print("Welcome to the UI media ")
print("Fill the following to login")
name = input("Enter your name: ")
matric = input("Enter your matriculation number: ")
date_of_birth = input("Enter your date of birth(in the format DD/MM/YYYY): ")
Username = input("Enter your username: ")
while True:
        password = input("Enter your password: ")

        if len(password) < 6:
            print("Your pasword must contain 6 or more characters")
        elif password == Username:
            print("You cannot use username as password, try again")
        elif password == date_of_birth:
            print("You cannot use date of birth as password, try again")
        elif password == matric:
            print("You cannot use matriculation number as password, try again")
        else:
            print("Your login was sucessful, welcome to the UI media")
            break              
