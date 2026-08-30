trivia = {
    "Which country is home to the kangaroo?": "Australia",
    "What is the hardest natural substance on Earth?": "Diamond",
    "Which ocean is the largest ocean in the world?": "Pacific Ocean",
    "How many bones do sharks have in their bodies?": "0",
    "What is the smallest country in the world?": "Vatican City",
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    
    }
def ask_question(question, answer):
    user = input(f"{question} ").strip() .lower()
    return user == answer.strip().lower()

score = 0
for q, a in trivia.items():
    if ask_question(q, a):
        print("Correct!✅")
        score += 1
    else:
        print(f"Nope!❎ The correct answer is: {a}")

print(f"\nYour final score is: {score}/{len(trivia)}")