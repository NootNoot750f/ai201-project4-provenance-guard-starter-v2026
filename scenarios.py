"""
What your test runs. <- UNIT 8, MILESTONE 3

run_eval.py runs every scenario here three times. Texts come from the sample
files so the sets are fixed:
  tests/human_samples.txt   10 pieces I wrote (criterion 1)
  tests/ai_samples.txt      10 AI-generated pieces (criterion 2)

Criterion 2 is run on human + AI together (first 10 human, last 10 AI); the
score-spread average and the label counts are both read from that one run.
Criterion 4 (the appeal path) is NOT in this file: run_eval.py only sends
submissions, so the appeal trials are a separate step (see README).
"""

from pathlib import Path

ROOT = Path(__file__).parent


def load_samples(path):
    """Return the text of each '## ' block, in order. Blank lines are dropped."""
    texts, current = [], None
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            if current is not None:
                texts.append(" ".join(current))
            current = []
        elif current is not None and line.strip():
            current.append(line.strip())
    if current is not None:
        texts.append(" ".join(current))
    return texts


HUMAN = load_samples(ROOT / "tests" / "human_samples.txt")
AI = load_samples(ROOT / "tests" / "ai_samples.txt")

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": HUMAN,
    },
    {
        "name": "human and AI pool",
        "criterion": 2,
        "texts": HUMAN + AI,
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},
            {"text": "word " * 2100, "creator_id": "eval_bad_long"},
        ],
    },
]


def validate() -> list[str]:
    """Complain about anything malformed before a long run."""
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")
        texts = scenario.get("texts")
        bodies = scenario.get("bodies")
        if texts and bodies:
            problems.append(f"scenario {i} has both texts and bodies")
        elif bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(f"scenario {i}, body {j} is not a dict")
        elif not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
        else:
            for j, text in enumerate(texts, 1):
                if not str(text).strip():
                    problems.append(f"scenario {i}, text {j} is empty")
    return problems
