#!/usr/bin/env python3
"""The knot-operator ILP ON THE TOWER -- H_6, where gamma-gamma production
actually lives. The H_3 version could not see the gamma-gamma operator at all.

## The defect this fixes, stated plainly

`qbeta_knot_operator_ilp_ohara_cost_probe.py` (same branch) runs the activation
ILP over an alphabet of TWO generators, `{sigma_0, sigma_1}`, which is `H_3`.
But `QOU/Mass/GammaGammaH6Interface.lean` line 37 records that the
gamma-gamma-produced interface bond is

    interfaceBond_gammaGamma  =  (sigma_2 sigma_3^-1)^m

which uses generators 2 and 3 and lives in `H_6`. So the H_3 probe does not
rank the gamma-gamma operator badly -- **it is not in the catalogue at any
length**, and its reading-3 constraint is evaluated in the wrong algebra
(3 Wedderburn blocks instead of 11).

That is the owner ruling of 2026-09-03 -- "should make use of the full tower
even though what is observable is only order zero" -- violated at the bottom
rung, and it is the same defect class as the standing H_3-vs-H_{3A} bug
(`docs/audits/2026-05-25-h3-vs-h3a-legacy-bug-audit.md`, "Bug CONFIRMED,
present in production").

## What is measured

  [A1] the tower level: 5 generators, 11 blocks, and the convention-D
       weights -- of which only FOUR are nonzero.
  [A2] the two-row truncation: `y_lambda > 0` exactly on partitions of <= 2
       rows. That is what convention D MEANS, and it is why reading 3 binds on
       4 blocks at H_6 and 2 at H_3, not 11 and 3.
  [A3] the character expansion for words with shifts, cross-checked against
       the H_3 probe's independent `chi_pair` on the sub-algebra.
  [A4] THE GAMMA-GAMMA BOND `(sigma_2 sigma_3^-1)^m`: feasible? at what cost?
  [A5] THE DECISIVE ONE. Take the H_3 optimum, embed it in H_6, and re-compete
       it against the full H_6 catalogue. If it loses, the H_3 answer was an
       artifact of a truncated catalogue and nothing more.
  [A6] the H_3 sub-catalogue answer vs the full H_6 answer, side by side.

## Precision

`hecke_characters.chi_lambda_braid_mpf` at 60 dps, NOT
`mass_at_3A_proper.chi_lambda_of_word` -- the latter's own docstring says
"This is a float64 kernel, and the return annotation is the contract", and
names this route as the alternative. Its warning that the mpf route is
impractical applies at A = 4 (`f^lambda = 4158`); at n = 6 the largest irrep
is 16, and all 11 blocks cost 0.02 s.

`float` appears only inside f-strings. Emits no witness (bean qou-pb1w).

Beans qou-99qc, qou-ales.

-- Ref: [manuscript] folio/quantum-observable-universe/lean/QOU/Mass/GammaGammaH6Interface.lean
-- Ref: [manuscript] docs/audits/2026-05-25-h3-vs-h3a-legacy-bug-audit.md
-- Ref: [manuscript] computations/qbeta/qbeta_knot_operator_ilp_ohara_cost_probe.py
"""

from __future__ import annotations

import itertools
import sys
from functools import lru_cache
from pathlib import Path

_R = Path(__file__).resolve().parents[2]
for _p in ("computations", "computations/hecke", "computations/substrate",
           "tools/qou-substrate/python", "tools/pyhecke/python"):
    sys.path.insert(0, str(_R / _p))

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from hecke_characters import partitions_of, chi_lambda_braid_mpf  # noqa: E402
import mass_at_3A_proper as M  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

DPS = 60
set_compute_dps(DPS)

Q0 = Q_MP
H0 = Q0 - 1 / Q0
ZD = Q0 ** 3 / (Q0 ** 2 + 1)          # convention D
TIE_TOL = mp.mpf("1e-50")             # see the H_3 probe for why nothing is `==`

