import tkinter as tk
import random

# ---------- GAME LOGIC ----------
choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

def play(player_choice):
    global player_score, computer_score
    computer = random.choice(choices)

    if player_choice == computer:
        result = f"Both selected {player_choice}. It's a tie!"
    elif (player_choice == "rock" and computer == "scissors") or \
         (player_choice == "paper" and computer == "rock") or \
         (player_choice == "scissors" and computer == "paper"):
        result = f"You win! {player_choice} beats {computer}."
        player_score += 1
    else:
        result = f"Computer wins! {computer} beats {player_choice}."
        computer_score += 1

    # update what's shown on screen
    result_label.config(text=result)
    score_label.config(text=f"Score → You: {player_score}  Computer: {computer_score}")

# ---------- UI SETUP ----------
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("350x200")

result_label = tk.Label(window, text="Make your move!", font=("Arial", 14))
result_label.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack()

rock_btn = tk.Button(button_frame, text="Rock", command=lambda: play("rock"))
rock_btn.pack(side="left", padx=10)

paper_btn = tk.Button(button_frame, text="Paper", command=lambda: play("paper"))
paper_btn.pack(side="left", padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", command=lambda: play("scissors"))
scissors_btn.pack(side="left", padx=10)

score_label = tk.Label(window, text="Score → You: 0  Computer: 0", font=("Arial", 12))
score_label.pack(pady=15)

window.mainloop()