#!/usr/bin/env python3
"""
Append a fresh agent QA verdict to a `<block>.qa.json` sidecar (latest-wins),
used by the proof-QA judgment/rater **re-audit** fleet (PR follow-up to #2775).

Each re-audit sub-agent reads a block's `.md` claim + resolved Lean and calls
this once per (criterion) to record its considered verdict, superseding the
`n/a "pending canonical re-sweep"` placeholder left by the #2775 invalidation.

Usage:
  python3 scripts/reaudit_verdict.py <qa_path> <criterion> <result> \
      --notes "<evidence-based one-liner>" [--score 0.85]

  result ∈ {pass, fail, warn, n/a}
  --score (0..1) only for proof-rater-* criteria.

Concurrency: re-audit batches are disjoint sets of files, so parallel agents
never write the same sidecar — safe without locking.
"""
from __future__ import annotations
import argparse, datetime, hashlib, json, os, subprocess, sys

VALID_RESULTS = {"pass", "fail", "warn", "n/a"}
VALID_CRITERIA = {
    "proof-statement-integrity", "proof-no-self-assuming-projection",
    "proof-no-unused-hypotheses", "proof-no-false-premise",
    "proof-rater-goal-plausibility", "proof-rater-strategy-clarity",
    "proof-rater-novelty",
}


def file_hash(path: str) -> str | None:
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def field_hash(qa: str) -> dict:
    base = qa[: -len(".qa.json")]
    out = {}
    for ext in ("md", "ts", "lean"):
        h = file_hash(f"{base}.{ext}")
        if h:
            out[ext] = h
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("qa")
    ap.add_argument("criterion")
    ap.add_argument("result")
    ap.add_argument("--notes", required=True)
    ap.add_argument("--score", type=float, default=None)
    args = ap.parse_args()

    if args.result not in VALID_RESULTS:
        print(f"bad result {args.result!r}; want one of {sorted(VALID_RESULTS)}", file=sys.stderr)
        return 2
    if args.criterion not in VALID_CRITERIA:
        print(f"bad criterion {args.criterion!r}; want one of {sorted(VALID_CRITERIA)}", file=sys.stderr)
        return 2
    if not os.path.exists(args.qa):
        print(f"no such sidecar: {args.qa}", file=sys.stderr)
        return 2

    head = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    today = now[:10]

    with open(args.qa, encoding="utf-8") as f:
        d = json.load(f)
    crit = d.setdefault("criteria", {})
    entry = {
        "field_hash": field_hash(args.qa),
        "result": args.result,
        "notes": args.notes,
        "reviewed_at": now,
        "reviewed_sha": head,
        "reviewer": {
            "kind": "agent",
            "id": "local/qa-agent-drain",
            "agent_skill": "local/qa-agent-drain",
            "agent_model": "claude-opus-4-8",
            "agent_date": today,
        },
    }
    if args.score is not None:
        entry["score"] = {"max": 1, "value": args.score}
    crit.setdefault(args.criterion, []).append(entry)

    with open(args.qa, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"{args.criterion} <- {args.result}"
          + (f" ({args.score})" if args.score is not None else "")
          + f"  [{os.path.basename(args.qa)}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
