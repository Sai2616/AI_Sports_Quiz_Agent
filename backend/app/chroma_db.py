import chromadb
from app.embeddings import EmbeddingManager


class ChromaDBManager:
    def __init__(self):
        """
        Initialize ChromaDB client, collection,
        and embedding model.
        """

        # Create/Open persistent database
        self.client = chromadb.PersistentClient(
            path="../chroma_storage"
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

        Parameters
        ----------
        chunks : List[str]
            List of text chunks.

        ids : List[str]
            Unique IDs for every chunk.

        metadatas : List[dict]
            Metadata for every chunk.
        """

        embeddings = []

        # Generate embedding for every chunk
        for chunk in chunks:
            vector = self.embedding_manager.generate_embedding(chunk)
            embeddings.append(vector)

        # Store inside ChromaDB
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

        Parameters
        ----------
        query : str
            User search query.

        n_results : int
            Number of results to return.

        Returns
        -------
        dict
            Search results.
        """

        # Convert query into embedding
        query_embedding = self.embedding_manager.generate_embedding(query)

        # Search vector database
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

        return results

    def delete_collection(self):
        """
        Delete collection.
        Useful while rebuilding database.
        """

        self.client.delete_collection("sports_articles")

        print("Collection deleted successfully.")

    def count_documents(self):
        """
        Returns total stored chunks.
        """

        return self.collection.count()