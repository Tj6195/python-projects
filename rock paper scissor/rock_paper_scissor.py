import random
choices = ["rock", "paper", "scissors"]
player = input("Enter your choice (rock, paper, scissors): ").lower()
computer = random.choice(choices)
if player == computer:
    print(f"Both players selected {player}. It's a tie!")
elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
    print(f"You win! {player} beats {computer}.")
else:
    print(f"Computer wins! {computer} beats {player}.")