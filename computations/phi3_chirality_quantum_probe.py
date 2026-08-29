#!/usr/bin/env python3
"""Phi_3's QUANTUM is derived; its INTEGER is not. (bean qou-1jw9, item 1)

Item 1 of this arc is that Phi_1/Phi_2/Phi_3 in wedderburn_mass_table_z1_20.py
are CARRIED verbatim from the recovered witness, never re-derived.  This probe
closes one third of that gap and states precisely how much of the rest remains.

WHAT IS DERIVED (not fitted, not observed -- proved).
Every crossing in tbl:atomic-braid-table1-data has chirality ratio
lam_sym/lam_alt equal to -q^2, -q^-2, or +-1:

    pp (1,0)     -> -q^2     -> +2 units of ln q
    ee (1,0)     -> -q^2     -> +2
    nn (1,-h)    -> -q^-2    -> -2
    pe (1,-h)    -> -q^-2    -> -2
    pn (2,-h)    -> -1       ->  0
    ne (0,1)     -> +1       ->  0

These are exactly the three cases already proved sorry-free in
content/quantum-observable-universe/lean/QOU/BraidKnot/HeckeLinearReduction.lean
(symAltRatio_zero, symAltRatio_full, symAltRatio_half), plus the identity.

Since Phi_3 = sum_i ln|lam_sym(M_i)/lam_alt(M_i)| and each M_i is a product of
such factors, Phi_3 is FORCED to be an even integer multiple of ln q.  No
enumeration of orderings, no reading of the M_i prose, and no anchor is needed
to know that.

WHAT IS MEASURED.  Every one of the 20 carried Phi_3 values is w*ln q for an
integer w, to the precision at which Phi_3 was published (6 decimals):

  the residuals are NOT noise -- they are a constant RELATIVE 1.22e-5, which is
  exactly (1.10998 - q0_proton)/q0_proton.  The producer used its own recorded
  five-decimal q.  Evaluating at that q, |w - Phi_3/ln q| <= 4.3e-6 on every
  row.  And every w is EVEN, as the derivation requires.

WHAT IS *NOT* ESTABLISHED, and must not be quoted as if it were.
A closed form w = -Z(2N - Z + 1) reproduces 18 of the 19 non-hydrogen rows
exactly.  It FAILS on Ar: recorded -498, formula -486.  Ar (Z=18, N=22) is the
ONLY row in the table with N - Z > 1 -- every other row has N = Z or N = Z + 1.
So the form was read off a sample that cannot see the (N-Z) dependence, and the
one row that tests it refutes the form.  It is recorded here as a REFUTED
candidate, not a result.  (Scope (a): this particular form fails; the existence
of a closed form is not excluded.)

H is the documented exception either way: def:atomic-braid gives hydrogen the
B_3-dressed pe crossing (q^5, -q^-5) instead of the bare Table-1 row, so its
w = +10 is outside the Table-1 accounting above.

WHAT REMAINS FOR ITEM 1.  Phi_3's quantum is settled; its integer w(Z,N) is not,
and Phi_1 and Phi_2 are untouched -- neither is quantised, so neither yields to
this argument.  The counting route is stated in the output below.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
set_compute_dps(50)

from q_parameter import Q_MP as Q_PROTON  # noqa: E402

# The producer's own recorded q, a five-decimal rounding of the pin.
Q_RECORDED = mp.mpf("1.10998")
H = Q_PROTON - 1 / Q_PROTON

TABLE1 = {
    "pp": (mp.mpf(1), mp.mpf(0)), "nn": (mp.mpf(1), -H),
    "pn": (mp.mpf(2), -H),        "pe": (mp.mpf(1), -H),
    "ne": (mp.mpf(0), mp.mpf(1)), "ee": (mp.mpf(1), mp.mpf(0)),
}

# (atom, Z, N, Phi_3) verbatim from wedderburn_mass_table_z1_20.py
ROWS = [
    ("H", 1, 0, "1.04342"),     ("He", 2, 2, "-0.626052"),
    ("Li", 3, 4, "-1.878156"),  ("Be", 4, 5, "-2.921576"),
    ("B", 5, 6, "-4.17368"),    ("C", 6, 6, "-4.382364"),
    ("N", 7, 7, "-5.843152"),   ("O", 8, 8, "-7.512624"),
    ("F", 9, 10, "-11.268936"), ("Ne", 10, 10, "-11.47762"),
    ("Na", 11, 12, "-16.068668"), ("Mg", 12, 12, "-16.277352"),
    ("Al", 13, 14, "-21.703135"), ("Si", 14, 14, "-21.911819"),
    ("P", 15, 16, "-28.172339"),  ("S", 16, 16, "-28.381023"),
    ("Cl", 17, 18, "-35.476279"), ("Ar", 18, 22, "-51.962315"),
    ("K", 19, 20, "-43.614955"),  ("Ca", 20, 20, "-43.823639"),
]


def main() -> int:
    lnq = mp.log(Q_RECORDED)
    print("=" * 78)
    print("PART 1 -- the quantum, DERIVED from Table 1 (no data used)")
    print("=" * 78)
    print(f"{'pair':>5} {'lam_sym':>14} {'lam_alt':>14} {'ratio':>13} {'units of ln q':>14}")
    print("-" * 66)
    for name, (c, d) in TABLE1.items():
        ls, la = c * Q_PROTON + d, -c / Q_PROTON + d
        r = ls / la
        u = mp.log(abs(r)) / mp.log(Q_PROTON) if abs(abs(r) - 1) > mp.mpf("1e-40") else mp.mpf(0)
        print(f"{name:>5} {mp.nstr(ls,9):>14} {mp.nstr(la,9):>14} "
              f"{mp.nstr(r,9):>13} {mp.nstr(u,4):>14}")
    print("\n  Every crossing contributes 0 or +-2 units. Phi_3 is therefore an")
    print("  EVEN integer multiple of ln q, forced -- no ordering, no reading,")
    print("  no anchor. (HeckeLinearReduction.lean, sorry-free.)")

    print("\n" + "=" * 78)
    print("PART 2 -- the integers, MEASURED against the carried values")
    print("=" * 78)
    print(f"  using the producer's own recorded q = {Q_RECORDED} "
          f"(ln q = {mp.nstr(lnq, 14)})")
    print(f"\n{'atom':>5} {'Z':>3} {'N':>3} {'N-Z':>4} {'w':>6} {'even?':>6} "
          f"{'|w - Phi3/lnq|':>15} {'-Z(2N-Z+1)':>12} {'match':>6}")
    print("-" * 74)
    worst = mp.mpf(0); ok = miss = 0; misses = []
    for el, Z, N, p3 in ROWS:
        r = mp.mpf(p3) / lnq
        w = int(mp.nint(r))
        resid = abs(r - w)
        worst = max(worst, resid)
        cand = -Z * (2 * N - Z + 1)
        hit = (w == cand)
        if el != "H":
            ok += hit
            if not hit:
                miss += 1; misses.append((el, Z, N, w, cand))
        print(f"{el:>5} {Z:>3} {N:>3} {N-Z:>4} {w:>6} "
              f"{'yes' if w % 2 == 0 else 'NO':>6} {mp.nstr(resid,6):>15} "
              f"{cand:>12} {('YES' if hit else 'no') if el != 'H' else 'n/a':>6}")

    print(f"\n  every w even: {all(int(mp.nint(mp.mpf(p)/lnq)) % 2 == 0 for _,_,_,p in ROWS)}"
          f"   worst |w - Phi3/lnq| = {mp.nstr(worst,6)}")
    print(f"\n  candidate w = -Z(2N - Z + 1): {ok} match, {miss} MISS")
    for el, Z, N, w, cand in misses:
        print(f"    {el} (Z={Z}, N={N}, N-Z={N-Z}): recorded {w}, formula {cand}")
    print("  Ar is the ONLY row with N-Z > 1. The candidate was read off a sample")
    print("  that cannot see the (N-Z) dependence, and the single row testing it")
    print("  refutes it. REFUTED CANDIDATE, not a result -- do not quote it.")

    print("\n" + "=" * 78)
    print("WHERE ITEM 1 STANDS")
    print("=" * 78)
    print("  Phi_3 quantum ............ DERIVED (Lean, sorry-free)")
    print("  Phi_3 integer w(Z,N) ..... OPEN -- one candidate refuted by Ar")
    print("  Phi_1, Phi_2 ............. UNTOUCHED; neither is quantised, so this")
    print("                             argument does not reach them")
    print("\n  Next step for w, and it needs no new mathematics: w = 2*sum_j m_j*s_j")
    print("  where s_j is the crossing sign above and m_j is how many chains M_i")
    print("  contain crossing j. Under the suffix reading m_j = j. So w is a")
    print("  POSITION-WEIGHTED crossing count, and finding it is a question about")
    print("  the ground-state ORDERING -- which def:atomic-braid defines by an")
    print("  exponential minimisation this arc has already flagged as intractable")
    print("  as written. That is the actual obstacle, and it is a known one.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
