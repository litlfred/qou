#!/usr/bin/env python3
"""Kashaev's quantum-dilogarithm R-matrix [Kas95] (q-alg/9504020,
`uploads/9504020v1.pdf`) — the root-of-unity r-matrix underlying the
descendant colored Jones / Kashaev link invariant.

Item #2 of the plan: the [Kas95] state-sum cross-check; also the shared
r-matrix foundation for the descendant route (#3) to c_σ.

Definitions (ω a primitive N-th root of unity):
  (ω)_n = ∏_{j=1}^n (1−ω^j),  0≤n<N            (2.1)
  θ(n)  = 1 if 0≤n<N else 0                      (2.3)
  [n]   = n mod N ∈ {0,…,N−1}                    (2.4)
  W(k,l,m,n) = N ω^{(l+m)(m+n)} θ([k]+[m]) θ([l]+[n])
               / ( (ω)_{[k]} (ω*)_{[l]} (ω)_{[m]} (ω*)_{[n]} )   (2.7)
  R(i,j,k,l|a,b,c,d) = ω^{a−k−j} W(j−i−a, i−l−d, l−k−c, k−j−b)   (2.8)
   with a+b+c+d ≡ 1 (mod N).                                     (2.9)

VALIDATED here against the paper's own symmetries (2.10),(2.11).
Audit-only; no wiring.
"""
from __future__ import annotations

import cmath
import math


class KashaevR:
    def __init__(self, N: int):
        self.N = N
        self.om = cmath.exp(2j * math.pi / N)
        self.oms = self.om.conjugate()

    def _poch(self, n, base):
        n %= self.N
        p = 1.0 + 0j
        for j in range(1, n + 1):
            p *= (1 - base ** j)
        return p

    def W(self, k, l, m, n):
        N = self.N
        rk, rl, rm, rn = k % N, l % N, m % N, n % N
        th1 = 1.0 if 0 <= rk + rm < N else 0.0
        th2 = 1.0 if 0 <= rl + rn < N else 0.0
        if th1 == 0.0 or th2 == 0.0:
            return 0j
        den = self._poch(rk, self.om) * self._poch(rl, self.oms) \
            * self._poch(rm, self.om) * self._poch(rn, self.oms)
        if den == 0:
            return 0j
        return N * self.om ** ((l + m) * (m + n)) * th1 * th2 / den

    def R(self, i, j, k, l, a, b, c, d):
        """Boltzmann weight (2.8); caller ensures a+b+c+d≡1 (mod N)."""
        return self.om ** (a - k - j) * self.W(j - i - a, i - l - d, l - k - c, k - j - b)


def _validate(N=5, trials=300, tol=1e-9):
    import random
    r = KashaevR(N)
    random.seed(1)
    ok10 = ok11 = True
    for _ in range(trials):
        i, j, k, l = (random.randint(0, N - 1) for _ in range(4))
        a, b, c = (random.randint(0, N - 1) for _ in range(3))
        d = (1 - a - b - c) % N
        v1 = r.R(i, j, k, l, a, b, c, d)
        if abs(v1 - r.R(k, l, i, j, c, d, a, b)) > tol:               # (2.10)
            ok10 = False
        if abs(v1 - r.R(-j, -i, -l, -k, a, d, c, b) * r.om ** (-i - j - k - l)) > tol:  # (2.11)
            ok11 = False
    return ok10, ok11


if __name__ == "__main__":
    for N in (3, 5, 7):
        a, b = _validate(N)
        print(f"N={N}: symmetry (2.10)={a}  (2.11)={b}")
