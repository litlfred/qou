#!/usr/bin/env python3
# polynomial_q_not_applicable: value-preserving serialization repair.
"""Strip float64 padding from committed witnesses — provably value-preserving.

Owner directive: NO FLOAT64.

**What this does.** `witness_float64_padding_audit.py` finds strings that are
the *decimal expansion of a binary64*, e.g.

    "B_AME_MeV": "8.4817962000000015621026250300928950309753417968750000000000"

The datum is `8.4817962`; the remaining 40+ digits are binary-representation
artifact. This rewrites each such string to its shortest round-tripping form.

**Why this is not "hand-editing a witness".** The standing discipline —
never edit a witness value, re-run its producer — exists to stop anyone
*inventing* a number. That risk is absent here because the transformation is
**provably value-preserving**: the invariant

    float(new) == float(old)      exactly, bit for bit

is asserted for every single replacement, and any failure aborts the whole
file. Nothing is invented; digits that were never information are removed.
The stored value is bit-identical as a double — only the *claim about how
well it is known* changes, which is the entire defect.

**This does not replace the producer fix.** Stripping cleans existing data;
`mpf_float_source_audit.py` stops new padding being authored. Both are
needed and neither substitutes for the other — a producer that still promotes
a float to `mpf` will re-pad on its next run.

Dry-run by default. `--apply` writes. `--check` exits 1 if anything would
change (useful once the corpus is clean).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from mpmath import mp, mpf

mp.dps = 90

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
NUMSTR = re.compile(r"^-?\d+\.\d{20,}$")
MIN_SIG_FRAC = 17
F64_GAP = mpf("1e-30")

SELF_OUTPUTS = {
    "witness-float64-padding-audit.witness.json",
    "q0-value-drift-audit.witness.json",
    "no-free-parameter-certificate.witness.json",
    "mpf-float-source-audit.witness.json",
    # An audit that RECORDS offending literals must not have them rewritten.
    "hardcoded-literal-audit.witness.json",
}


def is_padded(s: str) -> bool:
    t = s.strip()
    if "." not in t:
        return False
    if len(t.split(".")[1].rstrip("0")) <= MIN_SIG_FRAC:
        return False
    try:
        x = mpf(t)
    except Exception:
        return False
    return x != 0 and abs(x - mpf(float(x))) / abs(x) < F64_GAP


def honest(s: str) -> str:
    """Shortest decimal that round-trips to the same double."""
    return repr(float(mpf(s.strip())))


def rewrite(obj, stats: dict):
    if isinstance(obj, dict):
        return {k: rewrite(v, stats) for k, v in obj.items()}
    if isinstance(obj, list):
        return [rewrite(v, stats) for v in obj]
    if isinstance(obj, str) and NUMSTR.match(obj.strip()) and is_padded(obj):
        new = honest(obj)
        # THE INVARIANT. Bit-identical as a double, or we do not touch it.
        if float(new) != float(obj.strip()):
            raise AssertionError(
                f"value-preserving invariant VIOLATED: {obj.strip()!r} -> {new!r}")
        stats["replaced"] += 1
        stats["examples"].append((obj.strip(), new))
        return new
    return obj


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    ap.add_argument("--check", action="store_true", help="exit 1 if anything would change")
    ap.add_argument("--include-deprecated", action="store_true",
                    help="also rewrite computations/_deprecated/ (default: skip — those "
                         "are historical records with no consumer, so rewriting them is "
                         "churn; the padding ratchet's baseline already absorbs them)")
    args = ap.parse_args()

    total = {"files": 0, "replaced": 0, "examples": []}
    changed_files = []

    for p in sorted(HERE.rglob("*.witness.json")):
        if p.name in SELF_OUTPUTS:
            continue
        if not args.include_deprecated and ("_deprecated" in p.parts or "fsh-guts" in p.parts):
            continue
        try:
            raw = p.read_text(encoding="utf-8")
            data = json.loads(raw)
        except Exception:
            continue
        stats = {"replaced": 0, "examples": []}
        try:
            new = rewrite(data, stats)
        except AssertionError as e:
            print(f"  ABORT {p.relative_to(ROOT)}: {e}", file=sys.stderr)
            return 2
        if stats["replaced"]:
            total["files"] += 1
            total["replaced"] += stats["replaced"]
            total["examples"].extend(stats["examples"][:2])
            changed_files.append((p, new, stats["replaced"]))

    print("=" * 74)
    print("STRIP FLOAT64 PADDING — " + ("APPLY" if args.apply else "DRY RUN"))
    print("=" * 74)
    print(f"  files with padding : {total['files']}")
    print(f"  strings to rewrite : {total['replaced']}")
    print("\n  sample rewrites (each verified float(new) == float(old)):")
    seen = set()
    for old, new in total["examples"]:
        if new in seen:
            continue
        seen.add(new)
        print(f"    {old[:56]}…")
        print(f"      -> {new}")
        if len(seen) >= 8:
            break

    if args.apply:
        for p, new, n in changed_files:
            p.write_text(json.dumps(new, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"\n  wrote {len(changed_files)} file(s)")
    else:
        print("\n  (dry run — pass --apply to write)")

    return 1 if (args.check and total["replaced"]) else 0


if __name__ == "__main__":
    sys.exit(main())
