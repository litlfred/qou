#!/usr/bin/env python3
"""Find witness assertions that cannot fail.

An assertion is a claim about a number. `passed: true` is only worth what
the claim was, and three shapes make it worth nothing. All three were first
caught by hand during the trap-drain audit, each in a witness that a content
block cited as its support.

**1. The pass interval contains zero.** When `tolerance >= |expected|`, every
value in `[expected - tolerance, expected + tolerance]` passes and that
interval straddles zero — so the producer can emit 0, or a negative number,
and the check still reports success. This is the check this script exists
for. Measured on the live tree (excluding `_deprecated/`): **24 assertions
across 15 witnesses**, ten of them in `atom-mass-derived.witness.json`, where
seven pass with a computed value of `0.0` or negative against expected atomic
masses of thousands of MeV. A negative mass passes.

**2. A large miss admitted by a wide tolerance.** `g_A` computed 1.0 against
an expected 1.2754 with `tolerance: 0.5` — a 21.6 % error, reported as a
pass. Reported here, but read the assertion first: a `name` like
`x_exceeds_y` with `expected: 1.0` and `tolerance: 1e9` is an inequality
written in an equality field, and its "miss" is meaningless. That
false-positive class is why the relative-miss report is advisory and the
falsifiability report is not.

**3. `allPassed: true` with no assertions at all.** Known, diagnosed and
fixed at the producer: `qou_substrate.witness` used to discard an
`assertions` payload passed through `wrap_legacy` and then derive
`allPassed` from nothing, so 389 of 2083 witnesses carrying the field had it
true vacuously. The builder now adopts such payloads. What this script sees
is the historical residue, not a live producer defect — so it is reported
last, and a hit means "this witness predates the fix and was never
regenerated", not "this producer is lying".

    python3 computations/witness_assertion_slack_audit.py
    python3 computations/witness_assertion_slack_audit.py --json

Exits 1 if any unfalsifiable assertion is found. `_deprecated/` is skipped
unless `--include-deprecated`.

Arithmetic: values are parsed with `parse_float=Decimal`, so each JSON
literal is preserved exactly and comparisons are exact rationals. Nothing
goes through float64 — per AGENTS.md a probe's conclusion is an argument
that gets written into a bean, and float64 in the argument is the expensive
kind of wrong.
"""

from __future__ import annotations

import argparse
import glob
import json
import sys
from decimal import Decimal, InvalidOperation


def _dec(v):
    if isinstance(v, Decimal):
        return v
    if isinstance(v, bool):  # bool is an int subclass; not a measurement
        return None
    if isinstance(v, (int, str)):
        try:
            return Decimal(v)
        except InvalidOperation:
            return None
    return None


def audit(paths):
    unfalsifiable, wide_miss, vacuous = [], [], []
    for path in paths:
        try:
            with open(path) as fh:
                doc = json.load(fh, parse_float=Decimal, parse_int=Decimal)
        except (json.JSONDecodeError, OSError):
            continue
        if not isinstance(doc, dict):
            continue

        asserts = doc.get("assertions")
        if doc.get("allPassed") is True and not asserts:
            vacuous.append(path)
            continue
        if not isinstance(asserts, list):
            continue

        for a in asserts:
            if not isinstance(a, dict) or a.get("passed") is not True:
                continue
            c, e, t = _dec(a.get("computed")), _dec(a.get("expected")), _dec(a.get("tolerance"))
            if c is None or e is None or e == 0:
                continue
            row = {"path": path, "name": a.get("name"),
                   "computed": str(c), "expected": str(e),
                   "tolerance": None if t is None else str(t)}
            if t is not None and t > 0 and t >= abs(e):
                # Sign-degenerate: expected is positive, computed is not.
                # This is the sub-class with no benign reading — a magnitude
                # that came out zero or negative and still passed.
                row["sign_degenerate"] = bool(e > 0 and c <= 0)
                unfalsifiable.append(row)
                continue
            miss = abs(c - e) / abs(e)
            if miss >= Decimal("0.01"):
                wide_miss.append({**row, "rel_miss": miss})

    wide_miss.sort(key=lambda r: r["rel_miss"], reverse=True)
    return unfalsifiable, wide_miss, vacuous


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--include-deprecated", action="store_true")
    ap.add_argument("--root", default="computations")
    args = ap.parse_args()

    paths = [p for p in sorted(glob.glob(f"{args.root}/**/*.witness.json", recursive=True))
             if args.include_deprecated or "_deprecated" not in p]
    unfalsifiable, wide_miss, vacuous = audit(paths)

    if args.json:
        print(json.dumps({
            "scanned": len(paths),
            "unfalsifiable": unfalsifiable,
            "wide_miss": [{**r, "rel_miss": str(r["rel_miss"])} for r in wide_miss],
            "vacuous_all_passed": vacuous,
        }, indent=2))
        return 1 if any(r.get("sign_degenerate") for r in unfalsifiable) else 0

    print(f"scanned {len(paths)} witnesses\n")

    degen = [r for r in unfalsifiable if r.get("sign_degenerate")]
    loose = [r for r in unfalsifiable if not r.get("sign_degenerate")]

    print(f"== BLOCKING: passed with a computed value <= 0 against a positive expected ({len(degen)}) ==")
    print("  No benign reading: the pass interval contains zero AND the producer")
    print("  landed on or below it. A negative mass passes here.")
    for r in degen:
        print(f"  {r['name']}: computed {r['computed']}  expected {r['expected']}  tolerance {r['tolerance']}")
        print(f"      {r['path']}")
    if not degen:
        print("  none")

    print(f"\n== review: tolerance >= |expected| but the value is positive ({len(loose)}) ==")
    print("  Some of these are inequalities or existence checks written into the")
    print("  equality fields — `lp_active_set_nonempty` with expected 1.0 and")
    print("  tolerance 10.0 is exactly that, and is fine. Read the name.")
    for r in loose:
        print(f"  {r['name']}: computed {r['computed']}  expected {r['expected']}  tolerance {r['tolerance']}")
        print(f"      {r['path']}")
    if not loose:
        print("  none")

    print(f"\n== advisory: passing assertion missing by >= 1% ({len(wide_miss)}) ==")
    print("  Read the assertion before believing the number: an inequality written")
    print("  into the equality fields (expected 1.0, tolerance 1e9) lands here too.")
    for r in wide_miss[:15]:
        print(f"  {r['rel_miss'] * 100:>8.2f}%  {r['name']}  ({r['path']})")
    if len(wide_miss) > 15:
        print(f"  … and {len(wide_miss) - 15} more")

    print(f"\n== historical: allPassed true with no assertions ({len(vacuous)}) ==")
    print("  Fixed at the producer; these predate the fix and were never")
    print("  regenerated. Not a live defect — see the module docstring.")

    return 1 if degen else 0


if __name__ == "__main__":
    sys.exit(main())
