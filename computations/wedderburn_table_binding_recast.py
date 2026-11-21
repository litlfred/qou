#!/usr/bin/env python3
"""The published mass table's error column measures the INPUTS, not the prediction.

tbl:mass-table-z1-20-table-data reports Delta/m -- the error as a fraction of
the TOTAL atomic mass.  But thm:wedderburn-mass-formula is

    m(Z,N) = Z*m_p + N*m_n + Z*m_e + alpha*( Phi_1 - 2[3]_q Phi_2 + h_A^2 Phi_3 )

and the first three terms are INPUTS (the absolute-mass excision, owner ruling
2026-08-11: the framework does not claim absolute nucleon mass).  The entire
predictive content is the correction term, whose job is to equal -B_total.
Since the base is ~99.8 % of the mass, Delta/m divides the error by the inputs.
This script divides it by the prediction instead.

It also asks whether the M_i constructor
(computations/wedderburn_Mi_constructor_test.py) reproduces the published rows.

TWO MEASUREMENTS, both reported.  Neither is a closure attempt.

PROVENANCE OF THE PUBLISHED TABLE -- read before drawing any conclusion from
a disagreement with it.  mass-table-z1-20.md states its own backing witness
`atom-mass-complete-wedderburn` is absent from the tree, which is true.

CORRECTED 2026-08-25: this docstring previously went further and said the
witness "never existed in git history".  THAT IS FALSE.  It was added
2026-04-10 in commit 1359fe23ac at
folio-assistant/computations/atom-mass-complete-wedderburn.witness.json and
left the tree with the platform code in the miga migration.  Retrieve it:
  git show 1359fe23ac:folio-assistant/computations/atom-mass-complete-wedderburn.witness.json

Recovered, it reproduces the published table exactly (all 20 rows, mean
0.074 pct) -- so the table DOES have a producer.  But its own parameter block
does not match the published formula: beta3 = 0.0499 against h_A^2 =
0.0437073 (a 14.2 pct departure, with "fitted": 0 recorded beside it), and the
nucleon masses fed in are not CODATA (-44 and -36 ppm).  So a constructor
disagreeing with the table is still not thereby refuted -- the table was
produced by a computation that DIFFERS FROM THE FORMULA AS PUBLISHED.
Full account: docs/audits/2026-08-25-atom-mass-complete-wedderburn-witness-recovered.md.

H-1 CAVEAT.  The published masses carry 3 decimals (+/- 0.5 keV) while
hydrogen's binding is 13.598 eV -- 37x finer.  A binding read off that column
is rounding, not physics.  The H-1 row therefore uses the CODATA ionization
energy, and the table-derived value is shown alongside to make the gap visible.
"""
from __future__ import annotations

import sys
from pathlib import Path
from math import comb

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
set_compute_dps(50)

sys.path.insert(0, str(Path(__file__).resolve().parent / "alpha"))
from experimental_constants import M_P_MEV, M_N_MEV, M_E_MEV  # noqa: E402
from alpha_blend_tower import (  # noqa: E402
    ALPHA_CANONICAL, BRACKET_3Q, H_A, Phi_1, Phi_2, Phi_3,
)
from wedderburn_Mi_constructor_test import chains_for, orderings  # noqa: E402
from codata_constants import M_C12_ATOMIC_MEV_VALIDATION, M_HE4_ATOMIC_MEV_VALIDATION  # noqa: E402  (AME registry)
from mpmath import nstr as _ame_nstr  # noqa: E402  (AME registry, string form)

MP_, MN_, ME_ = (mp.mpf(str(x)) for x in (M_P_MEV, M_N_MEV, M_E_MEV))

# CODATA hydrogen ionization energy, MeV -- the H-1 binding the published
# 3-decimal mass column cannot resolve.
H1_BINDING_MEV = mp.mpf("13.598434599702") * mp.mpf("1e-6")

# (Z, element, A, m_pred, m_obs) verbatim from tbl:mass-table-z1-20-table-data
ROWS = [
    (1, "H", 1, "938.910", "938.783"),      (2, "He", 4, "3734.624", _ame_nstr(M_HE4_ATOMIC_MEV_VALIDATION, 30)),
    (3, "Li", 7, "6534.188", "6535.367"),   (4, "Be", 9, "8378.704", "8394.794"),
    (5, "B", 11, "10237.301", "10255.103"), (6, "C", 12, "11168.874", _ame_nstr(M_C12_ATOMIC_MEV_VALIDATION, 30)),
    (7, "N", 14, "13029.983", "13043.782"), (8, "O", 16, "14890.701", "14899.169"),
    (9, "F", 19, "17690.792", "17696.901"), (10, "Ne", 20, "18615.219", "18622.835"),
    (11, "Na", 23, "21418.256", "21414.830"), (12, "Mg", 24, "22342.658", "22341.908"),
    (13, "Al", 27, "25143.149", "25133.143"), (14, "Si", 28, "26067.918", "26060.344"),
    (15, "P", 31, "28872.696", "28851.873"), (16, "S", 32, "29797.187", "29781.800"),
    (17, "Cl", 35, "32597.913", "32573.283"), (18, "Ar", 40, "37273.796", "37224.719"),
    (19, "K", 39, "36324.625", "36294.464"), (20, "Ca", 40, "37248.739", "37213.777"),
]

