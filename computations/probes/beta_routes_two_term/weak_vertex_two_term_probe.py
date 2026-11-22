"""Two-term weak-vertex form factor of the T(3,5) braid (σ₀σ₁)⁵ on V^{⊗3} (bean qou-99qc).

Owner ruling 2026-11-21: the two-term Lagrangian trace covers the β-decay half-life rate.
Cross-checks the closed forms of Lean `QOU.QBeta.WeakVertexTwoTerm` against the block engine
`two_term_engine.py` (exact ℚ(q)) for every quark/lepton colouring of the three vertex strands,
and prints t₂ and 2t₂/t₁ at the proton q₀ (70 dps). No witness; nothing is wired.

    PYTHONPATH=computations python3 -u computations/probes/beta_routes_two_term/weak_vertex_two_term_probe.py
"""
import itertools
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import two_term_engine as E  # noqa: E402
from sympy import Rational, factor, simplify, symbols, sympify  # noqa: E402
import mpmath as mp  # noqa: E402

mp.mp.dps = 70
Q0 = mp.mpf("1.1099785827513808")  # proton pin, qou_substrate.constants.Q (display/evaluation only)
qs = symbols("q")


def S(x):
    return factor(sympify(str(x.as_expr())).subs("q", qs))


def at_q0(expr):
    return mp.mpf(str(expr.subs(qs, sympify(mp.nstr(Q0, 70))).evalf(70)))


def main():
    E.use()
    rho = E.rho_blocks(3, [[(E.ONE, [0, 1] * 5)]])
    t1 = S(E.t_one(3, rho))
    lean_t1 = qs**2 * (qs**12 + qs**8 - 1) / (qs**2 + 1) ** 2
    assert simplify(t1 - lean_t1) == 0, "tOne_eq_weakVertexTrace"
    nrm = 1 + qs**2 + qs**4
    d = [1 / nrm, qs**2 / nrm, qs**4 / nrm]
    ok = 1
    t1v = at_q0(t1)
    print(f"t1 = {t1}   t1(q0) = {mp.nstr(t1v, 15)}")
    for col in itertools.product(("quark", "lepton"), repeat=3):
        t2 = S(E.t_two(col, rho, "cov"))
        # Lean tTwo_eq: (q κ₊ + q⁻¹ κ₋)(2q¹⁰+1)/(2[2]³), κ = Σ_b Q_b (d_b − 1/3)
        kap = {}
        for m in (1, -1):
            Qb = [sympify(str(E.qpair_diag(col, b))) for b in E.blocks(3)[m]]
            kap[m] = sum(Qb[i] * (d[i] - Rational(1, 3)) for i in range(3))
        lean_t2 = (qs * kap[1] + kap[-1] / qs) * (2 * qs**10 + 1) / (2 * (qs + 1 / qs) ** 3)
        same = simplify(t2 - lean_t2) == 0
        ok &= same
        v = at_q0(t2)
        print(f"{col}: t2 = {t2}  | t2(q0) = {mp.nstr(v, 10)}  2t2/t1 = {mp.nstr(2 * v / t1v, 10)}"
              f"  lean-form {'OK' if same else 'FAIL'}")
    lf = -2 * qs**2 * (qs**2 - 1) * (2 * qs**10 + 1) / (9 * (qs**2 + 1) ** 3)
    assert simplify(S(E.t_two(("lepton", "quark", "quark"), rho, "cov")) - lf) == 0, "tTwo_lepton_first"
    print("all colourings match tTwo_eq:", bool(ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
