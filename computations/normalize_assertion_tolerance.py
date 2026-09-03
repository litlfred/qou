#!/usr/bin/env python3
# polynomial_q_not_applicable: value-preserving serialization repair.
"""Serialize DECLARED assertion tolerances as literals — provably value-preserving.

Owner directive: NO FLOAT64.

**What this does.** `witness_raw_float64_audit.py` counts 1296 raw float64
fields at `.assertions[].tolerance` across 506 committed witnesses. A tolerance
is not a measurement — `1e-9` is a threshold the author chose — so it should
never have entered the corpus as a binary64 in the first place. This rewrites
the DECLARED ones to the literal their author typed:

    "tolerance": 1e-09      ->   "tolerance": "1e-09"
    "tolerance": 0.5        ->   "tolerance": "0.5"

The rule is `qou_substrate.witness._tolerance_literal`, IMPORTED rather than
re-implemented, so what this writes is byte-for-byte what a re-run of the
producer now emits. A repair that disagrees with the producer would be undone
by the next run and would read as a regression when it was.

**Why this is not "hand-editing a witness".** The standing discipline — never
edit a witness value, re-run its producer — exists to stop anyone *inventing* a
number. That risk is absent here, for the same reason it is absent in
`strip_float64_padding.py`, whose argument this follows:

    float(new) == old       exactly, bit for bit

is asserted for every single replacement, and the whole file is re-parsed and
compared against the expected document before anything is written. Nothing is
invented, no verdict moves (`Assertion.passed` already coerces its tolerance
with `float()`), and the producers are not re-run — so no computed number can
move either.

**What it deliberately does NOT touch.**

* **Computed tolerances.** An error budget scaled off the expected value
  arrives as `1025.6028557082007`. That really did lose precision against
  whatever produced it, it is a genuine finding, and stringifying it would hide
  a defect behind a convention. `_tolerance_literal` refuses them and they stay
  counted. Measured: 64 of 1296.
* **Integral-valued tolerances** (`0.0`, `1.0`). Exact in binary64, already
  excused by the ratchet, and converting them would churn ~200 values for no
  gate benefit.
* **`tolerance` keys outside `assertions[]`.** Those are not the assertion
  schema's field and are out of scope.
* **Anything but the tolerance token.** The edit is TEXTUAL and surgical, not a
  JSON round-trip: 46 of the 499 affected files do not re-serialize
  byte-identically under the canonical dump format, so a round-trip would
  produce diff noise indistinguishable from real edits. Every other byte of
  every file is left alone.

Dry-run by default. `--apply` writes. `--check` exits 1 if anything would
change (useful once the corpus is clean).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))

from qou_substrate.witness import _tolerance_literal  # noqa: E402

# `"tolerance": <scalar>` — matched for EVERY scalar shape, not only numbers.
# Matching numbers alone would silently break the 1:1 correspondence with the
# parsed document that `_ordered_tolerances` establishes, and a mis-aligned
# correspondence is exactly how a repair like this writes the right value into
# the wrong field.
_TOL = re.compile(
    r'("tolerance"\s*:\s*)'
    r'("(?:[^"\\]|\\.)*"|null|true|false|-?\d[0-9.eE+\-]*)'
)


def _ordered_tolerances(doc, path=(), out=None):
    """Every `tolerance` key in DOCUMENT order, with its path and value.

    Document order is text order: `json.loads` preserves object insertion
    order, so a depth-first walk in dict/list order visits the keys in exactly
    the sequence they appear in the file. That is what lets the n-th regex
    match be identified with the n-th parsed key without parsing JSON by hand.
    """
    if out is None:
        out = []
    if isinstance(doc, dict):
        for k, v in doc.items():
            if k == "tolerance" and not isinstance(v, (dict, list)):
                out.append((path + (k,), v))
            else:
                _ordered_tolerances(v, path + (k,), out)
    elif isinstance(doc, list):
        for i, v in enumerate(doc):
            _ordered_tolerances(v, path + (i,), out)
    return out


def _is_assertion_tolerance(path) -> bool:
    """`.assertions[<int>].tolerance` and nothing else."""
    return (len(path) == 3 and path[0] == "assertions"
            and isinstance(path[1], int) and path[2] == "tolerance")


def repair(text: str) -> tuple[str, int, list[str]]:
    """(new_text, n_replaced, notes). Raises on any correctness failure."""
    doc = json.loads(text)
    keys = _ordered_tolerances(doc)
    matches = list(_TOL.finditer(text))
    notes: list[str] = []
    if len(matches) != len(keys):
        # Not a failure of the corpus, a failure of THIS script to read it.
        # Skip rather than guess: a mis-aligned replacement is worse than none.
        raise ValueError(
            f"tolerance key count mismatch: {len(matches)} in text, "
            f"{len(keys)} parsed — refusing to guess the correspondence")

    want = json.loads(text)  # independent copy to mutate
    pieces: list[str] = []
    cursor = 0
    n = 0
    for m, (path, value) in zip(matches, keys):
        if not _is_assertion_tolerance(path):
            continue
        literal = _tolerance_literal(value)
        if literal is None:
            continue
        # The invariant. Bit for bit, or nothing is written.
        if float(literal) != value:
            raise ValueError(f"NOT value-preserving at {path}: "
                             f"{value!r} -> {literal!r}")
        pieces.append(text[cursor:m.start(2)])
        pieces.append(json.dumps(literal))
        cursor = m.end(2)
        want["assertions"][path[1]]["tolerance"] = literal
        n += 1
    if n == 0:
        return text, 0, notes
    pieces.append(text[cursor:])
    new = "".join(pieces)

    # Structural verification: the ONLY thing that changed is the tolerances we
    # intended to change. This is what makes a textual edit safe — it catches a
    # mis-aimed substitution regardless of how the regex was targeted.
    if json.loads(new) != want:
        raise ValueError("re-parsed document differs from the intended one")
    return new, n, notes


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write the repairs")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if anything would change")
    ap.add_argument("--root", default="computations",
                    help="tree to scan (default: computations)")
    args = ap.parse_args()

    root = ROOT / args.root
    changed_files = 0
    changed_fields = 0
    skipped: list[tuple[str, str]] = []
    for p in sorted(root.rglob("*.witness.json")):
        if "_deprecated" in p.parts:
            continue
        text = p.read_text(encoding="utf-8")
        try:
            new, n, _ = repair(text)
        except json.JSONDecodeError:
            continue
        except ValueError as e:
            skipped.append((p.relative_to(ROOT).as_posix(), str(e)))
            continue
        if n == 0:
            continue
        changed_files += 1
        changed_fields += n
        if args.apply:
            p.write_text(new, encoding="utf-8")
        else:
            print(f"  {p.relative_to(ROOT).as_posix()}: {n}")

    verb = "repaired" if args.apply else "would repair"
    print(f"{verb} {changed_fields} declared tolerances in {changed_files} files")
    if skipped:
        print(f"SKIPPED {len(skipped)} file(s) this script could not read safely:")
        for rel, why in skipped:
            print(f"  {rel}: {why}")
    if args.check and changed_fields:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
