import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to decide the winner
def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

# Main game function
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"\nComputer chose: {computer_choice}")

        # Determine the winner
        winner = decide_winner(user_choice, computer_choice)

        if winner == 'user':
            print("You win!")
            user_score += 1
        elif winner == 'computer':
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a draw!")

        # Display current score
        print(f"\nScore: You {user_score} - {computer_score} Computer")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nThanks for playing!")

if __name__ == "__main__":
    play_game()
