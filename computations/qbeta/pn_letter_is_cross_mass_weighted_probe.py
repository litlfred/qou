#!/usr/bin/env python3
"""The production p-n letter is CROSS-mass-weighted: `(m_n*sigma + m_p*sigma^-1)/(m_p+m_n)`.

WHAT THIS ESTABLISHES
---------------------
`pn_interface_bar_structure_probe.py` fact 3 already records that the canonical
p-n interface is a convex combination of the two like-pair letters,

    f_pn  =  w_p * f_pp  +  w_n * f_nn ,
    w_p = 1/2 + delta/4 ,   w_n = 1/2 - delta/4 ,   w_p + w_n = 1

with `delta = (m_n - m_p)/M_N` the substrate flavour split at `M_N = (m_p+m_n)/2`.
It reads the colour weighting as "a delta-TILT of that mean, toward the p-p side".

This probe identifies what those two weights ARE:

    w_p  =  m_n / (m_p + m_n)        <-- the NEUTRON's mass fraction
    w_n  =  m_p / (m_p + m_n)        <-- the PROTON's mass fraction

exactly, not to leading order.  Each like-pair letter is carried by the mass
fraction of **the other** nucleon.  So the production letter is

    sigma_pn  =  ( m_n * sigma  +  m_p * sigma^-1 ) / (m_p + m_n)

with no `delta`, no `1/4`, and no normalisation convention in it at all.  In the
mixing parameter of `QOU.Hecke.BondLetterIdentification.tr_bond_interp`
(`sigma_t := (1-t) sigma + t sigma^-1`) this is `t_pn = m_p/(m_p+m_n)`, which is
that file's `tPN_eq_proton_mass_fraction`.

WHY THE WORD "CROSS" IS THE CONTENT
-----------------------------------
The like pairs fix the per-nucleon endpoint values `t_p = 0` (pp is `sigma`) and
`t_n = 1` (nn is `sigma^-1`).  Interpolating those two endpoints between a proton
and a neutron admits two natural weightings, and they are NOT the same:

    direct   t = (m_p*t_p + m_n*t_n)/(m_p+m_n) = m_n/(m_p+m_n) = 1/2 + delta/4
    cross    t = (m_n*t_p + m_p*t_n)/(m_p+m_n) = m_p/(m_p+m_n) = 1/2 - delta/4

They differ by exactly `delta/2` and production selects the **cross** one.  That
is the same fact as "the tilt goes toward the p-p side", restated as a statement
about which nucleon's mass carries which letter — which is falsifiable, where a
direction of tilt is a description.

IT IS AN IDENTITY, NOT A DERIVATION
-----------------------------------
Nothing here derives the cross weighting.  `canonical_braid_crossings.d_for_ctype`
returns `-h(1/2 - delta/4)` for `averaged_weighted` with no rationale in its
source; `prop:pn-averaging-uniqueness` fixes the candidate set by bar-invariance
and normalisation, both of which the `direct` alternative satisfies equally (it
is the `delta -> -delta` reflection).  So this probe converts an unexplained
numeral into an unexplained CHOICE BETWEEN TWO NAMED WEIGHTINGS, which is a
smaller open item, not a closed one.  Bean `qou-qqm4`.

WHERE THE TWO ARE DISTINGUISHABLE -- AND WHERE THEY ARE NOT
-----------------------------------------------------------
* **Not at A = 3.**  The mirror ratio `tr(3H)/tr(3He)` is
  `(b_pn*b_nn)/(b_pp*b_pn)`, so the p-n factor cancels and both weightings give
  `q^-4` identically.  This is the cancellation
  `QOU.QBeta.InterfaceScalar.mirror_split_eq_L_diff` already records; the point
  here is that it makes the mirror splitting blind to this sign.
* **At the deuteron.**  `2H` carries exactly one bond and it is `pn`, so the
  whole discriminator sits there: `b_pn` moves by `-h*delta/2`, reported below.

Run: python3 computations/qbeta/pn_letter_is_cross_mass_weighted_probe.py
"""

from __future__ import annotations

import sympy as sp
from mpmath import mp, mpf

mp.dps = 60

_q = sp.symbols("q", positive=True)
_mp_sym, _mn_sym = sp.symbols("m_p m_n", positive=True)

# ── the substrate flavour split, MEAN-normalised (_li_2_q_util.flavor_split_leading)
DELTA_MASS = (_mn_sym - _mp_sym) / ((_mp_sym + _mn_sym) / 2)
DELTA_Q = (_q - 1) ** 2 * (1 - _q**-4) / 3

# ── the interior bond factor (Lean: tr_bond_interp)
Z = _q**3 / (_q**2 + 1)
H = _q - 1 / _q


def bond(t):
    return Z - H * t


W_PP = sp.Rational(1, 2) + DELTA_MASS / 4      # weight carried by the pp letter
W_NN = sp.Rational(1, 2) - DELTA_MASS / 4      # weight carried by the nn letter

T_PROD = sp.Rational(1, 2) - DELTA_Q / 4       # production, ctype averaged_weighted
T_FLIP = sp.Rational(1, 2) + DELTA_Q / 4       # the direct-mass alternative


