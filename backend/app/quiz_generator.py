import json

from app.rag import RAGPipeline
from app.llm import LLMManager
from app.prompts import QUIZ_PROMPT
from app.web_search import WebSearch


class QuizGenerator:

    def __init__(self):
        """
        Initialize all required components.
        """
        self.rag = RAGPipeline()
        self.llm = LLMManager()
        self.web = WebSearch()

    def generate_quiz(
        self,
        sport,
        difficulty,
        num_questions,
        topic=None
    ):
        """
        Generate a sports quiz using:
        1. ChromaDB (Local Knowledge)
        2. Web Search (Latest Information)
        3. Gemini LLM
        """

        # Build search query
        query = f"{sport} {topic}" if topic else sport

        # Retrieve local context from ChromaDB
        local_context = self.rag.retrieve_context(
            query=query,
            n_results=5
        )

        # Retrieve latest information from Web Search
        try:
            web_context = self.web.search(query)
        except Exception as e:
            print(f"Web Search Error: {e}")
            web_context = ""

        # Combine both contexts
        combined_context = f"""
LOCAL KNOWLEDGE
=========================
{local_context}

LATEST WEB INFORMATION
=========================
{web_context}
"""

        # Build prompt
        prompt = QUIZ_PROMPT.format(
            sport=sport,
            difficulty=difficulty,
            num_questions=num_questions,
            context=combined_context
        )

        # Generate quiz using Gemini
        quiz_text = self.llm.generate(prompt)

        if quiz_text is None:
            raise Exception("Failed to generate quiz from Gemini.")

        # Remove markdown code blocks if present
        quiz_text = quiz_text.strip()

        if quiz_text.startswith("```json"):
            quiz_text = quiz_text[len("```json"):]

        elif quiz_text.startswith("```"):
            quiz_text = quiz_text[len("```"):]

        if quiz_text.endswith("```"):
            quiz_text = quiz_text[:-3]

        quiz_text = quiz_text.strip()

        # Convert JSON string to Python object
        try:
            quiz = json.loads(quiz_text)

            if not isinstance(quiz, list):
                raise ValueError("Quiz must be returned as a list.")

            return quiz

        except json.JSONDecodeError as e:
            print("\n========== RAW GEMINI RESPONSE ==========\n")
            print(quiz_text)
            print("\n=========================================\n")

            raise ValueError(
                f"Invalid JSON returned by Gemini.\n{e}"
            )