from pathlib import Path

import tiktoken

# Tokenizer load pannu
enc = tiktoken.get_encoding("cl100k_base")

texts_folder = Path("data/texts")

print("| file | characters | tokens |")
print("|---|---|---|")

for file in sorted(texts_folder.glob("*.txt")):
    text = file.read_text(encoding="utf-8")
    tokens = enc.encode(text)
    print(f"| {file.name} | {len(text)} | {len(tokens)} |")
