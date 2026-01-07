from random import choice
from enum import Enum

TRIALS = 3


class GameOptions(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"


GAME_OPTIONS = [option.value for option in GameOptions]


def get_user_input():
    return input("Enter your choice (rock, paper, scissors): ").lower()


def get_user_choice():
    trials = 0
    while trials < TRIALS:
        user_input = get_user_input()
        if user_input in GAME_OPTIONS:
            return user_input
        else:
            print("Invalid input. Please try again.")
            trials += 1
    print("You have reached the maximum number of trials.")
    return None


def get_computer_choice():
    return choice(GAME_OPTIONS)


def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("Computer wins!")


def main():
    print("Welcome to Rock, Paper, Scissors!")
    play_game()
    print("Do you want to play again? (y/n): ")
    play_again = input().lower()
    if play_again == "y":
        main()
    else:
        print("Thank you for playing!")


if __name__ == "__main__":
    main()
