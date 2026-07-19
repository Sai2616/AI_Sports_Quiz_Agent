from app.chroma_db import ChromaDBManager


class RAGPipeline:

    def __init__(self):
        self.db = ChromaDBManager()

    def retrieve_context(self, query, n_results=5):
        """
        Retrieve relevant chunks from ChromaDB
        and combine them into one context string.
        """

        results = self.db.search(
            query=query,
            n_results=n_results
        )

        documents = results["documents"][0]

        context = "\n\n".join(documents)

        return context