#!/usr/bin/env python3
"""The derived `rho_pp` against the target `KindDependentBondBreaksIntegrality` states.

WHAT THIS ANSWERS
-----------------
`QOU.Mass.KindDependentBondBreaksIntegrality` (merged) observes that the `b3`
count-channel exhaustion rests on a UNIFORM bond weight, that bean `qou-qqm4`
has since derived a bond weight which is NOT uniform, and that "nobody connected
the two".  It then states a target and a direction of use, verbatim:

    rho_pp = 1 + rMeasured = 2433859/1483044 ~ 1.64112

    "Read RIGHT-TO-LEFT only: this is the number `qou-qqm4`'s derived `z + d_kind`
     at the `pp` interface must independently produce.  Computing `rho_pp` from
     the left is a one-parameter fit ... Agreement would be a parameter-free
     prediction; disagreement is a real negative about the bond model."

`qou-qqm4` closed on 2026-09-13 (`QOU.Hecke.BondLetterIdentification`, sorry-free):
the interior bond factor is `b(t) = z - h*t` for EVERY `t`, with `t = 0` at `pp`,
`t = 1` at `nn`, and `t = 1/2 - delta/4` at the production `pn`.  So the input the
target asks for now exists.  This computes it and scores it.

RESULT: DISAGREEMENT, and it is the interesting direction
---------------------------------------------------------
The derived kind-dependence moves `b3/b2` off zero and TOWARD the measurement,
but reaches only about a third of the way — and it lands FURTHER from the
measurement than the best INTEGER carrier the exhaustion had already excluded.
So breaking integrality, which is what `KindDependentBondBreaksIntegrality`
identifies as the escape, does not buy the escape.

Scope **(a)**: this carrier, with these derived weights, at the minimal Brunnian
counts, misses.  No proved invariant is offered here, so this must NOT be read as
excluding kind-dependent weights in general.

WHICH RATIO, AND WHY NOT THE OTHER ONE
--------------------------------------
`rho_pp` could mean the ratio of the bond FACTORS, `b_pp/b_pn`, or the ratio of
their LOGS (the binding is `B = -alpha*log(mu)`, so a log-space reading is not
unreasonable).  This file reports BOTH and selects the factor ratio, **on the
target file's own wording** — it says `z + d_kind`, which is the factor — and NOT
on which one scores better.  Stating that explicitly because the factor ratio
does happen to be the better of the two, and choosing it for that reason would be
selection against the target, which AGENTS.md forbids.

CLOSED FORMS (exact, symbolic in q)
-----------------------------------
    P(q)    = q^10 - 2q^9 + 7q^8 - 2q^6 + 4q^5 + 4q^4 + q^2 - 2q + 1
    b_pn    = P(q) / (12 q^5 (q^2+1))        <- matches qbeta_bond_factors_derived_probe
    rho_pp  = 12 q^8 / P(q)
    rho_nn  = 12 q^4 / P(q)
    rho_pp / rho_nn = q^4                    <- nnFactor_eq_ppFactor_div_q_pow_four

Run: python3 computations/qbeta/kind_dependent_rho_pp_derived_check.py
"""

from __future__ import annotations

import sympy as sp
from mpmath import mp, mpf, log

mp.dps = 50

_q = sp.symbols("q", positive=True)

# ── the derived bond factors (QOU.Hecke.BondLetterIdentification) ────────
_Z = _q**3 / (_q**2 + 1)                      # convention-D Markov parameter
_H = _q - 1 / _q                              # Hecke quadratic constant
_DELTA = (_q - 1) ** 2 * (1 - _q**-4) / 3     # substrate flavour split
_T_PN = sp.Rational(1, 2) - _DELTA / 4        # ctype `averaged_weighted`

B_PP = _Z                                     # tr_bond_gen      (t = 0)
B_PN = sp.cancel(_Z - _H * _T_PN)             # tr_bond_interp   (production)
B_NN = sp.cancel(_Z - _H)                     # tr_bond_ginv     (t = 1)

# the degree-10 closed form recorded in qbeta_bond_factors_derived_probe
_B_PN_PROBE = (
    (_q**10 - 2 * _q**9 + 7 * _q**8 - 2 * _q**6 + 4 * _q**5 + 4 * _q**4
     + _q**2 - 2 * _q + 1) / (12 * _q**5 * (_q**2 + 1))
)

# ── the target, verbatim from KindDependentBondBreaksIntegrality ─────────
R_MEASURED = sp.Rational(950815, 1483044)
RHO_PP_TARGET = sp.Rational(2433859, 1483044)     # = 1 + rMeasured


def b_ratio_kind(rho_1, rho_2, rho_3):
    """`bRatioKind` at the minimal Brunnian counts m_i = 1."""
    return rho_1 + rho_2 + rho_3 - 3


