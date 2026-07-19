from app.chroma_db import ChromaDBManager
from pprint import pprint

db = ChromaDBManager()

results = db.search("Virat Kohli", n_results=3)

print("\n===== COMPLETE SEARCH RESULT =====\n")
pprint(results)