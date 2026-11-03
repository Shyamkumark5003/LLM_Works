import json
from pathlib import Path
from chunkers import fixed_chunks, paragraph_chunks, overlap_chunks
from store import VectorStore

K = 3
questions = json.loads(Path("data/questions.json").read_text(encoding="utf-8"))
docs = sorted(Path("data/policies").glob("*.txt"))

methods = [
    ("fixed", fixed_chunks),
    ("paragraph", paragraph_chunks),
    ("overlap", overlap_chunks),
]

results = {}  # method name -> ✔/✘ list

for name, fn in methods:
    store = VectorStore()
    for f in docs:
        store.add(fn(f.read_text(encoding="utf-8")), source=f.name)

    row = []
    for q in questions:
        found = store.search(q["question"], k=K)
        # ✔ = sariyaana doc AND chunk la keyword irukku
        ok = any(
            src.startswith(q["doc"]) and q["keyword"].lower() in text.lower()
            for src, text, _ in found
        )
        row.append(ok)
    results[name] = row

# Table print
print(f"Top-{K} retrieval, 10 questions\n")
print("| # | question | fixed | paragraph | overlap |")
print("|---|---|---|---|---|")
for i, q in enumerate(questions):
    marks = ["✔" if results[n][i] else "✘" for n, _ in methods]
    print(f"| {i+1} | {q['question']} | {marks[0]} | {marks[1]} | {marks[2]} |")

print("| | **Total** | " + " | ".join(f"**{sum(results[n])}/10**" for n, _ in methods) + " |")