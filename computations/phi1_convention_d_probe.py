#!/usr/bin/env python3
"""Does Phi_1 survive the convention-C excision? (bean qou-1jw9)

Phi_2 and Phi_3 are re-derived and CONVENTION-FREE -- neither uses the Markov
parameter z (phi_allpairs_reconstruction.py). Phi_1 is the only one of the
three that does:

    Phi_1 = sum_i ln| z*(M_i)_12 + (M_i)_22 |

so it is the only invariant the C/D ruling of 2026-08-15 can touch, and the
only one whose value moves when C is excised.

THIS PROBE COMPUTES IN CONVENTION D ONLY (z = q^3/(q^2+1)), per the owner
directive to excise C. It asks one question: under the correct ALL-PAIRS chain
structure and def:atomic-braid's own ground-state rule (minimise Phi_1), does
convention D reproduce the carried Phi_1 values?

WHY THE ANSWER MATTERS EITHER WAY. The 20 carried Phi_1 values are what the
published mass table is computed from. If D reproduces them, the table is
convention-independent in practice and the excision costs nothing. If D does
not, then the table as published is a convention-C artifact, and that is a
finding about the table, not about this probe.

NO FITTING. Orderings are enumerated, not searched over parameters; z is fixed
by convention D; the carried values are targets, never inputs.
"""
from __future__ import annotations

import sys
from itertools import permutations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
set_compute_dps(50)

# The producer's own recorded q, a five-decimal rounding of the pin. Used so the
# comparison is against what the producer actually evaluated; the convention is
# the variable under test, not the anchor.
Q = mp.mpf("1.10998")
H = Q - 1 / Q
Z_D = Q ** 3 / (Q ** 2 + 1)          # convention D -- canonical, 2026-08-15

# Table 1, with the pn coefficient in the UN-DOUBLED form (1, -h/2) that Phi_2
# discriminates in favour of (phi2_pn_coefficient_probe.py).
TBL = {("p", "p"): (1, mp.mpf(0)), ("n", "n"): (1, -H), ("p", "n"): (1, -H / 2),
       ("p", "e"): (1, -H), ("n", "e"): (0, mp.mpf(1)), ("e", "e"): (1, mp.mpf(0))}


def cr(a, b):
    return TBL[(a, b)] if (a, b) in TBL else TBL[(b, a)]


def V(chain, z):
    a, b = mp.mpf(0), mp.mpf(1)
    for c, d in chain:
        c = mp.mpf(c)
        a, b = a * (c * H + d) + b * c, a * c + b * d
    return z * a + b


def phi1(seq, z):
    """All-pairs: M_i = prod_{j>i} T(s_i, s_j)."""
    n = len(seq)
    tot = mp.mpf(0)
    for i in range(n):
        ch = [cr(seq[i], seq[j]) for j in range(i + 1, n)]
        if ch:
            tot += mp.log(abs(V(ch, z)))
    return tot


def orderings(Z, N, cap):
    """Every arrangement with each electron immediately before a proton."""
    out = set()
    for nuc in sorted(set(permutations("p" * Z + "n" * N)))[:cap]:
        s = []
        for c in nuc:
            s.extend(["e", "p"]) if c == "p" else s.append("n")
        out.add(tuple(s))
    return sorted(out)


ROWS = [("He", 2, 2, "-5.558902"), ("Li", 3, 4, "-9.838642"),
        ("Be", 4, 5, "-18.272718"), ("B", 5, 6, "-22.803608"),
        ("C", 6, 6, "-24.310734")]
CAP = 400   # reported, not silent


def main() -> int:
    print(f"convention D:  z = q^3/(q^2+1) = {mp.nstr(Z_D, 14)}   "
          f"q = {Q}  (the producer's recorded value)")
    print(f"chain structure: ALL-PAIRS.  ground state: minimise Phi_1 "
          f"(def:atomic-braid).  ordering cap {CAP}.\n")
    print(f"{'atom':>5} {'carried Phi_1':>14} {'min over D':>14} "
          f"{'max over D':>14} {'carried in range?':>18} {'rel gap at min':>15}")
    print("-" * 86)
    inrange = 0
    for el, Z, N, tgt in ROWS:
        seqs = orderings(Z, N, CAP)
        vs = [phi1(list(s), Z_D) for s in seqs]
        lo, hi = min(vs), max(vs)
        t = mp.mpf(tgt)
        ok = lo <= t <= hi
        inrange += ok
        gap = abs(lo - t) / abs(t)
        print(f"{el:>5} {tgt:>14} {mp.nstr(lo, 10):>14} {mp.nstr(hi, 10):>14} "
              f"{('YES' if ok else 'NO'):>18} {mp.nstr(gap, 6):>15}")
        if len(seqs) == CAP:
            print(f"      (cap hit: {CAP} of {len(set(permutations('p'*Z+'n'*N)))} "
                  f"nuclear arrangements enumerated -- min may not be global)")

    print(f"\n  carried value reachable under convention D: {inrange}/{len(ROWS)}")
    print()
    if inrange == 0:
        print("  READING: convention D does not reach ANY carried Phi_1. The")
        print("  carried values -- and therefore the published mass table that is")
        print("  computed from them -- are a CONVENTION-C artifact.")
        print()
        print("  This is a finding about the table, not about this probe. Phi_2 and")
        print("  Phi_3 are unaffected: both are convention-free and stay re-derived.")
        print("  What it means concretely: excising convention C does NOT leave the")
        print("  table intact. Phi_1 has to be recomputed under D, which will move")
        print("  every published row, and that is an owner decision -- the same one")
        print("  the beta3 repair needed.")
    else:
        print("  READING: convention D reaches the carried value for the rows above.")
        print("  Whether it reproduces it exactly (not merely brackets it) needs the")
        print("  full enumeration, not this capped one.")
    print("\n  SCOPE (a): capped enumeration, five light atoms, one chain structure.")
    print("  No claim is made that no convention-D construction reaches these values.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
