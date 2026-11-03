from embedder import cosine, embed

texts = [
    "How many days of annual leave do I get?",
    "Employees receive 20 days of paid vacation per year.",
    "The office canteen serves lunch at 1 PM.",
]

vecs = embed(texts)
print("Numbers per text:", vecs.shape[1])
print("Q vs leave answer :", round(cosine(vecs[0], vecs[1]), 3))
print("Q vs canteen text :", round(cosine(vecs[0], vecs[2]), 3))
