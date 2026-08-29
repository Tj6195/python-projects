import random
choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
while True:
    player = input("Enter your choice (rock, paper, scissors) or 'quit': ").lower()
    
    if player == "quit":
        break
    
    computer = random.choice(choices)
    
    if player == computer:
        print(f"Both players selected {player}. It's a tie!")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print(f"You win! {player} beats {computer}.")
        player_score += 1
    else:
        print(f"Computer wins! {computer} beats {player}.")
        computer_score += 1
    
    print(f"Score → You: {player_score}  Computer: {computer_score}")
print(f"Final Score → You: {player_score}  Computer: {computer_score}")