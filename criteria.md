# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False Positives

No more than 1 out of 10 pieces of human-written text that I personally wrote should be incorrectly labeled as AI.

Why this target:

I chose this target because falsely identifying human writing as AI can have serious consequences for the writer, including loss of credibility and potential academic penalties. For this reason, I believe it is more important to protect genuine writers from false accusations than to catch every instance of AI-generated writing.

---

## 2. Score Spread

<!-- Your criterion. -->
The average AI detection score across 10 AI-generated writing samples must be at least 0.20 higher than the average score across 10 human-written writing samples in each of the three trials.

**Why this target:**
I chose this target because the detector should be able to distinguish between human and AI-generated writing. A difference of at least 0.20 on a 0–1 scale provides a measurable separation between the two groups. If their scores are too similar, it could indicate that the detector struggles to identify the source of the writing.



---

## 3. Label Coverage

<!-- Your criterion. -->
Each of the three available classifications (Human, AI, and Unsure) must be assigned to at least 2 of 10 predefined test samples across each of the three trials.


**Why this target:**
I chose this target because having three classifications is only useful if the system can actually utilize all three. Requiring each classification to appear at least twice makes it harder for the system to pass simply because one unusual piece of writing received an unexpected result.


---

## 4. The appeal path

<!-- Your criterion. -->
All 5 predefined appeal submissions must successfully update their original classification status and create an entry in logs/audit.jsonl containing event: appeal during each of the three trials.


**Why this target:**
I chose this target because users should be able to challenge classifications they believe are incorrect. Every appeal should result in a status change and be recorded in the audit log. This provides accountability and allows appeals to be tracked rather than silently ignored.


---

## 5. Bad Input

<!-- Your criterion. -->
The system must handle missing text, empty text, and text exceeding the 10,000-character limit by returning an appropriate HTTP 400 response with an error message, without crashing, in all three trials.


**Why this target:**
I chose this target because users may accidentally submit incomplete or excessively large pieces of text. The system should recognize invalid input and explain the problem instead of crashing or attempting to process invalid data. This makes the service more reliable and user-friendly.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