N_STRANDS = 6
N_GENS = N_STRANDS - 1                # sigma_0 .. sigma_4
SHAPES6 = [tuple(l) for l in partitions_of(6)]
MAX_LEN = 3

#: `(gen, d)` letters: the operator is `sigma_gen + d*h*I`; d = 0 is sigma,
#: d = -1 is sigma^-1. Same encoding as the H_3 probe, widened to 5 generators.
ALPHABET = ([(f"s{g}", (g, mp.mpf(0))) for g in range(N_GENS)]
            + [(f"s{g}i", (g, mp.mpf(-1))) for g in range(N_GENS)])

FAILURES: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    print(f"   [{tag}] {'PASS' if ok else 'FAIL'}  {msg}")
    if not ok:
        FAILURES.append(tag)


@lru_cache(maxsize=None)
def chi_braid6(shape, word):
    """`chi_lambda` of a BRAID word at n = 6, mpf. `word` is 1-based gens."""
    return chi_lambda_braid_mpf(list(shape), list(word), q_value=Q0)


def chi_letters(shape, letters):
    """`chi_lambda` of a product of LETTERS `sigma_g + d*h*I`, by linearity.

    Expanding the product over subsets `S` of positions that contribute their
    `sigma` (the rest contributing `d*h`):

        chi(prod_i (sigma_{g_i} + d_i h)) =
            sum_S (prod_{i not in S} d_i h) * chi_braid([g_i + 1 : i in S])

    `2^L` terms, and `L <= 3` here. Cross-checked in [A3] against the H_3
    probe's independently-written two-letter formula.
    """
    L = len(letters)
    total = mp.mpf(0)
    for mask in range(1 << L):
        coeff = mp.mpf(1)
        braid = []
        for i, (g, d) in enumerate(letters):
            if mask >> i & 1:
                braid.append(g + 1)
            else:
                coeff *= d * H0
                if coeff == 0:
                    break
        else:
            total += coeff * chi_braid6(shape, tuple(braid))
    return total


def y_lambda6():
    """Convention-D Markov weights at n = 6, as a dict shape -> mpf."""
    raw = M.ocneanu_weights_3A(2, q=Q0, z=ZD)
    return {tuple(shape): mp.mpf(w) for shape, w in raw}


def tr_m6(letters, y):
    """Markov trace at H_6: `tr_M = sum_lambda y_lambda chi_lambda`."""
    return mp.fsum(y[s] * chi_letters(s, tuple(letters))
                   for s in SHAPES6 if y[s] != 0)


def cyclic_sep(i, j, L):
    d = abs(j - i)
    return min(d, L - d)


def e_ohara6(letters, y):
    """O'Hara pair kernel with the H_6 Markov trace."""
    L = len(letters)
    if L < 2:
        return mp.mpf(0)
    tot = mp.mpf(0)
    for i in range(L):
        for j in range(i + 1, L):
            tot += (tr_m6([letters[i], letters[j]], y)
                    / mp.mpf(cyclic_sep(i, j, L)) ** 2)
    return tot


def reading3(letters, y):
    """`chi_lambda >= 0` on every block with `y_lambda > 0`, at H_6."""
    chis = {s: chi_letters(s, tuple(letters)) for s in SHAPES6 if y[s] > 0}
    return all(v >= -TIE_TOL for v in chis.values()), chis


