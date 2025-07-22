
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print(" Invalid choice.")
        choice = input("Please enter rock, paper, or scissors: ").lower()
    return choice

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock-Paper-Scissors!")
    
    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        print(f"\n You chose: {user}")
        print(f" Computer chose: {computer}")

        winner = determine_winner(user, computer)

        if winner == "tie":
            print(" It's a tie!")
        elif winner == "user":
            print(" You win!")
            user_score += 1
        else:
            print(" Computer wins!")
            computer_score += 1

        print(f"\n Score => You: {user_score} | Computer: {computer_score}")

        again = input("\n Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print(" Thanks for playing! Goodbye!")
            break

# Run the game
play_game()
