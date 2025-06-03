import random

def guess_number():
    guess_target = random.randint(1, 20)
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        guess = int(input("Guess a number between 1 and 20: "))
        guess_count += 1
        if guess < guess_target:
            print("Too low!\n")
        elif guess > guess_target:
            print("Too high!\n")
        else:
            print("Congratulations! You've guessed the number.\n")
            return
    else:
        print("Sorry, you've used all your guesses. The number was", guess_target, "\n")

if __name__ == "__main__":
    print("Welcome to the Guessing Game!\nYou have 3 attempts to guess the number between 1 and 20.\n")
    guess_number()
    print("Thank you for playing!")