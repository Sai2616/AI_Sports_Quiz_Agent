from app.rag import RAGPipeline

rag = RAGPipeline()

context = rag.retrieve_context(
    "Virat Kohli"
)

print(context)