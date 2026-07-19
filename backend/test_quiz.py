from app.quiz_generator import QuizGenerator
from pprint import pprint

generator = QuizGenerator()

quiz = generator.generate_quiz(
    sport="Cricket",
    difficulty="Easy",
    num_questions=5
)

pprint(quiz)