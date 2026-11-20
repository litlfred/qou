#!/usr/bin/env python3
"""The flavour-split baseline IS the Markov trace of the crossing reversal — at the AUGMENTATION.

WHAT THIS ESTABLISHES
---------------------
`conj:flavor-split-habiro-derivation` carries the nucleon flavour split in two
sections that do not connect.

  * Its NARRATIVE half computes the crossing reversal at k = 3,
    `sigma^3 - sigma^-3 = 3h + h^3 = q^3 - q^-3`, and concludes "the bare
    topological difference is thus a central scalar: the chiral sigma_1 terms
    cancel identically".  That is correct, and it is the odd case of
    `QOU.Hecke.CrossingReversalParity.reversal_rec`.

  * Its FORMULA half displays `X_baseline = (q-1)^2 (1 - q^-4)/3`, which is
    `hbar_q^2 (q^2 - q^-2)/3` -- the reversal at k = 2.

Section 1 below measures that gap: the two are different objects, off by 51.17 %
against the measured split, related by a factor
`(q^2-q+1)(q^2+q+1)/(q(q^2+1)) = 1.5136` that the block neither states nor
derives.  So the quantity the block ACTUALLY uses sits at k = 2, where the
reversal is NOT central -- `sigma^2 - sigma^-2 = h(sigma + sigma^-1)` -- and
therefore needs a channel or a trace to become a number.

This probe does the trace.  The Markov trace is fixed on this element by two
facts alone, `tr(1) = 1` and `tr(sigma) = z`:

    tr_z(sigma^2 - sigma^-2)  =  2 h z - h^2  =  h * (b_pp + b_nn)

with `b_pp = z`, `b_nn = z - h` the corpus's own like-pair bond letters
(`QOU.Hecke.BondLetterIdentification.tr_bond_interp` at t = 0 and t = 1).
Evaluated at the two admissible Markov parameters of bean `qou-99qc`:

    augmentation  z = q                ->  q^2 - q^-2          EXACTLY
    convention D  z_D = q^3/(q^2+1)    ->  alpha * (q^2 - q^-2)

with `alpha = (q^4+1)/(q^2+1)^2`, and `1/2 < alpha < 1` strictly for every
q > 1.  So `hbar_q^2 tr_z(...)/3` reproduces the block's displayed baseline
EXACTLY at the augmentation, and `alpha` times it (0.5054 x, i.e. barely more
than half) at the canonical convention-D parameter.

`alpha` IS NOT A NEW CONSTANT.  It is the same alpha AGENTS.md records in the
2026-09-08 Q_beta ruling -- "the augmentation cell ... is proportional to z_D's
(alpha = (q^4+1)/(q^2+1)^2)".  The same two Markov parameters, the same ratio
between them, in a second observable.  Section 5 checks that it is literally the
same rational function and not a coincidence of shape.

WHAT IS *NOT* ESTABLISHED -- read this before quoting the exactness
------------------------------------------------------------------
That the flavour split IS `hbar_q^2 tr_z(sigma^2 - sigma^-2)/3` for any z is NOT
derived.  The prefactor `hbar_q^2/3` is the block's, is unexplained there, and is
unexplained here.  What is established is that GIVEN that shape, the Markov
parameter is pinned -- and pinned to the augmentation, not to the canonical z_D.

DO NOT READ THE EXACTNESS AS EVIDENCE FOR THE AUGMENTATION.  AGENTS.md
"NO FITTING, EXCEPT CAL-1/2/3" is explicit that choosing a branch because it
reproduces the measured value is fitting even with no continuous parameter, and
that accuracy is never a tie-breaker.  The content here is the FORK and its exact
size: under the owner-ruled z_D this construction predicts a model flavour split
of `alpha * X_baseline`, i.e. 49.5 % LOW against the measurement.  That is a
falsifiable consequence of the ruling, not an argument against it.

A FRAMING OF MY OWN THAT THIS RETRACTS
--------------------------------------
PR #7320 said the conjecture's OWN stated channel gives the flavour split the
wrong sign, reading "the weak interaction is strictly left-handed, so it projects
onto the fully alternating channel" as a claim about the split.  That conflated
the block's two LEVELS: the alternating channel is claimed there for the
RESIDUAL -- the ~1.76e-6, 0.128 % Schwinger-analogue refinement on top of the
baseline -- not for the baseline.  The mathematics of #7320 is untouched
(sections 6-7 below use it); only that interpretive sentence was wrong, and it is
corrected in `crossing_reversal_parity_probe.py` and in
`QOU/Hecke/CrossingReversalParity.lean` in the same commit.

Lean: `QOU/Hecke/MarkovCrossingReversal.lean` (12 decls, lean-direct exit 0,
#print axioms clean on all of them).

Run: python3 computations/qbeta/flavour_split_baseline_is_augmentation_trace_probe.py
"""

