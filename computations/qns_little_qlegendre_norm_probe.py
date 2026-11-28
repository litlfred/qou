#!/usr/bin/env python3
"""Exact check of the little q-Legendre norm on the O_q(SU(2)) Cartan block.

Bean qou-q3dc. Lean: QOU/FluidDynamics/q_ns_triad_raising_coupling.lean reduces the
spin-raising triad coupling to the Haar norms h(P_n^2) of the monic orthogonal
polynomials in zeta = beta*gamma. This probe checks, in exact rational arithmetic
(fractions.Fraction, no floats), that for monic P_n

    h(P_n^2) = q^(-2n) p^(n^2) (p;p)_n^4 (1-p) / ((p;p)_{2n} (p;p)_{2n+1}),  p = q^-2,

using only the Haar moments h(zeta^m) = (-q)^m / [m+1]_{q^2} (haarState_zetaB_pow).
It is evidence for the GAP stated in the Lean file, not a proof. No empirical input.
"""
from fractions import Fraction as F
import sys


def check(q: F, nmax: int) -> bool:
    def qs(m):
        return sum(q ** (2 * i) for i in range(m + 1))

    def h(a):
        return sum(c * (-q) ** i / qs(i) for i, c in enumerate(a))

    def mul(a, b):
        r = [F(0)] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                r[i + j] += x * y
        return r

    p = 1 / q ** 2

    def poch(n):
        r = F(1)
        for i in range(1, n + 1):
            r *= 1 - p ** i
        return r

    basis, norms, ok = [], [], True
    for n in range(nmax + 1):
        f = [F(0)] * n + [F(1)]
        for b, nb in zip(basis, norms):
            c = h(mul(f, b)) / nb
            f = [x - c * (b[i] if i < len(b) else 0) for i, x in enumerate(f)]
        basis.append(f)
        norms.append(h(mul(f, f)))
        pred = q ** (-2 * n) * p ** (n * n) * poch(n) ** 4 * (1 - p) / (poch(2 * n) * poch(2 * n + 1))
        good = norms[-1] == pred
        ok &= good
        print(f"q={q} n={n} exact_match={good}")
    return ok


if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    allok = all(check(F(s), nmax) for s in ("2", "3/2", "5/4", "7/3"))
    print("ALL EXACT" if allok else "MISMATCH")
    sys.exit(0 if allok else 1)
