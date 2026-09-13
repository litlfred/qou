#!/usr/bin/env python3
"""atom_closure_component_count_probe — the canonical atom word's Markov closure
has exactly ``A + 1`` components, for every ``A``, under BOTH intra-orderings.

WHY THIS EXISTS.  Bean ``qou-o6ml`` (the EM-linking invariant arc) closed its
route (2) on a refutation recorded in ``he4-link-volume-braid-closure.witness.json``:
the Markov closure of the canonical atomic braid word gives **4** components at
A = 3, where the census-assigned binding carriers have **1** (``8_11``, for 3H)
and **3** (``L6a4`` = Borromean, for 3He).  That witness was computed
**2026-07-04**.

The producer's import cone changed after it.  ``he4_link_volume_braid_closure``
calls ``canonical_braid_crossings.atom_canonical_crossings``, whose source of
truth is ``mass_at_3A_proper.atom_braid_word_3A`` -- and commit ``7db032fb48``
(2026-09-05) changed that word's default ``intra_order`` to ``"borromean"``, so
each nucleon's confinement core became the alternating ``(s0 s1^-1)^3``.  That
same change moved ``tr_M(p)`` by 45 % and ``tr_M(n)`` by 52 % and left >= 8
committed witnesses carrying the retired values (bean ``qou-sikd``).  So the
natural worry is that the refutation is a measurement of a retired element --
exactly the import-cone-drift class AGENTS.md documents, where a producer's own
source is byte-stable while a module it calls changed.

THE WORRY IS WRONG, AND THAT IS THE RESULT.  The two words genuinely differ
(asserted below), and the component count is **identical** under both, because
the count is an invariant of the induced permutation's orbit structure and the
re-ordering is a permutation-preserving rearrangement of the same transposition
multiset.  So the refutation's load-bearing half is NOT stale.

AND IT IS STRONGER THAN THE BEAN STATES.  The bean says "refuted at the two
isotopes where the answer is checkable".  Measured here over A = 2, 3, 4, 6:
the closure has ``A + 1`` components on ``3A`` strands, exactly, at every A and
under both orderings.  A 4-component closure is not a 1-component knot and not
a 3-component link, and no re-run at any word ordering will make it one.

NO FLOATS.  Every quantity here is an integer: letters, strands, and the orbit
count of a permutation.  There is no arithmetic that could lose precision, so
the NO-FLOAT64 family has nothing to bind on -- stated explicitly rather than
left to inference, per AGENTS.md "PROBES ARE NOT EXEMPT".

NOT CLAIMED.  Nothing about hyperbolic volume or geometricity: ``snappy`` and
``spherogram`` are absent in this container, so the witness's ``geometric: no``
and ``Vol: 0`` rows are NOT re-measured here and are NOT asserted either way.
Nothing about whether ``A + 1`` components is the *wrong* answer -- that depends
on which object a nucleus should close to, which is the open question, not this
probe's.  And nothing about the census assignment's own correctness; bean
``qou-5vhf`` establishes separately that it is an admitted AME-driven fit.
"""

from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402

# (isotope label, Z, N) -- 2H..6Li; A = Z + N.
CASES = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2), ("6Li", 3, 3)]
ORDERS = ("borromean", "grouped")

# The census-assigned binding carriers the 2026-07-04 witness compares against.
CENSUS_CARRIER_COMPONENTS = {"3H": ("8_11", 1), "3He": ("L6a4 (Borromean)", 3)}


def closure_components(crossings: list[tuple[int, str]]) -> tuple[int, int]:
    """Strand count and component count of the Markov (plat-free) closure.

    The closure's components are the orbits of the permutation the braid induces
    on its strands: generator ``i`` contributes the transposition ``(i, i+1)``,
    and the closure identifies strand ``k`` at the top with strand ``perm[k]``
    at the bottom.  Crossing SIGN is irrelevant to this count, which is exactly
    why the count cannot depend on the sign pattern that distinguishes the two
    intra-orderings.
    """
    gens = [g for g, _ in crossings]
    n_strands = max(gens) + 2
    perm = list(range(n_strands))
    for g in gens:
        perm[g], perm[g + 1] = perm[g + 1], perm[g]
    seen: set[int] = set()
    components = 0
    for start in range(n_strands):
        if start in seen:
            continue
        components += 1
        cur = start
        while cur not in seen:
            seen.add(cur)
            cur = perm[cur]
    return n_strands, components


def main() -> int:
    words: dict[tuple[str, str], list[tuple[int, str]]] = {}
    rows: list[tuple[str, int, str, int, int, int]] = []

    for label, Z, N in CASES:
        for order in ORDERS:
            crossings = atom_canonical_crossings(Z, N, intra_order=order)
            words[(label, order)] = crossings
            n_strands, comps = closure_components(crossings)
            rows.append((label, Z + N, order, len(crossings), n_strands, comps))

    print(f"{'isotope':8s} {'A':>2s} {'intra_order':12s} "
          f"{'letters':>7s} {'strands':>7s} {'comps':>5s}")
    for label, A, order, letters, strands, comps in rows:
        print(f"{label:8s} {A:2d} {order:12s} {letters:7d} {strands:7d} {comps:5d}")

    checks: list[tuple[str, bool, str]] = []

    # 1. The two intra-orderings really are different WORDS. Without this the
    #    invariance below would be vacuous -- it would just be comparing a thing
    #    to itself, which is the shape that produced four vacuous declarations
    #    in QOU.MobiusEnergy (bean qou-pc85).
    differ = all(words[(lab, "borromean")] != words[(lab, "grouped")]
                 for lab, _, _ in CASES)
    checks.append(("the two intra-orderings are genuinely different words",
                   differ, "if equal, every invariance claim below is vacuous"))

    # 2. The component count does not depend on the ordering.
    invariant = all(
        closure_components(words[(lab, "borromean")])
        == closure_components(words[(lab, "grouped")])
        for lab, _, _ in CASES
    )
    checks.append(("component count is invariant under intra_order",
                   invariant, "this is what makes the 2026-07-04 refutation non-stale"))

    # 3. The count is A + 1 on 3A strands, at every A tested.
    law = all(comps == A + 1 and strands == 3 * A
              for _, A, _, _, strands, comps in rows)
    checks.append(("closure has A + 1 components on 3A strands at every A",
                   law, "the refutation is structural, not two isolated isotopes"))

    # 4. The A = 3 counts reproduce the committed witness exactly.
    a3 = {(lab, comps) for lab, A, _, _, _, comps in rows if A == 3}
    reproduces = a3 == {("3H", 4), ("3He", 4)}
    checks.append(("A = 3 reproduces the 2026-07-04 witness (4 and 4)",
                   reproduces, "cross-check against he4-link-volume-braid-closure"))

    # 5. And it still misses both census carriers.
    misses = all(
        comps != CENSUS_CARRIER_COMPONENTS[lab][1]
        for lab, A, _, _, _, comps in rows
        if lab in CENSUS_CARRIER_COMPONENTS
    )
    checks.append(("the closure misses BOTH census carriers' component counts",
                   misses, "8_11 has 1, L6a4 has 3; the closure has 4"))

    print()
    for name, ok, why in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"         {why}")

    passed = sum(1 for _, ok, _ in checks if ok)
    print(f"\n{passed}/{len(checks)} assertions passed")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
