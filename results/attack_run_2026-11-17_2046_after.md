# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-17 20:46
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `981acd3445bf4817aeb5c58233f995a2` | unsure | 0.423 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `092f8ad28a1445e0a5e0522324435678` | unsure | 0.396 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `701dc582d9e446c6bfafd2a7bfb2b1ec` | unsure | 0.504 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `f3427fbe28a749b1a4b10988c29ee964` | unsure | 0.555 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `fcf700b3cad742b1856a00b9035eb152` | human | 0.325 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `f078bede4da148958f0e0ba79cc480d5` | unsure | 0.378 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `7e9ccea42c2d4f228ff5bd8414089e45` | unsure | 0.403 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `d250afed571841338bf54b17568b7d6b` | unsure | 0.474 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `7576d9593d4b4399a47f3eb0f7df2afc` | unsure | 0.499 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `0225be27883d40afb8fd679ce1153850` | ai | 0.892 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `321bd00e6701404db253a53fe4613846` | unsure | 0.558 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `7800600c987e4e59af3c7d4ac75cdef3` | ai | 0.653 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c103b465945c48b79f92fb4b922296e7` | ai | 0.668 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `41c154e09c75438ba952874432139e14` | unsure | 0.608 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `cba3568d15fb420fb6fda6f7495b6e10` | ai | 0.698 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `6b2f68a5576249888af798efc50c79f9` | unsure | 0.616 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `6cb610f65f7e475a8cf42f15b96057ac` | ai | 0.668 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `9fbd1de58d0645d88305be51478d0234` | unsure | 0.462 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `08f9008fbcbe4d59bafe1f10003e321f` | unsure | 0.451 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `a2581988fd714eea8c703dff49c80368` | human | 0.307 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `bb14fb3e2e8048579f241d59dfcc67ce` | unsure | 0.537 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `11cf283eac7e4e179fdafb2ec4187eee` | unsure | 0.463 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `76c92adcde6b490c9f10b50c770f477c` | unsure | 0.408 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `2d3fa1629a5142f68e6b0de517161391` | unsure | 0.546 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `ff97149647414aaaba9ac21a0e5028b0` | unsure | 0.425 |  |
| MF04 | malformed | text is only punctuation | 200 | `0eabb404c1c44c89ace4197f39f65fe9` | unsure | 0.602 |  |
| MF05 | malformed | text is a very long single word | 200 | `4f6770cf3c644d26bb5bf25a16c00f25` | unsure | 0.575 |  |
| MF06 | malformed | text is emoji only | 200 | `7fccc548f5da477aa7c50b889bb36bec` | ai | 0.882 |  |
| MF07 | malformed | text is right-to-left script | 200 | `2a6da0c33ea74729b6699c89712784c9` | ai | 0.855 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2cd40b862e514cd79eb1d08c580a8ca2` | unsure | 0.429 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `356a85b63a244c3782e279099ad4da80` | unsure | 0.429 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `80499e0e6d9644ba81a65e8d9ffcc4bc` | unsure | 0.429 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9dd41fb297234f5a92f3a0c9ebe74e3d` | unsure | 0.429 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `980c2d87cc174876abf4be1dfa55dc02` | unsure | 0.429 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "981acd3445bf4817aeb5c58233f995a2",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.4233,
  "model_score": 0.1635,
  "style_score": 0.5347,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "092f8ad28a1445e0a5e0522324435678",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.3956,
  "model_score": 0.5943,
  "style_score": 0.3104,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "701dc582d9e446c6bfafd2a7bfb2b1ec",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5044,
  "model_score": 0.6662,
  "style_score": 0.435,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "f3427fbe28a749b1a4b10988c29ee964",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5552,
  "model_score": 0.6114,
  "style_score": 0.5311,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "fcf700b3cad742b1856a00b9035eb152",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3254,
  "model_score": 0.3212,
  "style_score": 0.3272,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "f078bede4da148958f0e0ba79cc480d5",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.3778,
  "model_score": 0.5727,
  "style_score": 0.2942,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "7e9ccea42c2d4f228ff5bd8414089e45",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4025,
  "model_score": 0.5862,
  "style_score": 0.1845,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "d250afed571841338bf54b17568b7d6b",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4742,
  "model_score": 0.2452,
  "style_score": 0.5724,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "7576d9593d4b4399a47f3eb0f7df2afc",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.4987,
  "model_score": 0.7042,
  "style_score": 0.4107,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "0225be27883d40afb8fd679ce1153850",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8923,
  "model_score": 0.9792,
  "style_score": 0.855,
  "label": "This looks like it was likely generated by an AI tool. If you wrote it yourself, you can appeal this decision.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "321bd00e6701404db253a53fe4613846",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5576,
  "model_score": 0.6175,
  "style_score": 0.5319,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "7800600c987e4e59af3c7d4ac75cdef3",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6535,
  "model_score": 0.7387,
  "style_score": 0.617,
  "label": "This looks like it was likely generated by an AI tool. If you wrote it yourself, you can appeal this decision.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "c103b465945c48b79f92fb4b922296e7",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.6676,
  "model_score": 0.8051,
  "style_score": 0.6087,
  "label": "This looks like it was likely generated by an AI tool. If you wrote it yourself, you can appeal this decision.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "41c154e09c75438ba952874432139e14",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6081,
  "model_score": 0.8329,
  "style_score": 0.5118,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "cba3568d15fb420fb6fda6f7495b6e10",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.6977,
  "model_score": 0.8005,
  "style_score": 0.6537,
  "label": "This looks like it was likely generated by an AI tool. If you wrote it yourself, you can appeal this decision.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "6b2f68a5576249888af798efc50c79f9",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6162,
  "model_score": 0.8814,
  "style_score": 0.5026,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "6cb610f65f7e475a8cf42f15b96057ac",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.6676,
  "model_score": 0.8816,
  "style_score": 0.5759,
  "label": "This looks like it was likely generated by an AI tool. If you wrote it yourself, you can appeal this decision.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "9fbd1de58d0645d88305be51478d0234",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4623,
  "model_score": 0.3223,
  "style_score": 0.5223,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "08f9008fbcbe4d59bafe1f10003e321f",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4508,
  "model_score": 0.4625,
  "style_score": 0.4458,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "a2581988fd714eea8c703dff49c80368",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.3067,
  "model_score": 0.2044,
  "style_score": 0.3506,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "bb14fb3e2e8048579f241d59dfcc67ce",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5366,
  "model_score": 0.5943,
  "style_score": 0.5119,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "11cf283eac7e4e179fdafb2ec4187eee",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.463,
  "model_score": 0.4998,
  "style_score": 0.4473,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "76c92adcde6b490c9f10b50c770f477c",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4077,
  "model_score": 0.6401,
  "style_score": 0.1762,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "2d3fa1629a5142f68e6b0de517161391",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5456,
  "model_score": 0.5583,
  "style_score": 0.5402,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "ff97149647414aaaba9ac21a0e5028b0",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.425,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "0eabb404c1c44c89ace4197f39f65fe9",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.6017,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "4f6770cf3c644d26bb5bf25a16c00f25",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.5746,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "7fccc548f5da477aa7c50b889bb36bec",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.8824,
  "model_score": 0.9969,
  "style_score": 0.8333,
  "label": "This looks like it was likely generated by an AI tool. If you wrote it yourself, you can appeal this decision.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "2a6da0c33ea74729b6699c89712784c9",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.8552,
  "model_score": 0.9064,
  "style_score": 0.8333,
  "label": "This looks like it was likely generated by an AI tool. If you wrote it yourself, you can appeal this decision.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "2cd40b862e514cd79eb1d08c580a8ca2",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4293,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "356a85b63a244c3782e279099ad4da80",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4293,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "80499e0e6d9644ba81a65e8d9ffcc4bc",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4293,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "9dd41fb297234f5a92f3a0c9ebe74e3d",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4293,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "980c2d87cc174876abf4be1dfa55dc02",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4293,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We couldn't tell with confidence whether this was written by a person or generated by AI. This is not a judgment against you. If you wrote it yourself, you can appeal and a person will look at it.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
