#!/usr/bin/env python3
"""Label C (T3 flavour) for Q_beta: what the quantum trace gives (bean qou-99qc, owner '3 2').

QBetaChiralityReduction.lean: Q_beta = (h[2]/2) * y3 * E0 with y3 = tau(J), J = (s1 + s1^-1)/[2].
Label C puts u, d at the T3 = +-1/2 weights of V = C^2 (u = e1, OverStrandWeight.lean),
H_3 acting on V^{x3} through the Jimbo R-matrix, which commutes with U_q(gl2), so no braid word
changes T3 (qou-0whz C2). This probe evaluates tau(J) for the natural quantum-trace restrictions,
exactly over Q(q) (sympy), and prints Q_beta at the proton pin (mpmath, 50 dps).

Prints only; writes no witness; selects nothing.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402,F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from sympy import kronecker_product as kp  # noqa: E402

from qou_substrate.constants import q_at  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

Q_BETA_CODATA_STR = "0.78233341"  # comparison only


def exact() -> tuple[dict[str, sp.Expr], list[tuple[str, bool]]]:
    q = sp.symbols("q", positive=True)
    h = q - 1 / q
    R = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
    I2 = sp.eye(2)
    s1, s2 = kp(R, I2), kp(I2, R)
    K = sp.diag(q, 1 / q)
    K3 = kp(kp(K, K), K)
    J = (s1 + s1.inv()) / (q + 1 / q)
    half = sp.Rational(1, 2)

    def t3(i: int) -> sp.Rational:
        return sum(half if ((i >> k) & 1) == 0 else -half for k in range(3))

    def wproj(w):
        return sp.diag(*[1 if t3(i) == w else 0 for i in range(8)])

    # isospin sectors via the H_3 central element: the (3) block is where s1 = s2 = q.
    # Its projector on V^{x3} is the q-symmetriser; the (2,1) block is the rest of the
    # T3 = +-1/2 weight spaces (no (1^3) block on C^2, y_(1^3) = 0 automatically).
    # q-symmetriser P3 = (1 + q s1 + q s2 + q^2 s1 s2 + q^2 s2 s1 + q^3 s1 s2 s1)/[3]!_{q^2-style}
    num = sp.eye(8) + q * s1 + q * s2 + q**2 * s1 * s2 + q**2 * s2 * s1 + q**3 * s1 * s2 * s1
    P3 = sp.simplify(num / (1 + 2 * q**2 + 2 * q**4 + q**6))
    P21 = sp.eye(8) - P3

    def tau(P):
        return sp.factor(sp.simplify((K3 * P * J).trace() / (K3 * P).trace()))

    vals = {
        "whole V^x3 (quantum trace)": tau(sp.eye(8)),
        "T3 = +1/2 weight space (proton charge sector)": tau(wproj(half)),
        "T3 = -1/2 weight space (neutron charge sector)": tau(wproj(-half)),
        "isospin-1/2 = H3 (2,1) block (nucleon)": tau(P21),
        "isospin-3/2 = H3 (3) block": tau(P3),
    }
    checks = [
        ("Hecke relation", sp.simplify(R * R - h * R - sp.eye(4)) == sp.zeros(4)),
        ("braid relation", sp.simplify(s1 * s2 * s1 - s2 * s1 * s2) == sp.zeros(8)),
        ("P3 idempotent", sp.simplify(P3 * P3 - P3) == sp.zeros(8)),
        ("whole-space quantum trace = convention-D y3",
         sp.simplify(vals["whole V^x3 (quantum trace)"] - (q**4 + 1) / (q**2 + 1) ** 2) == 0),
        ("nucleon (2,1) block gives 0 (cf. chi21_deltaS)", sp.simplify(vals["isospin-1/2 = H3 (2,1) block (nucleon)"]) == 0),
    ]
    return {k: (v, q) for k, v in vals.items()}, checks


def main() -> int:
    mp.mp.dps = 50
    QC = mp.mpf(Q_BETA_CODATA_STR)
    vals, checks = exact()
    ok = True
    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
        ok &= passed
    q0 = mp.mpf(str(q_at()))
    me = mp.mpf(str(M_E_MEV))
    h, b2 = q0 - 1 / q0, q0 + 1 / q0
    E0 = me / (q0 * (q0 - 1))
    print(f"\nproton pin; y3 needed for CODATA (order-zero E0) = {mp.nstr(QC / (h * b2 / 2 * E0), 10)}")
    for name, (expr, q) in vals.items():
        y = mp.mpf(str(sp.N(expr.subs(q, sp.Rational(str(q0))), 40))) if expr.free_symbols else mp.mpf(str(sp.N(expr, 40)))
        Qb = h * b2 / 2 * y * E0
        print(f"  {name:48} tau(J) = {str(expr):28} = {mp.nstr(y, 8):>10}  Q_beta = {mp.nstr(Qb, 8)} MeV"
              f" ({mp.nstr((Qb / QC - 1) * 100, 5)} %)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
