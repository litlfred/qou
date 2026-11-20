#!/usr/bin/env python3
"""two_term_qed_pair_choice_probe.py — are the #8518 two-term QED figures parameter-free?

Measures the discrete choices inside M_p^{QED,conn} = +0.220 keV and Delta m_QED^{conn} = -0.332 keV
(canonical_mass.proton_qed_self_energy_borromean_mev / np_qed_splitting_borromean_conn_mev),
using the same 3x3 weight-space matrices as QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm:
  A_i on W_p = (2,1), B_i on W_n = (1,2); V = s1 s2^{-1}; pair charge operators Q_ij^{(p,n)}.
The "connected" term of the published figures is
  t_N = (1/3) tr( (O_N - (tr O_N / 3) 1) V_N^3 ),   O_N = Q12 + Q23  (pair 1-3 left out),
scaled by m_e. This probe evaluates the same expression for every choice of which pair to leave
out, for no pair left out, and with the static (scalar) part kept. Exact in Q(q) (sympy); numbers at the proton q0 with mpmath.
Nothing is fitted or scored.

-- Ref: [leitner2026] bean qou-99qc (2026-11-19 00:10Z); issue #8524; PR #8367
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
import _path_bridge  # noqa: E402,F401
from q_parameter import Q_MP  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from canonical_mass import (  # noqa: E402
    proton_qed_self_energy_borromean_mev,
    np_qed_splitting_borromean_conn_mev,
)
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
q = sp.symbols("q", positive=True)
h = q - 1 / q
Mx = sp.Matrix
A1 = Mx([[q, 0, 0], [0, 0, 1], [0, 1, h]])
A2 = Mx([[0, 1, 0], [1, h, 0], [0, 0, q]])
B1 = Mx([[0, 1, 0], [1, h, 0], [0, 0, q]])
B2 = Mx([[q, 0, 0], [0, 0, 1], [0, 1, h]])
V3 = {"p": (A1 * A2.inv()) ** 3, "n": (B1 * B2.inv()) ** 3}
R = sp.Rational
Q = {
    "p": {"12": sp.diag(R(4, 9), R(-2, 9), R(-2, 9)), "23": sp.diag(R(-2, 9), R(-2, 9), R(4, 9)),
          "13": sp.diag(R(-2, 9), R(4, 9), R(-2, 9))},
    "n": {"12": sp.diag(R(-2, 9), R(-2, 9), R(1, 9)), "23": sp.diag(R(1, 9), R(-2, 9), R(-2, 9)),
          "13": sp.diag(R(-2, 9), R(1, 9), R(-2, 9))},
}
CHOICES = [("none left out", ["12", "23", "13"]), ("1-3 left out (published)", ["12", "23"]),
           ("1-2 left out", ["23", "13"]), ("2-3 left out", ["12", "13"])]


def conn(s, pairs, subtract_static=True):
    O = sp.zeros(3)
    for k in pairs:
        O += Q[s][k]
    if subtract_static:
        O = O - (O.trace() / 3) * sp.eye(3)
    return sp.factor(sp.simplify((O * V3[s]).trace() / 3))


def at_q0(expr):
    return mp.mpf(sp.N(expr.subs(q, sp.Float(str(Q_MP), 70)), 70))


def main():
    me = mp.mpf(str(M_E_MEV))
    checks, rows = [], {}
    for name, pairs in CHOICES:
        tp, tn = conn("p", pairs), conn("n", pairs)
        Mp_keV = me * abs(at_q0(tp)) * 1000
        dm_keV = -me * at_q0(sp.simplify(tn - tp)) * 1000
        rows[name] = {"t_p": str(tp), "t_n": str(tn), "M_p_keV": mp.nstr(Mp_keV, 25),
                      "Delta_m_keV": mp.nstr(dm_keV, 25)}
        print(f"{name:26s} M_p = {mp.nstr(Mp_keV, 8):>12s} keV   Delta_m = {mp.nstr(dm_keV, 8):>12s} keV", flush=True)

    tp_raw, tn_raw = conn("p", CHOICES[1][1], False), conn("n", CHOICES[1][1], False)
    dm_raw = -me * at_q0(sp.simplify(tn_raw - tp_raw)) * 1000
    rows["1-3 left out, static part kept"] = {"t_p": str(tp_raw), "t_n": str(tn_raw),
                                              "M_p_keV": mp.nstr(me * abs(at_q0(tp_raw)) * 1000, 25),
                                              "Delta_m_keV": mp.nstr(dm_raw, 25)}
    print(f"{'1-3 left out, static kept':26s} Delta_m = {mp.nstr(dm_raw, 8)} keV", flush=True)

    none = CHOICES[0][0]
    checks.append(("C1_all_pairs_connected_term_is_zero_p_and_n",
                   rows[none]["t_p"] == "0" and rows[none]["t_n"] == "0", "both t_p and t_n simplify to 0"))
    pub = CHOICES[1][0]
    lean_p = -2 * (q**2 - 1) ** 4 * (q**4 + q**2 + 1) / (27 * q**6)
    lean_d = (q**2 - 1) ** 4 * (4 * q**4 + q**2 + 4) / (27 * q**6)
    tp, tn = conn("p", CHOICES[1][1]), conn("n", CHOICES[1][1])
    checks.append(("C2_published_choice_matches_Lean_closed_forms",
                   sp.simplify(tp - lean_p) == 0 and sp.simplify(tn - tp - lean_d) == 0,
                   "trace_QAdjp_borromeanV3, trace_QAdj_connected_diff_borromeanV3"))
    cm_Mp = mp.mpf(str(proton_qed_self_energy_borromean_mev())) * 1000
    cm_dm = mp.mpf(str(np_qed_splitting_borromean_conn_mev("plain"))) * 1000
    checks.append(("C3_reproduces_canonical_mass_figures",
                   abs(cm_Mp - mp.mpf(rows[pub]["M_p_keV"])) < mp.mpf("1e-18")
                   and abs(cm_dm - mp.mpf(rows[pub]["Delta_m_keV"])) < mp.mpf("1e-18"),
                   f"canonical_mass: M_p {mp.nstr(cm_Mp, 12)} keV, Delta_m {mp.nstr(cm_dm, 12)} keV"))
    drops = [rows[c[0]] for c in CHOICES[1:]]
    signs = {mp.sign(mp.mpf(r["Delta_m_keV"])) for r in drops}
    checks.append(("C4_sign_of_Delta_m_depends_on_which_pair_is_left_out", len(signs) == 2,
                   ", ".join(r["Delta_m_keV"][:10] for r in drops)))
    mps = [mp.mpf(r["M_p_keV"]) for r in drops]
    checks.append(("C5_M_p_spread_over_left_out_pair", max(mps) / min(mps) > 5,
                   f"max/min = {mp.nstr(max(mps) / min(mps), 6)}"))

    ok = all(c[1] for c in checks)
    for n, g, s in checks:
        print(("PASS " if g else "FAIL ") + n + ": " + s)
    wb = WitnessBuilder("two-term-qed-pair-choice", engine="mpmath", output_dir=HERE)
    for name, good, src in checks:
        wb.add_assertion(name, computed="1" if good else "0", expected="1", source=src)
    wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "same q_parameter.Q_MP as canonical_mass",
        "description": "PROBE (issue #8524, bean qou-99qc): the 'connected' two-term QED term evaluated for each "
                       "choice of left-out quark pair. With no pair left out it is identically zero; the published "
                       "+0.220 keV / -0.332 keV come from leaving out pair 1-3. Nothing fitted or scored.",
        "results": rows,
    })
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
