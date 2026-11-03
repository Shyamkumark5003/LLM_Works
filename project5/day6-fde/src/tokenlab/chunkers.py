def fixed_chunks(text, size=200):
    """Ovvoru 200 characters-ku vettu. Words naduvula kooda cut aagum."""
    return [text[i:i + size] for i in range(0, len(text), size)]


def paragraph_chunks(text):
    """Blank line vandha vettu. Oru paragraph = oru chunk."""
    parts = text.split("\n\n")
    return [p.strip() for p in parts if p.strip()]


def overlap_chunks(text, size=200, overlap=50):
    """200 characters chunk, aana 50 characters adutha chunk la repeat aagum."""
    step = size - overlap
    chunks = []
    for i in range(0, len(text), step):
        chunks.append(text[i:i + size])
        if i + size >= len(text):
            break
    return chunks