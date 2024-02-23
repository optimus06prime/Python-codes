import random

correct_number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number (between 1 and 100): "))

    if guess < correct_number:
       print("Nice try!, but too low, Try again!.")
    elif guess > correct_number:
        print("Nice try!, but too high, Try again.")
    else:
        print("Great pick! You are correct!")
        break       
