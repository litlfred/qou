#!/usr/bin/env python3
"""Ghost-value sweep — committed 'passing' accuracy claims whose producer
has since changed (so the pass is unverified and may be stale numerology).

Generalises the hadron-knot-table de-fitting finding (a committed binding of
28.19 ≈ experiment that the current categorical path no longer produces —
0.72). A "ghost value" is a witness that:

  (a) declares `allPassed == true`,
  (b) carries an ACCURACY/PRECISION assertion — one comparing a predicted
      value to experiment/expected within a tolerance (the kind of claim
      whose truth depends on the exact compute), and
  (c) is SELF-STALE — its recorded `scriptHash` differs from the current
      hash of its producer file.

(a)+(b)+(c) means: the witness asserts a quantitative match that PASSED when
last generated, but the producer has changed since — so the pass is
unverified and may no longer hold (the hadron pattern). This does NOT prove
the value is wrong; it ranks where to look.

Read-only; no recompute (that is the expensive follow-up, per candidate).
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTE_ROOT = HERE.parent

# Assertion is "accuracy/precision" if its name/source mentions a match to
# experiment / a tolerance-bearing comparison.
ACCURACY_RX = re.compile(
    r"matches|within|ppb|ppm|ppt|ppq|codata|ame|_pred|residual|agree|"
    r"accuracy|sigma|100x|target|deviat|rel_?diff|close_to|equals",
    re.IGNORECASE,
)


def _producer_index(roots: list[Path]) -> dict[str, list[Path]]:
    idx: dict[str, list[Path]] = {}
    for root in roots:
        if not root.is_dir():
            continue
        for py in root.rglob("*.py"):
            if "_deprecated" in py.parts or ".lake" in py.parts:
                continue
            idx.setdefault(py.name, []).append(py)
    return idx


def _hash12(path: Path) -> str | None:
    if not path.exists():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def _resolve(cands: list[Path], wp: Path) -> Path:
    if len(cands) == 1:
        return cands[0]
    same = [c for c in cands if c.parent == wp.parent]
    pool = same or cands
    return min(pool, key=lambda c: (len(c.parts), str(c)))


def main() -> int:
    idx = _producer_index([COMPUTE_ROOT, COMPUTE_ROOT.parent / "tools"])
    ghosts = []
    n_passing_accuracy = n_checked = 0
    for wp in sorted(COMPUTE_ROOT.rglob("*.witness.json")):
        n_checked += 1
        try:
            w = json.loads(wp.read_text())
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(w, dict) or w.get("allPassed") is not True:
            continue
        asserts = w.get("assertions") or []
        acc = [a for a in asserts if isinstance(a, dict)
               and ACCURACY_RX.search(
                   f"{a.get('name','')} {a.get('source','')} {a.get('unit','')}")]
        if not acc:
            continue
        n_passing_accuracy += 1
        # self-staleness
        rec = w.get("scriptHash")
        sf = w.get("scriptFile")
        if not rec or not sf or sf not in idx:
            continue
        cur = _hash12(_resolve(idx[sf], wp))
        if cur is not None and cur != rec:
            ghosts.append({
                "witness": wp.name,
                "scriptFile": sf,
                "recorded": rec, "current": cur,
                "n_accuracy_assertions": len(acc),
                "sample_claim": acc[0].get("name"),
            })

    print(f"Ghost-value sweep: {n_checked} witnesses; "
          f"{n_passing_accuracy} allPassed+accuracy-claim; "
          f"{len(ghosts)} are SELF-STALE (ghost candidates).")
    print("\nGhost candidates (passing accuracy claim, producer changed since):")
    for g in sorted(ghosts, key=lambda x: -x["n_accuracy_assertions"]):
        print(f"  {g['witness']}  [{g['scriptFile']}]  "
              f"{g['recorded']}→{g['current']}  "
              f"({g['n_accuracy_assertions']} acc-claims; "
              f"e.g. {g['sample_claim']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
