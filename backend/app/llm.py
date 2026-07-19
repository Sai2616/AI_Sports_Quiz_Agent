import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

from app.models import QuizItem
class LLMManager:

    def __init__(self):
        """
        Initialize Gemini client.
        """

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file.")

        self.client = genai.Client(api_key=api_key)

        # Default model
        self.model = "gemini-3.5-flash"

    def generate(self, prompt):
        """
        Generate response from Gemini.
        """

        try:
            response = self.client.models.generate_content(
                model=self.model,
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": list[QuizItem]
        }
            )

            return response.text

        except Exception as e:
            print(f"\nGemini Error: {e}")
            return None