import os
import chromadb

from app.embeddings import EmbeddingManager


class ChromaDBManager:
    def __init__(self):
        """
        Initialize ChromaDB client, collection,
        and embedding model.
        """

        # Get backend project root directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Chroma storage path
        CHROMA_PATH = os.path.join(BASE_DIR, "chroma_storage")

        # Create folder if it doesn't exist
        os.makedirs(CHROMA_PATH, exist_ok=True)

        # Initialize Persistent ChromaDB
        self.client = chromadb.PersistentClient(
            path=CHROMA_PATH
        )

        # Create/Open collection
        self.collection = self.client.get_or_create_collection(
            name="sports_articles"
        )

        # Load embedding model
        self.embedding_manager = EmbeddingManager()

    def add_documents(self, chunks, ids, metadatas):
        """
        Store document chunks inside ChromaDB.
        """

        embeddings = []

        for chunk in chunks:
            vector = self.embedding_manager.generate_embedding(chunk)
            embeddings.append(vector)

        self.collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=ids,
            metadatas=metadatas
        )

        print(f"{len(chunks)} chunks added successfully.")

    def search(self, query, n_results=3):
        """
        Perform semantic search.
        """

        query_embedding = self.embedding_manager.generate_embedding(query)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

        return results

    def delete_collection(self):
        """
        Delete collection.
        """

        self.client.delete_collection("sports_articles")

        print("Collection deleted successfully.")

    def count_documents(self):
        """
        Return total stored chunks.
        """

        return self.collection.count()