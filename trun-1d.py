def create_account():
    name = input("Enter your name: ")
    matric_nos = input("Enter your matric number: ")
    dob = input("Enter your date of birth (format: DD-MM-YYYY): ")
    username = input("Enter a username: ")
    
    while True:
        password = input("Enter a password: ")

        if len(password) < 6:
            print("Password must have at least 6 characters")
        elif password == name:
            print("Password cannot be the same as your name")
        elif password == dob:
            print("Password cannot be the same as your date of birth")
        elif password == matric_nos:
            print("Password cannot be the same as your matric number")
        else:
            print("Account created successfully!")
            break
