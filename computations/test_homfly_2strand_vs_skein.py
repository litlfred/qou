#!/usr/bin/env python3
# polynomial_q_not_applicable: exact-integer knot invariants; no substrate q.
"""`homflypt_2strand`'s hardcoded table must agree with an exact skein engine.

Why this exists
---------------
`homflypt_engine.homflypt_2strand` is a hardcoded lookup table of HOMFLY
polynomials for `closure(sigma_1^k)`, `|k| <= 3`. Until 2026-08-21 four of its
seven entries were wrong (bean `qou-7ue5`):

    k = +3  held the LEFT trefoil          mirror swap
    k = -3  held the RIGHT trefoil         mirror swap
    k = +2  held the NEGATIVE Hopf link    mirror swap
    k = -2  held MINUS the positive Hopf   mirror swap AND a sign error

The module already contained a correct independent reference —
`homflypt_reference_qa._torus_homfly`, which derives the same family from the
skein relation by hand and disagreed with the table. **Nothing ever compared
them.** That QA's own docstring says the path under test is
`_homflypt_nstrand_numerical`, so the 2-strand table sat outside its coverage
for its whole life. This file is that missing comparison.

It is the same shape as `test_ctype_consumer_coverage.py`: *a private copy
cannot learn what the canonical one learns.* A hardcoded table is a private
copy of a computation, and the only durable defence is to re-derive and
compare mechanically.

What is checked
---------------
Part A  every table entry equals `homfly_skein_braid.homfly`, an exact-integer
        skein recursion — the external ground truth.

Part B  the table is **self-consistent under mirroring**: applying the HOMFLY
        mirror `(v, z) -> (v^-1, -z)` to the entry at `k` must give the entry
        at `-k`. This needs no external reference at all, and it alone would
        have caught the `k = -2` sign error, which was the one defect the
        mirror-swap story does not explain.

Part C  a regression guard on the trap that produced that error: at `k = 2`
        the true mirror and a naive `v -> v^-1` **differ**, while at `k = 3`
        they coincide (because `z` occurs there only as `z^2`). The old
        `k = -2` entry was built by the naive substitution, and k=3's
        coincidence is exactly why nobody noticed. Both facts are proved in
        `QOU/Knot/HomflySkeinReference.lean`
        (`plain_inversion_ne_mirror`, `plain_inversion_eq_mirror_at_three`);
        this pins them in the code so the coincidence cannot be re-read as a
        rule.

No floats, no substrate constant, no numpy — this runs anywhere.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from homfly_skein_braid import homfly  # noqa: E402
from homflypt_engine import homflypt_2strand  # noqa: E402

# |k| <= 3 is the table's whole domain; it raises above that.
CASES = {0: [], 1: [1], -1: [-1], 2: [1, 1], -2: [-1, -1],
         3: [1, 1, 1], -3: [-1, -1, -1]}


def mirror(terms: dict[tuple[int, int], int]) -> dict[tuple[int, int], int]:
    """The HOMFLY mirror `(v, z) -> (v^-1, -z)` on a term dict.

    The `z` sign is the whole point: `v^i z^j -> v^-i (-z)^j`, so a term of
    ODD `z`-degree changes sign. Dropping that is what produced the `k = -2`
    defect, and it is invisible wherever `z` happens to appear only evenly.
    """
    out: dict[tuple[int, int], int] = {}
    for (i, j), c in terms.items():
        out[(-i, j)] = out.get((-i, j), 0) + (c if j % 2 == 0 else -c)
    return {k: v for k, v in out.items() if v}


def naive_v_inversion(terms):
    """`v -> v^-1` alone — NOT the mirror. Kept only to assert it differs."""
    return {(-i, j): c for (i, j), c in terms.items()}


def main() -> int:
    print("=" * 74)
    print(" homflypt_2strand vs exact skein — the comparison that was missing")
    print("=" * 74)
    ok = True

    print("\n[A] table vs exact skein ground truth")
    table = {}
    for k, word in CASES.items():
        got = homflypt_2strand(word).terms
        want = homfly(word, 2).t
        table[k] = got
        match = got == want
        ok = ok and match
        print(f"    k = {k:>2}: {'OK' if match else 'MISMATCH'}")
        if not match:
            print(f"        table  {dict(sorted(got.items()))}")
            print(f"        skein  {dict(sorted(want.items()))}")

    print("\n[B] table self-consistency under the mirror (needs no reference)")
    for k in (1, 2, 3):
        match = mirror(table[k]) == table[-k]
        ok = ok and match
        print(f"    mirror(k = {k}) == k = {-k}: {'OK' if match else 'MISMATCH'}")
        if not match:
            print(f"        mirror  {dict(sorted(mirror(table[k]).items()))}")
            print(f"        actual  {dict(sorted(table[-k].items()))}")

    print("\n[C] the trap: naive v-inversion differs at k=2, coincides at k=3")
    c2 = naive_v_inversion(table[2]) != mirror(table[2])
    c3 = naive_v_inversion(table[3]) == mirror(table[3])
    ok = ok and c2 and c3
    print(f"    k = 2  naive != mirror: {'OK' if c2 else 'UNEXPECTED'}"
          "   (z to odd powers — sign flips)")
    print(f"    k = 3  naive == mirror: {'OK' if c3 else 'UNEXPECTED'}"
          "   (z only as z^2 — the coincidence)")

    print(f"\n  RESULT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
