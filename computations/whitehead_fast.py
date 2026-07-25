#!/usr/bin/env python3
"""Fast (numpy complex128) port of the validated U_q(sl₂) colored-Jones
machinery, for volume identification and the c₀ tower where pure-mpmath
N^m dense algebra is too slow.

Cross-checked against the mpmath machinery (whitehead_colored_jones.py) at
small N; used only where float64 precision suffices (link identification by
volume; leading-order growth).  The final high-precision c₀ extraction on
the identified word falls back to mpmath.

Audit-only; no wiring.
"""
from __future__ import annotations

import numpy as np


def qint(n, q):
    if abs(q - 1) < 1e-15:
        return complex(n)
    return (q**n - q**(-n)) / (q - q**(-1))


def qfact(n, q):
    r = 1.0 + 0j
    for k in range(1, n + 1):
        r *= qint(k, q)
    return r


def generators(N, q):
    E = np.zeros((N, N), dtype=complex)
    F = np.zeros((N, N), dtype=complex)
    Kd = np.zeros(N, dtype=complex)          # K diagonal
    for i in range(N):
        Kd[i] = q**(N - 1 - 2 * i)
        if i - 1 >= 0:
            E[i - 1, i] = qint(N - i, q)
        if i + 1 <= N - 1:
            F[i + 1, i] = qint(i + 1, q)
    return E, F, Kd


def r_check(N, q):
    E, F, Kd = generators(N, q)
    w = np.array([N - 1 - 2 * i for i in range(N)])
    # q^{H⊗H/2} diagonal on v_i⊗v_j
    D = np.zeros(N * N, dtype=complex)
    for i in range(N):
        for j in range(N):
            D[i * N + j] = q ** (0.5 * w[i] * w[j])
    # Σ_n q^{n(n-1)/2}(q-q⁻¹)^n/[n]! E^n⊗F^n
    S = np.zeros((N * N, N * N), dtype=complex)
    En = np.eye(N, dtype=complex)
    Fn = np.eye(N, dtype=complex)
    for n in range(N):
        coeff = q**(0.5 * n * (n - 1)) * (q - q**(-1))**n / qfact(n, q)
        S += coeff * np.kron(En, Fn)
        En = En @ E
        Fn = Fn @ F
    R = (D[:, None]) * S
    # permutation P
    P = np.zeros((N * N, N * N), dtype=complex)
    for i in range(N):
        for j in range(N):
            P[j * N + i, i * N + j] = 1
    Rc = P @ R
    Rci = np.linalg.inv(Rc)
    return Rc, Rci


def braid_rep(word, m, N, Rc, Rci):
    dim = N ** m
    rho = np.eye(dim, dtype=complex)
    for g in word:
        i = abs(g)
        block = Rc if g > 0 else Rci
        left = np.eye(N ** (i - 1), dtype=complex)
        right = np.eye(N ** (m - i - 1), dtype=complex)
        op = np.kron(np.kron(left, block), right)
        rho = op @ rho
    return rho


def closure_norm(word, m, N, q):
    """Normalized closure invariant raw/[N], raw = tr(K^{⊗m} ρ(word))."""
    Rc, Rci = r_check(N, q)
    rho = braid_rep(word, m, N, Rc, Rci)
    _, _, Kd = generators(N, q)
    dim = N ** m
    # μ = K^{⊗m}: weight of basis index x = ∏ Kd[digit]
    idx = np.arange(dim)
    mu = np.ones(dim, dtype=complex)
    y = idx.copy()
    for _ in range(m):
        mu *= Kd[y % N]
        y //= N
    raw = np.sum(mu * np.diag(rho))
    return raw / qint(N, q)


def perm_cycles(word, m):
    perm = list(range(m))
    for g in word:
        i = abs(g) - 1
        perm[i], perm[i + 1] = perm[i + 1], perm[i]
    seen = [False] * m
    cyc = 0
    for s in range(m):
        if not seen[s]:
            cyc += 1
            j = s
            while not seen[j]:
                seen[j] = True
                j = perm[j]
    return cyc


def volume_estimate(word, m, Ns, delta=1e-8):
    """(2π/N) log|norm| at q = e^{iπ(1-δ)/N}, Richardson in (log N)/N."""
    import math
    rows = []
    prev = None
    for N in Ns:
        theta = math.pi * (1 - delta) / N
        q = complex(math.cos(theta), math.sin(theta))
        val = abs(closure_norm(word, m, N, q))
        est = (2 * math.pi / N) * math.log(val) if val > 0 else float("nan")
        rich = None
        if prev is not None:
            Np, ep = prev
            xp = math.log(Np) / Np
            xn = math.log(N) / N
            rich = (ep * xn - est * xp) / (xn - xp)
        prev = (N, est)
        rows.append((N, est, rich))
    return rows


if __name__ == "__main__":
    print("Fast numpy machinery — figure-eight volume self-test (target 2.02988):")
    for delta in (1e-6, 1e-8, 1e-10):
        rows = volume_estimate([1, -2, 1, -2], 3, [4, 6, 8, 10], delta=delta)
        best = rows[-1][2]
        print(f"  δ={delta:.0e}: " + "  ".join(
            f"N={N}:{(f'{r:.4f}' if r is not None else est.__format__('.4f'))}"
            for N, est, r in rows) + f"   best={best:.5f}")
