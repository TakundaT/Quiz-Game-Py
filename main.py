from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a list of Question objects
question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize QuizBrain with question_bank
quiz = QuizBrain(question_bank)

# Call next_question to print the first question
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()