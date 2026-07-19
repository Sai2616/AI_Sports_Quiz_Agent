from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"


def load_documents():
    docs = []

    for file in DATA_DIR.glob("*.txt"):
        text = file.read_text(encoding="utf-8")

        docs.append({
            "sport": file.stem,
            "text": text
        })

    return docs