import customtkinter as ctk
import random

# ---------- GAME LOGIC ----------
choices = ["rock", "paper", "scissors"]
emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
player_score = 0
computer_score = 0

# ---------- COLOR PALETTE (ocean theme) ----------
BG_COLOR = "#0B2C3D"        # deep navy outer background
CARD_COLOR = "#12415A"      # teal-blue card
TITLE_COLOR = "#5EC8C0"     # seafoam accent
TEXT_COLOR = "#E8F4F2"      # pale foam text
BTN_COLOR = "#1B5A73"       # mid teal
BTN_HOVER = "#5EC8C0"       # seafoam on hover
BORDER_COLOR = "#5EC8C0"

RESULT_BOX_COLOR = "#DCEEF7"  # pale blue result box
WIN_COLOR = "#2E7D32"         # bright green
LOSE_COLOR = "#D32F2F"        # bright red
TIE_COLOR = "#B8860B"         # gold

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

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
window.geometry("440x340")
window.configure(fg_color=BG_COLOR)

card = ctk.CTkFrame(window, fg_color=CARD_COLOR, corner_radius=20)
card.pack(padx=25, pady=25, fill="both", expand=True)

title_label = ctk.CTkLabel(card, text="Rock · Paper · Scissors",
                            font=("Georgia", 19, "bold"), text_color=TITLE_COLOR)
title_label.pack(pady=(25, 12))

result_box = ctk.CTkFrame(card, fg_color=RESULT_BOX_COLOR, corner_radius=10)
result_box.pack(pady=(0, 16), padx=20, fill="x")

result_label = ctk.CTkLabel(result_box, text="Make your move!", font=("Georgia", 13, "bold"),
                             text_color="#333333", wraplength=340)
result_label.pack(pady=10, padx=10)

button_frame = ctk.CTkFrame(card, fg_color="transparent")
button_frame.pack(pady=12)

for choice in choices:
    btn = ctk.CTkButton(
        button_frame, text=f"{emojis[choice]}  {choice.capitalize()}",
        command=lambda c=choice: play(c),
        fg_color=BTN_COLOR, hover_color=BTN_HOVER,
        text_color=TEXT_COLOR, font=("Georgia", 12, "bold"),
        corner_radius=14, width=115, height=42, border_width=1,
        border_color=BORDER_COLOR
    )
    btn.pack(side="left", padx=8)

score_label = ctk.CTkLabel(card, text="You: 0      Computer: 0",
                            font=("Georgia", 14, "bold"), text_color=TEXT_COLOR)
score_label.pack(pady=(15, 20))

window.mainloop()