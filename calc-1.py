print("Menu: ")
print("0. Quit")
print("1. Addution")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus of two numbers")

operation = input("Enter your choice: ")

if operation == '0':
    print("Farewell!")
    breakpoint
elif operation in ('1', '2', '3', '4', '5'):
        first_number = float(input("Enter first number: "))
        second_number = float(("Enter second number: ")) 
if operation == '1':
            answer = first_number + second_number
            print("Your answer: " + answer)
elif operation == '2':
            answer = first_number - second_number
            print("Your answer: " + answer)
elif operation == '3':
            answer = first_number * second_number
            print("Your answer: " , answer)           
elif operation == '4':
            if second_number == 0:
                    print("Impossible operation")
            else:
                    answer: first_number / second_number        
                    print("Your answer: " + answer)
elif operation == '5':
        if second_number == 0:
                print("Impossible operation")
        else:
            answer = first_number % second_number
            print("Your answer:", answer)                


