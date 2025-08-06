
def run_quiz():
    questions = [
{
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"

  },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            "answer": "B"
},
        {
            "question": "What is 7 + 8?",
            "options": ["A. 12", "B. 13", "C. 14", "D. 15"],
            "answer": "D"
 },
        {
            "question": "Is the sun a star? (True/False)",
            "options": ["A. True", "B. False"],
            "answer": "A"
  }
    ]

    score = 0
    total_questions = len(questions)

print("Welcome to the Interactive Quiz Game!\n")

for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)

user_answer = input("Enter your answer (A, B, C, or D/True/False): ").strip().upper()

    if user_answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
print(f"Wrong! The correct answer was {q['answer']}.\n")

print("---")
    print("\nQuiz Completed!")
    print(f"You got {score} out of {total_questions} questions correct.")
    print(f"Your final score is: {score / total_questions * 100:.2f}%\n")

 play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        run_quiz()
    else:
print("Thanks for playing! Goodbye!")

# Run the quiz game
if __name__ == "__main__":
    run_quiz()
