from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models import QuizRequest, QuizResponse
from app.quiz_generator import QuizGenerator

app = FastAPI(
    title="AI Sports Quiz Generator API",
    version="1.0.0"
)

quiz_generator = QuizGenerator()

# Allow React frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # We'll restrict this later for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "AI Sports Quiz Generator API is running."
    }


@app.post("/generate-quiz", response_model=QuizResponse)
def generate_quiz(request: QuizRequest):

    quiz = quiz_generator.generate_quiz(
        sport=request.sport,
        difficulty=request.difficulty,
        num_questions=request.num_questions,
        topic=request.topic
    )

    return QuizResponse(
        quiz=quiz
    )