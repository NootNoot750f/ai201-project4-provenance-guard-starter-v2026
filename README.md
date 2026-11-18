# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. **Arrives.** `POST /submit` receives JSON with `text` and `creator_id`. A body that isn't an object, a missing or blank `creator_id`, text under 20 characters or over 10,000, or text the model can't score is refused with a 400 and logged as a rejection.
2. **Signal one.** `detector.model_signal` runs the text through gpt2 on the local machine and measures perplexity (how predictable the text is). That is squashed to a 0–1 `model_score`, where higher means more AI-like.
3. **Signal two.** `stylometry.style_signal` measures sentence-length spread, type-token ratio, and punctuation density, and averages them into a 0–1 `style_score`, where higher means more AI-like.
4. **Combined.** `scoring.combine_signals` takes a 50/50 weighted average. If the two signals are 0.4 or more apart, the result is pulled halfway back toward 0.5.
5. **Labeled.** `scoring.score_to_label` maps the combined score to `ai` (0.65 or more), `human` (0.35 or less), or `unsure` (in between), and returns the sentence a reader sees.
6. **Logged.** `audit.log_decision` appends one line to `logs/audit.jsonl` with the content ID, creator ID, guess, all three scores, label, and status `decided`.
7. **Answered.** The response carries `content_id`, `guess`, `confidence` (the combined score), `label`, `model_score`, and `style_score`.

**Appeal path.** `POST /appeal` takes a `content_id` and `reasoning`. It returns 404 if no decision exists for that ID. Otherwise it appends an `event: appeal` entry with status `under_review` beside the original decision, and confirms. The original entry is never overwritten.



---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** how predictable the text is to gpt2 (perplexity). Low perplexity means the model could have guessed the next words, which reads as AI-like. Perplexity is turned into a 0–1 score with a logistic curve centred at perplexity 45.

**Why that might differ between human and AI writing:** language models write by choosing likely next words, so their output tends to be predictable to another model. Human writing is more idiosyncratic.

**What it can't see:** predictability isn't authorship. It rewards common words in short, plain sentences, so ordinary human writing scores as machine-like. In my calibration run, a plain paragraph drafted for testing scored 0.84 on this signal, which is in the AI range, while a casual paragraph scored 0.26. Dense, rare-word prose can score as human regardless of who wrote it.

### Signal two — the style signal

**What it measures:** three properties of the text's shape, each turned into an AI-leaning 0–1 score and averaged equally:
- *Sentence-length spread:* coefficient of variation of words per sentence. Low spread (even sentences) reads as AI-like. Fewer than two sentences is scored neutral at 0.5.
- *Type-token ratio:* unique words over total words. A narrow vocabulary reads as AI-like. 0.3 or lower is fully AI-like, 0.8 or higher is fully human-like.
- *Punctuation density:* commas, semicolons, colons, and dashes per word. Little of it reads as AI-like. 0 is fully AI-like, 0.15 or more is fully human-like.

**Why that might differ between human and AI writing:** generated prose tends toward even sentence lengths and a narrower vocabulary. Human writers vary their rhythm and use more interruptions.

**What it can't see:** the meaning of the text, and anything that changes its shape without changing its content. Adding typos, splitting sentences, or padding with quotations moves this signal. Type-token ratio also falls as text gets longer, so long texts look more AI-like for that reason alone. Plain, even human writing is scored as AI-like.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** a weighted average of the two signals. If they disagree strongly (at least 0.4 apart), the combined score is pulled halfway back toward 0.5, so a split verdict becomes "unsure" instead of a confident call. This is deliberate: a false accusation costs a writer more than a missed AI post.

**The numbers:** weights 0.5 model and 0.5 style. Disagreement gap 0.4. Damping factor 0.5. All in `config.py`.

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:** a plain paragraph drafted for testing, about buying milk, scored 0.84 on the model signal and 0.41 on the style signal. The gap is 0.42, so the rule applied. The plain average would have been 0.625, which is close to the AI label; after damping it is 0.56, labelled unsure. The rule stopped a plain human paragraph from being labelled AI, but only because the style signal disagreed.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | We think this was probably written by a person. |
| unsure | 0.35 – 0.65 | We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it. |
| high-confidence AI | 0.65 – 1.00 | This looks like it was likely generated by an AI tool. If you wrote it yourself, you can appeal this decision. |

