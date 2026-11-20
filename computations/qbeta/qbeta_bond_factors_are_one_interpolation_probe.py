#!/usr/bin/env python3
"""All three qbeta bond constants are ONE law: `b(t) = z - h*t`.

WHAT THIS SETTLES
-----------------
`qbeta_bond_factors_derived_probe` extracts five closed forms from the 2H / 3H
traces and records three identities among them, two of which concern the bond
factors:

    1.  b_pp - z = 0            (z = q^3/(q^2+1), the convention-D Ocneanu parameter)
    2.  b_pp/b_nn - q^4 = 0

Those are stated there as *identities among extracted constants*.  This probe
shows they are two instances of a single interpolation law, and that the third
bond constant -- the degree-10 rational `b_pn`, which that file records with no
structural reading at all -- is the same law at a third value of one parameter:

    b(t) = z - h*t,   z = q^3/(q^2+1),   h = q - 1/q

    letter   t                 b(t)
    ------   ---------------   -------------------------------------------
    pp       0                 z                        = q^3/(q^2+1)
    pn       1/2 - delta/4     z - h*(1/2 - delta/4)    = the deg-10 rational
    nn       1                 z - h                    = 1/(q^3+q)

with `delta = (q-1)^2 (1 - q^-4)/3` the substrate flavour split.  All three
differences simplify to EXACTLY zero in sympy over the symbol `q` -- these are
rational-function identities, not numerical agreements at q0.

`b(t)` is the interior bond factor proved in Lean as
`QOU.Hecke.BondLetterIdentification.tr_bond_interp`: for a bond letter
`sigma_t := (1-t)*sigma + t*sigma^-1` sandwiched between lower-filtration and
upper-filtration material, the Markov trace scales by `z - h*t`.  So the three
constants that file extracted from nuclear traces are the three letters of that
law, and identity 2 above is `tr_bond_ginv` divided by `tr_bond_gen`.

WHAT THIS DOES NOT SETTLE
-------------------------
* It does not derive `t_pn = 1/2 - delta/4`.  It shows the extracted `b_pn` IS
  that value of `t` -- which is an independent, exact confirmation that the
  production p-n letter is `averaged_weighted` and not `averaged` (`t = 1/2`,
  which gives a different rational function; printed below) -- but the `1/4`
  and the `(q-1)^2/3` in `delta` remain underived.  Bean `qou-qqm4`.
* It does not bear on the `pp -> sigma` / `nn -> sigma^-1` ORIENTATION, which
  bean `qou-0pzi` reports falsified on the two-nucleon signs.  The law says
  what a letter contributes; it does not say which letter a flavour pair gets.
* `t_p` / `t_n` (the per-nucleon traces in that file) are untouched here, and
  are exactly the two constants its own 2026-09-07 note (bean `qou-4383`)
  flags as GROUPED-era.  See the frame remark below.

FRAME REMARK (offered to `qou-4383`, not a resolution of it)
------------------------------------------------------------
`qbeta_bond_factors_derived_probe` carries a standing flag that it mixes a
canonical atom frame with superseded grouped-frame nucleon traces.  `b(t)` has
no intra-nucleon content -- it is the Markov property plus the Hecke quadratic
relation, both of which are statements about the INTERFACE crossing -- so the
exact agreement of all three `b_*` with it is evidence that the flagged frame
mismatch is confined to `t_p` / `t_n`.  That is evidence, not proof, and this
probe does not check `r_previous`.

Run: python3 computations/qbeta/qbeta_bond_factors_are_one_interpolation_probe.py
"""

from __future__ import annotations

import sympy as sp
from mpmath import mp, mpf

mp.dps = 60

_q = sp.symbols("q", positive=True)

# ── the three bond closed forms, copied verbatim from
#    computations/qbeta/qbeta_bond_factors_derived_probe.py ──────────────
B_PP = _q**3 / (_q**2 + 1)
B_PN = (
    (_q**10 - 2 * _q**9 + 7 * _q**8 - 2 * _q**6 + 4 * _q**5 + 4 * _q**4
     + _q**2 - 2 * _q + 1)
    / (12 * _q**5 * (_q**2 + 1))
)
B_NN = 1 / (_q**3 + _q)

