from pathlib import Path

from chunkers import fixed_chunks, overlap_chunks, paragraph_chunks

docs = sorted(Path("data/policies").glob("*.txt"))

for name, fn in [
    ("fixed", fixed_chunks),
    ("paragraph", paragraph_chunks),
    ("overlap", overlap_chunks),
]:
    total = 0
    for f in docs:
        total += len(fn(f.read_text(encoding="utf-8")))
    print(name, "->", total, "chunks")

# Oru doc oda fixed chunks paaru
sample = docs[0].read_text(encoding="utf-8")
for c in fixed_chunks(sample):
    print("---")
    print(c)
