while True:
    print("-- Calculator Menu --")
    print("0. Quit")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Modulus of two numbers")
    
    choice = input("Enter your choice: ")
    
    if choice == "0":
        print("Exiting the calculator. Goodbye!")
        break
    elif choice in ["1", "2", "3", "4", "5"]:
        first_number = float(input("Enter first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == "1":
            result = first_number + second_number
        elif choice == "2":
            result = first_number - second_number
        elif choice == "3":
            result = first_number * second_number
        elif choice == "4":
            if num2 != 0:
                result = first_number / second_number 
            else:
                print("You cannot divide by zero!")
                continue
        elif choice == "5":
            result = first_number % second_number
        
        print("Result: ", result)
    else:
        print("Invalid choice. Please select a number between 0 and 5.")
