from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for element in question_data:
    question_text = element['text']
    question_answer = element['answer']
    question_info = Question(question_text, question_answer)

    question_bank.append(question_info)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f'You complete the quiz.\nYour final score was: {quiz.score}/{len(question_bank)}')