from __future__ import annotations

import sys

import sympy as sp
from mpmath import mp

mp.dps = 60

_q = sp.symbols("q", positive=True)

H = _q - 1 / _q
HBAR = 1 - 1 / _q
Z_D = _q**3 / (_q**2 + 1)
Z_AUG = _q

SYM = _q**2 - _q**-2                       # the k = 2 reversal's symmetric value
K3 = _q**3 - _q**-3                        # the block's narrative k = 3 value
X_BASELINE = (_q - 1) ** 2 * (1 - _q**-4) / 3
ALPHA = (_q**4 + 1) / (_q**2 + 1) ** 2

# n-p mass ratio, CODATA 2022; delta = 2(r-1)/(r+1) is the MEAN-normalised split
TARGET = sp.Rational("1.00137841917")
TARGET_DELTA = 2 * (TARGET - 1) / (TARGET + 1)


def R(z):
    """tr_z(sigma^2 - sigma^-2), from tr(1) = 1 and tr(sigma) = z alone."""
    return 2 * H * z - H**2


def _n(expr, q0, digits=45):
    return mp.mpf(str(sp.N(expr.subs(_q, sp.Float(str(q0), 50)), digits)))


def main() -> int:
    ok = True

    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP      # noqa: PLC0415
    q0 = Q_MP
    tgt = _n(TARGET_DELTA, q0)

    print("1. THE BLOCK'S TWO HALVES ARE DIFFERENT OBJECTS  (k = 3 narrative vs k = 2 formula)")
    is_k2 = sp.simplify(X_BASELINE - HBAR**2 * SYM / 3) == 0
    is_k3 = sp.simplify(X_BASELINE - HBAR**2 * K3 / 3) == 0
    ok &= is_k2 and not is_k3
    print(f"   X_baseline == hbar^2 (q^2-q^-2)/3   [k=2] : {is_k2}")
    print(f"   X_baseline == hbar^2 (q^3-q^-3)/3   [k=3] : {is_k3}")
    v2, v3 = _n(HBAR**2 * SYM / 3, q0), _n(HBAR**2 * K3 / 3, q0)
    print(f"   k=2 value = {mp.nstr(v2, 14)}   rel to measured split "
          f"{mp.nstr((v2 - tgt) / tgt, 6)}")
    print(f"   k=3 value = {mp.nstr(v3, 14)}   rel to measured split "
          f"{mp.nstr((v3 - tgt) / tgt, 6)}")
    ratio = sp.factor(sp.simplify(K3 / SYM))
    print(f"   k3/k2 = {ratio} = {mp.nstr(_n(K3 / SYM, q0), 12)}  "
          f"-- neither stated nor derived in the block")

    print()
    print("2. AT k = 2 THE REVERSAL IS NOT CENTRAL, SO IT NEEDS A TRACE")
    print("   sigma^2 - sigma^-2 = h (sigma + sigma^-1) = 2 h sigma - h^2")
    print("   (QOU.Hecke.CrossingReversalParity.reversal_two, merged, sorry-free)")
    print("   tr(1) = 1, tr(sigma) = z   =>   tr_z = 2 h z - h^2")
    bond_form = sp.simplify(R(Z_D) - H * (Z_D + (Z_D - H)))
    ok &= bond_form == 0
    print(f"   tr_z == h*(b_pp + b_nn), b_pp = z, b_nn = z-h : {bond_form == 0}  "
          f"(the corpus's own like-pair letters)")

    print()
    print("3. THE AUGMENTATION z = q REPRODUCES THE BASELINE EXACTLY")
    aug = sp.simplify(R(Z_AUG) - SYM)
    aug_x = sp.simplify(HBAR**2 * R(Z_AUG) / 3 - X_BASELINE)
    ok &= aug == 0 and aug_x == 0
    print(f"   tr_q(sigma^2-sigma^-2) - (q^2-q^-2)      = {aug}   "
          f"{'EXACT' if aug == 0 else 'MISMATCH'}")
    print(f"   hbar^2 tr_q(...)/3 - X_baseline          = {aug_x}   "
          f"{'EXACT' if aug_x == 0 else 'MISMATCH'}")

    print()
    print("4. AT CONVENTION D THE SAME CONSTRUCTION GIVES alpha TIMES THE BASELINE")
    zd = sp.simplify(R(Z_D) - ALPHA * SYM)
    zd_x = sp.simplify(HBAR**2 * R(Z_D) / 3 - ALPHA * X_BASELINE)
    ok &= zd == 0 and zd_x == 0
    print(f"   tr_zD(sigma^2-sigma^-2) - alpha(q^2-q^-2) = {zd}   "
          f"{'EXACT' if zd == 0 else 'MISMATCH'}")
    print(f"   hbar^2 tr_zD(...)/3 - alpha*X_baseline   = {zd_x}   "
          f"{'EXACT' if zd_x == 0 else 'MISMATCH'}")
    a0 = _n(ALPHA, q0)
    print(f"   alpha(q0) = {mp.nstr(a0, 14)}     1/2 < alpha < 1 for every q > 1")
    lo = sp.factor(sp.simplify(ALPHA - sp.Rational(1, 2)))
    hi = sp.factor(sp.simplify(1 - ALPHA))
    print(f"   alpha - 1/2 = {lo}   (>0 for q != 1)")
    print(f"   1 - alpha   = {hi}   (>0 for q != 0)")

    print()
    print("5. alpha IS THE SAME alpha AS THE 2026-09-08 Q_beta RULING")
    print("   AGENTS.md: 'the augmentation cell ... is proportional to z_D's")
    print("              (alpha = (q^4+1)/(q^2+1)^2)'")
    same = sp.simplify(ALPHA - (_q**4 + 1) / (_q**2 + 1) ** 2) == 0
    ok &= same
    print(f"   identical rational function : {same}")
    print("   -> the SAME two Markov parameters and the SAME ratio, in a second")
    print("      observable.  The Q_beta half of the fork is bean qou-99qc.")

    print()
    print("6. THE SYM/ALT CHANNEL AVERAGE VANISHES  (w_sym = w_alt, audit 2026-06-17)")
    w_sym = _q**2 / (_q**4 + 4 * _q**2 + 1)
    w_alt = _q**2 / (_q**4 + 4 * _q**2 + 1)
    w_std = (_q**2 + 1) ** 2 / (_q**4 + 4 * _q**2 + 1)
    eq_w = sp.simplify(w_sym - w_alt) == 0
    sums1 = sp.simplify(w_sym + w_std + w_alt) == 1
    cancel = sp.simplify(w_sym * SYM + w_alt * (-SYM)) == 0
    ok &= eq_w and sums1 and cancel
    print(f"   w_sym == w_alt                       : {eq_w}")
    print(f"   w_sym + w_std + w_alt == 1           : {sums1}")
    print(f"   w_sym*(q^2-q^-2) + w_alt*(q^-2-q^2)  = 0 : {cancel}")
    print("   -> the split cannot be a sym/alt-weighted average under equal")
    print("      weights.  Scope (b) for THAT reading only; says nothing about")
    print("      the standard channel or about unequal weights.")

    print()
    print("7. THE THREE CANDIDATE NUMBERS, SIDE BY SIDE  (mpmath, dps=60)")
    rows = [
        ("augmentation  z = q", HBAR**2 * R(Z_AUG) / 3),
        ("convention D  z = z_D", HBAR**2 * R(Z_D) / 3),
        ("alternating channel", -HBAR**2 * SYM / 3),
        ("sym/alt equal-weight avg", sp.Integer(0)),
    ]
    print(f"   measured split (CODATA 2022 n/p ratio) = {mp.nstr(tgt, 14)}")
    for lbl, e in rows:
        v = _n(e, q0) if e != 0 else mp.mpf(0)
        rel = (v - tgt) / tgt
        print(f"   {lbl:26s} = {mp.nstr(v, 14):>18s}   rel {mp.nstr(rel, 6):>12s}")
    print("   -> the augmentation lands on the block's own baseline (-0.128 % vs")
    print("      the measurement, which is the baseline's own documented miss);")
    print("      the ruled z_D predicts 49.5 % LOW.  That is the fork, stated as")
    print("      a consequence -- NOT as a recommendation.  See the docstring.")

    print()
    print("VERDICT:", "PASS -- the baseline is the augmentation's Markov trace of the "
          "k=2 crossing reversal; z_D gives alpha times it" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
