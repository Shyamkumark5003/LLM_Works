# Which chunking works best?

Test: 20 synthetic policy docs, 10 questions, top-3 retrieval,
embedding model nomic-embed-text (local, Ollama).

| Chunking | Score |
|---|---|
| fixed (200 chars) | 10/10 |
| paragraph | 9/10 |
| overlap (200 chars, 50 overlap) | 10/10 |

## Winner
Overlap and fixed tied at 10/10. I would choose **overlap** for real use.

## Why
- Fixed chunking cuts text at random places (for example "befo" / "re"),
  so an answer can be split across two chunks. Overlap repeats 50
  characters, so a cut sentence still appears whole in one chunk.
- Paragraph chunking failed on question 1. The answer ("7 days") sat in
  the "How to follow" paragraph, but the "Exception" paragraph, which also
  talks about leave, ranked higher. Paragraphs mix several ideas, so the
  embedding is not focused on one fact.

## Limits of this test
- Documents are short (about 450 characters), so cuts hurt less.
- Only 10 easy questions, and the check only looks for a keyword in
  the top-3 chunks.
- With longer real documents the gap between fixed and overlap would
  likely be bigger. Not tested here.
