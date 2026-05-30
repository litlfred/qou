#!/usr/bin/env python3
# polynomial_q_not_applicable: validator, not a q-series compute.
"""Detect witnesses stale with respect to the substrate constant q₀.

**Why this exists.** `run_pipeline.py`'s staleness check keys on the
PRODUCER SCRIPT's `scriptHash` — so it is **blind to changes in imported
constants** like q₀. The 2026-05-28 q₀ re-pin (muon-anchor `m_μ/m_e` →
proton-anchor `m_p/m_e`, commit `01c18125`) shifted q₀ ~1.3e-8 *without
touching any producer script*, leaving ~394 witnesses carrying the
pre-re-pin q₀ that `run_pipeline.py` happily reports as "fresh". See
`docs/audits/2026-05-30-q0-repin-stale-witness-audit.md`.

This detector compares each witness's recorded q₀-shaped value(s) against
the *current* q₀ and flags mismatches — the detection half of the systemic
fix. Wire it into the witness-pipeline so any future constant re-pin
auto-flags the affected witnesses (which the `scriptHash` gate cannot).

    python3 witness_constant_staleness.py            # report
    python3 witness_constant_staleness.py --strict   # exit 1 if any stale
    python3 witness_constant_staleness.py --list      # full list (for regen)
"""
from __future__ import annotations

import argparse
import glob
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
for p in (str(HERE), str(HERE.parent.parent / "tools" / "qou-substrate" / "python")):
    if p not in sys.path:
        sys.path.insert(0, p)

from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402  current q₀

# q₀-shaped decimals near the substrate value (1.10997858… / 1.10997859…).
Q0_SHAPE = re.compile(r"\b1\.10997[0-9]{8,}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any q₀-stale witness is found")
    ap.add_argument("--ndigits", type=int, default=12,
                    help="significant digits of q₀ to compare (default 12)")
    ap.add_argument("--list", action="store_true",
                    help="print every stale witness (for driving the regen)")
    args = ap.parse_args()

    cur = Q_50_DIGIT_STR[: args.ndigits + 2]  # "1." + ndigits sig
    stale: list[tuple[str, list[str]]] = []
    total = 0
    for wf in sorted(glob.glob(str(HERE / "*.witness.json"))):
        total += 1
        raw = Path(wf).read_text()
        vals = {m.group(0)[: args.ndigits + 2] for m in Q0_SHAPE.finditer(raw)}
        bad = sorted(v for v in vals if v != cur)
        if bad:
            stale.append((Path(wf).name, bad))

    print(f"current q₀ (≈{args.ndigits} sig): {cur}")
    print(f"scanned {total} witnesses; q₀-stale: {len(stale)}")
    show = stale if args.list else stale[:20]
    for name, bad in show:
        print(f"  {name}: {bad}")
    if not args.list and len(stale) > 20:
        print(f"  … +{len(stale) - 20} more (use --list)")

    if args.strict and stale:
        print(f"\nSTRICT FAIL: {len(stale)} witnesses carry a stale q₀ "
              f"(re-pin regeneration incomplete).")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
