from app.llm import LLMManager

llm = LLMManager()

response = llm.generate(
    "Who won the 2011 Cricket World Cup?"
)

print(response)