import os
from pathlib import Path

import httpx
import tiktoken

# 20 policy docs ellam serthu oru periya prompt
docs = sorted(Path("data/policies").glob("*.txt"))
context = "\n\n=====\n\n".join(f.read_text(encoding="utf-8") for f in docs)

QUESTIONS = [
    ("FIRST doc", "How many days of annual leave do employees get per year?", "20"),
    ("LAST doc", "In which months do performance reviews happen?", "June"),
]


def make_prompt(q):
    return (
        "Answer using ONLY the policies below. "
        "If the answer is not there, say 'not found'.\n\n"
        f"{context}\n\nQuestion: {q}\nAnswer:"
    )


enc = tiktoken.get_encoding("cl100k_base")
print("Prompt tokens (approx):", len(enc.encode(make_prompt(QUESTIONS[0][1]))))


def ask_local(prompt, model="qwen3.5:2b", num_ctx=1024):
    r = httpx.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {"num_ctx": num_ctx, "temperature": 0},
        },
        timeout=300,
    )
    r.raise_for_status()
    return r.json()["response"].strip()


def ask_hosted(prompt):
    r = httpx.post(
        os.environ["HOSTED_BASE_URL"].rstrip("/") + "/chat/completions",
        headers={"Authorization": "Bearer " + os.environ["HOSTED_API_KEY"]},
        json={
            "model": os.environ["HOSTED_MODEL"],
            "temperature": 0,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=120,
    )
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"].strip()


for label, q, expected in QUESTIONS:
    p = make_prompt(q)
    print(f"\n### {label}: {q} (expected: {expected})")
    print("LOCAL  :", ask_local(p)[:200])
    print("HOSTED :", ask_hosted(p)[:200])
