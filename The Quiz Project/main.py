from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import Symbol
question_bank = []
for i in range(len(question_data)):
    question_bank.append(
        Question(question_data[i]['text'], question_data[i]['answer']))
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print('You have completed the test😊😊')
print(f'Your final score is {quiz.score}/{len(quiz.question_list)}')
