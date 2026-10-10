#!/usr/bin/env python3
"""Report published decimals in `content/` that no file in the repo produces.

A DIAGNOSTIC, NOT A GATE
------------------------
The output is a **candidate list, not a defect list**, and it is wired into
nothing. Many entries are legitimate: experimental inputs (CODATA, AME), values
quoted from cited work, and closed forms a human evaluated. The first candidate
spot-checked, `0.00137748` in `flavor-split-habiro-derivation`, is
`Delta_target = (m_n - m_p)/((m_p + m_n)/2)` from CODATA masses -- correctly
published and not computed anywhere, exactly as it should be. Deciding any entry
needs a human reading its block. Ship no verdict from this file.

WHY IT EXISTS
-------------
`thm:markov-trace-factorization` published a transfer-matrix readout copied from
DEPRECATED code, wrong on every bond, while a merged probe already recorded that
readout as a trap (bean `qou-qnqf`, 2026-09-05). That prompted two questions.

  1. Does any published figure have DEPRECATED-only provenance? Measured: **no**.
     93 decimals live in `computations/_deprecated/` and nowhere live, and none
     of them reaches `content/`. That is a real negative -- the detector is
     selftested against an injected known positive, per bean `qou-5pgl`'s rule
     that a detector without one can report a whole class clean.

  2. Does any published figure have NO provenance at all? 36 of 333, once
     rounding is allowed for. Those are the candidates below.

ROUNDING IS THE WHOLE DIFFICULTY. Exact string matching reports 132, and most of
those are false: `0.00155060213`, `0.00155060` and `0.0015506` are three
roundings of one quantity published at three precisions. A figure counts as
sourced here if some source value rounds to it at the published number of
decimals.

    python3 scripts/unsourced-published-figures.py            # report
    python3 scripts/unsourced-published-figures.py --selftest # detector only
"""
from __future__ import annotations

import argparse
import bisect
import pathlib
import re
import sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUB = re.compile(r"\d+\.\d{7,}")     # published figures worth tracing
SRC = re.compile(r"\d+\.\d{3,}")     # sources may carry fewer digits
SRC_GLOBS = ("computations/**/*.py", "computations/**/*.json", "qou-mass/**/*",
             "tools/**/*.py", "folio/**/lean/**/*.lean", "docs/**/*.md")
PUB_GLOBS = ("content/**/*.md", "content/**/*.ts")


def _scan(paths, rx):
    out: dict[str, set[str]] = defaultdict(set)
    for p in paths:
        if not p.is_file():
            continue
        try:
            t = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for m in rx.findall(t):
            out[m].add(str(p.relative_to(ROOT)))
    return out


def _sourced(c: str, vals: list[float]) -> bool:
    """True if some source value rounds to `c` at `c`'s decimal count."""
    k = len(c.split(".")[1])
    tol = 0.5 * 10 ** (-k) * 1.000001
    x = float(c)
    i = bisect.bisect_left(vals, x - tol)
    return i < len(vals) and vals[i] <= x + tol


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    src = _scan([p for g in SRC_GLOBS for p in ROOT.glob(g)], SRC)
    vals = sorted({float(x) for x in src})

    # Selftest, always. A fabricated figure must be unsourced and a real source
    # value must be sourced; without both, "0 unsourced" would mean nothing.
    fabricated = "0.12345678901234"
    fails = []
    if _sourced(fabricated, vals):
        fails.append("a fabricated figure was reported SOURCED — the tolerance "
                     "is too wide and every result is meaningless")
    if vals and not _sourced(f"{vals[len(vals) // 2]:.9f}", vals):
        fails.append("a real source value was reported UNSOURCED — the matcher "
                     "is broken")
    dep = _scan(ROOT.glob("computations/_deprecated/**/*.py"), SRC)
    live = _scan([p for p in ROOT.glob("computations/**/*.py")
                  if ("_deprecated" not in str(p) and "fsh-guts" not in str(p))], SRC)
    dep_only = sorted(set(dep) - set(live))
    if not dep_only:
        fails.append("no deprecated-only values found, so the deprecated-"
                     "provenance question cannot be answered either way")
    if fails:
        for f in fails:
            print(f"unsourced-published-figures SELFTEST FAILED: {f}",
                  file=sys.stderr)
        return 2
    print(f"selftest ok — {len(vals)} source values, {len(dep_only)} of them "
          f"deprecated-only")
    if args.selftest:
        return 0

    pub = _scan([p for g in PUB_GLOBS for p in ROOT.glob(g)], PUB)
    dep_pub = sorted(c for c in pub if c in dep and c not in live)
    print(f"\npublished figures with DEPRECATED-only provenance: {len(dep_pub)}")
    for c in dep_pub:
        print(f"    {c}   {sorted(pub[c])[0]}")

    orphan = sorted(c for c in pub if not _sourced(c, vals))
    print(f"\npublished figures ({len(pub)} total) with NO source anywhere: "
          f"{len(orphan)}")
    print("CANDIDATES ONLY — experimental inputs and quoted values belong here "
          "legitimately.")
    for c in orphan:
        print(f"    {c:<32} {sorted(pub[c])[0]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
