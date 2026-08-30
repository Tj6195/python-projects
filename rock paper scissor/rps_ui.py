import tkinter as tk
import random

# ---------- GAME LOGIC ----------
choices = ["rock", "paper", "scissors"]
emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
player_score = 0
computer_score = 0

# ---------- COLOR PALETTE (muted, aesthetic) ----------
BG_COLOR = "#F4F1EA"       # warm cream background
TEXT_COLOR = "#3B3A36"     # soft charcoal
WIN_COLOR = "#7C9885"      # muted sage green
LOSE_COLOR = "#C97B63"     # muted terracotta
TIE_COLOR = "#B69A6B"      # muted gold
BTN_COLOR = "#5C6B73"      # slate blue-gray
BTN_HOVER = "#455158"      # darker slate on hover

def play(player_choice):
    global player_score, computer_score
    computer = random.choice(choices)
    p_emoji, c_emoji = emojis[player_choice], emojis[computer]

    if player_choice == computer:
        result = f"{p_emoji} Both chose {player_choice}. It's a tie! {c_emoji}"
        result_label.config(fg=TIE_COLOR)
    elif (player_choice == "rock" and computer == "scissors") or \
         (player_choice == "paper" and computer == "rock") or \
         (player_choice == "scissors" and computer == "paper"):
        result = f"{p_emoji} You win! {player_choice} beats {computer} {c_emoji}"
        result_label.config(fg=WIN_COLOR)
        player_score += 1
    else:
        result = f"{c_emoji} Computer wins! {computer} beats {player_choice} {p_emoji}"
        result_label.config(fg=LOSE_COLOR)
        computer_score += 1

    result_label.config(text=result)
    score_label.config(text=f"You: {player_score}      Computer: {computer_score}")

def on_enter(e):
    e.widget.config(bg=BTN_HOVER)

def on_leave(e):
    e.widget.config(bg=BTN_COLOR)

# ---------- UI SETUP ----------
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("420x260")
window.configure(bg=BG_COLOR)

title_label = tk.Label(window, text="Rock · Paper · Scissors",
                        font=("Georgia", 16, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
title_label.pack(pady=(20, 5))

result_label = tk.Label(window, text="Make your move!", font=("Georgia", 12),
                         bg=BG_COLOR, fg=TEXT_COLOR, wraplength=380)
result_label.pack(pady=10)

button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=10)

for choice in choices:
    btn = tk.Button(
        button_frame, text=f"{emojis[choice]}  {choice.capitalize()}",
        command=lambda c=choice: play(c),
        bg=BTN_COLOR, fg="white", font=("Georgia", 11),
        relief="flat", padx=12, pady=8, cursor="hand2"
    )
    btn.pack(side="left", padx=8)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

score_label = tk.Label(window, text="You: 0      Computer: 0",
                        font=("Georgia", 12, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
score_label.pack(pady=20)

window.mainloop()