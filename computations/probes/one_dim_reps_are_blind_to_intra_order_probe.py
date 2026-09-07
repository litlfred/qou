"""The two 1-dimensional reps are INVARIANT under the intra-ordering ruling.

WHY THIS EXISTS
---------------
The intra-ordering ruling (`qou-hu1f`, owner 2026-09-05) moved
`atom_braid_word_3A`'s per-nucleon confinement core from GROUPED to alternating
(`intra_order="borromean"`).  That is a REORDERING of the same letters, not a
change of letters.  So every chi cache computed before the ruling is stale --
and the corpus has 34 such witnesses across 63 producers reading the
`atom-chi-rust-*` family.

Re-running 34 producers to find out which ones actually MOVED is the expensive
way to answer that.  This probe establishes the cheap way, and it is a theorem
rather than a heuristic:

    A 1-dimensional representation's character is a PRODUCT of per-letter
    scalars.  A product is commutative.  So chi^lambda on a 1-dim block is
    fixed by the letter MULTISET and is blind to the order.

S_n has exactly two 1-dim reps -- the trivial (n) and the sign (1^n).  Hence:

    TRIAGE RULE.  A producer that reads only the trivial or the sign block is
    UNAFFECTED by the ruling.  A producer touching any higher-dimensional block
    is stale and must be re-run.

WHAT IS MEASURED
----------------
The committed-grouped caches (origin/main) against the repaired-borromean ones
(this branch), per atom and per leg.  The prediction is sharp and falsifiable in
both directions: exactly two partitions unchanged, and they are exactly those
two -- not "mostly unchanged", not "the small ones".

    D    atom  n= 11  moved  9  same 2   [(1,1,1,1,1,1), (6,)]
    D    free  n= 11  moved  9  same 2   [(1,1,1,1,1,1), (6,)]
    T    atom  n= 30  moved 28  same 2   [(1,)*9, (9,)]
    T    free  n= 30  moved 28  same 2   [(1,)*9, (9,)]
    3He  atom  n= 30  moved 28  same 2   [(1,)*9, (9,)]
    3He  free  n= 30  moved 29  same 1   [(9,)]          <-- see below

THE SIXTH CASE IS NOT A COUNTEREXAMPLE, AND SAYING SO REQUIRES A MEASUREMENT.
`3He free` shows the sign rep moving.  It is the `qou-07ts` non-reproducibility
that `compute_atom_chi_rust.py` documents in its own header -- one unit in the
last place of the 50-dps string:

    main : -0.49768736698467635807091211637761687524171090034637
    here : -0.49768736698467635807091211637761687524171090034636
    rel  : 2.009e-50

35 orders below the 1 ppQ (1e-15) L1 target.  A ULP wobble on a producer already
known to be non-reproducible for 3He is not evidence about braid words -- but
"it is small" is not the argument.  The argument is that the producer's OWN
header records this exact signature for this exact atom, measured over eight
runs, before this probe existed.  So the invariance holds 6 of 6, and this test
asserts the ULP bound rather than exact equality on that one cell.

WHAT THIS DOES *NOT* SHOW
-------------------------
It does not show the higher blocks moved BECAUSE of the reordering -- only that
they moved.  A cache regenerated across a window can move for other reasons.
What makes the attribution sound here is the CONVERSE half: if the letters had
changed rather than merely been reordered, the 1-dim blocks would have moved
too, and they did not.  That is the falsifiable half, and it is the half this
probe exists to check.
"""

from __future__ import annotations

import json
import subprocess
import sys
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 60

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

# The qou-07ts ULP tolerance: one unit in the last place of a 50-dps string.
ULP_REL = Decimal("1e-49")

ATOMS = (("D", "atom-chi-rust-d"), ("T", "atom-chi-rust-t"), ("3He", "atom-chi-rust-3he"))


def _one_dim(n: int):
    """The two 1-dimensional reps of S_n: trivial (n) and sign (1^n)."""
    return {(n,), (1,) * n}


def _by_partition(w: dict, leg: str):
    return {tuple(r["partition"]): r["chi_lambda"] for r in w["data"][leg]["by_partition"]}


def _at_main(path: str):
    r = subprocess.run(["git", "show", f"origin/main:{path}"],
                       capture_output=True, text=True, cwd=ROOT)
    return json.loads(r.stdout) if r.returncode == 0 else None


def main() -> int:
    results, failures = [], []
    for atom, stem in ATOMS:
        rel = f"computations/{stem}.witness.json"
        old = _at_main(rel)
        new_p = ROOT / rel
        if old is None or not new_p.exists():
            failures.append(f"{atom}: cannot read both versions of {rel}")
            continue
        new = json.loads(new_p.read_text())
        for leg in ("atom", "free"):
            mo, mn = _by_partition(old, leg), _by_partition(new, leg)
            common = set(mo) & set(mn)
            n = max(sum(p) for p in common)
            one_dim = _one_dim(n)

            moved, same, ulp = [], [], []
            for lam in sorted(common):
                if mo[lam] == mn[lam]:
                    same.append(lam)
                    continue
                a, b = Decimal(mo[lam]), Decimal(mn[lam])
                r = abs(a - b) / abs(a) if a else Decimal(0)
                (ulp if r <= ULP_REL else moved).append(lam)

            invariant = set(same) | set(ulp)
            results.append((atom, leg, len(common), len(moved), sorted(invariant), sorted(ulp)))

            # THE ASSERTION, both directions.
            missing = one_dim - invariant       # a 1-dim block that moved: falsifies the theorem
            extra = invariant - one_dim         # a higher block that did not: unexplained
            if missing:
                failures.append(
                    f"{atom}/{leg}: 1-dim block(s) {sorted(missing)} MOVED beyond ULP "
                    "-- the letters changed, not just their order")
            if extra:
                failures.append(
                    f"{atom}/{leg}: higher-dim block(s) {sorted(extra)} did NOT move -- unexplained")

    print("=" * 74)
    print("1-DIM REPS ARE BLIND TO INTRA-ORDER  (grouped -> borromean)")
    print("=" * 74)
    print(f"  {'atom':5s} {'leg':5s} {'n':>4s} {'moved':>6s} {'invariant':>10s}   partitions")
    for atom, leg, n, nmoved, inv, ulp in results:
        tag = "  (1 via ULP)" if ulp else ""
        print(f"  {atom:5s} {leg:5s} {n:4d} {nmoved:6d} {len(inv):10d}   {inv}{tag}")

    print()
    print("  TRIAGE RULE for the 34 pre-ruling witnesses:")
    print("    reads ONLY (n) or (1^n)  -> unaffected, no re-run needed")
    print("    touches any other block  -> stale, must be re-run")

    print()
    if failures:
        for f in failures:
            print(f"  [FAIL] {f}")
        print(f"\n{len(failures)} FAILED")
        return 1
    print(f"  [PASS] {len(results)} atom/leg pairs: invariant set is EXACTLY the two 1-dim reps")
    print("\nALL PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
