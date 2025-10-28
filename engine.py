
from mathquestions import mathquestions
from general import general

def ask_questions(question_list):
    score = 0
    for q, ans in question_list:
        user_ans = input(q + " ")
        if user_ans.strip().lower() == ans.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The answer is {ans}.")
    return score

def main():
    print("Welcome to the Simple Quiz Game!")
    total_questions = mathquestions + general
    score = ask_questions(total_questions)
    print(f"Your total score: {score}/{len(total_questions)}")

if __name__ == "__main__":
    main()
