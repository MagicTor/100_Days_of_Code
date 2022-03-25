from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["question"], question_data[i]["correct_answer"]))

#for i in range(len(question_bank)):
#    print(question_bank[i].text, question_bank[i].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.final_report()