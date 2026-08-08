#!/usr/bin/env python3
"""lean_cone_triage.py — summarise a `lean-direct-cone.sh --all -k --report` run.

Turns the per-module TSV into the numbers a corpus survey actually needs:

* the **measured** red count (modules compiled with every dependency's olean
  present, which still failed) — a hard lower bound on genuine reds;
* the **blocked** count (never compiled, because an upstream module was red) —
  status genuinely *unknown*, so `error + blocked` is the upper bound;
* per-subtree breakdown and the distinct error shapes.

Usage: scripts/lean_cone_triage.py /tmp/qou-cone-all.tsv [--log-dir DIR]
"""

from __future__ import annotations

import argparse
import collections
import re
from pathlib import Path

# Normalise a lean error line into a coarse "shape" for grouping.
SHAPES: list[tuple[str, re.Pattern]] = [
    ("unknown-identifier", re.compile(r"unknown (identifier|constant|declaration)")),
    ("unknown-namespace-or-attr", re.compile(r"unknown (namespace|attribute|tactic)")),
    ("type-mismatch", re.compile(r"type mismatch|has type\b.*but is expected")),
    ("unsolved-goals", re.compile(r"unsolved goals")),
    ("tactic-failed", re.compile(r"tactic '(\w+)' failed|simp made no progress|linarith failed")),
    ("function-expected/app", re.compile(r"function expected|application type mismatch")),
    ("failed-to-synth-instance", re.compile(r"failed to synthesize")),
    ("elab-motive/universe", re.compile(r"motive is not type correct|universe|maximum recursion")),
    ("deterministic-timeout", re.compile(r"deterministic timeout|(?i)timeout")),
    ("missing-olean", re.compile(r"object file .* does not exist")),
    ("syntax-error", re.compile(r"unexpected token|expected .* term|unterminated")),
    ("sorry", re.compile(r"declaration uses 'sorry'")),
]


def shape_of(text: str) -> str:
    for name, rx in SHAPES:
        if rx.search(text):
            return name
    return "other"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("tsv")
    ap.add_argument("--log-dir", default="/tmp/lean-cone-logs")
    ap.add_argument("--top", type=int, default=15)
    args = ap.parse_args()

    rows = []
    with open(args.tsv, encoding="utf-8") as fh:
        next(fh)
        for line in fh:
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 5:
                rows.append(dict(zip(
                    ("module", "status", "seconds", "blocker", "error_head"), parts)))

    counts = collections.Counter(r["status"] for r in rows)
    total = len(rows)
    ok = counts["ok"] + counts["up-to-date"]
    err = counts["error"]
    blocked = counts["blocked"]
    missing = counts["missing-source"]

    print(f"total modules            : {total}")
    print(f"GREEN (compiled clean)   : {ok}")
    print(f"RED, measured directly   : {err}   <- lower bound on genuine reds")
    print(f"dangling-import defects  : {missing}")
    print(f"BLOCKED (never compiled) : {blocked}   <- status unknown")
    print(f"upper bound on non-green : {err + missing + blocked}")
    print()

    # blocked modules attributed to their ultimate upstream culprit
    by_blocker = collections.Counter(r["blocker"] for r in rows if r["status"] == "blocked")
    if by_blocker:
        print(f"blocked attributed to {len(by_blocker)} distinct root culprits; top:")
        for b, n in by_blocker.most_common(args.top):
            print(f"  {n:5d}  {b}")
        print()

    bad = [r for r in rows if r["status"] in ("error", "missing-source")]

    def subtree(m: str) -> str:
        p = m.split(".")
        return ".".join(p[:2]) if len(p) > 1 else m

    print("genuine reds by subtree:")
    for s, n in collections.Counter(subtree(r["module"]) for r in bad).most_common():
        print(f"  {n:5d}  {s}")
    print()

    logdir = Path(args.log_dir)
    shapes = collections.Counter()
    for r in bad:
        lp = logdir / (r["module"] + ".log")
        text = lp.read_text(encoding="utf-8", errors="replace") if lp.is_file() else r["error_head"]
        r["shape"] = shape_of(text)
        shapes[r["shape"]] += 1
    print("genuine reds by error shape:")
    for s, n in shapes.most_common():
        print(f"  {n:5d}  {s}")
    print()

    print("every genuine red (module | shape | first error line):")
    for r in sorted(bad, key=lambda r: (r.get("shape", ""), r["module"])):
        print(f"  [{r.get('shape','?')}] {r['module']}\n        {r['error_head'][:180]}")


if __name__ == "__main__":
    main()
