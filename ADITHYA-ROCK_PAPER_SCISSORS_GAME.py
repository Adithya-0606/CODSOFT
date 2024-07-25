import random
user_score = 0
computer_score = 0
winning_point = 0
choices = ["Rock", "Paper", "Scissors"]
symbols = {
    "Rock": "✊",
    "Paper": "✋",
    "Scissors": "✌"
}

def play(player_choice):
    global user_score, computer_score, winning_point
    
    computer_choice = random.choice(choices)
    result = ""
    
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1
    
    print(f"\nYou chose {symbols[player_choice]} {player_choice}")
    print(f"Computer chose {symbols[computer_choice]} {computer_choice}")
    print(result)
    update_scores()
    
    if user_score >= winning_point:
        print("\nCongratulations! You have won the game!")
        return True
    elif computer_score >= winning_point:
        print("\nSorry, the computer has won the game!")
        return True
    return False

def update_scores():
    print(f"\nScore - User: {user_score}  Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_scores()

def start_game():
    global winning_point
    try:
        winning_point = int(input("\nEnter the number of points required to win: "))
        if winning_point <= 0:
            raise ValueError
        
        print("\nGame started! First to reach", winning_point, "points wins!")
        
        while True:
            game_over = False
            while not game_over:
                print("\nChoose an option:")
                print("1. Rock")
                print("2. Paper")
                print("3. Scissors")
                print("4. Quit")
                
                try:
                    choice = int(input("Enter the number of your choice: "))
                    if choice == 1:
                        player_choice = "Rock"
                    elif choice == 2:
                        player_choice = "Paper"
                    elif choice == 3:
                        player_choice = "Scissors"
                    elif choice == 4:
                        print("\nThanks for playing! Goodbye!")
                        return
                    else:
                        print("\nInvalid choice. Please select a number between 1 and 4.")
                        continue

                    game_over = play(player_choice)
                
                except ValueError:
                    print("\nInvalid input. Please enter a number.")
            
            if not game_over:
                break
            while True:
                play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
                if play_again == 'yes':
                    reset_game()
                    break
                elif play_again == 'no':
                    print("\nThanks for playing! Goodbye!")
                    return
                else:
                    print("\nInvalid input. Please enter 'yes' or 'no'.")
                    
    except ValueError:
        print("\nInvalid input. Please enter a valid positive integer for the winning point.")
        
if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors!")
    start_game()
