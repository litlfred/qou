#!/usr/bin/env python3
"""Label C, option 2 first attempt: the single-quark E/F round trip (bean qou-99qc).

Beta decay changes ONE quark d -> u, so the natural label-C transition is a single-site raising
operator E_k on (C^2)^{x3}, not the coproduct Delta(E) (which commutes with the Hecke algebra and
cannot leave the nucleon's isospin-1/2 sector). A single-site E_k does reach isospin 3/2. This probe
builds A = sum_k E_k P_n F_k (P_n = nucleon (2,1) block at T3 = -1/2), reads the induced functional
tau_A(J) = Tr(K^{x3} A J) / Tr(K^{x3} A) on the chirality grading J, and the (3)-block fraction of
A, exactly over Q(q) (sympy). Both the bare and the coproduct-dressed (E (x) K) site operators are
evaluated; they agree. Q_beta = (h[2]/2) tau_A(J) E0 at the proton pin (mpmath, 50 dps).

Prints only; writes no witness; selects nothing. Result: a scope-(a) negative.
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


def build(q):
    h = q - 1 / q
    R = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
    I2 = sp.eye(2)
    s1, s2 = kp(R, I2), kp(I2, R)
    K, Ki = sp.diag(q, 1 / q), sp.diag(1 / q, q)
    E = sp.Matrix([[0, 1], [0, 0]])
    F = E.T
    K3 = kp(kp(K, K), K)
    num = sp.eye(8) + q * s1 + q * s2 + q**2 * s1 * s2 + q**2 * s2 * s1 + q**3 * s1 * s2 * s1
    P3 = sp.simplify(num / (1 + 2 * q**2 + 2 * q**4 + q**6))
    half = sp.Rational(1, 2)

    def t3(i):
        return sum(half if ((i >> k) & 1) == 0 else -half for k in range(3))

    Wn = sp.diag(*[1 if t3(i) == -half else 0 for i in range(8)])
    Pn = sp.simplify((sp.eye(8) - P3) * Wn)
    J = (s1 + s1.inv()) / (q + 1 / q)

    def site(op, k, right):
        m = [I2] * k + [op] + [right] * (2 - k)
        return kp(kp(m[0], m[1]), m[2])

    out = {}
    for lab, (rE, rF) in {"bare site operator": (I2, I2), "coproduct-dressed (E (x) K)": (K, Ki)}.items():
        A = sp.zeros(8)
        for k in range(3):
            A += site(E, k, rE) * Pn * site(F, k, rF)
        out[lab] = (sp.factor(sp.simplify((K3 * A * J).trace() / (K3 * A).trace())),
                    sp.factor(sp.simplify((K3 * P3 * A).trace() / (K3 * A).trace())))
    DE = sp.zeros(8)
    for k in range(3):
        DE += site(E, k, K)
    commutes = sp.simplify(DE * s1 - s1 * DE) == sp.zeros(8) and sp.simplify(DE * s2 - s2 * DE) == sp.zeros(8)
    return out, commutes


def main() -> int:
    mp.mp.dps = 50
    q = sp.symbols("q", positive=True)
    out, commutes = build(q)
    print(f"[{'PASS' if commutes else 'FAIL'}] Delta(E) = sum E_k with K on the right commutes with s1, s2 (Jimbo)")
    q0 = mp.mpf(str(q_at()))
    me = mp.mpf(str(M_E_MEV))
    QC = mp.mpf(Q_BETA_CODATA_STR)
    h, b2 = q0 - 1 / q0, q0 + 1 / q0
    E0 = me / (q0 * (q0 - 1))
    vals = []
    for lab, (tauJ, frac3) in out.items():
        y = mp.mpf(str(sp.N(tauJ.subs(q, sp.Rational(str(q0))), 40)))
        f3 = mp.mpf(str(sp.N(frac3.subs(q, sp.Rational(str(q0))), 40)))
        Qb = h * b2 / 2 * y * E0
        vals.append(tauJ)
        print(f"  {lab:30} tau_A(J) = {tauJ} = {mp.nstr(y, 10)}; (3)-block fraction = {mp.nstr(f3, 10)};"
              f" Q_beta = {mp.nstr(Qb, 8)} MeV ({mp.nstr((Qb / QC - 1) * 100, 5)} %)")
    same = sp.simplify(vals[0] - vals[1]) == 0
    print(f"[{'PASS' if same else 'FAIL'}] bare and dressed site operators give the same tau_A(J)")
    return 0 if (commutes and same) else 1


if __name__ == "__main__":
    raise SystemExit(main())
