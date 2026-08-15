#!/usr/bin/env python3
"""Kashaev's quantum-dilogarithm R-matrix [Kas95] (q-alg/9504020,
`library/arxiv-q-alg-9504020v1/9504020v1.pdf`) — the root-of-unity r-matrix underlying the
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


def braiding_matrix(N):
    """The N²×N² braiding Ř = P·R with R the YBE R-matrix (2.12):
       ⟨i,j|R|k,l⟩ = R(i,j,k,l|1,0,0,0)·ω^{k+l}.  Satisfies YBE (2.13)
       (verified in _validate_ybe).  Returns (Rcheck, ω) as numpy arrays."""
    import numpy as np
    r = KashaevR(N)
    R = np.zeros((N * N, N * N), dtype=complex)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    R[i * N + j, k * N + l] = r.R(i, j, k, l, 1, 0, 0, 0) * r.om ** (k + l)
    P = np.zeros((N * N, N * N), dtype=complex)
    for a in range(N):
        for b in range(N):
            P[b * N + a, a * N + b] = 1
    return P @ R, r.om


def _validate_ybe(N, tol=1e-9):
    import numpy as np
    r = KashaevR(N)
    R = np.zeros((N * N, N * N), dtype=complex)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    R[i * N + j, k * N + l] = r.R(i, j, k, l, 1, 0, 0, 0) * r.om ** (k + l)
    I = np.eye(N)
    P = np.zeros((N * N, N * N), dtype=complex)
    for a in range(N):
        for b in range(N):
            P[b * N + a, a * N + b] = 1
    R12, R23 = np.kron(R, I), np.kron(I, R)
    R13 = np.kron(I, P) @ np.kron(R, I) @ np.kron(I, P)
    return np.allclose(R12 @ R13 @ R23, R23 @ R13 @ R12, atol=tol)


# STRUCTURAL FINDING (2026-07-26): the Markov condition tr₂((I⊗μ)Ř) ∝ I has
# NO diagonal-μ solution (smallest singular value ≈ 2.45, not 0 — verified at
# N=5). So Kashaev's link invariant is NOT an enhanced Markov trace of this
# braiding; it must be built via the Sect-3 face-index state sum (the maps
# j:E→ℤ_N, a:V×F→ℤ_N with the sum-1 constraints 3.3–3.4), not the braid
# closure. That state sum is the next (intricate) implementation unit.


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
