import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("🎲 Guess the Number (1 to 100)")

    while attempts < max_attempts:
        try:
            print("Attempt", attempts + 1)
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == number:
                print("🎉 Correct! You guessed it.")
                break
            elif guess < number:
                print("📉 Too low!")
            else:
                print("📈 Too high!")

        except ValueError:
            print("❌ Please enter a valid number.")

    if attempts == max_attempts and guess != number:
        print("😢 Out of attempts! The number was", number)

# Main loop for replay
while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing! Goodbye.")
        break