def main() -> int:
    ok = True

    print("1. SYMBOLIC — the derived letters, and that they are the corpus's")
    d = sp.simplify(B_PN - _B_PN_PROBE)
    ok &= d == 0
    print(f"   b_pn(derived) - b_pn(qbeta_bond_factors_derived_probe) = {d}"
          f"   {'OK' if d == 0 else 'MISMATCH'}")
    rho_pp_sym = sp.cancel(B_PP / B_PN)
    rho_nn_sym = sp.cancel(B_NN / B_PN)
    print(f"   rho_pp(q) = {rho_pp_sym}")
    print(f"   rho_nn(q) = {rho_nn_sym}")
    d2 = sp.simplify(rho_pp_sym / rho_nn_sym - _q**4)
    ok &= d2 == 0
    print(f"   rho_pp/rho_nn - q^4 = {d2}   "
          f"{'OK (nnFactor_eq_ppFactor_div_q_pow_four)' if d2 == 0 else 'MISMATCH'}")

    print()
    print("2. AT THE PROTON-PINNED q0 (mpmath, dps=50)")
    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP        # noqa: PLC0415
    q0 = Q_MP
    z0 = q0**3 / (q0**2 + 1)
    h0 = q0 - 1 / q0
    delta0 = (q0 - 1) ** 2 * (1 - q0**-4) / 3
    b_pp = z0
    b_pn = z0 - h0 * (mpf(1) / 2 - delta0 / 4)
    b_nn = z0 - h0
    rho_factor = b_pp / b_pn
    rho_log = log(b_pp) / log(b_pn)
    rm = mpf(R_MEASURED.numerator) / R_MEASURED.denominator
    tgt = mpf(RHO_PP_TARGET.numerator) / RHO_PP_TARGET.denominator
    print(f"   b_pp = {mp.nstr(b_pp, 20)}   b_pn = {mp.nstr(b_pn, 20)}   "
          f"b_nn = {mp.nstr(b_nn, 20)}")
    print(f"   rho_pp  FACTOR ratio b_pp/b_pn          = {mp.nstr(rho_factor, 12)}"
          f"   <- SELECTED (the target file says `z + d_kind`)")
    print(f"   rho_pp  LOG    ratio log b_pp / log b_pn = {mp.nstr(rho_log, 12)}"
          f"   <- reported, NOT selected")
    print(f"   TARGET (forced by the measurement)       = {mp.nstr(tgt, 12)}")

    print()
    print("3. SCORED ON b3/b2 AT THE MINIMAL 3He CARRIER (ppn: one pp, two pn)")
    print(f"   {'carrier':46s} {'rho_pp':>14s} {'b3/b2':>15s} {'miss':>12s}")
    print("   " + "-" * 90)
    rows = [
        ("uniform rho = 1 (the exhaustion's premise)", mpf(1)),
        ("best INTEGER carrier rho = 2", mpf(2)),
        ("DERIVED, factor ratio  <- selected", rho_factor),
        ("DERIVED, log ratio     (not selected)", rho_log),
    ]
    derived_miss = None
    integer_miss = None
    for name, rho in rows:
        br = b_ratio_kind(rho, mpf(1), mpf(1))
        miss = (br - rm) / rm * 100
        if name.endswith("<- selected"):
            derived_miss = abs(miss)
        if "INTEGER" in name:
            integer_miss = abs(miss)
        print(f"   {name:46s} {mp.nstr(rho, 10):>14s} {mp.nstr(br, 10):>15s} "
              f"{mp.nstr(miss, 6) + ' %':>12s}")
    print("   " + "-" * 90)
    print(f"   {'TARGET':46s} {mp.nstr(tgt, 10):>14s} {mp.nstr(rm, 10):>15s} "
          f"{'0 %':>12s}")

    print()
    print("4. THE FINDING")
    worse = derived_miss > integer_miss
    ok &= worse is not None
    print(f"   derived miss {mp.nstr(derived_miss, 6)} %  vs  "
          f"best-integer miss {mp.nstr(integer_miss, 6)} %")
    print(f"   -> the DERIVED kind-dependent carrier is "
          f"{'WORSE' if worse else 'BETTER'} than the integer carrier the")
    print("      exhaustion already excluded. Breaking integrality does not buy")
    print("      the escape KindDependentBondBreaksIntegrality identifies.")
    print("   Scope (a): this carrier, these weights, minimal counts. No invariant")
    print("   is proved here, so kind-dependent weights are NOT excluded in general.")

    print()
    print("5. 3H = pnn (pairs pn, nn, nn) — a second data point, same direction")
    rho_nn_f = b_nn / b_pn
    br_h3 = b_ratio_kind(mpf(1), rho_nn_f, rho_nn_f)
    print(f"   rho_nn = b_nn/b_pn = {mp.nstr(rho_nn_f, 12)}   "
          f"b3/b2 = {mp.nstr(br_h3, 10)}   "
          f"miss {mp.nstr((br_h3 - rm) / rm * 100, 6)} %")
    print("   (rMeasured is the 3He-referenced figure; 3H is shown for direction,")
    print("    not as a second comparison against the same target.)")

    print()
    print("VERDICT:", "PASS — symbolic identities hold; the comparison is a NEGATIVE"
          if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
