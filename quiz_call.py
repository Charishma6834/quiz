from quiz_def import questions
from quiz_def import options
print("***************************************")
print("check your basic python >>>")

score=0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False

for question_num in range(len(questions)):
    print("***************************************")
    print(questions[question_num]["data"])
    for i in options[question_num]:
        print(i)

    guess=input("Enter your answer(A/B/C/D): ").upper()
    is_correct=check_answer(guess,questions[question_num]["answer"])
    if is_correct:
        print("Correct Answer")
        score +=1
    else:
        print("Incorrect Answer")
        print(f"The correct answer is{questions[question_num]['answer']}")
    print(f"Your current score is {score}/{question_num+1}")
    print(f"You have given {score} correct answers")
    print(f"Your score is {(score/len(questions))*100}%")

