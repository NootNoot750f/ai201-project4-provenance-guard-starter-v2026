#!/usr/bin/env python3
"""
Criterion 4 (the appeal path): 5 submissions, then 5 appeals, per trial.

    python run_appeals.py --label before

For each appeal, checks that the response is 200 with status under_review,
and that the audit log has an `event: appeal` entry for that content_id.
Writes results/appeals_<date>_<label>.md. Does not decide a verdict.
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

REASONING = "I wrote this myself. Please review it."


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=f"http://{config.HOST}:{config.PORT}")
    args = parser.parse_args()

    texts = scenarios.HUMAN[:5]
    report = []
    for trial in range(1, args.trials + 1):
        results = []
        for i, text in enumerate(texts, 1):
            creator = f"appeal_t{trial}_{i}"
            sub = requests.post(f"{args.url}/submit",
                                json={"text": text, "creator_id": creator}, timeout=90)
            cid = sub.json().get("content_id") if sub.status_code == 200 else None
            appeal = None
            if cid:
                appeal = requests.post(f"{args.url}/appeal",
                                       json={"content_id": cid, "reasoning": REASONING},
                                       timeout=30)
            log = requests.get(f"{args.url}/log?limit=1000", timeout=30).json()["entries"]
            logged = any(e.get("event") == "appeal" and e.get("content_id") == cid for e in log)
            ok = bool(appeal is not None and appeal.status_code == 200
                      and appeal.json().get("status") == "under_review" and logged)
            results.append({
                "submit_status": sub.status_code,
                "content_id": cid,
                "appeal_status": appeal.status_code if appeal is not None else None,
                "appeal_body_status": appeal.json().get("status") if appeal is not None else None,
                "logged_appeal": logged,
                "passed": ok,
            })
        passed = sum(r["passed"] for r in results)
        print(f"trial {trial}: {passed} of {len(results)} appeals updated status and were logged")
        report.append(results)

    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"appeals_{stamp}{label}.md"
    lines = [f"# Appeal trials{f' — {args.label}' if args.label else ''}", "",
             "- Produced by: `run_appeals.py`", "- Service: `app.py::appeal`, `audit.log_appeal`", ""]
    for n, results in enumerate(report, 1):
        lines += [f"**Trial {n}**", "", "```json", json.dumps(results, indent=2), "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
