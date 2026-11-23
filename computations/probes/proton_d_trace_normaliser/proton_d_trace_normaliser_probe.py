#!/usr/bin/env python3
"""q0 and m_p when the proton normaliser comes from a convention-D closure.

Pre-registered in PREREGISTRATION.md (same directory, committed first).
Diagnostics only: no arm is adopted. mpmath, 50 dps, no float64.
"""
import json
import pathlib
import sys

import mpmath as mp
from qou_substrate import constants as C

mp.mp.dps = 60
DPS = 50
D_REF = mp.mpf("0.99856216383678726595121313514665020209")  # registry, convention D


def trD(q):
    h = q - 1 / q
    return mp.fabs((4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4))


def q2(q):
    return q + 1 / q


def zD(q):
    return q**3 / (q**2 + 1)


ARMS = {
    "A0 [3]!/q^3 (production)": lambda q: (q**2 + 1 + q**-2) * q2(q) / q**3,
    "B0 1 (normalised trace)": lambda q: mp.mpf(1),
    "B1 [2]^2 (3-strand closure, loop [2])": lambda q: q2(q) ** 2,
    "B2 [2]^3 (quantum trace, delta^n)": lambda q: q2(q) ** 3,
    "B3 (1/z_D)^2 (Ocneanu closure)": lambda q: 1 / zD(q) ** 2,
}

vol = C.vol_4_1_at(DPS + 10)
mp_me = mp.mpf(C.MASS_RATIO_P_E_STR)
me = mp.mpf(str(C.M_E_MEV))
qmu = mp.mpf(C.Q_MUON_50_DIGIT_STR)
q_prod = C.q_at(DPS)


def ratio(q, N):
    return 2 * vol / (1 - 1 / q) ** 2 * trD(q) * N(q) - 12


gate_D = abs(trD(q_prod) - D_REF) < mp.mpf("1e-30")
rows = []
for name, N in ARMS.items():
    g = lambda q: ratio(q, N) - mp_me
    grid = [mp.mpf(1) + mp.mpf(k) / 400 for k in range(1, 801)]
    roots = [mp.findroot(g, (a, b), solver="anderson")
             for a, b in zip(grid, grid[1:]) if g(a) * g(b) < 0]
    row = {"arm": name, "N_at_q0": mp.nstr(N(q_prod), 12),
           "roots_in_(1,3)": [mp.nstr(r, 25) for r in roots]}
    if roots:
        r = min(roots, key=lambda x: abs(x - q_prod))
        row["q0"] = mp.nstr(r, 25)
        row["dq0_vs_A0_ppb"] = mp.nstr((r - q_prod) / q_prod * 10**9, 8)
    row["m_p_at_muon_pin_MeV"] = mp.nstr(me * ratio(qmu, N), 12)
    row["m_p_err_pct_muon_pin"] = mp.nstr((ratio(qmu, N) - mp_me) / mp_me * 100, 6)
    rows.append(row)

gate_q = abs(mp.mpf(rows[0]["q0"]) - q_prod) < mp.mpf("1e-22")
print("gate tr == registry D value:", gate_D, " gate A0 q0 == q_at:", gate_q)
for r in rows:
    print(json.dumps(r, ensure_ascii=False))
pathlib.Path(__file__).with_name("result.json").write_text(
    json.dumps({"gate_trace_is_D": gate_D, "gate_q0": gate_q, "rows": rows},
               indent=1, ensure_ascii=False))
sys.exit(0 if (gate_D and gate_q) else 1)
