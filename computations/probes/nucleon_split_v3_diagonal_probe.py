#!/usr/bin/env python3
"""80-dps numbers for the nucleon split from the position-labelled diagonal of V^3.

Lean: ``QOU.Nuclear.NucleonSplitV3Diagonal`` (closed forms of tau_p(c_p)/tau_n(c_n) for all nine
pairings, and the strand-reversal symmetry J V^3(q) J = V^3(1/q)^T that singles out the middle
pairing udu <-> dud). Pre-registration:
``computations/probes/nucleon_split_v3_diagonal/PREREGISTRATION.md``. Audit:
``docs/audits/2026-11-27-nucleon-split-v3-diagonal.md``. Beans ``qou-myts``, ``qou-99qc``.

Gibbs map (route 1, ``NucleonSplitGibbsCoulomb``, no Coulomb term):
    m_n - m_p = E0 * log(tau_p(c_p) / tau_n(c_n)),  E0 = k_B T_q (qbeta_e0.order_zero).
The tower E0 (qbeta_e0.canonical) is printed as a labelled second column. A pairing with ratio <= 0
is reported as "log undefined". No pairing is selected by the CODATA column; the pre-registered
headline is the middle pairing (1,1), selected by the symmetry before any number was computed.

Exact arithmetic: the diagonal entries are recomputed from the 3x3 Jimbo matrices over Fraction at
rational test points and checked against the Lean closed forms, then evaluated in mpmath at q0.

Run:  python3 -u computations/probes/nucleon_split_v3_diagonal_probe.py
"""
from __future__ import annotations

import sys
from fractions import Fraction
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

from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qbeta import qbeta_e0  # noqa: E402

DPS = 80
M_E = mpf(_codata.codata("electron mass energy equivalent in MeV").value_str)
M_P_EXP = mpf(_codata.codata("proton mass energy equivalent in MeV").value_str)
M_N_EXP = mpf(_codata.codata("neutron mass energy equivalent in MeV").value_str)
DM_NP_EXP = M_N_EXP - M_P_EXP          # comparison only

P_NAMES = ("uud", "udu", "duu")
N_NAMES = ("udd", "dud", "ddu")


# --- exact matrices (NucleonWeightSpaceTraces / TwoTerm) -------------------------------------
def mat_mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def A1(q): return [[q, 0, 0], [0, 0, 1], [0, 1, q - 1 / q]]
def A2Inv(q): return [[-(q - 1 / q), 1, 0], [1, 0, 0], [0, 0, 1 / q]]
def B1(q): return [[0, 1, 0], [1, q - 1 / q, 0], [0, 0, q]]
def B2Inv(q): return [[1 / q, 0, 0], [0, -(q - 1 / q), 1], [0, 1, 0]]


def v3(X, Y, q):
    V = mat_mul(X(q), Y(q))
    return mat_mul(mat_mul(V, V), V)


# --- Lean closed forms (BorromeanRingColouredTrace.borromeanV3{A,B}_diag_*) -------------------
def diagA(q):
    return (-(q**2 - 2) * (q**4 - q**2 + 1), q**0, (2 * q**2 - 1) * (q**4 - q**2 + 1) / q**6)


def diagB(q):
    return ((q**6 - 2 * q**4 + 3 * q**2 - 1) / q**4,
            -(q**4 - q**2 + 1) * (q**8 - 3 * q**6 + 3 * q**4 - 3 * q**2 + 1) / q**6,
            -(q**6 - 3 * q**4 + 2 * q**2 - 1) / q**2)


def ratio(q, i, j):
    """tau_p(i)/tau_n(j) = q^2 <c_p|V^3|c_p>/<c_n|V^3|c_n> (NucleonSplitV3Diagonal.ratio_eq)."""
    return q**2 * diagA(q)[i] / diagB(q)[j]


def kind(i, j):
    if i == 2 - j:
        return f"(a) same position k={j}"
    return "(b) single flip"


def exact_checks():
    ok = True
    for q in (Fraction(3, 2), Fraction(111, 100), Fraction(7, 5)):
        MA, MB = v3(A1, A2Inv, q), v3(B1, B2Inv, q)
        ok &= all(MA[i][i] == diagA(q)[i] and MB[i][i] == diagB(q)[i] for i in range(3))
        # strand reversal o bar: <rev c|V3|rev c>(q) = <c|V3|c>(1/q)
        qb = 1 / q
        ok &= all(diagA(q)[2 - i] == diagA(qb)[i] and diagB(q)[2 - i] == diagB(qb)[i]
                  for i in range(3))
        MAb, MBb = v3(A1, A2Inv, qb), v3(B1, B2Inv, qb)
        ok &= all(MA[2 - i][2 - j] == MAb[j][i] and MB[2 - i][2 - j] == MBb[j][i]
                  for i in range(3) for j in range(3))
    return ok


