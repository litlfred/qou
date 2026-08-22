#!/usr/bin/env python3
"""Partition the muon-valued q₀ population in computations/.

Why this exists
---------------
`qou-1c4y` has twice carried a headline count of "muon witnesses" that was
produced by grepping a *prefix* of the muon pin.  A 12-digit prefix does not
identify the muon pin: the corpus carries **two** muon values that agree to
11 digits and diverge at the 12th —

    current     1.10997859555733471989...   (live ideal / CAL-2 pin)
    superseded  1.10997859555418057528...   (the "old muon value")

so a prefix grep silently sums two populations with different defects and
different fixes.  This script keeps the split honest and re-runnable.

It is pure string/JSON inspection — no arithmetic — so the NO-FLOAT64
discipline is satisfied vacuously.

Usage
-----
    python3 computations/audits/q0_muon_population_partition.py
    python3 computations/audits/q0_muon_population_partition.py --list-contradictions
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from collections import Counter

COMP = pathlib.Path(__file__).resolve().parent.parent

# The two muon values, to enough digits to separate them (they share 11).
MUON_CURRENT = "1.109978595557334"
MUON_OLD = "1.109978595554180"
# Loose prefix: matches BOTH, and nothing proton (proton is 1.10997858275...).
MUON_LOOSE = "1.1099785955"

PIN_WITNESS = "q-pinning-50-digit"
ROUTES_ANCHOR = re.compile(
    r"(import\s+q_parameter|from\s+q_parameter"
    r"|qou_substrate.*constants|\bq_at\(|Q_50_DIGIT_STR)"
)
READS_JSON = re.compile(r"(json\.load|read_text|open\()")


def witness_populations() -> dict:
    """Split every witness carrying a muon-family value by WHICH muon value."""
    tally = Counter()
    stamp_by_value = Counter()
    for path in sorted(COMP.rglob("*.witness.json")):
        text = path.read_text(errors="replace")
        if MUON_LOOSE not in text:
            continue
        cur, old = MUON_CURRENT in text, MUON_OLD in text
        kind = "both" if (cur and old) else ("current" if cur else ("old" if old else "rounded"))
        tally[kind] += 1
        try:
            anchor = json.loads(text).get("q0Anchor")
        except Exception:
            anchor = None
        stamp_by_value[(anchor, kind)] += 1
    return {"tally": tally, "stamp_by_value": stamp_by_value}


def direct_pinners() -> list[tuple[str, str]]:
    """Producers that bind q₀ straight out of the muon-anchored pin witness.

    A producer here never imports the anchor-resolving module, so it inherits
    whatever anchor that witness carries rather than choosing one.  Returns
    (relative path, manifest bucket).
    """
    manifest = json.loads((COMP / "q0_anchor_manifest.json").read_text())
    bucket = {
        stem: name
        for name in ("ideal_muon", "physical_proton", "ambiguous")
        for stem in manifest.get(name, [])
    }
    out = []
    for path in sorted(COMP.rglob("*.py")):
        if "_deprecated" in path.parts:
            continue
        text = path.read_text(errors="replace")
        if PIN_WITNESS not in text or not READS_JSON.search(text):
            continue
        if ROUTES_ANCHOR.search(text):
            continue  # resolves its anchor properly
        if not (re.search(r'derived_50_digit"\]', text) and re.search(r'\[\s*"q"\s*\]', text)):
            continue  # reads the file, but not as its pin
        rel = str(path.relative_to(COMP))
        out.append((rel, bucket.get(path.stem, "UNDECLARED")))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list-contradictions", action="store_true",
                    help="list only the producers declared proton that pin muon")
    args = ap.parse_args()

    pins = direct_pinners()
    contradictions = [r for r, b in pins if b == "physical_proton"]

    if args.list_contradictions:
        for rel in contradictions:
            print(rel)
        return 1 if contradictions else 0

    pops = witness_populations()
    tally = pops["tally"]
    print("witness populations carrying a muon-family q₀ value")
    print(f"  current  {MUON_CURRENT}…  {tally['current']}")
    print(f"  OLD      {MUON_OLD}…  {tally['old']}   <- superseded pin, stale on its own terms")
    print(f"  both (cross-anchor comparison)          {tally['both']}")
    print(f"  rounded / low-precision                 {tally['rounded']}")
    print(f"  TOTAL matching the loose prefix         {sum(tally.values())}")
    print()
    print("  NOTE: a grep for the 12-digit prefix sums the first two rows and")
    print("        reports one number.  They are different defects.")
    print()
    print(f"producers binding q₀ direct from {PIN_WITNESS}.witness.json")
    print("  (no anchor resolution — inherits whatever that witness carries)")
    by_bucket = Counter(b for _, b in pins)
    for name, count in by_bucket.most_common():
        print(f"  {count:4d}  declared {name}")
    print()
    if contradictions:
        print(f"CONTRADICTION — declared physical_proton, pins muon: {len(contradictions)}")
        for rel in contradictions:
            print(f"    {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
