import random

class GuessTheNumberGame:
    def __init__(self, min_num, max_num, max_attempts):
        # Initialize the game parameters
        self.min_num = min_num
        self.max_num = max_num
        self.max_attempts = max_attempts
        # Generate a random secret number within the specified range
        self.secret_number = random.randint(self.min_num, self.max_num)
        # Keep track of guessed numbers and attempts
        self.guessed_numbers = []
        self.attempts = 0

    def check_guess(self, guess):
        # Check the user's guess against the secret number
        if guess < self.secret_number:
            self.guessed_numbers.append(guess)
            return "Try a higher number."
        elif guess > self.secret_number:
            self.guessed_numbers.append(guess)
            return "Try a lower number."
        else:
            self.guessed_numbers.append(guess)
            return "Congratulations! You guessed the number."

def main():
    play_again = True
    while play_again:
        # Instantiate the game object
        game = GuessTheNumberGame(1, 100, 10)
        print("Welcome to the Guess the Number Game!")
        print(f"Guess a number between {game.min_num} and {game.max_num}.")

        # Main game loop
        while game.attempts < game.max_attempts:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter an integer.")
                continue

            # Check if the guess is within the valid range
            if guess < game.min_num or guess > game.max_num:
                print(f"Please enter a number between {game.min_num} and {game.max_num}.")
                continue
            elif guess in game.guessed_numbers:
                print("You already guessed that number")
                continue

            result = game.check_guess(guess)
            print(result)
            print(f"You have {game.max_attempts - game.attempts - 1} attempts left")

            game.attempts += 1

            # If the user guesses the number, end the game
            if result == "Congratulations! You guessed the number.":
                print(f"You guessed the number in {game.attempts} attempts.")
                break
        else:
            print(f"Sorry, you've exceeded the maximum number of attempts. The correct number was {game.secret_number}.")

        # Ask if the player wants to play another round
        response = input("Do you want to play again? (yes/no): ").lower()
        if response != "yes":
            play_again = False

    print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()