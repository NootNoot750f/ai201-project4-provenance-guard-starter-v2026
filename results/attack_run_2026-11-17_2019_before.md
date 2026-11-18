# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-17 20:19
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `7a9925a995904b30998da604af33251e` | human | 0.349 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `84f46405e154440a9b1a28d8cdf3e269` | unsure | 0.452 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `d871bf4734654842969f9304769bbb03` | unsure | 0.551 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `afea8c1d00514c0e8855db269fe88e61` | unsure | 0.571 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `e443eaf0c46045028f84baed7506aed3` | human | 0.324 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `2c6f7710f6df4c3eaa393825e13b48b5` | unsure | 0.433 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `0ae2e7bdc9b445aa922b81e084f2709d` | unsure | 0.443 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `a10b9b3bd78844a6b6e77f6d3a0fa31a` | unsure | 0.409 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `4bd6630d887147edb5a23892c8361ba0` | unsure | 0.557 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `59502650a754465da7631101df0c0015` | ai | 0.917 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `65e7234c533a4ac3baea7304b47aab15` | unsure | 0.575 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `b04a6d2ac9b64c96bbbf2ab78573f105` | ai | 0.678 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `7dc50e4df7ee45a09e8f31c643db5dec` | ai | 0.707 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `6a9d44b9d5464c74b953f75443c43fe6` | ai | 0.672 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `d7da8f5b42774f5c9b9931aa8e34dac6` | ai | 0.727 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `7848611cbbeb4c23b5f1621993049a47` | ai | 0.692 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `5b95ded2efc24d1ba261880e19535c98` | ai | 0.729 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `9aff057d12c14bdea82c8b265112e998` | unsure | 0.422 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `da279df2d7fa43a09f81b53a89196bce` | unsure | 0.454 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `8cd5f5d1224548aeacb2a936e46ad2f8` | human | 0.278 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `fb284de031a64586999ef82dc88ab08e` | unsure | 0.553 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `ec07154029ae4a51ab2d8f07e3463934` | unsure | 0.474 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `1da593ac5b8b4212bd3a2f757f026d1c` | unsure | 0.454 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `d114493df5d641a2ac29feebcc9cd156` | unsure | 0.549 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `37d0272f5a30475e856ddf941189434b` | unsure | 0.375 |  |
| MF04 | malformed | text is only punctuation | 200 | `692753d86e1b46bc9171da70c408214c` | unsure | 0.503 |  |
| MF05 | malformed | text is a very long single word | 200 | `98494959c94d4a7bb185f2fdba62f4c1` | unsure | 0.624 |  |
| MF06 | malformed | text is emoji only | 200 | `8a0d4e81db1242359a7749076add93c2` | ai | 0.915 |  |
| MF07 | malformed | text is right-to-left script | 200 | `cb271d63e3104a749d68bf3c349ac70c` | ai | 0.870 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `688f3bf7ce5b4b77aed5626341d94b3d` | unsure | 0.382 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `aac9d9be67b3484bb7a8e7cf2b75f361` | unsure | 0.382 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d209bfb529ba42c497e7163600d1d39a` | unsure | 0.382 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `edfd07499dac4b74b88deda461f65fe9` | unsure | 0.382 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `dbf6e76b8ce2416bb32b3964cd868e59` | unsure | 0.382 |  |
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
  "content_id": "7a9925a995904b30998da604af33251e",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3491,
  "model_score": 0.1635,
  "style_score": 0.5347,
  "label": "We think this was probably written by a person.",
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
  "content_id": "84f46405e154440a9b1a28d8cdf3e269",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4524,
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
  "content_id": "d871bf4734654842969f9304769bbb03",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5506,
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
  "content_id": "afea8c1d00514c0e8855db269fe88e61",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5713,
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
  "content_id": "e443eaf0c46045028f84baed7506aed3",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3242,
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
  "content_id": "2c6f7710f6df4c3eaa393825e13b48b5",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4335,
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
  "content_id": "0ae2e7bdc9b445aa922b81e084f2709d",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4427,
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
  "content_id": "a10b9b3bd78844a6b6e77f6d3a0fa31a",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4088,
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
  "content_id": "4bd6630d887147edb5a23892c8361ba0",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5575,
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
  "content_id": "59502650a754465da7631101df0c0015",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.9171,
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
  "content_id": "65e7234c533a4ac3baea7304b47aab15",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5747,
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
  "content_id": "b04a6d2ac9b64c96bbbf2ab78573f105",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6779,
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
  "content_id": "7dc50e4df7ee45a09e8f31c643db5dec",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7069,
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
  "content_id": "6a9d44b9d5464c74b953f75443c43fe6",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.6724,
  "model_score": 0.8329,
  "style_score": 0.5118,
  "label": "This looks like it was likely generated by an AI tool. If you wrote it yourself, you can appeal this decision.",
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
  "content_id": "d7da8f5b42774f5c9b9931aa8e34dac6",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7271,
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
  "content_id": "7848611cbbeb4c23b5f1621993049a47",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.692,
  "model_score": 0.8814,
  "style_score": 0.5026,
  "label": "This looks like it was likely generated by an AI tool. If you wrote it yourself, you can appeal this decision.",
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
  "content_id": "5b95ded2efc24d1ba261880e19535c98",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.7288,
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
  "content_id": "9aff057d12c14bdea82c8b265112e998",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4223,
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
  "content_id": "da279df2d7fa43a09f81b53a89196bce",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4541,
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
  "content_id": "8cd5f5d1224548aeacb2a936e46ad2f8",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2775,
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
  "content_id": "fb284de031a64586999ef82dc88ab08e",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5531,
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
  "content_id": "ec07154029ae4a51ab2d8f07e3463934",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4736,
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
  "content_id": "1da593ac5b8b4212bd3a2f757f026d1c",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4541,
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
  "content_id": "d114493df5d641a2ac29feebcc9cd156",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5493,
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
  "content_id": "37d0272f5a30475e856ddf941189434b",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.375,
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
  "content_id": "692753d86e1b46bc9171da70c408214c",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.5028,
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
  "content_id": "98494959c94d4a7bb185f2fdba62f4c1",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.6244,
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
  "content_id": "8a0d4e81db1242359a7749076add93c2",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9151,
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
  "content_id": "cb271d63e3104a749d68bf3c349ac70c",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.8699,
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
  "content_id": "688f3bf7ce5b4b77aed5626341d94b3d",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3822,
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
  "content_id": "aac9d9be67b3484bb7a8e7cf2b75f361",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3822,
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
  "content_id": "d209bfb529ba42c497e7163600d1d39a",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3822,
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
  "content_id": "edfd07499dac4b74b88deda461f65fe9",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3822,
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
  "content_id": "dbf6e76b8ce2416bb32b3964cd868e59",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.3822,
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
