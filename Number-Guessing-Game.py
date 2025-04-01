import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)
attempts = 0
max_attempts = 5

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess the number. Good luck!")
print("Type 'exit' to quit the game at any time.")
print("--------------------------------------------------------------------------------------------------------------------------")

# Game loop
while attempts < max_attempts:
    user_input = input("Enter your guess: ")

    if user_input.lower() == 'exit':
        print("You have exited the game. The number was:", number)
        break  # Exit the loop

    elif user_input.lower() == 'attempts':
        print(f"You have used {attempts} attempts. {max_attempts - attempts} left.")

    elif user_input.lower() == 'max_attempts':
        print(f"The maximum attempts allowed are {max_attempts}.")

    else:
        try:
            guess = int(user_input)  # Convert input to integer
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
                break  # Exit the loop

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 100.")

    # Check if attempts are over
    if attempts == max_attempts:
        print("You've used all attempts! The correct number was:", number)
        break  # Exit the loop

print("Thank you for playing the Number Guessing Game!")
print("--------------------------------------------------------------------------------------------------------------------------")