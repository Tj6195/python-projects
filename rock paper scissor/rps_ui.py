import customtkinter as ctk
import random

# ---------- GAME LOGIC ----------
choices = ["rock", "paper", "scissors"]
emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
player_score = 0
computer_score = 0

# ---------- COLOR PALETTE (earthy jewel tones) ----------
BG_COLOR = "#1F2A24"        # deep forest green background
CARD_COLOR = "#2C3B32"      # slightly lighter forest for contrast panels
TEXT_COLOR = "#EDE6D6"      # warm cream text (readable on dark bg)
WIN_COLOR = "#4E9E6F"       # emerald
LOSE_COLOR = "#8C2F39"      # burgundy
TIE_COLOR = "#C99A3E"       # amber/gold
BTN_COLOR = "#3D5A45"       # forest green button
BTN_HOVER = "#4E9E6F"       # emerald on hover

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

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

# ---------- UI SETUP ----------
window = ctk.CTk()
window.title("Rock Paper Scissors")
window.geometry("440x320")
window.configure(fg_color=BG_COLOR)

card = ctk.CTkFrame(window, fg_color=CARD_COLOR, corner_radius=20)
card.pack(padx=25, pady=25, fill="both", expand=True)

title_label = ctk.CTkLabel(card, text="Rock · Paper · Scissors",
                            font=("Georgia", 19, "bold"), text_color="#C99A3E")
title_label.pack(pady=(25, 8))

result_label = ctk.CTkLabel(card, text="Make your move!", font=("Georgia", 13),
                             text_color=TEXT_COLOR, wraplength=360)
result_label.pack(pady=8)

button_frame = ctk.CTkFrame(card, fg_color="transparent")
button_frame.pack(pady=12)

for choice in choices:
    btn = ctk.CTkButton(
        button_frame, text=f"{emojis[choice]}  {choice.capitalize()}",
        command=lambda c=choice: play(c),
        fg_color=BTN_COLOR, hover_color=BTN_HOVER,
        text_color=TEXT_COLOR, font=("Georgia", 12, "bold"),
        corner_radius=14, width=115, height=42, border_width=1,
        border_color="#4E9E6F"
    )
    btn.pack(side="left", padx=8)

score_label = ctk.CTkLabel(card, text="You: 0      Computer: 0",
                            font=("Georgia", 14, "bold"), text_color=TEXT_COLOR)
score_label.pack(pady=(15, 20))

window.mainloop()