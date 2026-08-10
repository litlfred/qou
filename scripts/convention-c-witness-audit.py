#!/usr/bin/env python3
"""Find convention-C witnesses STRUCTURALLY, not by matching known numbers.

## Why this replaces the fingerprint approach

The witness-regeneration campaign (`qou-eea0`) built its work list by grepping
witnesses for known convention-C decimal strings:

    0.49932033418369   0.41539579536   0.2809296   0.02274491

Those are the `n = 3` values — `z_C` and the three `y_λ` at three strands. A
witness computed at `n = 6`, `9` or `12` contains none of them, so **the entire
nuclear layer was invisible to that scan**: deuteron at `H₆`, helium-3 at `H₉`,
helium-4 at `H₁₂`, the `a_K` LP duals, the `binding-a3plus` assemblies.

Measured against this detector at the time it was written:

| | |
|---|---|
| fingerprint-detected | 46 |
| structurally convention C | 53 |
| overlap | **12** |
| **missed by fingerprints** | **41** |

The campaign reported "total impact" over a list that missed most of the surface.
That is the failure this file exists to prevent recurring.

## The structural test

Under convention D the Markov trace restricted to block `λ` is `y_λ · χ^λ`, and

    y_λ = 0   for every λ with ℓ(λ) ≥ 3

exactly — the fibre is the two-dimensional fundamental of `SU_q(2)`, so by
Schur–Weyl no partition with three or more rows survives. So:

> **A witness recording a nonzero `y_λ` on a three-or-more-row partition is
> convention C. No exceptions, at any `n`, whatever numbers it happens to
> contain.**

This is a property of the physics rather than of a decimal expansion, so it
cannot be evaded by a different `n`, a different precision, a different variable
name, or a value nobody thought to add to a fingerprint list.

Proved, and the claim above is quantified over ALL `n`, so it takes both halves:

- `TemperleyLiebTower.conventionD_kills_antisymmetriser` — the **base case**,
  `n = 3`. From the three Markov moment equations plus `z·(q²+1) = q³` (which
  *is* convention D), `y₍₁³₎ = 0`. Sorry-free.
- `YoungDiagramThreeRowCorner.threeRow_vanishing_all_levels` — the **lift** to
  every `n > 3`, given non-negativity and branching domination. Its
  combinatorial input is discharged by `card_three_threeRow_unique`: at three
  cells `(1³)` is the only three-row shape, so the base case has nothing to
  quantify over. Sorry-free.

Only the base case was cited here before, while the test it justifies runs at
`n = 6, 9, 12`. The lift is what carries it there.

Also `MarkovGramDegenerate.wedderburnGram_det_eq_zero_of_dead` for the
consequence on `det G`. Named in compute by `computations/live_channels.py`.

## Usage

    python3 scripts/convention-c-witness-audit.py            # summary
    python3 scripts/convention-c-witness-audit.py --list
    python3 scripts/convention-c-witness-audit.py --json out.json
    python3 scripts/convention-c-witness-audit.py --selftest

Exit 1 when any witness is structurally convention C.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent

#: Below this a weight is dead. Convention D gives exact zeros symbolically; a
#: float pipeline may deliver 1e-300. Far below the smallest live weight
#: (y_(2,1) ≈ 0.247 at n = 3).
DEAD_TOL = 1e-30

#: Keys that hold a Wedderburn weight.
WEIGHT_KEYS = ("y_lambda", "y_lam", "y_at_q0", "weight_lambda")


def _partition_of(node: dict):
    """Extract a partition from a witness node, tolerating odd encodings.

    Some witnesses store `['3','_','2','_','1']` — underscore-separated digits
    rather than a list of ints. Those are real entries in
    `binding-a3plus-*.witness.json` and must not be silently skipped, since
    skipping is how the fingerprint scan missed things.
    """
    part = node.get("partition")
    if part is None:
        return None
    if isinstance(part, (list, tuple)):
        cleaned = [x for x in part if x not in ("_", "", None)]
        try:
            return tuple(int(x) for x in cleaned)
        except (TypeError, ValueError):
            return None
    if isinstance(part, str):
        try:
            return tuple(int(x) for x in part.replace("_", " ").split())
        except ValueError:
            return None
    return None


def scan_doc(doc, tol: float = DEAD_TOL):
    """Yield (partition, key, value) for every nonzero weight on a 3+ row block."""
    found = []

    def walk(node):
        if isinstance(node, dict):
            part = _partition_of(node)
            if part is not None and len(part) >= 3:
                for k, v in node.items():
                    if any(w in k for w in WEIGHT_KEYS):
                        try:
                            val = abs(float(v))
                        except (TypeError, ValueError):
                            continue
                        if val > tol:
                            found.append((part, k, v))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(doc)
    return found


def scan_repo(root: pathlib.Path = None):
    root = root or (REPO / "computations")
    out = []
    for p in sorted(root.rglob("*.json")):
        if "_deprecated" in str(p):
            continue
        try:
            raw = p.read_text()
        except OSError:
            continue
        if "partition" not in raw:
            continue
        try:
            doc = json.loads(raw)
        except json.JSONDecodeError:
            continue
        hits = scan_doc(doc)
        if hits:
            out.append((str(p.relative_to(REPO)), hits))
    return out


def selftest() -> int:
    """A detector that cannot fail is worse than none."""
    cases = [
        ("nonzero weight on a 3-row block -> FLAG",
         {"per_lambda": [{"partition": [1, 1, 1], "y_lambda": 0.0227449}]}, True),
        ("nonzero weight at n=6, no n=3 fingerprint anywhere -> FLAG",
         {"per_lambda": [{"partition": [3, 1, 1, 1], "y_lambda": -0.000685309}]}, True),
        ("underscore-encoded partition -> FLAG",
         {"rows": [{"partition": ["3", "_", "2", "_", "1"], "y_lambda": 0.00731845}]}, True),
        ("zero weight on a 3-row block -> clear (this is convention D)",
         {"per_lambda": [{"partition": [1, 1, 1], "y_lambda": 0.0}]}, False),
        ("nonzero weight on a TWO-row block -> clear (live channel)",
         {"per_lambda": [{"partition": [2, 1], "y_lambda": 0.2472979}]}, False),
        ("nonzero on a one-row block -> clear",
         {"per_lambda": [{"partition": [3], "y_lambda": 0.5054042}]}, False),
        ("no partitions at all -> clear",
         {"data": {"mass": 938.272}}, False),
    ]
    bad = 0
    for name, doc, want in cases:
        got = bool(scan_doc(doc))
        ok = got == want
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {name}")
    print(f"selftest: {len(cases)-bad}/{len(cases)}"
          + ("" if bad else " — flags a 3+row nonzero weight at any n, clears convention D."))
    return bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--json", metavar="OUT")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        return 1 if selftest() else 0

    hits = scan_repo()
    total = sum(len(h) for _, h in hits)
    print("convention-C witnesses, detected STRUCTURALLY "
          "(nonzero y_lambda on a 3+ row block)\n")
    print(f"  {len(hits)} witness(es), {total} dead-block entries\n")
    for path, entries in hits:
        print(f"  {path}   ({len(entries)} entries)")
        if a.list:
            for part, k, v in entries[:6]:
                print(f"      {list(part)}  {k} = {str(v)[:38]}")

    if a.json:
        pathlib.Path(a.json).write_text(json.dumps(
            [{"witness": p,
              "entries": [{"partition": list(pt), "key": k, "value": str(v)}
                          for pt, k, v in e]}
             for p, e in hits], indent=2))
        print(f"\n  json -> {a.json}")

    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