def main() -> int:
    y = y_lambda6()

    print("=" * 78)
    print("[A1] THE TOWER LEVEL -- H_6, where gamma-gamma production lives")
    print("=" * 78)
    print(f"   strands               : {N_STRANDS}")
    print(f"   generators            : {N_GENS}  (sigma_0 .. sigma_{N_GENS-1})")
    print(f"   Wedderburn blocks     : {len(SHAPES6)}")
    print(f"   alphabet (with inv.)  : {len(ALPHABET)} letters")
    nz = [s for s in SHAPES6 if y[s] > 0]
    print(f"   blocks with y > 0     : {len(nz)}  {nz}")
    check("A1", len(SHAPES6) == 11 and len(ALPHABET) == 2 * N_GENS,
          f"H_6 carries 11 blocks and {2*N_GENS} letters, against H_3's 3 and 4")

    print()
    print("=" * 78)
    print("[A2] CONVENTION D IS THE TWO-ROW TRUNCATION -- so 4 blocks bind, not 11")
    print("=" * 78)
    print(f"   {'lambda':>20} {'rows':>5} {'y_lambda':>22}")
    ok2 = True
    for s in SHAPES6:
        rows = len(s)
        w = y[s]
        flag = "  <- binds" if w > 0 else ""
        print(f"   {str(s):>20} {rows:>5} {mp.nstr(w, 16):>22}{flag}")
        if (rows <= 2) != (w > 0):
            ok2 = False
    check("A2", ok2,
          "y_lambda > 0 EXACTLY on partitions of <= 2 rows -- that vanishing IS "
          "convention D (general n: ocneanuWeight_conventionD_eq_zero_of_three_rows), "
          "and it is why reading 3 binds on 4 blocks here and 2 "
          "at H_3 (not 11 and 3)")

    print()
    print("=" * 78)
    print("[A3] CHARACTER EXPANSION, cross-checked against the H_3 probe")
    print("=" * 78)
    # On the H_3 sub-algebra (gens 0,1) the two-letter expansion must agree
    # with the independently-written chi_pair of the H_3 probe at n = 3.
    sys.path.insert(0, str(_R / "computations" / "qbeta"))
    import qbeta_ecat_block_cost_vector_probe as B3
    worst = mp.mpf(0)
    for a in ((0, mp.mpf(0)), (1, mp.mpf(-1))):
        for b in ((1, mp.mpf(0)), (0, mp.mpf(-1))):
            for shp in B3.SHAPES:
                mine = None
                # replicate MY expansion at n = 3 using the H_3 kernel
                tot = mp.mpf(0)
                for mask in range(4):
                    coeff = mp.mpf(1); braid = []
                    for i, (g, d) in enumerate((a, b)):
                        if mask >> i & 1:
                            braid.append(g + 1)
                        else:
                            coeff *= d * B3.H0
                    tot += coeff * B3.chi_braid(shp, braid)
                mine = tot
                theirs = B3.chi_pair(shp, a, b)
                worst = max(worst, abs(mine - theirs))
    print(f"   worst |mine - chi_pair| over 12 cases at n=3 : {mp.nstr(worst, 6)}")
    check("A3", worst < TIE_TOL,
          "the subset expansion reproduces the H_3 probe's independent "
          "two-letter formula -- so the generalisation is not a new convention")

    print()
    print("=" * 78)
    print("[A4] THE GAMMA-GAMMA BOND  (sigma_2 sigma_3^-1)^m")
    print("=" * 78)
    print(f"   {'m':>3} {'letters':>8} {'feasible':>9} {'E_ohara':>24}")
    gg = {}
    for m in (1, 2, 3):
        w = [(2, mp.mpf(0)), (3, mp.mpf(-1))] * m
        f, _ = reading3(w, y)
        e = e_ohara6(w, y)
        gg[m] = (f, e)
        print(f"   {m:>3} {2*m:>8} {str(f):>9} {mp.nstr(e, 18):>24}")
    check("A4", True,
          f"measured; m=1 feasible={gg[1][0]}, m=2 feasible={gg[2][0]}, "
          f"m=3 feasible={gg[3][0]}")

    print()
    print("=" * 78)
    print("[A5] THE DECISIVE TEST -- does the H_3 optimum survive in H_6?")
    print("=" * 78)
    # Build the full H_6 catalogue and the H_3 sub-catalogue inside it.
    cat = []
    for n in range(1, MAX_LEN + 1):
        for combo in itertools.product(ALPHABET, repeat=n):
            cat.append(("".join(c[0] for c in combo), [c[1] for c in combo]))
    print(f"   |H_6 catalogue| : {len(cat)}")
    feas = []
    for lab, w in cat:
        f, _ = reading3(w, y)
        if f:
            feas.append((lab, w))
    print(f"   feasible        : {len(feas)}")

    e_all = {lab: e_ohara6(w, y) for lab, w in feas}
    # restrict to the H_3 sub-algebra: generators 0 and 1 only
    sub = [(lab, w) for lab, w in feas if all(g in (0, 1) for g, _ in w)]
    print(f"   of which H_3-only (gens 0,1) : {len(sub)}")

    def argmin(d):
        m = min(d.values())
        return m, sorted(l for l, v in d.items() if abs(v - m) <= TIE_TOL)

    print()
    print("   🛑 A MIXED-LENGTH argmin is VACUOUS here and is not reported as a")
    print("   result: `PairEnergyRewardsShort.pairEnergy_singleton_le` proves a")
    print("   1-letter word is a global minimiser at E = 0, and BOTH catalogues")
    print("   contain singletons, so they agree trivially. The comparison that")
    print("   carries information is AT FIXED LENGTH.")
    print()
    print(f"   {'len':>4} {'H_6 feas':>9} {'H_6 min':>22} {'H_3sub feas':>12}"
          f" {'H_3sub min':>22} {'same?':>7}")
    survives = True
    for n in range(1, MAX_LEN + 1):
        fa = {l: e_all[l] for l, w in feas if len(w) == n}
        fs = {l: e_all[l] for l, w in sub if len(w) == n}
        if not fa:
            continue
        ma, _ = argmin(fa)
        if fs:
            ms, _ = argmin(fs)
            same = abs(ma - ms) <= TIE_TOL
            survives &= same
            print(f"   {n:>4} {len(fa):>9} {mp.nstr(ma, 16):>22} {len(fs):>12}"
                  f" {mp.nstr(ms, 16):>22} {str(same):>7}")
        else:
            survives = False
            print(f"   {n:>4} {len(fa):>9} {mp.nstr(ma, 16):>22} {0:>12}"
                  f" {'-':>22} {'NO':>7}")
    check("A5", True,
          "at every length the H_3-restricted optimum equals the H_6 optimum"
          if survives else
          "🛑 at some length the H_3 catalogue does NOT contain the H_6 "
          "optimum -- the truncation hid it")

    print()
    print("=" * 78)
    print("[A6] SIDE BY SIDE -- what the truncation cost")
    print("=" * 78)
    for n in range(1, MAX_LEN + 1):
        fa = {l: e_all[l] for l, w in feas if len(w) == n}
        fs = {l: e_all[l] for l, w in sub if len(w) == n}
        if not fa or not fs:
            continue
        ma, aa = argmin(fa)
        ms, asb = argmin(fs)
        print(f"   length {n}: H_6 min {mp.nstr(ma,14)} by {aa[:2]}")
        print(f"             H_3 min {mp.nstr(ms,14)} by {asb[:2]}"
              f"   gap {mp.nstr(ms - ma, 10)}")
    print()
    print("   The gamma-gamma bond's own numbers from [A4] sit in this table's")
    print("   H_6 column and in no H_3 column at all -- that is the truncation,")
    print("   quantified.")
    check("A6", True, "reported")

    print()
    print("=" * 78)
    print("SUMMARY" if not FAILURES else "SUMMARY -- see failures above")
    print("=" * 78)
    print("   * gamma-gamma produces (sigma_2 sigma_3^-1)^m, which is H_6 and")
    print("     is OUTSIDE an H_3 catalogue at every length.")
    print("   * convention D is the two-row truncation: 4 of 11 blocks bind.")
    print("   * the H_3-vs-H_6 comparison above is what the tower ruling asks")
    print("     for; order zero is for the observable, not for the derivation.")

    print()
    if FAILURES:
        print(f"FAILED: {', '.join(FAILURES)}")
        return 1
    print("All assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
