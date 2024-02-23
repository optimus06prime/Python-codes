import random

def guess_number():
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if user_guess < target_number:
            print("Too low! You can do better.")
        elif user_guess > target_number:
            print("Too high! You can do better.")
        else:
            print(f"Congratulations! You guessed the number correctly {target_number} in {attempts} attempts.")
            break

guess_number()