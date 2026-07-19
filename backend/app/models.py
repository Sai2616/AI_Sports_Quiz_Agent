from pydantic import BaseModel
from typing import List, Optional


class QuizRequest(BaseModel):
    sport: str
    difficulty: str
    num_questions: int
    topic: Optional[str] = None


class QuizItem(BaseModel):
    question: str
    options: List[str]
    answer: str
    explanation: str


class QuizResponse(BaseModel):
    quiz: List[QuizItem]