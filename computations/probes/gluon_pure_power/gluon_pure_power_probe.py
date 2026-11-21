#!/usr/bin/env python3
"""Gluon segment: which pure power of the chiral vertex is admissible? (bean qou-99qc, Q1)

Companion to QOU/QBeta/GluonVertexPurePower.lean, which proves q-generically:
  * on the (2,1) block of H_3(q), V = sigma0 sigma1^{-1} has det 1 and trace
    t = -(q^2 - 1 + q^-2) <= -1;
  * s_k = chi_(2,1)(V^k) obeys s_{k+2} = t s_{k+1} - s_k;
  * if t^2 < 2 then s_1 < 0, s_2 < 0, s_3 > 0 (V^3 is the least admissible
    positive power under reading 3); the window edges are t^2 = 2 and t^2 = 3.

This probe does what the Lean deliberately does not: it evaluates the
hypothesis t^2 < 2 at the substrate pin q0 (read from the substrate, proton
anchor) and maps the q-windows. It also lists, for k <= 30, which powers are
admissible at q0, so the periodicity is visible. Exact sympy for the
q-window endpoints; mpmath (no float) for evaluations.
"""
from __future__ import annotations

import json
import pathlib
import sys

import mpmath as mp
import sympy as sp

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402  (proton pin)

DPS = 60


def main() -> int:
    mp.mp.dps = DPS
    q = sp.symbols("q", positive=True)
    qi = 1 / q
    I2 = sp.eye(2)
    S0 = sp.Matrix([[q, 1], [0, -qi]])
    S1 = sp.Matrix([[-qi, 0], [1, q]])
    S1i = S1 - (q - qi) * I2
    checks = {}
    checks["braid"] = sp.simplify(S0 * S1 * S0 - S1 * S0 * S1) == sp.zeros(2)
    checks["hecke0"] = sp.simplify(S0 * S0 - (q - qi) * S0 - I2) == sp.zeros(2)
    checks["hecke1"] = sp.simplify(S1 * S1 - (q - qi) * S1 - I2) == sp.zeros(2)
    checks["inverse"] = sp.simplify(S1 * S1i - I2) == sp.zeros(2)
    V = sp.simplify(S0 * S1i)
    t = sp.simplify(V.trace())
    checks["det_V_is_1"] = sp.simplify(V.det() - 1) == 0
    checks["trace_V"] = sp.simplify(t + (q**2 - 1 + q**-2)) == 0
    # closed forms vs direct powers, k <= 8
    s = [sp.Integer(2), t]
    for k in range(2, 9):
        s.append(sp.expand(t * s[-1] - s[-2]))
    checks["chebyshev_matches_powers_k_le_8"] = all(
        sp.simplify((V**k).trace() - s[k]) == 0 for k in range(9))
    # exact q-window edges: t^2 = 2 and t^2 = 3 with q > 1
    edge2 = [r for r in sp.solve(sp.Eq(t**2, 2), q) if r.is_real and r > 1]
    edge3 = [r for r in sp.solve(sp.Eq(t**2, 3), q) if r.is_real and r > 1]
    q2 = mp.mpf(sp.N(edge2[0], DPS))
    q3 = mp.mpf(sp.N(edge3[0], DPS))

    q0 = mp.mpf(Q_50_DIGIT_STR)
    tq = -(q0**2 - 1 + q0**-2)
    sv = [mp.mpf(2), tq]
    for k in range(2, 31):
        sv.append(tq * sv[-1] - sv[-2])
    admissible = [k for k in range(1, 31) if sv[k] >= 0]
    theta = mp.acos(tq / 2)
    checks["t_sq_lt_2_at_q0"] = bool(tq**2 < 2)
    checks["s1_s2_neg_s3_pos_at_q0"] = bool(sv[1] < 0 and sv[2] < 0 and sv[3] > 0)
    first_non_mult3 = next((k for k in admissible if k % 3), None)
    out = {
        "dps": DPS,
        "q0Anchor": "proton",
        "q0Value": Q_50_DIGIT_STR,
        "lean": "QOU.QBeta.GluonVertexPurePower.least_admissible_power",
        "t_at_q0": mp.nstr(tq, 30),
        "t_sq_at_q0": mp.nstr(tq**2, 30),
        "rotation_angle_over_2pi_at_q0": mp.nstr(theta / (2 * mp.pi), 30),
        "q_edge_t_sq_eq_2": mp.nstr(q2, 30),
        "q_edge_t_sq_eq_3": mp.nstr(q3, 30),
        "s_k_at_q0": {str(k): mp.nstr(sv[k], 20) for k in range(0, 31)},
        "admissible_k_le_30_at_q0": admissible,
        "first_admissible_k_not_multiple_of_3": first_non_mult3,
        "checks": checks,
    }
    out["allPassed"] = all(checks.values())
    print(json.dumps({k: out[k] for k in out if k != "s_k_at_q0"}, indent=1))
    HERE.with_name("gluon-pure-power.witness.json").write_text(json.dumps(out, indent=1) + "\n")
    return 0 if out["allPassed"] else 1


if __name__ == "__main__":
    sys.exit(main())