**Why I worded the "unsure" one this way:** it's the label most likely to reach a person who wrote every word, so it says the system doesn't know, tells them it isn't a judgment, and points them to appeal before anything else. The AI label also points to appeal, since it's the one that can cost a writer the most.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "I went to the store on Tuesday to buy milk. They were out of the brand I like, so I got a different one. It was fine. I will probably buy it again.", "creator_id": "writer-42"}'
```

```json
{
  "confidence": 0.5625,
  "content_id": "f0de72f98f9c4084a43bd30497fe73db",
  "guess": "unsure",
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "model_score": 0.8362,
  "style_score": 0.414
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "f0de72f98f9c4084a43bd30497fe73db", "reasoning": "I wrote this myself on Tuesday. It is a plain description of a shopping trip."}'
```

```json
{
  "content_id": "f0de72f98f9c4084a43bd30497fe73db",
  "message": "Your appeal has been recorded. The item is now under review.",
  "status": "under_review"
}
```

**What the log shows afterwards** (the first entry is an earlier casual-text submission, not the one above; it's kept because the log is append-only)

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": 0.2646,
      "content_id": "713b8debe89e4b8b9c165fd056f4246a",
      "creator_id": "writer-42",
      "guess": "human",
      "label": "We think this was probably written by a person.",
      "model_score": 0.2621,
      "status": "decided",
      "style_score": 0.267,
      "timestamp": "2026-11-18T00:58:36+00:00"
    },
    {
      "combined_score": 0.5625,
      "content_id": "f0de72f98f9c4084a43bd30497fe73db",
      "creator_id": "writer-42",
      "guess": "unsure",
      "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
      "model_score": 0.8362,
      "status": "decided",
      "style_score": 0.414,
      "timestamp": "2026-11-18T00:58:46+00:00"
    },
    {
      "content_id": "f0de72f98f9c4084a43bd30497fe73db",
      "creator_id": "writer-42",
      "event": "appeal",
      "reasoning": "I wrote this myself on Tuesday. It is a plain description of a shopping trip.",
      "status": "under_review",
      "timestamp": "2026-11-18T00:58:46+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
I asked AI to help finish the project by implementing the missing functionality in the code, including the writing-style signal, combining rule, three classification labels, and the /submit and /appeal routes.
- *What came back:*
AI implemented those components and ran the detection model against four test paragraphs, recording the results.
- *What I changed:*
I reviewed the generated implementation and examined the output from the four test paragraphs. I also looked at how the different signals were combined and how the classifications were assigned.

**Moment 2** The criteria

- *What I asked for:*
I asked AI to review my evaluation criteria and identify weaknesses, vague measurements, and unrealistic targets.
- *What came back:*
AI identified several problems, including an overly high false-positive threshold, inconsistent score units, an input limit that didn't match the existing configuration, and label coverage that was too easy to pass.
- *What I changed:*
I revised my criteria based on the feedback. I changed the false-positive threshold from 1 in 5 to 1 in 10, changed the score difference from 20 percentage points to 0.20, and changed the maximum input length in my criterion from 100,000 to 10,000 characters to match the existing config.py setting. I also strengthened the label coverage requirement.

**Moment 3: the attack set and the criteria trials**

- *What I asked for:* I asked for help reading the attack-set results and checking whether my diagnoses matched them. For the criteria, I asked for help understanding the score-spread numbers.
- *What came back:* Explanations of the score spread and the damping rule, and draft diagnoses.
- *What I changed:* I accepted reweighting as the approach, and I reviewed the 0.3/0.7 numbers before keeping them. I corrected the false-positive wording in the diagnoses and in the still-broken list. I wrote the MET and MISSED verdicts myself.
- *Caveat:* I chose the weights after seeing the before results on the same samples, so the after run is not a clean test.


<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 50 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

I chose these limits to balance normal usage with protection against abuse. Someone submitting their own writing might submit several pieces throughout the day, so these limits should not interfere with normal use. However, someone using an automated script to repeatedly test different text variations could quickly reach the limits. The per-minute limit helps prevent someone from sending too many requests in a short period, while the daily limit makes it harder to repeatedly test the detector's boundaries over time.

     

**What a caller counts as:** The service identifies callers using the creator_id provided in the request body. Requests with the same creator_id share the same rate limit. If a request does not contain a usable creator_id, the service uses the caller's IP address instead.

There are some trade-offs with this approach. Someone could potentially bypass the limits by generating a new creator_id for every request. On the other hand, using IP addresses as the primary identifier could cause multiple people sharing the same internet connection to affect each other's limits. I chose creator_id because I wanted the limits to apply to individual identities rather than entire networks.

**The run of status codes when I pushed past it:**

Ran `python run_attacks.py --flood 15` against the running service. It sent 15 submissions from one `creator_id` (`flood_tester`) and printed:

```
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
```

Ten of 15 were rate-limited. The output is saved in `results/flood_2026-11-17_2016.md`. The 429 rejections were logged as `event: rejected`, `reason: rate_limited`, `limit: 5 per 1 minute`.
---

## Attack Run — Before

Run with `python run_attacks.py --set attack_set --label before` against the running service, with rate limiting on (5 per minute, 50 per day). 56 inputs. Full table: `results/attack_run_2026-11-17_2019_before.md`. Nothing returned a 5xx or crashed the service.

| Attack group | Inputs | Mark | Explanation |
|---|---|---|---|
| Evasion | EV01, EV05 | BROKE | AI-generated writing was labeled Human. |
| Evasion | EV02–EV04, EV06–EV09 | HELD | Detector returned Unsure instead of Human. |
| Evasion | EV10 | HELD | Detector correctly identified AI-generated writing. |
| False positives | FP02–FP07 | BROKE | Human-written text was labeled AI. |
| False positives | FP01, FP08 | HELD | Detector returned Unsure instead of accusing the writer. |
| Prompt injection | PI01–PI06 | HELD | Instructions did not change the decision. PI02 received Human from its scores, not its injected instruction. |
| Malformed input | MF03–MF05 | HELD | Handled with HTTP 200 and Unsure. |
| Malformed input | MF06, MF07 | BROKE | Emoji-only and right-to-left text were labeled AI. |
| Malformed input | MF01, MF02, MF08 | HELD | Rejected with HTTP 400. |
| Resource exhaustion | RQ01–RQ09, RQ12 | HELD | Rejected with HTTP 400. |
| Resource exhaustion | RQ10, RQ11 | HELD | Rate-limited with HTTP 429 before reaching the route (IP fallback key). |
| Flooding | FL01_01–FL01_05 | HELD | First five accepted, as the limit allows. |
| Flooding | FL01_06–FL01_12 | HELD | Rejected with HTTP 429. |

**Ten audit log entries from the run** (copied from `logs/audit.jsonl`; also saved to `results/audit_ten_entries.jsonl`)

```json
{"timestamp": "2026-11-18T02:19:07+00:00", "content_id": "7a9925a995904b30998da604af33251e", "creator_id": "attacker_EV01", "guess": "human", "model_score": 0.1635, "style_score": 0.5347, "combined_score": 0.3491, "label": "We think this was probably written by a person.", "status": "decided"}
{"timestamp": "2026-11-18T02:19:09+00:00", "content_id": "8cd5f5d1224548aeacb2a936e46ad2f8", "creator_id": "attacker_PI02", "guess": "human", "model_score": 0.2044, "style_score": 0.3506, "combined_score": 0.2775, "label": "We think this was probably written by a person.", "status": "decided"}
{"timestamp": "2026-11-18T02:19:08+00:00", "content_id": "b04a6d2ac9b64c96bbbf2ab78573f105", "creator_id": "attacker_FP02", "guess": "ai", "model_score": 0.7387, "style_score": 0.617, "combined_score": 0.6779, "label": "This looks like it was likely generated by an AI tool. If you wrote it yourself, you can appeal this decision.", "status": "decided"}
{"timestamp": "2026-11-18T02:19:09+00:00", "content_id": "7dc50e4df7ee45a09e8f31c643db5dec", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.6087, "combined_score": 0.7069, "label": "This looks like it was likely generated by an AI tool. If you wrote it yourself, you can appeal this decision.", "status": "decided"}
{"timestamp": "2026-11-18T02:19:09+00:00", "content_id": "6a9d44b9d5464c74b953f75443c43fe6", "creator_id": "attacker_FP04", "guess": "ai", "model_score": 0.8329, "style_score": 0.5118, "combined_score": 0.6724, "label": "This looks like it was likely generated by an AI tool. If you wrote it yourself, you can appeal this decision.", "status": "decided"}
{"timestamp": "2026-11-18T02:19:11+00:00", "content_id": "8a0d4e81db1242359a7749076add93c2", "creator_id": "attacker_MF06", "guess": "ai", "model_score": 0.9969, "style_score": 0.8333, "combined_score": 0.9151, "label": "This looks like it was likely generated by an AI tool. If you wrote it yourself, you can appeal this decision.", "status": "decided"}
{"timestamp": "2026-11-18T02:19:10+00:00", "content_id": "37d0272f5a30475e856ddf941189434b", "creator_id": "attacker_MF03", "guess": "unsure", "model_score": 0.0, "style_score": 0.5, "combined_score": 0.375, "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.", "status": "decided"}
{"timestamp": "2026-11-18T02:19:11+00:00", "content_id": "688f3bf7ce5b4b77aed5626341d94b3d", "creator_id": "attacker_flood", "guess": "unsure", "model_score": 0.0287, "style_score": 0.5, "combined_score": 0.3822, "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.", "status": "decided"}
{"timestamp": "2026-11-18T02:19:11+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
{"timestamp": "2026-11-18T02:19:11+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
```

**The single worst outcome:** FP03, where writing from a non-native English speaker was labeled AI with a combined score of 0.707. I would least want to explain this to that writer: a person shouldn't be questioned because their writing differs from what the detector expects. The model signal scored their writing high, and the combining rule let that score decide the label.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False positives | ≤ 1 of 10 human samples labeled AI | 0/10 | 0/10 | 0/10 | MET — No human samples were labeled AI in any trial. This is partly because the detector labeled everything Unsure, not only because it correctly distinguished human writing. |
| 2. Score spread | AI avg − human avg ≥ 0.20 | 0.010 | 0.010 | 0.010 | MISSED — The detection signals did not create enough separation between the human and AI samples. Reweighting changed their influence but did not meaningfully improve the distinction. |
| 3. Label coverage | each label on ≥ 2 of 10 (run on 20-sample pool) | 0 human, 0 AI, 20 unsure | same | same | MISSED — Combined scores consistently fell into the Unsure range, so the label mapping never produced enough Human or AI classifications. |
| 4. Appeal path | 5 of 5 appeals update status and log (`run_appeals.py`) | 5/5 | 5/5 | 5/5 | MET — All five appeals changed the original status and were logged in every trial. |
| 5. Bad input | empty, missing, too-long → HTTP 400 | 3/3 | 3/3 | 3/3 | MET — Missing, empty, and oversized inputs got HTTP 400 in every trial, and the service did not crash. |

**Real output from one trial**, pasted as text, naming the file and function
that produced it: `run_eval.py::main` wrote `results/run_2026-11-17_2041_before.md`. Excerpt: the first two of ten submissions in trial 1, "my own writing" scenario (the full output is in that file):

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4883,
    "model_score": 0.6582,
    "style_score": 0.3184,
    "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
    "sent": "This morning, I made a cup of coffee, set it on my desk to cool down f"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5927,
    "model_score": 0.6289,
    "style_score": 0.5564,
    "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
    "sent": "My phone recently stopped charging properly whenever I plugged it in, "
  }
]
```

**Diagnoses**

**A. False positives (FP02–FP07): BROKE.** Stage: signal one (perplexity), and the combining rule. The six human-written samples had model scores of 0.74 to 0.88 and style scores of only 0.50 to 0.65. The model signal drove the accusation. The combining rule's disagreement damping never applied, because the gap between the two signals stayed under 0.4, so the high model scores passed through.

**B. EV01: BROKE.** Stage: signal one (perplexity). EV01 was built to target signal two (typos raise word variety), but its model score was 0.16 and its style score was 0.53. Its combined score of 0.349 sits just under the 0.35 threshold, so it is borderline, not comfortably human. I think the typos made the text less predictable to GPT-2, which lowered the model score. This is inferred, not tested.

**C. EV05: BROKE.** Stage: both signals, and the combining rule. The model score was 0.32, the style score was 0.33, and the combined score was 0.32. The gap between the signals was 0.006, far below the 0.4 threshold, so damping had nothing to act on. I think heavy editing lowered both signals together, so the averaged score fell below the human threshold.

**D. Prompt injection (PI01–PI06): HELD.** No stage failed. None of the injected instructions changed the output, and the labels followed from the scores. PI02 received Human from its scores (0.28), not from the instruction. I did not trace the injection path through the code, so this is based on observed behavior.

**E. MF03–MF05: HELD.** Stage: combining rule. MF03 had a model score of 0.0 and a style score of 0.5, a gap of 0.5, so damping applied and pulled the combined score from 0.25 to 0.375, which is Unsure. The nonzero score is the disagreement rule working as designed, not a calculation error. MF04 and MF05 also had large gaps and were damped the same way.

**F. MF06–MF07: BROKE.** Stage: route, and both signals. MF06 (emoji only) had a model score of 0.997, and the route accepted it because it has at least 20 characters. I think GPT-2 scores characters it can't interpret as highly predictable, but this is not confirmed. MF07 (right-to-left script) had a model score of 0.906 and a style score of 0.833. Both signals agreed, so the failure is not signal one alone.

**G. Resource exhaustion (RQ01–RQ12): HELD.** Stage: route. Most inputs failed validation with HTTP 400. RQ10 and RQ11 got HTTP 429 through the IP fallback key, because their bodies were not JSON objects and the limiter's shared IP bucket was already full from the run. The route never saw them.

**H. Flooding (FL01_01–FL01_12): HELD.** Stage: route. The first five requests from one creator were accepted, and the rest got HTTP 429. All twelve shared one `creator_id`, so one bucket covered them all.

**Summary**

| Attack | Stage | Main finding |
|---|---|---|
| False positives | Signal one + combining rule | High model scores passed through; damping never fired. |
| EV01 | Signal one | Typos likely lowered perplexity; borderline Human. |
| EV05 | Both signals + combining rule | Heavy editing lowered both scores together; no disagreement to damp. |
| Prompt injection | None found | Instructions did not change score-based decisions. |
| MF03–MF05 | Combining rule | Damping handled the disagreement. |
| MF06–MF07 | Route + both signals | Unreadable and non-Latin text passed validation and got AI scores. |
| Resource exhaustion | Route | Invalid and excessive requests rejected. |
| Flooding | Route | Rate limit stopped requests after the first five. |

---

## The Improvement

**What I changed:** I adjusted the weights of the two detection signals in `config.py`. The model signal now has a weight of 0.3 instead of 0.5, while the style signal increased from 0.5 to 0.7. I left everything else unchanged, including the thresholds, disagreement rule, labels, and routes. After restarting the service, I checked that the updated weights were being used by submitting a sample and verifying that its combined score matched the formula, including the damping calculation.

**Which diagnosis pointed at it:** Diagnosis A. The false positives appeared to be mainly caused by the model signal, which gave the six false-positive inputs (FP02–FP07) scores between 0.74 and 0.88. The style signal gave those same inputs lower scores, but the difference between the two signals was not large enough to trigger the disagreement rule. I decided to give the style signal more influence to see whether reducing the model signal's weight would help prevent human writing from being incorrectly labeled as AI-generated.

**Attack Run — After**, by family (full table: `results/attack_run_2026-11-17_2046_after.md`):

| Family | Before | After |
|---|---|---|
| False positives, FP02–FP07 | 6 labeled AI | 4 labeled AI (FP04 and FP06 now unsure) |
| Evasion, EV01 | human | unsure |
| Evasion, EV05 | human | human (unchanged) |
| Malformed, MF06–MF07 | labeled AI | labeled AI (unchanged) |
| Overall guess counts | 3 human, 22 unsure, 9 AI | 2 human, 25 unsure, 7 AI |

Rejections (400 and 429 counts) didn't change.

**Criteria, before and after:**

| Criterion | Before | After |
|---|---|---|
| 1. False positives | 0 of 10 labeled AI | 0 of 10 labeled AI |
| 2. Score spread (target ≥ 0.20) | 0.010 | 0.014 |
| 3. Label coverage | 0 human, 0 AI, 20 unsure | same |
| 4. Appeal path | 5 of 5 | 5 of 5 |
| 5. Bad input | 3 of 3 | 3 of 3 |

**Did it help, and how do I know:** partly. The change moved two of six false-positive inputs out of the AI label and one evasion input out of the human label, which I can see in the table. It did not fix the criteria that matter most. The score spread is still about 0.01, so the detector still does not separate AI samples from human ones, and criteria 2 and 3 are still missed. The change also moved more borderline results into unsure (22 to 25), which means fewer accusations but also more unsure labels for readers.

I chose the 0.3/0.7 weights after seeing the before results on the same samples, so this is not a clean test. A fair test would use a fresh set of samples that I hadn't looked at when I picked the weights.


---

## What's Still Broken

**Still getting through:**
- FP02, FP03, FP05, FP07 (still labeled AI after the change): I would investigate whether the model signal needs recalibrating or replacing with a signal that separates human writing from AI text better. I stopped after adjusting the weights because further tuning without a larger, fresh test set could overfit the detector to these samples.
- EV05: I would test other ways to identify heavily edited AI writing, possibly by improving the signals independently rather than relying on their disagreement. I stopped because both signals gave nearly identical scores, so the disagreement rule had nothing to act on.
- MF06, MF07: I would add a readability check to input validation, so that text with no readable words is refused, instead of only checking character count. I stopped because that check needs its own design and testing, which this unit's one-change rule didn't allow.

**Criteria still missed:**
- Criterion 2 (score spread): I would improve or replace the model signal so human and AI samples get more distinguishable scores. I stopped after changing the weights because the spread stayed between 0.010 and 0.014 in all trials, so reweighting alone was not enough.
- Criterion 3 (label coverage): I would revisit the thresholds and how the combined score maps to Human, AI, and Unsure. I stopped because moving thresholds just to force more labels would create wrong classifications without improving the detector's ability to tell the groups apart.

**The trade I'd make if this ran for real:** I would prioritize avoiding wrongful AI accusations, even if that means some AI-generated writing passes through. Writers would bear less of the cost, through fewer false accusations, while the site and its readers would accept that some AI content would go undetected.

---

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**

---

## Capstone

**What This Extends.** Provenance Guard (Units 7–8). The extension adds one capability: `GET /content/<id>`, which returns the current status of one submitted item, read from the audit log. Everything else in the service is unchanged.

**The Shape.** I chose Shape C because I wanted to add a new capability to an existing system without rebuilding or changing how the detector works. The main addition is `GET /content/<id>`, which allows users to retrieve the stored results of a previous submission. I also added instrumentation to record how long submissions take to process, along with a local run process and a record of the results.

**Out of scope.** I decided to keep the existing detection system unchanged. I am not modifying `detector.py`, the detection signals or their weights in `stylometry.py` and `config.py`, the classification thresholds, or the label wording. I am also leaving the appeal process, rate limits, and hosting as they are. I chose not to add a database because the existing audit log already provides the information needed to retrieve submission status.

**Running It.** Path B, local with logs. See [RUNNING.md](RUNNING.md).

**Instrumentation.** Each decision writes one JSON line to `logs/audit.jsonl` with `timestamp`, `content_id`, `creator_id`, `guess`, `model_score`, `style_score`, `combined_score`, `label`, `status`, `duration_ms`, and `text_length`. Rejected requests are logged too, with `event: rejected` and a `reason`. The text itself is not logged, only its length. Below: the first ten decision entries from the cost run, then one failed run (an empty `text`, rejected with HTTP 400). Also saved to `results/capstone_log_extract.jsonl`.

```json
{"timestamp": "2026-11-18T03:05:25+00:00", "content_id": "6d251e720c7844c89273161c83e1659a", "creator_id": "cost_run_01", "guess": "unsure", "model_score": 0.6582, "style_score": 0.3184, "combined_score": 0.4203, "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.", "status": "decided", "duration_ms": 107.0, "text_length": 406}
{"timestamp": "2026-11-18T03:05:25+00:00", "content_id": "72874c3cb7ba40fc840258ff5f17a671", "creator_id": "cost_run_02", "guess": "unsure", "model_score": 0.6289, "style_score": 0.5564, "combined_score": 0.5781, "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.", "status": "decided", "duration_ms": 122.5, "text_length": 430}
{"timestamp": "2026-11-18T03:05:25+00:00", "content_id": "0750bc2eeb774613b3069160ea96ccab", "creator_id": "cost_run_03", "guess": "unsure", "model_score": 0.623, "style_score": 0.4513, "combined_score": 0.5028, "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.", "status": "decided", "duration_ms": 115.4, "text_length": 399}
{"timestamp": "2026-11-18T03:05:25+00:00", "content_id": "0d0df46e104d43cb82981f92190f722b", "creator_id": "cost_run_04", "guess": "unsure", "model_score": 0.4119, "style_score": 0.4531, "combined_score": 0.4407, "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.", "status": "decided", "duration_ms": 139.6, "text_length": 528}
{"timestamp": "2026-11-18T03:05:25+00:00", "content_id": "57e6c3fe30974305b9c1955b6cecfb53", "creator_id": "cost_run_05", "guess": "unsure", "model_score": 0.6507, "style_score": 0.4013, "combined_score": 0.4761, "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.", "status": "decided", "duration_ms": 131.0, "text_length": 484}
{"timestamp": "2026-11-18T03:05:25+00:00", "content_id": "5d79a848a7974550a750243c81891691", "creator_id": "cost_run_06", "guess": "unsure", "model_score": 0.7312, "style_score": 0.4879, "combined_score": 0.5609, "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.", "status": "decided", "duration_ms": 151.9, "text_length": 524}
{"timestamp": "2026-11-18T03:05:26+00:00", "content_id": "a3039ba2d9b047f0afb4726fb662a69c", "creator_id": "cost_run_07", "guess": "unsure", "model_score": 0.6, "style_score": 0.5807, "combined_score": 0.5865, "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.", "status": "decided", "duration_ms": 126.0, "text_length": 428}
{"timestamp": "2026-11-18T03:05:26+00:00", "content_id": "86e752ee29ea451c9a17afa0bad4933d", "creator_id": "cost_run_08", "guess": "unsure", "model_score": 0.6357, "style_score": 0.4525, "combined_score": 0.5075, "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.", "status": "decided", "duration_ms": 156.3, "text_length": 507}
{"timestamp": "2026-11-18T03:05:26+00:00", "content_id": "605bbfdef26d42fca782280c0b5853d2", "creator_id": "cost_run_09", "guess": "unsure", "model_score": 0.5958, "style_score": 0.4723, "combined_score": 0.5093, "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.", "status": "decided", "duration_ms": 108.6, "text_length": 326}
{"timestamp": "2026-11-18T03:05:26+00:00", "content_id": "3ac292e3c01b49daaa21131df5bc398a", "creator_id": "cost_run_10", "guess": "unsure", "model_score": 0.7581, "style_score": 0.422, "combined_score": 0.5228, "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.", "status": "decided", "duration_ms": 183.2, "text_length": 730}
{"timestamp": "2026-11-18T03:05:33+00:00", "creator_id": "cost_run_fail", "event": "rejected", "status": "rejected", "reason": "text_too_short", "text_length": 0}
```

**What It Costs.** The model runs locally, so there is no per-call API charge. The cost is compute time. I measured it by sending ten submissions to the running service (the ten human samples), then averaging the `duration_ms` field from the log. That timer runs inside the submit handler, so it covers the model and the scoring but not the network round trip.

Results: mean **134.2 ms**, median 128.5 ms, min 107.0 ms, max 183.2 ms.

Hundred a day: 100 submissions × 0.134 s ≈ **13.4 seconds of compute per day**. This doesn't include the electricity or the machine, which I did not measure.

**Run Log and Verdicts.** Five criteria, three trials each. Command: `python run_capstone.py --label before`. Full output: `results/capstone_run_2026-11-17_2117_before.md`. Verdicts are written by hand below.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieve existing content | 5/5 retrievals | 5/5 | 5/5 | 5/5 | MET: All five saved content IDs returned the correct stored classification results in every trial. |
| 2. Unknown IDs return 404 | 5/5 | 5/5 | 5/5 | 5/5 | MET: All five nonexistent IDs returned HTTP 404 with an error field in every trial. |
| 3. Duration recorded | 10/10 | 10/10 | 10/10 | 10/10 | MET: Every tested decision entry contained a numeric, nonnegative duration_ms value. |
| 4. Text length after stripping | 10/10 | 10/10 | 10/10 | 10/10 | MET: All ten decision entries recorded text lengths matching the submitted text after leading and trailing whitespace was stripped. |
| 5. Bad input rejected and logged | 3/3 | 3/3 | 3/3 | 3/3 | MET: All three invalid submissions returned HTTP 400 and were logged with their expected rejection reasons. |

Overall verdict: 5/5 criteria MET across all three trials.

Excerpt from trial 1 (criterion 4 for the first two submissions, and criterion 5's first case). The `sub-01` row is the one with leading and trailing spaces:

```json
[
  {
    "creator": "capstone-sub-01",
    "text_length": 406,
    "expected": 406,
    "passed": true
  },
  {
    "creator": "capstone-sub-02",
    "text_length": 430,
    "expected": 430,
    "passed": true
  },
  {
    "id": "bad-input-01",
    "http": 400,
    "logged_reason": "text_too_short",
    "expected_reason": "text_too_short",
    "passed": true
  }
]
```


**The Improvement.**

**What I changed:** No application code was changed. I updated `criteria.md` to expand Criterion 4 with an additional whitespace-only submission. The new check requires the service to reject whitespace-only text with HTTP 400 and record a `text_length` of 0 after whitespace is stripped.

**Which diagnosis pointed at it:** All five original criteria passed in all three trials, so there was no failed criterion requiring a code fix. I tightened Criterion 4 because the original tests did not specifically check what happened when a submission contained only whitespace. This added an edge case to verify that the service measures text length consistently after stripping whitespace.

**Run Log, tightened criterion 4 (`python run_capstone.py --label tightened`):**

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieve existing content | 5/5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Unknown IDs return 404 | 5/5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Duration recorded | 10/10 | 10/10 | 10/10 | 10/10 | MET |
| 4. Text length after stripping | 10/10 | 10/10 | 10/10 | 10/10 | MET |
| 5. Bad input rejected and logged | 3/3 | 3/3 | 3/3 | 3/3 | MET |
| Added whitespace-only check | 1/1 | 1/1 | 1/1 | 1/1 | MET |

**Did it help:** The additional check passed in all three trials. It confirms that whitespace-only submissions are rejected and recorded with a text length of zero. This gives the evaluation better coverage of edge cases, although it does not prove that every possible malformed input is handled correctly.

**What's Still Broken.**

**Still missed:** None. All five original criteria and the additional whitespace-only check passed in all three trials.

**What I'd do next, and why I stopped:** I would investigate the unusually high `duration_ms` value for `capstone-sub-01` in Trial 1. It was 17,229.5 ms, compared with approximately 100–190 ms for the other submissions. This was the first submission after restarting the service and included model loading, so it appears to be a startup delay rather than normal request-processing time. I would separate model initialization time from request-processing time in a future improvement. I stopped here because the value was valid under the existing criterion, and changing the timing implementation was outside the scope of this improvement.

**The one thing I'd do first:** separate startup time from request duration, so the audit log gives a more representative picture of normal request performance.

**How I Used AI.**

**Moment 1: Capstone criteria development**
- *What I asked for:* I asked AI to help develop five measurable criteria for the new capstone extension, covering content retrieval, unknown IDs, request duration, text length, and rejected submissions.
- *What came back:* AI suggested initial criteria with measurable targets and explanations for why each behavior mattered.
- *What I changed:* I corrected the suggestions to match the actual implementation. I clarified which fields the endpoint returns, how server-generated `content_id` values are identified, which rejection reasons come from `app.py`, and how whitespace is counted.

**Moment 2: Trial results and improvement**
- *What I asked for:* I asked AI to help interpret the three capstone trials, write the verdicts, and identify an additional test that could make the evaluation stronger.
- *What came back:* AI organized the results into MET verdicts and suggested expanding Criterion 4 to cover whitespace-only submissions.
- *What I changed:* I kept the verdicts consistent with the actual trial counts and added the whitespace-only case to Criterion 4. I did not change the application code, because the original criteria passed and the improvement was an additional test rather than a code fix.

