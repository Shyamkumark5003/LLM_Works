import numpy as np
from embedder import embed


class VectorStore:
    def __init__(self):
        self.texts = []  # chunk text
        self.sources = []  # edhu doc la irundhu vandhadhu
        self.vectors = None  # chunks oda numbers

    def add(self, chunks, source):
        """Oru doc oda chunks-ah store la serkkum."""
        vecs = embed(chunks)
        # Length 1 aakkidrom, appo cosine = simple dot product
        vecs = vecs / np.linalg.norm(vecs, axis=1, keepdims=True)
        self.texts.extend(chunks)
        self.sources.extend([source] * len(chunks))
        if self.vectors is None:
            self.vectors = vecs
        else:
            self.vectors = np.vstack([self.vectors, vecs])

    def search(self, question, k=3):
        """Question ku mosta match aagura top-k chunks."""
        q = embed([question])[0]
        q = q / np.linalg.norm(q)
        scores = self.vectors @ q
        top = np.argsort(scores)[::-1][:k]
        return [(self.sources[i], self.texts[i], float(scores[i])) for i in top]
