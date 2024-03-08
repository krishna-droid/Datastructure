import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Set the maximum number of attempts
    max_attempts = 5

    for attempt in range(1, max_attempts + 1):
        # Get user input
        user_guess = int(input("Guess the number (between 1 and 100): "))

        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number}.")
            return True
        elif user_guess < secret_number:
            print("The secret number is larger. Try again.")
        else:
            print("The secret number is smaller. Try again.")

    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
    return False

# Uncomment the line below to play the game
# guess_number()