def main() -> int:
    ok = True

    print("1. THE TWO CONVEX WEIGHTS ARE THE CROSSED MASS FRACTIONS  (exact in m_p, m_n)")
    for lbl, w, target, tlbl in (
        ("w_pp", W_PP, _mn_sym / (_mp_sym + _mn_sym), "m_n/(m_p+m_n)  [NEUTRON's]"),
        ("w_nn", W_NN, _mp_sym / (_mp_sym + _mn_sym), "m_p/(m_p+m_n)  [PROTON's]"),
    ):
        d = sp.simplify(w - target)
        good = d == 0
        ok &= good
        print(f"   {lbl} = 1/2 {'+' if lbl=='w_pp' else '-'} delta/4  -  {tlbl:<28}"
              f" = {d}   {'OK' if good else 'MISMATCH'}")
    s = sp.simplify(W_PP + W_NN)
    ok &= s == 1
    print(f"   w_pp + w_nn = {s}   (convex)   {'OK' if s == 1 else 'MISMATCH'}")

    print()
    print("2. THE ENDPOINT INTERPOLATION: DIRECT vs CROSS  (t_p = 0, t_n = 1)")
    direct = sp.simplify((_mp_sym * 0 + _mn_sym * 1) / (_mp_sym + _mn_sym))
    cross = sp.simplify((_mn_sym * 0 + _mp_sym * 1) / (_mp_sym + _mn_sym))
    t_prod_mass = sp.simplify(sp.Rational(1, 2) - DELTA_MASS / 4)
    d_cross = sp.simplify(cross - t_prod_mass)
    d_direct = sp.simplify(direct - t_prod_mass)
    gap = sp.simplify(direct - cross - DELTA_MASS / 2)
    ok &= (d_cross == 0) and (d_direct != 0) and (gap == 0)
    print(f"   direct  t = {direct}     - t_production = {d_direct}")
    print(f"   cross   t = {cross}     - t_production = {d_cross}")
    print(f"   direct - cross - delta/2 = {gap}")
    print(f"   -> production is the CROSS weighting: "
          f"{'CONFIRMED' if d_cross == 0 and d_direct != 0 else 'NOT CONFIRMED'}")

    print()
    print("3. THE LIKE PAIRS ARE FIXED POINTS OF BOTH  (no mean to tilt)")
    for lbl, ma, mb, ta, tb in (("pp", _mp_sym, _mp_sym, 0, 0),
                                ("nn", _mn_sym, _mn_sym, 1, 1)):
        v_direct = sp.simplify((ma * ta + mb * tb) / (ma + mb))
        v_cross = sp.simplify((mb * ta + ma * tb) / (ma + mb))
        good = v_direct == v_cross == ta
        ok &= good
        print(f"   t_{lbl}: direct = {v_direct}, cross = {v_cross}, "
              f"expected {ta}   {'OK' if good else 'MISMATCH'}")
    print("   -> a like pair averages a letter with ITSELF, so every convex weight")
    print("      returns it. The 'mass fraction' objection to the like pairs is void.")

    print()
    print("4. THE A = 3 MIRROR RATIO CANNOT SEE THE SIGN  (symbolic over q)")
    for lbl, t in (("production", T_PROD), ("direct-mass", T_FLIP)):
        r = sp.simplify((bond(t) * bond(1)) / (bond(0) * bond(t)))
        good = sp.simplify(r - _q**-4) == 0
        ok &= good
        print(f"   tr(3H)/tr(3He) [{lbl:<11}] = {r}   {'OK' if good else 'MISMATCH'}")
    print("   -> the p-n factor cancels; both weightings give q^-4 identically.")

    print()
    print("5. THE DEUTERON IS THE DISCRIMINATOR  (mpmath, dps=60)")
    d_sym = sp.simplify(bond(T_FLIP) - bond(T_PROD) + H * DELTA_Q / 2)
    ok &= d_sym == 0
    print(f"   b(direct) - b(production) + h*delta/2 = {d_sym}   "
          f"{'OK' if d_sym == 0 else 'MISMATCH'}")
    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP          # noqa: PLC0415
    q0 = Q_MP
    sub = {_q: sp.Float(str(q0), 50)}
    b_prod = mpf(str(sp.N(bond(T_PROD).subs(sub), 45)))
    b_flip = mpf(str(sp.N(bond(T_FLIP).subs(sub), 45)))
    shift = mpf(str(sp.N((H * DELTA_Q / 2).subs(sub), 45)))
    rel = abs(b_flip - b_prod) / abs(b_prod)
    measured = mpf("0.50822978937673896258")     # qbeta_bond_factors_derived_probe
    agrees = abs(b_prod - measured) / abs(measured) < mpf("1e-18")
    ok &= agrees
    print(f"   b_pn production  = {mp.nstr(b_prod, 22)}   (MEASURED "
          f"{measured}: {'OK' if agrees else 'MISMATCH'})")
    print(f"   b_pn direct-mass = {mp.nstr(b_flip, 22)}")
    print(f"   h*delta/2        = {mp.nstr(shift, 12)}   relative shift "
          f"{mp.nstr(rel, 6)}")
    print("   -> 2H carries exactly one bond and it is p-n, so the whole")
    print("      discriminator between the two weightings sits at the deuteron.")

    print()
    print("VERDICT:", "PASS — the production p-n letter is the cross-mass-weighted "
          "combination of the like-pair letters" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
