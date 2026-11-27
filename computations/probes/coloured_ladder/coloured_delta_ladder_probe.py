"""Coloured ring mass of the lepton ladder Delta^(2k+1) at every level N (no fitting).

Owner card 2026-11-27: "Coloured ring mass of Delta^n (all levels)". Words (owner ruling
22:37Z): e = Delta = s1 s2 s1, mu = Delta^3, tau = Delta^5 on three strands.

Level N = 2j + 1 is the U_q(sl2) spin-j module V_j. The braiding is the standard R-matrix
(Kassel conventions, Rcheck = P R). The pivotal trace uses K. The framing factor f per crossing is
fixed by stabilisation invariance, m(beta s_n) = m(beta), as in def:mass-identity. The ring mass is
m_N(beta) = f^{-w} tr(K^{x3} rho_N(beta)). At N = 2 it equals [2]^3 q^{-2w} tr_D (checked:
Delta -> [4]/q^3).

Twist structure (standard, checked here numerically): f = q^{2j(j+1)}. Delta^2 acts on the
spin-J isotypic part of V_j^{x3} by q^{2J(J+1) - 6j(j+1)}. So
m_N(Delta^(2k+1)) = sum_J a_J r_J^k with r_J = q^{2J(J+1) - 18j(j+1)}, and the largest
exponent (J = 3j) is -12j = -6(N-1) < 0. Lean: QOU/Observations/ColouredLadderTwist.lean.
Nothing is compared with a measured value.
"""
import sys
import numpy as np

Q0 = 1.1099785827513808  # display only; the substrate value is q_parameter.Q_50_DIGIT_STR
checks = []


def check(name, ok):
    checks.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name)


def qint(n, q):
    return (q**n - q**-n) / (q - 1 / q)


def qfact(n, q):
    r = 1.0
    for i in range(1, n + 1):
        r *= qint(i, q)
    return r


def rep(N, q):
    n = N - 1
    K = np.diag([q ** (n - 2 * p) for p in range(N)])
    E = np.zeros((N, N))
    F = np.zeros((N, N))
    for p in range(N):
        if p + 1 < N:
            F[p + 1, p] = qint(p + 1, q)
        if p >= 1:
            E[p - 1, p] = qint(n - p + 1, q)
    return K, E, F, [n - 2 * p for p in range(N)]


def rcheck(N, q):
    K, E, F, h = rep(N, q)
    D = np.diag([q ** (a * b / 2) for a in h for b in h])
    S = np.zeros((N * N, N * N))
    Ek, Fk = np.eye(N), np.eye(N)
    for k in range(N):
        S += q ** (k * (k - 1) / 2) * (q - 1 / q) ** k / qfact(k, q) * np.kron(Ek, Fk)
        Ek, Fk = Ek @ E, Fk @ F
    P = np.zeros((N * N, N * N))
    for i in range(N):
        for j in range(N):
            P[j * N + i, i * N + j] = 1
    return P @ D @ S, K


def ring_mass(N, q, word):
    Rc, K = rcheck(N, q)
    Id = np.eye(N)
    g = {1: np.kron(Rc, Id), 2: np.kron(Id, Rc)}
    g[-1], g[-2] = np.linalg.inv(g[1]), np.linalg.inv(g[2])
    M = np.eye(N**3)
    w = 0
    for s in word:
        M = M @ g[s]
        w += 1 if s > 0 else -1
    f = np.trace(np.kron(K, K) @ Rc) / qint(N, q)
    return np.trace(np.kron(np.kron(K, K), K) @ M) * f ** (-w)


DELTA = [1, 2, 1]
q = Q0
check("N=2: m(Delta) = [4]/q^3", abs(ring_mass(2, q, DELTA) - qint(4, q) / q**3) < 1e-9)
for N in range(2, 7):
    j = (N - 1) / 2
    Rc, K = rcheck(N, q)
    f = np.trace(np.kron(K, K) @ Rc) / qint(N, q)
    check(f"N={N}: framing f = q^(2j(j+1))", abs(np.log(f) / np.log(q) - 2 * j * (j + 1)) < 1e-6)
    check(f"N={N}: stabilisation m(s1 s2) = [N]", abs(ring_mass(N, q, [1, 2]) - qint(N, q)) < 1e-6 * qint(N, q))
    g1, g2 = np.kron(Rc, np.eye(N)), np.kron(np.eye(N), Rc)
    D2 = g1 @ g2 @ g1 @ g1 @ g2 @ g1
    ev = np.log(np.linalg.eigvals(D2).real) / np.log(q)
    allowed = [2 * J * (J + 1) - 6 * j * (j + 1) for J in np.arange(j % 1, 3 * j + 0.5, 1.0)]
    check(f"N={N}: Delta^2 eigenvalues are q^(2J(J+1)-6j(j+1))",
          all(min(abs(e - a) for a in allowed) < 1e-5 for e in ev))
    # r_J = (Delta^2 eigenvalue) * f^-6, f = q^(2j(j+1)); largest at J = 3j
    check(f"N={N}: top ratio exponent = -6(N-1)",
          abs(max(allowed) - 12 * j * (j + 1) + 6 * (N - 1)) < 1e-9)

print()
print(f"{'N':>2s} {'m(Delta)':>10s} {'mu/e':>10s} {'tau/e':>10s}   {'mirror mu/e':>12s} {'mirror tau/e':>12s}")
for N in range(2, 7):
    m = [ring_mass(N, q, DELTA * (2 * k + 1)) for k in range(3)]
    mi = [ring_mass(N, q, [-1, -2, -1] * (2 * k + 1)) for k in range(3)]
    print(f"{N:>2d} {m[0]:>10.5g} {m[1]/m[0]:>10.5g} {m[2]/m[0]:>10.5g}   {mi[1]/mi[0]:>12.5g} {mi[2]/mi[0]:>12.5g}")
    check(f"N={N}: ladder strictly lighter (q>1)", m[0] > m[1] > m[2] > 0)
print()
print(f"{sum(checks)}/{len(checks)} checks pass")
sys.exit(0 if all(checks) else 1)