# ── the one law ────────────────────────────────────────────────────────
Z = _q**3 / (_q**2 + 1)          # convention-D Markov / Ocneanu parameter
H = _q - 1 / _q                  # Hecke quadratic constant
DELTA = (_q - 1) ** 2 * (1 - _q**-4) / 3          # substrate flavour split
T_PP = sp.Integer(0)
T_PN = sp.Rational(1, 2) - DELTA / 4              # ctype `averaged_weighted`
T_NN = sp.Integer(1)
T_AVG = sp.Rational(1, 2)                         # ctype `averaged` (NOT production)


def bond(t):
    """The interior bond factor `z - h*t` (Lean: `tr_bond_interp`)."""
    return Z - H * t


def main() -> int:
    ok = True

    print("1. THE THREE BOND CONSTANTS AGAINST b(t) = z - h*t  (symbolic over q)")
    for name, extracted, t, tlabel in (
        ("b_pp", B_PP, T_PP, "0"),
        ("b_pn", B_PN, T_PN, "1/2 - delta/4"),
        ("b_nn", B_NN, T_NN, "1"),
    ):
        d = sp.simplify(sp.together(bond(t) - extracted))
        good = d == 0
        ok &= good
        print(f"   {name}  t = {tlabel:<16}  b(t) - {name} = {d}"
              f"   {'OK' if good else 'MISMATCH'}")

    print()
    print("2. THE TWO RECORDED IDENTITIES ARE COROLLARIES OF THE LAW")
    id1 = sp.simplify(bond(T_PP) - Z)
    id2 = sp.simplify(bond(T_PP) / bond(T_NN) - _q**4)
    ok &= (id1 == 0) and (id2 == 0)
    print(f"   b_pp - z        = b(0) - z            = {id1}   (tr_bond_gen)")
    print(f"   b_pp/b_nn - q^4 = b(0)/b(1) - q^4     = {id2}   "
          "(tr_bond_ginv / tr_bond_gen)")

    print()
    print("3. THE PRODUCTION p-n LETTER IS averaged_weighted, NOT averaged")
    d_avg = sp.simplify(sp.together(bond(T_AVG) - B_PN))
    distinct = d_avg != 0
    ok &= distinct
    print(f"   b(1/2) - b_pn   = {sp.simplify(d_avg)}")
    print(f"   -> the two ctypes are distinct rational functions: "
          f"{'CONFIRMED' if distinct else 'NOT DISTINGUISHED'}")
    t_from_bpn = sp.simplify((Z - B_PN) / H)
    print(f"   t recovered from b_pn  = {t_from_bpn}")
    print(f"   t_pn as 1/2 - delta/4  = {sp.simplify(T_PN)}")
    matches = sp.simplify(t_from_bpn - T_PN) == 0
    ok &= matches
    print(f"   -> identical: {'YES' if matches else 'NO'}")

    print()
    print("4. NUMERICAL SANITY AT THE PROTON-PINNED q0  (mpmath, dps=60)")
    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP          # noqa: PLC0415
    q0 = Q_MP
    # MEASURED values, verbatim from qbeta_bond_factors_derived_probe
    measured = {"b_pp": "0.6126880371464652516",
                "b_pn": "0.50822978937673896258",
                "b_nn": "0.40362773835082593617"}
    for name, t in (("b_pp", T_PP), ("b_pn", T_PN), ("b_nn", T_NN)):
        v = mpf(str(sp.N(bond(t).subs(_q, sp.Float(str(q0), 50)), 45)))
        m = mpf(measured[name])
        rel = abs(v - m) / abs(m)
        good = rel < mpf("1e-18")
        ok &= good
        print(f"   {name}  b(t) = {mp.nstr(v, 22):>24}   measured "
              f"{measured[name]:>22}   rel {mp.nstr(rel, 3)}   "
              f"{'OK' if good else 'MISMATCH'}")

    print()
    print("VERDICT:", "PASS — all three bond constants are one interpolation law"
          if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
