# What an LLM cannot do

A large language model (LLM) is very good at reading and writing text.
It is not magic. These are the limits you should plan for.

## 1. It can sound sure and still be wrong
An LLM predicts likely words. It does not check facts. Always add a
check (a source link, a human review) for answers that matter.

## 2. It does not know your private data
It only knows what it was trained on, plus what we put in the prompt.
Your policies, contracts and customer records must be given to it,
for example through search over your documents.

## 3. It does not know recent events
Its knowledge stops at a training date. Newer facts need search or
fresh documents.

## 4. It can only read a limited amount at once
Every model has a "context window". Anything beyond it is not seen,
and some tools cut the text without warning.

## 5. It is weak at exact counting and arithmetic
Use normal code or a calculator for numbers that must be exact.

## 6. Answers can change
The same question can give different wording each time.

## Example from our test: small local model vs hosted model
We gave both models the same 20 company policies (about 1,600 tokens)
and asked two questions.

| Question | Small local model (window 1,024 tokens) | Hosted model |
|---|---|---|
| How many days of annual leave? | No answer (empty) | "20 days per year." (correct) |
| In which months are performance reviews? | No answer (empty) | "June and December" (correct) |

**Why: context window.** We ran the same small model again with only
one change: a larger window (4,096 tokens). It then answered correctly
("June and December"). So the model could do the task; its window was
too small for the text.

The failure was silent: no error message, just an empty answer. The
likely cause is that the model needs room both to read the text and to
think before answering, and 1,024 tokens did not leave enough.

Other reasons a small model can fail (smaller size, different
training) were not the cause in this test.

## What we recommend
- Keep a human check on important answers.
- Give the model your documents; do not expect it to know them.
- Test with your real documents and size before going live.
