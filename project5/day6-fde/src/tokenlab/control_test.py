from pathlib import Path

import httpx

docs = sorted(Path("data/policies").glob("*.txt"))
context = "\n\n=====\n\n".join(f.read_text(encoding="utf-8") for f in docs)
q = "In which months do performance reviews happen?"
prompt = (
    "Answer using ONLY the policies below. "
    "If the answer is not there, say 'not found'.\n\n"
    f"{context}\n\nQuestion: {q}\nAnswer:"
)

for num_ctx in (1024, 4096):
    r = httpx.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen3.5:2b",
            "prompt": prompt,
            "stream": False,
            "options": {"num_ctx": num_ctx, "temperature": 0},
        },
        timeout=300,
    ).json()
    print(f"\nnum_ctx={num_ctx}")
    print("prompt tokens seen by model:", r.get("prompt_eval_count"))
    print("response:", repr(r.get("response", "")[:150]))
    print("thinking:", repr(str(r.get("thinking", ""))[:100]))
