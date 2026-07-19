QUIZ_PROMPT = """
You are an expert sports quiz generator.

Use ONLY the context provided.

Sport:
{sport}

Difficulty:
{difficulty}

Context:
{context}

Generate exactly {num_questions} multiple-choice questions.

Return ONLY valid JSON.

The JSON format must be:

[
  {{
    "question": "Question text",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": "Correct option",
    "explanation": "One sentence explanation"
  }}
]

Rules:

- Exactly four options.
- Only one correct answer.
- No markdown.
- No ```json.
- No extra text.
- Output must be valid JSON only.
"""