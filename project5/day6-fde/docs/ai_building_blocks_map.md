# AI building blocks map

## 1. Multimodal input
**What it is:** The model can read more than text, such as images, scanned PDFs or audio. We send the file along with the question.
**When to use:** Invoices, scanned forms, screenshots, photos of documents.
**Cost / risk:** Images use many tokens, so cost and time go up. The file may contain hidden instructions, so treat it as untrusted data. Reading errors on blurry scans are possible.

## 2. Fine-tuning
**What it is:** We train an existing model a little more on our own examples. This changes how the model behaves or writes.
**When to use:** When prompts alone cannot give a fixed style or format, and we have many good examples.
**Cost / risk:** Needs good training data and effort to prepare it. Training and re-training cost money. It teaches style better than new facts, so for company documents, search over the documents is usually simpler.

## 3. Multi-agent systems
**What it is:** Several AI "workers" each do one job, for example one searches, one writes, one checks. They pass results to each other.
**When to use:** Big tasks that split into clear steps, or where a second agent should review the first.
**Cost / risk:** More model calls means higher cost and slower answers. Errors can pass from one agent to the next. Harder to debug than a single call.

## 4. Memory
**What it is:** The system saves useful facts from earlier chats and brings them back later. The model itself does not remember anything between calls.
**When to use:** Assistants that should remember user preferences or ongoing work.
**Cost / risk:** Privacy risk, because personal data is stored. Old or wrong memories can mislead answers. Users need a way to see and delete what is saved.

## 5. Context management
**What it is:** Choosing what goes into the model's limited window: instructions, retrieved documents, chat history. Long history is trimmed or summarized.
**When to use:** Long chats, big document sets, any case where everything does not fit (we saw this in our token lab).
**Cost / risk:** Too much text costs more and can hide the important part. Too little text drops key facts. Trimming can fail silently, so test with real sizes.

## 6. AI gateways
**What it is:** One central entry point that every model call passes through. It handles keys, limits, logs, and switching between models.
**When to use:** Many teams or apps using models, or when we need cost tracking, fallback and safety rules in one place.
**Cost / risk:** Extra system to run and maintain. It becomes a single point of failure and adds a small delay.

## 7. Skills
**What it is:** A packaged set of instructions (and files) for one kind of task. The model loads it only when the task needs it.
**When to use:** Repeated tasks with fixed steps or house style, such as report formats or review checklists.
**Cost / risk:** Low cost, since text loads only when needed. Wrong or outdated instructions give wrong work every time, so someone must own and update them.
