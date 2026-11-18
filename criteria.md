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

---

## Capstone criteria

Written before any capstone results existed. Committed in: capstone criteria

## 1. Retrieve existing content

**Criterion:** Before each trial, submit five valid capstone submissions and save the content_id returned by the server for each one in a list, named capstone-content-01 through capstone-content-05. For each of these five IDs, GET /content/<id> must return HTTP 200 and the correct guess, label, scores, status, and appeal flag for that submission.

**Target:** 5/5 successful retrievals in each trial.

**Why this target:** The new endpoint is intended to retrieve the stored classification results for previously submitted content. Returning incorrect scores, labels, or appeal status could make the endpoint unreliable when users review earlier submissions.

## 2. Handle unknown content IDs

**Criterion:** Requests to GET /content/<id> using the five nonexistent IDs missing-content-01, missing-content-02, missing-content-03, missing-content-04, and missing-content-05 must return HTTP 404 with an error field in the response body.

**Target:** 5/5 requests return HTTP 404 with an error field in each trial.

**Why this target:** Users may request IDs that do not exist. Returning a consistent 404 response makes it clear that the requested content could not be found.

## 3. Record request duration

**Criterion:** The audit log entries of type decision for submissions using the creator_id values capstone-sub-01 through capstone-sub-10 must each contain a duration_ms field that exists, is numeric, and is greater than or equal to zero. For each trial, evaluate the ten most recent matching decision entries, so earlier trial entries are not counted again.

**Target:** 10/10 entries contain valid duration_ms values in each trial.

**Why this target:** Request duration helps identify performance problems and investigate how long the service takes to process submissions. Every tested decision entry should contain a usable duration value.

## 4. Record text length accurately

**Criterion:** Every decision entry for submissions using the creator_id values capstone-sub-01 through capstone-sub-10 must contain a text_length field that matches the character count of the submitted text after leading and trailing whitespace is stripped. For each trial, evaluate the ten most recent matching decision entries.

**Target:** 10/10 entries have an accurate text_length value in each trial.

**Why this target:** Text length provides useful information about submission sizes without requiring someone to inspect the full content. Since the service strips leading and trailing whitespace, the logged length should reflect the text after that operation.

**Additional criterion (revised after the first run):** A whitespace-only submission using the creator_id capstone-whitespace-01 must be rejected with HTTP 400 and logged with text_length equal to 0 after leading and trailing whitespace is stripped.

**Target:** 10/10 accurate text-length entries for the original submissions, plus 1/1 whitespace-only submission handled correctly in each trial.

**Why this target:** A whitespace-only submission may contain characters before stripping, but it has no actual text content afterward. Testing this case verifies that the service measures the text consistently after trimming whitespace and does not treat whitespace as meaningful content.

## 5. Handle rejected submissions

**Criterion:** The following three predefined submissions must each return HTTP 400 and create a rejection entry in the audit log with the specified reason:
- bad-input-01: Empty text, expected reason text_too_short.
- bad-input-02: Missing text field, expected reason text_not_string.
- bad-input-03: Text containing 10,001 non-whitespace characters, expected reason text_too_long.

**Target:** 3/3 submissions return HTTP 400 and are logged with the correct rejection reason in each trial.

**Why this target:** Invalid submissions should be rejected consistently, and the audit log should explain why each request failed. These three cases cover missing, empty, and oversized text.
