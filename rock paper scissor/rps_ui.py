import customtkinter as ctk
import random

# ---------- GAME LOGIC ----------
choices = ["rock", "paper", "scissors"]
emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
player_score = 0
computer_score = 0

# ---------- COLOR PALETTE (muted, aesthetic) ----------
WIN_COLOR = "#7C9885"      # muted sage green
LOSE_COLOR = "#C97B63"     # muted terracotta
TIE_COLOR = "#B69A6B"      # muted gold
BTN_COLOR = "#5C6B73"      # slate blue-gray
BTN_HOVER = "#455158"      # darker slate on hover

ctk.set_appearance_mode("light")       # starting theme
ctk.set_default_color_theme("blue")    # base theme, we override colors manually

def play(player_choice):
    global player_score, computer_score
    computer = random.choice(choices)
    p_emoji, c_emoji = emojis[player_choice], emojis[computer]

    if player_choice == computer:
        result = f"{p_emoji} Both chose {player_choice}. It's a tie! {c_emoji}"
        result_label.configure(text_color=TIE_COLOR)
    elif (player_choice == "rock" and computer == "scissors") or \
         (player_choice == "paper" and computer == "rock") or \
         (player_choice == "scissors" and computer == "paper"):
        result = f"{p_emoji} You win! {player_choice} beats {computer} {c_emoji}"
        result_label.configure(text_color=WIN_COLOR)
        player_score += 1
    else:
        result = f"{c_emoji} Computer wins! {computer} beats {player_choice} {p_emoji}"
        result_label.configure(text_color=LOSE_COLOR)
        computer_score += 1

    result_label.configure(text=result)
    score_label.configure(text=f"You: {player_score}      Computer: {computer_score}")

def toggle_theme():
    current = ctk.get_appearance_mode()
    ctk.set_appearance_mode("dark" if current == "Light" else "light")

# ---------- UI SETUP ----------
window = ctk.CTk()
window.title("Rock Paper Scissors")
window.geometry("420x300")

title_label = ctk.CTkLabel(window, text="Rock · Paper · Scissors",
                            font=("Georgia", 18, "bold"))
title_label.pack(pady=(20, 5))

result_label = ctk.CTkLabel(window, text="Make your move!", font=("Georgia", 13),
                             wraplength=380)
result_label.pack(pady=10)

button_frame = ctk.CTkFrame(window, fg_color="transparent")
button_frame.pack(pady=10)

for choice in choices:
    btn = ctk.CTkButton(
        button_frame, text=f"{emojis[choice]}  {choice.capitalize()}",
        command=lambda c=choice: play(c),
        fg_color=BTN_COLOR, hover_color=BTN_HOVER,
        font=("Georgia", 12), corner_radius=12,
        width=110, height=40
    )
    btn.pack(side="left", padx=8)

score_label = ctk.CTkLabel(window, text="You: 0      Computer: 0",
                            font=("Georgia", 13, "bold"))
score_label.pack(pady=20)

theme_btn = ctk.CTkButton(window, text="🌓 Toggle Theme", command=toggle_theme,
                           fg_color="transparent", border_width=1,
                           text_color=("gray20", "gray90"), width=140, height=28)
theme_btn.pack(pady=5)

window.mainloop()