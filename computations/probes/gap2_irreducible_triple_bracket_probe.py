#!/usr/bin/env python3
"""GAP-2 is bracketed: 3-cliques overshoot, and its own proposed fix gives ZERO.

TWO CORPUS RESULTS THAT HAVE NOT BEEN PUT TOGETHER.

(1) 2026-07-11, `gap2_borromean_triple_count.py` + audit. With per-order
    energies pinned on the minimal nucleus of each order and `M_n` = the
    k-clique counts of the max-contact deltahedra, the A>=5 binding
    OVERSHOOTS by +13 -> +24 %, monotonically growing. Its stated resolution,
    verbatim from the producer:

        "M_3(K) is the mu-bar_123-IRREDUCIBLE triple count, NOT the 3-clique
         count [...] a bonded triple is reducible (mu-bar = 0), already carried
         by the 2-body edges."

    and it leaves "compute the irreducible count" as the open step.

(2) 2026-08-29, `gap2_he4_borromean_mu_bar.py` + audit (bean qou-klgu, merged
    today in 84f9d1c0a). On a cluster where every bonded pair is Hopf-linked
    (lk = 1) -- which is what the max-contact contact graph is -- Milnor's
    indeterminacy makes every higher mu-bar defined only modulo gcd(lk) = 1,
    so it carries NO invariant content: the irreducible count is 0.

PUT TOGETHER, (2) ANSWERS (1)'s OPEN STEP, AND THE ANSWER IS ZERO. Every
3-clique of a max-contact deltahedron has all three of its pairs bonded, hence
all lk = 1, hence indeterminate mu-bar, hence reducible. So the resolution
proposed in July yields `M_3 = 0` at every A >= 5, and the tower collapses to
its 2-body part.

THE BRACKET. The two readings fall on opposite sides of the measurement and
there is nothing between them, because mu-bar irreducibility is all-or-nothing
here -- a triple is either determinate (lk = 0 on all three pairs) or carries
no content at all:

    all 3-cliques        -> OVERSHOOT
    mu-bar-irreducible   -> M_3 = 0 identically -> UNDERSHOOT

WHY THERE IS NO INTERMEDIATE, and this is the load-bearing point: `e_3` is
pinned on the TRITON, whose single triple is genuinely Borromean (lk = 0,
mu-bar = +1, computed in qou-klgu). Under the max-contact model no such triple
occurs at any A >= 5 -- every triple there is bonded-hence-reducible. So the
3-body term is calibrated on a configuration type that never recurs, and the
mu-bar realisation cannot interpolate between the brackets.

SCOPE -- RE-SCOPED 2026-08-30, BEFORE THIS EVER MERGED. This was written as
scope-(b) for the MU-BAR REALISATION of `M_3` at A >= 5, with the invariant
cited (Milnor indeterminacy). It is now (a): CONDITIONAL ON THE LINK MODEL.
The premise "every bonded pair has lk = 1" is contradicted by the corpus's own
triton model -- see `bonded_pair_linking_inconsistency_probe.py`, which was
written an hour after this one and corrects both it and qou-klgu. The bracket
BELOW STANDS as arithmetic; what changes is that its lower arm (M_3 = 0) is a
consequence of an assumed link assignment rather than a forced one.
The original wording, kept for the record: scope-(b) with the invariant cited -- the same invariant and the same
argument as qou-klgu, applied to the A >= 5 deltahedra rather than to the
tetrahedron. It excludes NOTHING ELSE. A non-Milnor super-pairwise object is
untouched, exactly as in qou-klgu; so is the possibility that the contact model
itself (bonded => lk = 1) is the wrong link model, which is the assumption this
argument runs on and is worth attacking directly.

The graphs are built and their cliques counted here INDEPENDENTLY of the July
witness, and the counts are asserted against it as a cross-check.

Beans qou-x5bv / parent qou-y2l3; continues qou-ooqh (GAP-2) and qou-klgu.
Discipline: mpmath 60 dps, no float() outside display, AME from the canonical
table. No fit -- energies pinned on minimal nuclei, A >= 5 held out. No witness,
nothing wired.
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import mpmath as mp  # noqa: E402

import ame_2020_binding_energies as ame  # noqa: E402

mp.mp.dps = 60


def _B(Z: int, A: int) -> mp.mpf:
    return mp.mpf(str(ame._binding_mev_exact(Z, A)))


def _cliques(n: int, edges: set[frozenset[int]], k: int) -> int:
    """Count k-cliques by brute force over k-subsets (n <= 7 here)."""
    return sum(
        1
        for c in itertools.combinations(range(n), k)
        if all(frozenset(p) in edges for p in itertools.combinations(c, 2))
    )


def _deltahedron(A: int) -> set[frozenset[int]]:
    """Max-contact contact graph for each light nucleus (3-D packing fact)."""
    E: set[frozenset[int]] = set()
    add = lambda a, b: E.add(frozenset((a, b)))  # noqa: E731
    if A <= 4:                       # complete: all spheres mutually touch
        for a, b in itertools.combinations(range(A), 2):
            add(a, b)
    elif A == 5:                     # triangular bipyramid: apexes 3,4
        for a, b in itertools.combinations(range(3), 2):
            add(a, b)
        for ap in (3, 4):
            for e in range(3):
                add(ap, e)
    elif A == 6:                     # octahedron = K_{2,2,2}; antipodes unbonded
        for a, b in itertools.combinations(range(6), 2):
            if {a, b} not in ({0, 1}, {2, 3}, {4, 5}):
                add(a, b)
    elif A == 7:                     # pentagonal bipyramid: apexes 5,6
        for e in range(5):
            add(e, (e + 1) % 5)
        for ap in (5, 6):
            for e in range(5):
                add(ap, e)
    else:
        raise ValueError(f"no deltahedron recorded for A={A}")
    return E


def main() -> int:
    ISO = [("D", 1, 2), ("T", 1, 3), ("4He", 2, 4),
           ("5Li", 3, 5), ("6Li", 3, 6), ("7Li", 3, 7)]
    # July witness counts, asserted against the graphs built here.
    JULY = {"D": (1, 0, 0), "T": (3, 1, 0), "4He": (6, 4, 1),
            "5Li": (9, 7, 2), "6Li": (12, 8, 0), "7Li": (15, 10, 0)}

    print("== max-contact contact graphs, cliques counted independently ==")
    counts = {}
    for lab, _Z, A in ISO:
        E = _deltahedron(A)
        m2, m3, m4 = (_cliques(A, E, k) for k in (2, 3, 4))
        counts[lab] = (m2, m3, m4)
        ok = JULY[lab] == (m2, m3, m4)
        print(f"  {lab:5s} A={A}: M2={m2:3d} M3={m3:3d} M4={m4:2d}"
              f"   vs July witness {JULY[lab]}  {'MATCH' if ok else 'MISMATCH'}")
        assert ok, f"{lab}: clique counts disagree with the July witness"

    # Per-order energies, pinned on the minimal nucleus of each order (anti-fit).
    e2 = _B(1, 2)                                    # deuteron: the single bond
    e3 = (_B(1, 3) - 3 * e2) / counts["T"][1]        # triton: its single triple
    print()
    print("== per-order energies, pinned on minimal nuclei (no A>=5 input) ==")
    print(f"  e2 = B(D)               = {mp.nstr(e2, 12)} MeV")
    print(f"  e3 = (B(T) - 3e2)/M3(T) = {mp.nstr(e3, 12)} MeV")

    print()
    print("== the bracket: two readings of M3, held out at A >= 5 ==")
    print("   reading A = every 3-clique is a 3-body term  (July's tested form)")
    print("   reading B = only mu-bar-IRREDUCIBLE triples   (July's proposed fix)")
    print("   Under (2), reading B gives M3 = 0 on every max-contact cluster,")
    print("   because all three pairs of a 3-clique are bonded => all lk = 1.")
    print()
    hdr = f"  {'iso':5s} {'M2':>3s} {'M3cl':>5s} {'B_A':>9s} {'B_B':>9s} {'AME':>9s} {'A/AME':>7s} {'B/AME':>7s}"
    print(hdr)
    for lab, Z, A in ISO:
        if A < 5:
            continue
        m2, m3, _m4 = counts[lab]
        meas = _B(Z, A)
        BA = m2 * e2 + m3 * e3          # all 3-cliques
        BB = m2 * e2                    # irreducible-only, i.e. M3 = 0
        print(f"  {lab:5s} {m2:3d} {m3:5d} {mp.nstr(BA,7):>9s} {mp.nstr(BB,7):>9s}"
              f" {mp.nstr(meas,7):>9s} {mp.nstr(BA/meas,4):>7s} {mp.nstr(BB/meas,4):>7s}")

    print()
    print("== NORMALISATION NOTE — read before comparing to the July witness ==")
    print("  The ratios above are against RAW B_AME. The July witness reports")
    print("  ratio_2plus3 against B_strong, its COULOMB-CORRECTED binding")
    print("  (6Li: 1.2102 there vs 1.286 here). Those are the same quantity")
    print("  under two normalisations, NOT a discrepancy, and neither should")
    print("  be 'corrected' into the other.")
    print("  The bracket conclusion is invariant under the choice: Coulomb")
    print("  correction raises the denominator, so BOTH readings move down")
    print("  together and continue to straddle 1. Checked at 6Li against the")
    print("  witness's own B_strong = 34.0118: reading A 41.1596/34.0118 =")
    print("  1.2102 (> 1), reading B 26.6948/34.0118 = 0.7849 (< 1).")
    print()
    print("== VERDICT ==")
    print("  The two readings bracket the measurement from opposite sides, and")
    print("  mu-bar supplies nothing in between: a triple is either determinate")
    print("  (lk = 0 on all three pairs) or carries no content at all.")
    print()
    print("  e_3 is pinned on the TRITON triple, which is genuinely Borromean")
    print("  (lk = 0, mu-bar = +1). Under the max-contact model no such triple")
    print("  occurs at any A >= 5, so the 3-body term is calibrated on a")
    print("  configuration type that never recurs.")
    print()
    print("  RE-SCOPED (b) -> (a): CONDITIONAL ON THE LINK MODEL. The premise")
    print("  'every bonded pair has lk = 1' is contradicted by the corpus's own")
    print("  triton model (BORROMEAN, pairwise lk = [0,0,0], three BONDED")
    print("  pairs) -- see bonded_pair_linking_inconsistency_probe.py. The")
    print("  bracket above stands as arithmetic; its lower arm (M3 = 0) follows")
    print("  from an ASSUMED link assignment, not a forced one. Excludes")
    print("  nothing structurally. A non-Milnor")
    print("  super-pairwise object is untouched, and so is the possibility that")
    print("  'bonded => lk = 1' is the wrong link model. That assumption is what")
    print("  this argument runs on, and it is the thing to attack next.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
