from app.loader import load_documents
from app.chunking import chunk_text
from app.chroma_db import ChromaDBManager


def build_database():

    print("=" * 50)
    print("Building ChromaDB Database...")
    print("=" * 50)

    # Load all sports files
    documents = load_documents()

    db = ChromaDBManager()

    try:
        db.delete_collection()
        print("Old collection deleted.")
    except Exception:
        print("No existing collection found.")

    db = ChromaDBManager()

    all_chunks = []
    all_ids = []
    all_metadata = []

    chunk_counter = 1

    for document in documents:

        sport = document["sport"]
        text = document["text"]

        chunks = chunk_text(text)

        for index, chunk in enumerate(chunks):

            all_chunks.append(chunk)

            all_ids.append(f"{sport}_{chunk_counter}")

            all_metadata.append(
                {
                    "sport": sport,
                    "source": f"{sport}.txt",
                    "chunk": index + 1
                }
            )

            chunk_counter += 1

    print(f"\nTotal Chunks : {len(all_chunks)}")

    db.add_documents(
        chunks=all_chunks,
        ids=all_ids,
        metadatas=all_metadata
    )

    print("\nDatabase Created Successfully!")


if __name__ == "__main__":
    build_database()