def at_anchor(q0):
    E = qbeta_e0.order_zero(q=q0, m_e=M_E)
    E_twr = qbeta_e0.canonical(q=q0, m_e=M_E)
    rows = []
    for i in range(3):
        for j in range(3):
            r = ratio(q0, i, j)
            row = {"pair": f"{P_NAMES[i]}<->{N_NAMES[j]}", "i": i, "j": j, "kind": kind(i, j),
                   "ratio": r}
            if r > 0:
                row["split_ord0"] = E * mp.log(r)
                row["split_tower"] = E_twr * mp.log(r)
                row["gap_ord0"] = row["split_ord0"] - DM_NP_EXP
            else:
                row["split_ord0"] = row["split_tower"] = row["gap_ord0"] = None
            rows.append(row)
    sA, sB = sum(diagA(q0)), sum(diagB(q0))
    cls = q0**2 * sA / sB
    pA, pB = diagA(q0)[0] * diagA(q0)[1] * diagA(q0)[2], diagB(q0)[0] * diagB(q0)[1] * diagB(q0)[2]
    geo = q0**6 * pA / pB
    agg = []
    for name, r, p in (("(c) class sum", cls, 1), ("(c) geometric mean (any matching)", geo, 3)):
        d = {"pair": name, "ratio_power": r, "root": p}
        if r > 0:
            d["split_ord0"] = E * mp.log(r) / p
            d["split_tower"] = E_twr * mp.log(r) / p
            d["gap_ord0"] = d["split_ord0"] - DM_NP_EXP
        else:
            d["split_ord0"] = d["split_tower"] = d["gap_ord0"] = None
        agg.append(d)
    return E, E_twr, rows, agg, cls


def s(x, n=10):
    return "log undefined" if x is None else mp.nstr(x, n)


def main():
    wb = WitnessBuilder("nucleon-split-v3-diagonal", engine="mpmath")
    wb.set_description(
        "80-dps Gibbs n-p split E0*log(tau_p/tau_n) for all nine position-labelled pairings of the "
        "V^3 diagonal (QOU.Nuclear.NucleonSplitV3Diagonal) plus class aggregates; the middle "
        "pairing udu<->dud is the pre-registered, symmetry-selected headline. CODATA enters only "
        "the gap column."
    )
    ok = exact_checks()
    print(f"exact closed-form + strand-reversal checks (Fraction): {'PASS' if ok else 'FAIL'}")
    wb.add_assertion("closed_forms_and_symmetry_exact", computed=bool(ok), expected=True)
    res = {}
    for name, q0 in (("proton", mpf(q_at(DPS))), ("muon", mpf(q_muon_at(DPS)))):
        E, E_twr, rows, agg, cls = at_anchor(q0)
        print(f"\n[{name}] q0 = {mp.nstr(q0, 20)}  E0(ord0) = {mp.nstr(E, 12)}  "
              f"E0(tower) = {mp.nstr(E_twr, 12)} MeV")
        print(f"  {'pairing':<14}{'kind':<24}{'tau_p/tau_n':>18}{'MeV ord0':>16}"
              f"{'MeV tower':>16}{'gap ord0':>16}")
        for r in rows:
            tag = "  <- headline" if (r["i"], r["j"]) == (1, 1) else ""
            print(f"  {r['pair']:<14}{r['kind']:<24}{mp.nstr(r['ratio'], 12):>18}"
                  f"{s(r['split_ord0']):>16}{s(r['split_tower']):>16}{s(r['gap_ord0']):>16}{tag}")
        for d in agg:
            print(f"  {d['pair']:<38}{s(d['split_ord0']):>16}{s(d['split_tower']):>16}"
                  f"{s(d['gap_ord0']):>16}")
        cell_ok = abs(cls - q0**2) < mpf(10) ** -70
        wb.add_assertion(f"{name}_class_sum_is_qsq", computed=bool(cell_ok), expected=True)
        ok &= bool(cell_ok)
        res[name] = {"q0": fmt(q0), "E0_ord0": fmt(E), "E0_tower": fmt(E_twr),
                     "pairings": [{k: (fmt(v) if isinstance(v, mpf) else v) for k, v in r.items()}
                                  for r in rows],
                     "aggregates": [{k: (fmt(v) if isinstance(v, mpf) else v) for k, v in d.items()}
                                    for d in agg]}
    print(f"\nCODATA m_n - m_p = {mp.nstr(DM_NP_EXP, 10)} MeV (comparison only)")
    wb.add_data("lean_module", "QOU.Nuclear.NucleonSplitV3Diagonal")
    wb.add_data("beans_referenced", ["qou-myts", "qou-99qc"])
    wb.add_data("headline_preregistered", "udu<->dud (middle strand; strand reversal o bar fixed point)")
    wb.add_data("scope", "diagonal entries are not conjugation-invariant: boundary condition on the open braid")
    wb.add_data("anchors", res)
    wb.add_data("codata_comparison_only", {"dm_np": fmt(DM_NP_EXP)})
    path = wb.save({"q0Anchor": "comparison"})
    print(f"\nwitness: {path}\nALL CHECKS {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
