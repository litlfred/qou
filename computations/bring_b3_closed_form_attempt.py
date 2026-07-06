#!/usr/bin/env python3
r"""bring_b3_closed_form_attempt.py

B_3(C) closed-form attempt for the O(alpha^2) coefficient of 1/alpha_EM
(the additive next-order term after the derived 2/(3pi) photon IR
zero-mode).  Companion compute for
``docs/audits/2026-07-05-alpha4pi-coefficient-derivation-attempt.md``
(section "B_3(C) closed-form attempt").

WHAT THIS PROBE ESTABLISHES (all parameter-free, no fit):

  1. POSITIVE: the golden-ratio Bloch class [1/phi^2]_3 in B_3(Q(sqrt5))
     has an EXACT single-valued trilogarithm value

         L_3(1/phi^2) = (4/5) * zeta(3)          (verified to 40+ dps)

     with the companion distribution identity
         L_3(1/phi)  +  L_3(-1/phi)  =  (1/5) * zeta(3),
     and the cyclotomic (L(3,chi_5)) sector satisfies
         Im Li_3(zeta_5) = 2 * Im Li_3(zeta_5^2).
     These are the natural, canonical, parameter-free B_3 generators
     that Bring's sqrt5 / S_5 arithmetic actually supplies.  This is
     a genuine trilogarithm Bloch class with a closed form -- the
     object the RT-Phase-5 scaffold asked for.

  2. NEGATIVE (the coefficient does NOT close): no parameter-free
     archimedean normalization of these Borel/Zagier generators
     {zeta(3), L(3,chi_5)} reproduces the data-demanded coefficient
     C_data = (CODATA - bare - 2/3pi)/alpha.  A bounded PSLQ over the
     canonical generators (NOT a wide scan) finds no relation.

  3. NUMERICAL-FLOOR obstruction (sharpened): the target term T_data is
     a small difference (~5.7e-4) of large numbers (~137), so the
     ~3 ppb muon-q0 uncertainty inflates to ~0.5% RELATIVE uncertainty
     in C_data.  The "1.4% below 1/(4pi)" signal is only ~3x this band;
     no closed form can be numerically discriminated.

VERDICT: OPEN.  An exact B_3 value exists, but (a) a 2-real-dimensional
surface supplies no canonical ideal-TETRAHEDRON (3D) scissors cycle to
select a B_3 class, (b) the map from {zeta(3), L(3,chi_5)} to a 1/alpha
correction needs a normalization the geometry does not fix (the
un-evaluated a_D^{(2)} = closed-int lambda_SW^{(2)}), and (c) the target
is only ~0.5%-determined.  No closure; no fit.

Standalone (mpmath only); emits NO witness (records an open negative,
not a validated result).  Run:  python3 bring_b3_closed_form_attempt.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from mpmath import (mp, mpf, mpc, pi, polylog, re, im, log, zeta, sqrt, exp,
                    nstr, pslq, fabs)

mp.dps = 60

HERE = Path(__file__).resolve().parent


def q_int(n, q):
    return (q ** n - q ** (-n)) / (q - 1 / q)


def L3(z):
    """Zagier single-valued (BWR) trilogarithm: real-analytic, single
    valued, L3(zbar)=L3(z), L3(1/z)=L3(z)."""
    z = mpc(z)
    if z == 0:
        return mpf(0)
    lz = log(abs(z))
    Li1 = -log(1 - z)  # Li_1(z)
    return re(polylog(3, z) - lz * polylog(2, z) + (lz ** 2) / 3 * Li1)


def main() -> int:
    q_path = HERE / "q-pinning-50-digit.witness.json"
    q0 = mpf(json.load(q_path.open())["derived_50_digit"]["q"])

    alpha = 1 / mpf("137.035999084")
    codata_inv = mpf("137.035999084")
    bare = q0 * q_int(9, q0) * q_int(10, q0)
    term_2_3pi = mpf(2) / (3 * pi)
    T_data = codata_inv - bare - term_2_3pi          # data-demanded next term
    C_data = T_data / alpha
    ratio_to_4pi = C_data / (1 / (4 * pi))

    print("=" * 72)
    print("B_3(C) closed-form attempt for the O(alpha^2) coefficient")
    print("=" * 72)
    print(f"q0 (muon pin)        = {nstr(q0, 25)}")
    print(f"bare q[9]q[10]q      = {nstr(bare, 18)}")
    print(f"2/(3pi)              = {nstr(term_2_3pi, 18)}")
    print(f"T_data (next term)   = {nstr(T_data, 18)}")
    print(f"C_data = T_data/alpha= {nstr(C_data, 18)}")
    print(f"C_data / (1/4pi)     = {nstr(ratio_to_4pi, 12)}   "
          f"(1.4% below round 1/4pi)")
    print()

    # ---- 1. Exact golden-ratio B_3 generators (POSITIVE) --------------
    phi = (1 + sqrt(5)) / 2
    z3 = zeta(3)
    L3_iphi2 = L3(1 / phi ** 2)         # 1/phi^2 = (3-sqrt5)/2
    L3_iphi = L3(1 / phi)
    L3_miphi = L3(-1 / phi)
    err_45 = fabs(L3_iphi2 - mpf(4) / 5 * z3)
    err_15 = fabs((L3_iphi + L3_miphi) - mpf(1) / 5 * z3)

    z5 = exp(mpc(0, 1) * 2 * pi / 5)
    im1, im2 = im(polylog(3, z5)), im(polylog(3, z5 ** 2))
    err_dist = fabs(im1 - 2 * im2)

    print("--- Exact B_3(Q(sqrt5)) generators (parameter-free) ---")
    print(f"L3(1/phi^2)                    = {nstr(L3_iphi2, 30)}")
    print(f"  (4/5) zeta(3)                = {nstr(mpf(4)/5*z3, 30)}")
    print(f"  |L3(1/phi^2) - (4/5)zeta3|   = {nstr(err_45, 6)}   EXACT")
    print(f"L3(1/phi)+L3(-1/phi) - 1/5 z3  = {nstr(err_15, 6)}   EXACT")
    print(f"Im Li3(z5) - 2 Im Li3(z5^2)    = {nstr(err_dist, 6)}   EXACT")
    assert err_45 < mpf("1e-40"), "golden L3 ladder failed"
    assert err_15 < mpf("1e-40")
    assert err_dist < mpf("1e-40")
    print()

    # ---- 2. Does the coefficient close? (NEGATIVE) --------------------
    Lchi5_3 = mpf(0)                                  # L(3, chi_5), chi_5 Legendre
    chi = {1: 1, 2: -1, 3: -1, 4: 1, 0: 0}
    for n in range(1, 300000):
        c = chi[n % 5]
        if c:
            Lchi5_3 += c / mpf(n) ** 3
    zetaF3 = z3 * Lchi5_3                              # Dedekind zeta_{Q(sqrt5)}(3)

    print("--- Coefficient closure test (canonical Borel generators) ---")
    print(f"zeta(3)              = {nstr(z3, 18)}")
    print(f"L(3, chi_5)          = {nstr(Lchi5_3, 18)}")
    print(f"C_data / [(4/5)z3]   = {nstr(C_data / L3_iphi2, 15)}  (not clean)")
    print(f"C_data / zeta(3)     = {nstr(C_data / z3, 15)}  (not clean)")
    print(f"C_data*pi^2/zeta(3)  = {nstr(C_data * pi ** 2 / z3, 15)}  (not 2/3)")
    for label, basis in [
        ("T_data vs {zeta3, L(3,chi5)}", [T_data, z3, Lchi5_3]),
        ("T_data vs {zeta3, L(3,chi5), pi^3}", [T_data, z3, Lchi5_3, pi ** 3]),
        ("T_data vs {zeta_F(3), alpha/4pi}", [T_data, zetaF3, alpha / (4 * pi)]),
    ]:
        rel = pslq(basis, tol=mpf("1e-22"), maxcoeff=10 ** 6)
        print(f"  PSLQ {label:36}: {rel}")
    print("  -> no parameter-free B_3 combination reproduces the coefficient")
    print()

    # ---- 3. Numerical-floor obstruction (sharpened) ------------------
    dq = q0 * mpf("3e-9")                              # ~3 ppb muon-q0 band

    def T_of(qq):
        return codata_inv - qq * q_int(9, qq) * q_int(10, qq) - term_2_3pi

    dT = (T_of(q0 + dq) - T_of(q0 - dq)) / 2
    rel_unc = fabs(dT / T_data)
    print("--- Numerical-floor obstruction ---")
    print(f"T_data                         = {nstr(T_data, 15)}")
    print(f"dT from 3 ppb q0 band          = {nstr(dT, 8)}")
    print(f"=> relative uncertainty in C   = {nstr(rel_unc, 6)}  (~{nstr(rel_unc*100,3)}%)")
    print(f"   deficit vs 1/4pi is 1.4%  = only ~{nstr(mpf('0.0136')/rel_unc,3)}x the q0 band")
    print()
    print("VERDICT: OPEN.  Exact B_3 value L3(1/phi^2)=(4/5)zeta(3) exists,")
    print("but supplies no closed form for the coefficient; obstruction is")
    print("(a) no canonical 3D ideal-tetrahedron cycle from a 2-surface,")
    print("(b) unfixed archimedean normalization (a_D^{(2)} un-evaluated),")
    print("(c) target only ~0.5%-determined.  No closure; no fit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
