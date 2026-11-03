import httpx
import numpy as np


def embed(texts, model="nomic-embed-text"):
    """Text list kudu, numbers list tharum."""
    r = httpx.post(
        "http://localhost:11434/api/embed",
        json={"model": model, "input": texts},
        timeout=60,
    )
    r.raise_for_status()
    return np.array(r.json()["embeddings"])


def cosine(a, b):
    """Rendu numbers list evlo close nu solum. 1 = romba close."""
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
