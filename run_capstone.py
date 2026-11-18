#!/usr/bin/env python3
"""
Capstone trials: the five criteria in criteria.md, three trials each.

    python run_capstone.py --label before

Each trial:
  1. Submit capstone-sub-01..10 (the ten human samples; sub-01 has
     leading and trailing spaces so the whitespace rule is exercised).
     content_ids for sub-01..05 become capstone-content-01..05.
     Retrieve each with GET /content/<id> and compare to the submit response.
  2. GET /content/missing-content-01..05 -> expect 404 with an error field.
  3. For creator capstone-sub-01..10, take the most recent decision entry
     and check duration_ms is numeric and >= 0.
  4. For the same entries, check text_length == len(text.strip()).
  5. Send bad-input-01..03 and check 400 plus a rejection entry with the
     expected reason (the most recent rejection for that creator).
Writes results/capstone_run_<date>_<label>.md. Does not decide verdicts.
"""

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent))
import config  # noqa: E402
import scenarios  # noqa: E402

BASE = f"http://{config.HOST}:{config.PORT}"
TEXTS = list(scenarios.HUMAN[:10])
TEXTS[0] = "   " + TEXTS[0] + "   "          # whitespace case for criterion 4


def latest_entry(creator, predicate):
    entries = [json.loads(l) for l in config.AUDIT_LOG.read_text(encoding="utf-8").splitlines() if l.strip()]
    matches = [e for e in entries if e.get("creator_id") == creator and predicate(e)]
    return matches[-1] if matches else None


def run_trial():
    out = {}
    # submit ten
    subs = []
    for i, text in enumerate(TEXTS, 1):
        creator = f"capstone-sub-{i:02d}"
        r = requests.post(f"{BASE}/submit", json={"text": text, "creator_id": creator}, timeout=120)
        subs.append({"creator": creator, "status": r.status_code, "body": r.json() if r.content else {}, "text": text})

    # criterion 1
    c1 = []
    for i, s in enumerate(subs[:5], 1):
        cid = s["body"].get("content_id")
        g = requests.get(f"{BASE}/content/{cid}", timeout=30)
        b = g.json() if g.content else {}
        keys = ["guess", "label", "model_score", "style_score", "confidence"]
        match = all(b.get(k) == s["body"].get(k) for k in keys) and b.get("status") == "decided" and b.get("appealed") is False
        c1.append({"id": f"capstone-content-{i:02d}", "content_id": cid, "http": g.status_code, "passed": g.status_code == 200 and match, "retrieved": b})
    out["c1"] = c1

    # criterion 2
    c2 = []
    for i in range(1, 6):
        mid = f"missing-content-{i:02d}"
        g = requests.get(f"{BASE}/content/{mid}", timeout=30)
        body = g.json() if g.content else {}
        c2.append({"id": mid, "http": g.status_code, "passed": g.status_code == 404 and "error" in body})
    out["c2"] = c2

    # criterion 3 and 4
    c3, c4 = [], []
    for s in subs:
        e = latest_entry(s["creator"], lambda e: bool(e.get("guess")))
        d = e.get("duration_ms") if e else None
        c3.append({"creator": s["creator"], "duration_ms": d,
                   "passed": e is not None and isinstance(d, (int, float)) and not isinstance(d, bool) and d >= 0})
        tl = e.get("text_length") if e else None
        c4.append({"creator": s["creator"], "text_length": tl, "expected": len(s["text"].strip()),
                   "passed": e is not None and tl == len(s["text"].strip())})
    out["c3"] = c3
    out["c4"] = c4

    # criterion 5
    bad = [
        ("bad-input-01", {"text": "", "creator_id": "bad-input-01"}, "text_too_short"),
        ("bad-input-02", {"creator_id": "bad-input-02"}, "text_not_string"),
        ("bad-input-03", {"text": "x" * 10001, "creator_id": "bad-input-03"}, "text_too_long"),
    ]
    c5 = []
    for name, body, reason in bad:
        r = requests.post(f"{BASE}/submit", json=body, timeout=60)
        e = latest_entry(name, lambda e: e.get("event") == "rejected")
        c5.append({"id": name, "http": r.status_code, "logged_reason": e.get("reason") if e else None,
                   "expected_reason": reason,
                   "passed": r.status_code == 400 and e is not None and e.get("reason") == reason})
    out["c5"] = c5

    # criterion 4, additional: whitespace-only submission
    r = requests.post(f"{BASE}/submit", json={"text": "   \n\t  ", "creator_id": "capstone-whitespace-01"}, timeout=60)
    e = latest_entry("capstone-whitespace-01", lambda e: e.get("event") == "rejected")
    out["c4b"] = [{"id": "capstone-whitespace-01", "http": r.status_code,
                   "text_length": e.get("text_length") if e else None,
                   "passed": r.status_code == 400 and e is not None and e.get("text_length") == 0}]
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    args = parser.parse_args()

    trials = []
    for t in range(1, args.trials + 1):
        res = run_trial()
        trials.append(res)
        summary = {
            "criterion 1": f"{sum(x['passed'] for x in res['c1'])}/5",
            "criterion 2": f"{sum(x['passed'] for x in res['c2'])}/5",
            "criterion 3": f"{sum(x['passed'] for x in res['c3'])}/10",
            "criterion 4": f"{sum(x['passed'] for x in res['c4'])}/10",
            "criterion 5": f"{sum(x['passed'] for x in res['c5'])}/3",
            "criterion 4 (whitespace)": f"{sum(x['passed'] for x in res['c4b'])}/1",
        }
        print(f"trial {t}: " + ", ".join(f"{k} {v}" for k, v in summary.items()))

    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"capstone_run_{stamp}{label}.md"
    lines = [f"# Capstone run — {args.label or 'unlabeled'}", "",
             "- Produced by: `run_capstone.py`", "- Service: `app.py::get_content`, `app.py::submit`, `app.py::appeal`", ""]
    for n, res in enumerate(trials, 1):
        lines += [f"**Trial {n}**", "", "```json", json.dumps(res, indent=2, default=str), "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
