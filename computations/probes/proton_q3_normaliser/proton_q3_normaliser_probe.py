#!/usr/bin/env python3
"""q0, m_p and Q_beta under alternative /q^3 normalisers.

Pre-registered in PREREGISTRATION.md (same directory, committed first).
Diagnostics only: no arm is adopted on these numbers. mpmath, 50 dps, no float64.
"""
import json
import pathlib
import sys

import mpmath as mp
from qou_substrate import constants as C

mp.mp.dps = 60
DPS = 50


def trM(q):
    h = q - 1 / q
    return mp.fabs((4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4))


def f3(q):
    return (q**2 + 1 + q**-2) * (q + 1 / q)


ARMS = {
    "A0 [3]!/q^3 (production, c_sign)": lambda q: f3(q) / q**3,
    "A1 [3]! (bar-symmetric)": lambda q: f3(q),
    "A2 q^3 [3]! (c_triv)": lambda q: q**3 * f3(q),
    "A3 [2][3]!/q^3 (idempotent coord)": lambda q: (q + 1 / q) * f3(q) / q**3,
    "A4 [3]!/(q^4(q^2-1)(q^2+1)^2) (Wenzl a coord)":
        lambda q: f3(q) / (q**4 * (q**2 - 1) * (q**2 + 1) ** 2),
}

vol = C.vol_4_1_at(DPS + 10)
mp_me = mp.mpf(C.MASS_RATIO_P_E_STR)
me = mp.mpf(str(C.M_E_MEV))
qmu = mp.mpf(C.Q_MUON_50_DIGIT_STR)
q_prod = C.q_at(DPS)


def ratio(q, N):
    return 2 * vol / (1 - 1 / q) ** 2 * trM(q) * N(q) - 12


def R_qbeta(q):
    P = q**12 - 3 * q**10 + 3 * q**8 - 5 * q**6 + 3 * q**4 - 3 * q**2 + 1
    return -(q + 1) * P / (q**3 * (2 * q - 1) * (q**2 + 1) ** 3)


QBETA_CODATA = mp.mpf("0.78233")  # comparison value used on the scorecard (MeV)

rows = []
for name, N in ARMS.items():
    g = lambda q: ratio(q, N) - mp_me
    grid = [mp.mpf(1) + mp.mpf(k) / 200 for k in range(1, 201)]
    roots = []
    for a, b in zip(grid, grid[1:]):
        if g(a) * g(b) < 0:
            roots.append(mp.findroot(g, (a, b), solver="anderson"))
    row = {"arm": name, "roots_in_(1,2)": [mp.nstr(r, 25) for r in roots]}
    if roots:
        r = min(roots, key=lambda x: abs(x - q_prod))
        row["q0"] = mp.nstr(r, 25)
        row["dq0_vs_A0_ppb"] = mp.nstr((r - q_prod) / q_prod * 10**9, 8)
        qb = me * R_qbeta(r)
        row["Qbeta_MeV_at_q0"] = mp.nstr(qb, 12)
        row["Qbeta_err_pct"] = mp.nstr((qb - QBETA_CODATA) / QBETA_CODATA * 100, 6)
    mpm = me * ratio(qmu, N)
    row["m_p_at_muon_pin_MeV"] = mp.nstr(mpm, 12)
    row["m_p_err_pct_muon_pin"] = mp.nstr((ratio(qmu, N) - mp_me) / mp_me * 100, 6)
    rows.append(row)

# Gate: A0 must reproduce production.
a0 = rows[0]
gate_q = abs(mp.mpf(a0["q0"]) - q_prod) < mp.mpf("1e-22")
gate_qb = abs(mp.mpf(a0["Qbeta_MeV_at_q0"]) - mp.mpf("0.325433929")) < mp.mpf("1e-9")
print("gate A0 q0 == q_at:", gate_q, " gate A0 Q_beta == 0.325433929:", gate_qb)
for r in rows:
    print(json.dumps(r, ensure_ascii=False))
out = pathlib.Path(__file__).with_name("result.json")
out.write_text(json.dumps({"gate_q0": gate_q, "gate_qbeta": gate_qb, "rows": rows},
                          indent=1, ensure_ascii=False))
sys.exit(0 if (gate_q and gate_qb) else 1)
