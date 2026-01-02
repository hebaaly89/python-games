import random


CHOICES = ["paper", "rock", "scissor"]
CHOICES_PROMPT = "Enter your choice (Paper, Rock, scissor) : "
MAX_TRIALS = 3


def get_user_choice():
    trials = 0
    check = True
    while check and trials < MAX_TRIALS:
        user_choice = input(
           CHOICES_PROMPT
        ).lower()
        if user_choice in CHOICES:
            return user_choice
        else:
            print("Invalid choice. Please enter a valid choice.")
            trials += 1
            if trials == MAX_TRIALS:
                print(
                    "You have reached the maximum number of trials. "
                    "Please try again later."
                )
                return None


def get_computer_choice():
    return random.choice(CHOICES)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "rock" and computer_choice == "scissor") or
        (user_choice == "scissor" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"


def play_game():
    user_choice = get_user_choice()
    if user_choice is None:
        return
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    print(
        "You chose {}, the computer chose {}. {}".format(
            user_choice, computer_choice, winner
        )
    )
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        play_game()
    else:
        print("Thank you for playing!")


play_game()