# The ground-state rule ("minimize Phi_1 over all permutations") is exponential
# in A -- C(40,20) is 1.4e11 for Ca.  Cap the enumeration and REPORT what was
# dropped; a silent cap reads as "covered everything".
MAX_ORDERINGS = 1000


def base_mass(Z, N):
    return Z * MP_ + N * MN_ + Z * ME_


def part1_recast():
    print("=" * 92)
    print("PART 1 -- the published table, re-scored on what the formula predicts")
    print("=" * 92)
    print(f"{'atom':>7} {'Delta MeV':>10} {'Delta/m':>10} | {'B_total':>10} "
          f"{'Delta/B':>11} {'pred/true corr':>15}")
    print("-" * 92)
    for Z, el, A, mpred, mobs in ROWS:
        N = A - Z
        pred, obs = mp.mpf(mpred), mp.mpf(mobs)
        base = base_mass(Z, N)
        B = H1_BINDING_MEV if A == 1 else base - obs
        delta = pred - obs
        corr_pub = pred - base
        tag = " *" if A == 1 else ""
        print(f"{el + '-' + str(A):>7} {mp.nstr(delta, 6):>10} "
              f"{mp.nstr(delta / obs * 100, 4) + '%':>10} | {mp.nstr(B, 6):>10} "
              f"{mp.nstr(delta / B * 100, 5) + '%':>11} "
              f"{mp.nstr(corr_pub / (-B), 6):>15}{tag}")
    b_tab = base_mass(1, 0) - mp.mpf("938.783")
    print(f"\n  * H-1 uses the CODATA binding {mp.nstr(H1_BINDING_MEV, 8)} MeV "
          f"(13.598 eV).")
    print(f"    The table's own column implies {mp.nstr(b_tab, 6)} MeV -- "
          f"{mp.nstr(b_tab / H1_BINDING_MEV, 4)}x too large,")
    print("    because 3 published decimals cannot resolve a 13.6 eV binding.")
    print("\n  READING: Delta/m spans 0.003 % to 0.19 % and looks excellent.")
    print("  The same rows scored on the binding -- the only thing predicted --")
    print("  span 0.4 % to 28 %, and H-1, the BEST-looking row at +0.014 %, is")
    print("  the correction with the WRONG SIGN and ~9300x the magnitude.")
    print("  The metric divides the error by the inputs.")


def part2_constructor():
    print("\n" + "=" * 92)
    print("PART 2 -- does the M_i constructor reproduce those published rows?")
    print("=" * 92)
    print(f"{'atom':>7} {'n':>4} {'orderings':>10} | {'mine':>12} {'published':>12} "
          f"{'true':>12} | {'mine/true':>10} {'pub/true':>9}")
    print("-" * 92)
    skipped = []
    for Z, el, A, mpred, mobs in ROWS:
        N, n = A - Z, A + Z
        nperm = comb(A, Z)
        if nperm > MAX_ORDERINGS:
            skipped.append((el, A, nperm))
            continue
        base = base_mass(Z, N)
        B = H1_BINDING_MEV if A == 1 else base - mp.mpf(mobs)
        corr_true, corr_pub = -B, mp.mpf(mpred) - base
        best = None
        for strands in orderings(Z, N):
            chains = chains_for(list(strands), "suffix-inclusive")
            p1 = Phi_1(chains)
            if best is None or p1 < best[1]:
                best = (chains, p1)
        chains, p1 = best
        corr_mine = ALPHA_CANONICAL * (
            p1 - 2 * BRACKET_3Q * Phi_2(chains) + H_A ** 2 * Phi_3(chains))
        print(f"{el + '-' + str(A):>7} {n:>4} {nperm:>10} | "
              f"{mp.nstr(corr_mine, 8):>12} {mp.nstr(corr_pub, 8):>12} "
              f"{mp.nstr(corr_true, 8):>12} | "
              f"{mp.nstr(corr_mine / corr_true, 6):>10} "
              f"{mp.nstr(corr_pub / corr_true, 6):>9}")
    print(f"\n  DROPPED (enumeration cap {MAX_ORDERINGS}; the ground-state rule is")
    print("  exponential in A, which is itself a defect in def:atomic-braid):")
    for el, A, nperm in skipped:
        print(f"    {el}-{A}: {nperm} orderings")
    print("\n  H-1 is additionally NOT a fair test: def:atomic-braid gives hydrogen")
    print("  a special rule (pe uses B_3-dressed eigenvalues (q^5, -q^-5), not the")
    print("  bare Table-1 row). The generic constructor does not implement it.")
    print("\n  READING: the constructor does not reproduce the published table at")
    print("  ANY atom -- mine/true swings over four orders of magnitude while")
    print("  pub/true sits in a smooth 0.78-1.28 band. Per the provenance note in")
    print("  this file's docstring, that does NOT refute the constructor: the")
    print("  published numbers come from a witness that was RECOVERED "
          "(1359fe23ac)")
    print("  and whose own beta3 = 0.0499 does not match the published "
          "h_A^2 = 0.0437073.")


def main() -> int:
    part1_recast()
    part2_constructor()
    print("\n" + "=" * 92)
    print("WHAT THIS DOES NOT DO: propose a correction, a closure, or a seventh")
    print("Delta_lambda ansatz. Both parts are measurements of existing artifacts.")
    print("=" * 92)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
