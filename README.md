# Python Games

This repository contains a collection of simple Python games.

## Available Games

### Rock, Paper, Scissors

A classic command-line implementation of the Rock, Paper, Scissors game where you compete against the computer.

**File:** `paper_rock_scissor.py`

#### 🎮 How It Works

1. You are prompted to enter your choice: **Paper**, **Rock**, or **Scissors**
2. The computer randomly selects its choice
3. The winner is determined based on the classic rules
4. You can choose to play again or exit

#### 📜 Game Rules

| You Choose | Beats       | Loses To    |
|------------|-------------|-------------|
| Rock       | Scissors    | Paper       |
| Paper      | Rock        | Scissors    |
| Scissors   | Paper       | Rock        |

- If both players choose the same option, it's a **tie**!

#### ✨ Features

- Play against the computer with randomized choices
- Input validation with up to 3 attempts for a valid choice
- Option to replay after each round
- Clean, user-friendly command-line interface

#### 📋 Example Gameplay

```
Enter your choice (Paper, Rock, scissor) : rock
You chose rock, the computer chose scissor. You win!
Do you want to play again? (y/n): n
Thank you for playing!
```

## How to Run

Ensure you have Python 3 installed.

Run the game from the terminal:

```bash
python3 paper_rock_scissor.py
```
