#!/usr/bin/env python3
"""The float64 class PR #5910 deferred: `.assertions[].computed` / `.expected`.

#5910 drained `.assertions[].tolerance` -- 1232 fields -- and named what it was
deliberately leaving:

    ".assertions[].computed (84) and .assertions[].expected (27) in the
     small-file group. These are results, not thresholds -- the same argument
     does not apply and each needs its producer."

That figure is for the small-file group (witnesses with 1-4 raw fields).
Corpus-wide the class is an order of magnitude bigger, and this measures it so
the next agent starts from a scoped tranche rather than a grep.

WHY IT IS NOT ONE CLASS, and why a blanket stringify would be wrong. #5910's
whole argument for tolerance was that a threshold is DECLARED -- `1e-9` is a
number the author typed, nothing was measured to that precision. That argument
transfers to some of these and not others:

  * `computed`  is a MEASUREMENT almost by definition. A float() cast on an
    mpmath value here silently truncates a 50-dps result to binary64. Fixing it
    is a producer change (`fmt(x)`, not `float(x)`), and the value MOVES -- so
    it cannot be done by textual repair the way tolerance was.
  * `expected`  is mixed, exactly as tolerance was. `17.4`, `34.14`, `1.0` are
    author-typed targets; `0.9980774473848675` is a computed comparand. Only
    the first kind is a serialization question.

INTEGRAL VALUES ARE EXCUSED, not counted, matching the raw-float64 ratchet:
`0.0` and `1.0` are exact in binary64 and carry no lost precision. That
exclusion is most of the corpus occurrences, which is why a bare grep for
`computed=float(` (639 sites / 312 files) badly overstates the defect.

Worked instance, fixed in the q0-flip drain: `c_k_beta_decay_witness.py` wrote
`computed=float(max_ge_ratio_dev)` on a 50-dps residual. It was INVISIBLE while
the value happened to be exactly 0.0 -- integral, excused -- and became a
REGRESSED gate the moment a re-run produced a real residual, 9.96e-71. So the
integral majority is not safe by nature; it is safe by accident of its current
value.

Writes no witness. Read-only over committed artifacts.
"""
from __future__ import annotations

import argparse
import collections
import glob
import json
import os
import sys


def is_intlike(v) -> bool:
    try:
        return float(v) == int(float(v))
    except (ValueError, OverflowError):
        return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true", help="name every affected file")
    ap.add_argument("--field", choices=("computed", "expected", "both"), default="both")
    a = ap.parse_args()

    fields = ("computed", "expected") if a.field == "both" else (a.field,)
    counts = collections.Counter()
    per_file: dict[str, int] = collections.Counter()
    for p in glob.glob("computations/**/*.witness.json", recursive=True):
        if "_deprecated" in p:
            continue
        try:
            d = json.load(open(p))
        except Exception:
            counts["unparseable"] += 1
            continue
        if not isinstance(d, dict):
            continue
        for asrt in (d.get("assertions") or []):
            if not isinstance(asrt, dict):
                continue
            for k in fields:
                v = asrt.get(k)
                if isinstance(v, bool) or not isinstance(v, float):
                    continue
                if is_intlike(v):
                    counts[f"{k}: integral (excused, exact in binary64)"] += 1
                else:
                    counts[f"{k}: NON-integral (lost precision)"] += 1
                    per_file[p] += 1

    print("committed witnesses — .assertions[] value fields\n")
    for k in sorted(counts):
        print(f"  {k:<44} {counts[k]}")
    actionable = sum(v for k, v in counts.items() if "NON-integral" in k)
    print(f"\n  {'ACTIONABLE fields':<44} {actionable}")
    print(f"  {'files carrying at least one':<44} {len(per_file)}")

    if per_file:
        print("\n  worst offenders:")
        for p, n in per_file.most_common(10):
            print(f"    {n:>4}  {os.path.relpath(p)}")
    if a.list:
        print("\n  all affected files:")
        for p in sorted(per_file):
            print(f"    {per_file[p]:>4}  {os.path.relpath(p)}")

    print("\nREADING: this is NOT drainable the way tolerance was. A `computed`")
    print("field is a measurement, so the repair changes the VALUE (it recovers")
    print("digits the cast threw away) and must happen at the producer -- one at")
    print("a time, with the producer re-run. `expected` is mixed and its")
    print("author-typed half could follow #5910's serialization argument; its")
    print("computed half cannot. Nothing here is a candidate for a textual sweep.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
