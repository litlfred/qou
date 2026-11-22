#!/usr/bin/env python3
"""Exact check of the local relations behind QOU.QBeta.PairTermSectorSymmetry.readout_barSymm.

psi = transpose o Ad F o bar, with F the flip u <-> d on every strand and bar : q -> 1/q on
entries. psi reverses products and is a tensor product of one map per strand, so it is fixed by
its action on one crossing and on one site weight. Checked over Q(q) with sympy:

  (b1) psi(R) = R^{-1} and psi(R^{-1}) = R for the 4 x 4 Jimbo R-matrix, so psi(sigma_i) = sigma_i^{-1}
       on any number of strands;
  (b2) psi(k) = k for the site weight k = diag(q, 1/q), so psi(K^{(x)N}) = K^{(x)N} for every N and
       tr(K psi(x)) = bar(tr(K x)), with or without spectator strands;
  (b3) psi(sigma_a sigma_b^{-1}) = sigma_b sigma_a^{-1}, which the half twist Delta = sigma_a sigma_b sigma_a
       turns back into V = sigma_a sigma_b^{-1} (halfTwist_conj_left/right in Lean), so
       psi(C) = E C E^{-1} with E = Delta_A Delta_B; checked here on 3 strands.

F sends the block up-count a to 3 - a, so psi sends the sector (Q_A, Q_B) to (1 - Q_A, 1 - Q_B).
The end-to-end consequence, closure of the reachable span under the bar flip, is computed over
Q(q) for N = 6, 7, 8 by np_more_strands_symbolic_probe.py.

Run from the repo root:
  python3 computations/probes/np_splitting/np_pair_term_bar_symmetry_check.py
"""
import sympy as sp


def main():
    q = sp.Symbol("q")
    h = q - 1 / q
    R = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
    Ri = sp.simplify(R.inv())
    F1 = sp.Matrix([[0, 1], [1, 0]])
    F2 = sp.kronecker_product(F1, F1)

    def bar(M):
        return M.applyfunc(lambda x: sp.simplify(x.subs(q, 1 / q)))

    def psi(M, F):
        return sp.simplify(F * bar(M).T * F)

    checks = {}
    checks["(b1) psi(R) = R^-1"] = sp.simplify(psi(R, F2) - Ri) == sp.zeros(4)
    checks["(b1) psi(R^-1) = R"] = sp.simplify(psi(Ri, F2) - R) == sp.zeros(4)
    k = sp.diag(q, 1 / q)
    checks["(b2) psi(k) = k"] = sp.simplify(psi(k, F1) - k) == sp.zeros(2)

    I2 = sp.eye(2)
    s1, s2 = sp.kronecker_product(R, I2), sp.kronecker_product(I2, R)
    s1i, s2i = sp.kronecker_product(Ri, I2), sp.kronecker_product(I2, Ri)
    F3 = sp.kronecker_product(F1, F2)
    V = s1 * s2i
    lhs = psi(V, F3)
    checks["(b3) psi(V) = sigma_b sigma_a^-1"] = sp.simplify(lhs - s2 * s1i) == sp.zeros(8)
    Dl = s1 * s2 * s1
    checks["(b3) psi(V) = Delta V Delta^-1"] = sp.simplify(lhs - Dl * V * Dl.inv()) == sp.zeros(8)
    checks["(b3) psi(V^3) = Delta V^3 Delta^-1"] = sp.simplify(
        psi(V ** 3, F3) - Dl * V ** 3 * Dl.inv()) == sp.zeros(8)
    # F maps the up-count a of a block to 3 - a: Pi_a -> Pi_{3-a}
    for name, ok in checks.items():
        print(f"{'PASS' if ok else 'FAIL'}  {name}")
    print("ALL PASS" if all(checks.values()) else "SOME FAIL")
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
