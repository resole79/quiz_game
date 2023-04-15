# Import model
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

# List of question
question_bank = []

# Cycle "for" to read all question
for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

# call class "QuizBrain"
quiz_brain = QuizBrain(question_bank)

# Cycle while: condition to exit not anymore question
while quiz_brain.still_has_question():
    quiz_brain.nex_question()

# print out final score
print(f"Your final score is : {quiz_brain.score}/{quiz_brain.question_number}")