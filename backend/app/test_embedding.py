from embeddings import EmbeddingManager

embedding_manager = EmbeddingManager()

vector = embedding_manager.generate_embedding(
    "Virat Kohli scored 183 against Pakistan."
)

print(len(vector))

print(vector[:10])