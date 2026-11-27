#!/usr/bin/env python3
"""Exact + 80-dps probe for QOU.QBeta.NucleonChargeDressedWords (distinct uud / udd words).

Companion of folio/quantum-observable-universe/lean/QOU/Nuclear/NucleonChargeDressedWords.lean.

1. Exact over Q(q, c, a, b) (sympy): build the charge-dressed V^3 on W_p and W_n from the
   Jimbo R-matrix on (C^2)^{x3} (not from the Lean 3x3 matrices), check that the dressing
   commutes with its crossing, and check the Lean closed form
   tr Mn - tr Mp = c (a - b) (1 + abc)^3 G / q^6.
2. 80 dps at the proton and muon q0, charges a = 2/3, b = -1/3: the first-order coefficient of
   the split, and its effect on the Gibbs-map cell m_n - m_p = E (2 log q - log(tr Mn / tr Mp)).
   The coupling c is NOT derived; the c that would reach CODATA m_n - m_p is printed as a
   diagnostic only and is not adopted (comparison boundary).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps(80)

import mpmath as mp  # noqa: E402
from mpmath import mpf  # noqa: E402

mp.mp.dps = max(mp.mp.dps, 80)

import sympy as sp  # noqa: E402
from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qbeta import qbeta_e0  # noqa: E402

DPS = 80
LEAN_MODULE = "QOU.QBeta.NucleonChargeDressedWords"

M_E = mpf(_codata.codata("electron mass energy equivalent in MeV").value_str)
# comparison only
M_P_EXP = mpf(_codata.codata("proton mass energy equivalent in MeV").value_str)
M_N_EXP = mpf(_codata.codata("neutron mass energy equivalent in MeV").value_str)
DM_NP_EXP = M_N_EXP - M_P_EXP

q, c, a, b = sp.symbols("q c a b")
h = q - 1 / q


def jimbo_R():
    """Jimbo R on C^2 x C^2, basis uu, ud, du, dd: R(ud) = du, R(du) = ud + h du."""
    M = sp.zeros(4, 4)
    M[0, 0] = q
    M[3, 3] = q
    M[2, 1] = 1
    M[1, 2] = 1
    M[2, 2] = h
    return M


I2 = sp.eye(2)
S1 = sp.kronecker_product(jimbo_R(), I2)
S2 = sp.kronecker_product(I2, jimbo_R())
Qd = sp.diag(a, b)
Q12 = sp.kronecker_product(Qd, Qd, I2)
Q23 = sp.kronecker_product(I2, Qd, Qd)
D12 = sp.eye(8) + c * Q12
D23 = sp.eye(8) + c * Q23


def idx(t):
    return 4 * t[0] + 2 * t[1] + t[2]


WP = [idx(t) for t in ((0, 0, 1), (0, 1, 0), (1, 0, 0))]
WN = [idx(t) for t in ((0, 1, 1), (1, 0, 1), (1, 1, 0))]

M8 = (S1 * D12 * S2.inv() * D23) ** 3
trP = sp.expand(sp.simplify(sum(M8[i, i] for i in WP)))
trN = sp.expand(sp.simplify(sum(M8[i, i] for i in WN)))

Gc0 = 3 * (a * (q**12 - 3*q**10 + 3*q**8 - 4*q**6 + 3*q**4 - 3*q**2 + 1)
           + b * (q**10 - 4*q**8 + 4*q**6 - 4*q**4 + q**2))
Gc1 = 3 * (a**3 * (q**12 - 3*q**10 + 3*q**8 - 3*q**6 + 3*q**4 - 3*q**2 + 1)
           + a**2 * b * (q**12 - 3*q**10 + 3*q**8 - 5*q**6 + 3*q**4 - 3*q**2 + 1)
           + a * b**2 * (2*q**10 - 8*q**8 + 9*q**6 - 8*q**4 + 2*q**2) - b**3 * q**6)
Gc2 = a * (a**4 * (q**12 - 3*q**10 + 3*q**8 - 2*q**6 + 3*q**4 - 3*q**2 + 1)
           + a**3 * b * (q**12 - 3*q**10 + 3*q**8 - 5*q**6 + 3*q**4 - 3*q**2 + 1)
           + a**2 * b**2 * (q**12 - 3*q**10 + 3*q**8 - 5*q**6 + 3*q**4 - 3*q**2 + 1)
           + a * b**3 * (3*q**10 - 12*q**8 + 15*q**6 - 12*q**4 + 3*q**2) - 3 * b**4 * q**6)
G = Gc0 + c * Gc1 + c**2 * Gc2
lean_split = c * (a - b) * (1 + a * b * c) ** 3 * G / q**6

# Section 5: charges in the ruled photon's weights (photon pair 1 + h^2 L - h^2 L^2).
L8 = S1 * D12 * S2.inv() * D23
W8 = S1 * S2.inv()
PHI, PSI = q * h, -h / q


def photon_pair(L):
    return sp.eye(8) + (PHI + PSI) * L + PHI * PSI * L * L


QUARK = {a: sp.Rational(2, 3), b: sp.Rational(-1, 3)}


def common_c_factor(rows):
    """gcd over the 8-dim defect entries restricted to one weight space, as polynomials in c."""
    D = sp.simplify((L8 ** 3 - photon_pair(L8)).subs(QUARK))
    g = None
    for i in rows:
        for j in rows:
            num = sp.numer(sp.together(D[i, j]))
            if num == 0:
                continue
            P = sp.Poly(num, c)
            g = P if g is None else sp.gcd(g, P)
    return sp.factor(g.as_expr())


cf_p = common_c_factor(WP)
cf_n = common_c_factor(WN)
PP = photon_pair(L8)
pp_split = sp.factor(sp.simplify(sum(PP[i, i] for i in WN) - sum(PP[i, i] for i in WP)))
H = (a**4 * b * c**2 * (q**4 + 1) + a**3 * b**2 * c**2 * (q**4 + 1) + a**3 * c * (q**4 + 1)
     + 2 * a**2 * b**3 * c**2 * q**2 + 3 * a**2 * b * c * (q**4 + 1) + 4 * a * b**2 * c * q**2
     + a * (2 * q**4 + q**2 + 2) + 2 * b * q**2)

exact = {
    "undressed_photon_pair_is_V3": sp.simplify((photon_pair(W8) - W8 ** 3)) == sp.zeros(8, 8),
    "photon_factorisation_only_c0_on_Wp": sp.simplify(cf_p / c).is_number,
    "photon_factorisation_only_c0_on_Wn": sp.simplify(cf_n / c).is_number,
    "photon_pair_split_closed_form": sp.simplify(
        pp_split - c * (a - b) * (q**2 - 1) ** 4 * (1 + a * b * c) * H / q**6) == 0,
    "dressing_commutes_s1": sp.simplify(S1 * Q12 - Q12 * S1) == sp.zeros(8, 8),
    "dressing_commutes_s2": sp.simplify(S2 * Q23 - Q23 * S2) == sp.zeros(8, 8),
    "lean_closed_form": sp.simplify(trN - trP - lean_split) == 0,
    "undressed_equal": sp.simplify((trN - trP).subs(c, 0)) == 0,
    "equal_charges_equal": sp.simplify((trN - trP).subs(b, a)) == 0,
}

AQ, BQ = sp.Rational(2, 3), sp.Rational(-1, 3)
trP_q = sp.lambdify((q, c), trP.subs({a: AQ, b: BQ}), "mpmath")
trN_q = sp.lambdify((q, c), trN.subs({a: AQ, b: BQ}), "mpmath")
pp_first_q = sp.lambdify(
    q, sp.diff(pp_split, c).subs(c, 0).subs({a: AQ, b: BQ}), "mpmath")
first_q = sp.lambdify(q, ((a - b) * Gc0 / q**6).subs({a: AQ, b: BQ}), "mpmath")


def at_anchor(q0):
    t = trP_q(q0, 0)
    f1 = first_q(q0)
    out = {"q0": q0, "t_V3": t, "first_order_coeff": f1, "first_order_rel": f1 / t,
           "photon_pair_first_order_coeff": pp_first_q(q0)}
    for tag, E in (("ord0", qbeta_e0.order_zero(q=q0, m_e=M_E)),
                   ("twr", qbeta_e0.canonical(q=q0, m_e=M_E))):
        cell0 = 2 * E * mp.log(q0)

        def cell(cc, E=E):
            return E * (2 * mp.log(q0) - mp.log(trN_q(q0, cc) / trP_q(q0, cc)))

        # d cell / dc at c = 0
        slope = -E * f1 / t
        out[f"E0_{tag}"] = E
        out[f"gibbs_cell_c0_{tag}"] = cell0
        out[f"gibbs_slope_dc_{tag}"] = slope
        try:
            c_diag = mp.findroot(lambda cc: cell(cc) - DM_NP_EXP, (DM_NP_EXP - cell0) / slope)
        except (ValueError, ZeroDivisionError):
            c_diag = mp.nan
        out[f"diag_c_for_dm_np_{tag}"] = c_diag
    return out


def main():
    wb = WitnessBuilder("nucleon-charge-dressed-words", engine="sympy+mpmath")
    wb.set_description(
        "Exact Q(q,c,a,b) check of the charge-dressed uud/udd words "
        "(QOU.QBeta.NucleonChargeDressedWords) from the full 8-dim Jimbo action, and 80-dps "
        "first-order split and Gibbs-map slope at both q0 anchors; the coupling c reaching "
        "CODATA m_n - m_p is a diagnostic only."
    )
    ok = True
    for k, v in exact.items():
        print(f"[exact] {k}: {v}")
        wb.add_assertion(f"exact_{k}", computed=bool(v), expected=True)
        ok &= bool(v)
    res = {}
    for name, q0 in (("proton", q_at(DPS)), ("muon", q_muon_at(DPS))):
        r = at_anchor(mpf(q0))
        res[name] = {k: fmt(v) for k, v in r.items()}
        print(f"\n[{name}] q0 = {mp.nstr(r['q0'], 20)}  t(V^3) = {mp.nstr(r['t_V3'], 20)}")
        print(f"  d(tr_n - tr_p)/dc at c=0 = {mp.nstr(r['first_order_coeff'], 15)}"
              f"  (relative to t: {mp.nstr(r['first_order_rel'], 12)})")
        for tag in ("ord0", "twr"):
            print(f"  Gibbs, E0_{tag}: cell(c=0) = {mp.nstr(r[f'gibbs_cell_c0_{tag}'], 12)} MeV,"
                  f" d cell/dc = {mp.nstr(r[f'gibbs_slope_dc_{tag}'], 12)} MeV")
            print(f"    DIAGNOSTIC c reaching CODATA dm_np: "
                  f"{mp.nstr(r[f'diag_c_for_dm_np_{tag}'], 10)}  (not adopted)")
        print(f"  photon-pair dressing: d(tr_n - tr_p)/dc at c=0 = "
              f"{mp.nstr(r['photon_pair_first_order_coeff'], 15)}")
        wb.add_assertion(f"{name}_first_order_nonzero",
                         computed=bool(r["first_order_coeff"] != 0), expected=True)
        ok &= bool(r["first_order_coeff"] != 0)
    wb.add_data("lean_module", LEAN_MODULE)
    wb.add_data("beans_referenced", ["qou-2skq", "qou-myts", "qou-99qc"])
    wb.add_data("charges", {"a_u": "2/3", "b_d": "-1/3"})
    wb.add_data("split_exact", str(sp.factor(trN - trP)))
    wb.add_data("photon_factorisation_common_c_factor", {"W_p": str(cf_p), "W_n": str(cf_n)})
    wb.add_data("photon_pair_split_exact", str(pp_split))
    wb.add_data("anchors", res)
    wb.add_data("codata_comparison_only", {"dm_np": fmt(DM_NP_EXP)})
    path = wb.save({"q0Anchor": "comparison"})
    print(f"\nwitness: {path}\nALL CHECKS {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
