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

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



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
