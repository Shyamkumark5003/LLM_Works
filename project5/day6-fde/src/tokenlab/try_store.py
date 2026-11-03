from pathlib import Path
from chunkers import fixed_chunks, paragraph_chunks, overlap_chunks
from store import VectorStore

docs = sorted(Path("data/policies").glob("*.txt"))
question = "How many days before should I apply for leave?"

for name, fn in [("fixed", fixed_chunks), ("paragraph", paragraph_chunks), ("overlap", overlap_chunks)]:
    store = VectorStore()
    for f in docs:
        store.add(fn(f.read_text(encoding="utf-8")), source=f.name)

    print("=====", name, "=====")
    for source, text, score in store.search(question, k=3):
        print(round(score, 3), source)
        print("   ", text[:80].replace("\n", " "))