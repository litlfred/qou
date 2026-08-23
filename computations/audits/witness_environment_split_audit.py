#!/usr/bin/env python3
"""No single container reproduces the corpus: the witnesses are built under at
least two mpmath versions (bean qou-58sa, follow-on).

## Why this exists

The convention-C excision's largest actionable class (B4/B4t of `qou-cds1`, 19
sites) is: migrate C->D, RE-RUN the producer, DIFF the witness, justify the
value change.  That method assumes the producer reproduces its committed
witness BEFORE the change -- otherwise the diff cannot attribute what moved.

Measured on the four unblocked (proton-anchored) B4 candidates, that assumption
does not hold, and the reason is not the convention:

    alpha_blend_tower.py           exit 0, but 17 witness fields move
    alpha_high_precision.py        exit 1 -- "no sign change in bracket",
                                   already broken on main, before any edit
    convergence_safe_vhat_tower.py exit 0, 1 field moves at the ~40th digit
    hecke_core_symbolic.py         (library; no witness of its own)

The 17 fields in the first are last-digit float repr differences, and the
witness names the cause itself: `engineVersion: mpmath 1.3.0`.  The container
had 1.4.1 at the time -- installed deliberately, because a DIFFERENT witness
(`qbeta-h-frame-rungs`) records `mpmath: 1.4.1` in its own `environment` block
and would not reproduce under 1.3.0.

So matching one witness's environment un-matches another's.

## What this script measures

The version split across every committed `computations/**/*.witness.json`, from
each witness's own `environment.mpmath` (falling back to `engineVersion`).  It
takes no view on which version is correct; it reports that the corpus does not
have one.

## Why it matters beyond this excision

Any workflow that re-runs a producer and diffs against the committed witness --
witness-staleness triage, the q0 re-pin sweep, the convention migration, the
`scriptHash` drain -- inherits this.  A diff computed in a container that
disagrees with the witness's recorded environment mixes a real change with a
version artifact, and the artifact is at the same magnitude as a genuine
last-digit move.

## Scope

Scope-(a).  This says the corpus is version-split and that the split defeats
before/after witness diffing in a single container.  It does NOT say any
particular witness is wrong, does not say which version should win, and does not
propose a mass regeneration -- regenerating 1000+ witnesses to unify the version
is exactly the kind of sweep AGENTS.md warns is not a work order.
"""
from __future__ import annotations

import collections
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]


def main() -> int:
    cnt = collections.Counter()
    total = 0
    for p in sorted((REPO / "computations").rglob("*.witness.json")):
        if "_deprecated" in str(p):
            continue
        try:
            d = json.load(open(p))
        except Exception:
            continue
        total += 1
        env = d.get("environment") or {}
        v = env.get("mpmath")
        if not v:
            ev = str(d.get("engineVersion") or "")
            if "mpmath" in ev:
                v = ev.split()[-1]
        cnt[v or "(none recorded)"] += 1

    print("mpmath version recorded by committed witnesses")
    print("=" * 58)
    for k, c in cnt.most_common():
        print(f"  {k:<20} {c:>6}")
    print("-" * 58)
    print(f"  {'TOTAL':<20} {total:>6}")

    named = {k: c for k, c in cnt.items()
             if k not in ("(none recorded)",) and k[0].isdigit()}
    distinct = len(named)
    print()
    print(f"distinct recorded versions: {distinct}")
    top = sorted(named.items(), key=lambda kv: -kv[1])[:2]
    if len(top) >= 2:
        print(f"the split: {top[0][0]} ({top[0][1]}) vs {top[1][0]} ({top[1][1]})")
    print()
    if distinct > 1:
        print("VERDICT: no single container reproduces the corpus. A before/after")
        print("witness diff is only attributable when the container matches THAT")
        print("witness's recorded environment -- which cannot hold for all of them")
        print("at once. Sequence any migration that relies on witness diffing")
        print("behind a decision about the version.")
        return 0
    print("VERDICT: the corpus records a single version; witness diffing is safe.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
