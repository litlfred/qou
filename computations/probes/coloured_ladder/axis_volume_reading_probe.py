"""Volume reading of closure ∪ axis at the root of unity (no fitting to data, no comparison
with any measured mass).

Owner card 2026-11-28: "Volume reading at roots of unity". Least-trace ladder (ruling 23:35Z):
e = s1 s2 s1, mu = s1^2 s2^-1, tau = s1^4 s2^-1. The complement of closure(beta) ∪ axis is the
mapping torus of beta on the 3-punctured disc; its hyperbolic volume is 0 (e, periodic),
5.33349 (mu, the magic manifold) and 6.35459 (tau). These are cited/computed geometric
constants, not measurements.

Cut invariant. All components coloured N, q = e^{i pi/N} (Kashaev's root; Murakami's e^{2 pi i/N}
in q^2), axis cut open: c_N(beta) Id_N. Lean (QOU/Observations/AxisKashaevReading.lean):
c_N = f^-6 sum_a mu_a(beta) a (-1)^(a-1), with mu_a = T_a - T_{a+2} from the traces T_w of the
framed braid on the weight-w subspaces of V^{x3} (exact at the root, no division by [N]).

Checks:
1. Convention: the 3-strand cut of (s1 s2^-1)^2 (4_1) equals the Kashaev sum at N = 2..6.
2. The weight-space formula equals the 4-strand brute-force cut, N = 2..6.
3. e: |c_N| <= N^2 for N <= 24 (polynomial growth, volume 0).
4. mu: fitting log|c_N| = V N/2pi + a log N + b + c/N on 4 consecutive N (an asymptotic
   extrapolation in N, not a fit to data) gives V within 0.01 of 5.33349 and a within 0.05 of 3/2.
5. tau: the window estimate 2pi[log c_N - log c_{N-8} - 1.5 log(N/(N-8))]/8, N = 20..24, lies
   within 0.1 of 6.35459. Double precision holds to N ~ 25 (the R-matrix condition number grows
   like e^{cN} at the root); an arb-ball run confirmed the double values to N = 20.
"""
import cmath
import math
from collections import defaultdict

import numpy as np

checks = []


def check(name, ok):
    checks.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name)


def qint(n, q):
    return (q**n - q**-n) / (q - 1 / q)


def rep(N, q):
    n = N - 1
    K = np.diag([q ** (n - 2 * p) for p in range(N)]).astype(complex)
    E = np.zeros((N, N), complex)
    F = np.zeros((N, N), complex)
    for p in range(N):
        if p + 1 < N:
            F[p + 1, p] = qint(p + 1, q)
        if p >= 1:
            E[p - 1, p] = qint(n - p + 1, q)
    return K, E, F, [n - 2 * p for p in range(N)]


def rcheck(N, t):
    q = cmath.exp(t)
    K, E, F, h = rep(N, q)
    D = np.diag([cmath.exp(t * a * b / 2) for a in h for b in h])
    S = np.zeros((N * N, N * N), complex)
    Ek, Fk, fact = np.eye(N), np.eye(N), 1
    for k in range(N):
        if k > 0:
            fact *= qint(k, q)
        S += cmath.exp(t * k * (k - 1) / 2) * (q - 1 / q) ** k / fact * np.kron(Ek, Fk)
        Ek, Fk = Ek @ E, Fk @ F
    P = np.zeros((N * N, N * N))
    for i in range(N):
        for j in range(N):
            P[j * N + i, i * N + j] = 1
    return P @ D @ S, K


LOOP = [3, 2, 1, 1, 2, 3]
WORDS = {"e": [1, 2, 1], "mu": [1, 1, -2], "tau": [1, 1, 1, 1, -2]}
VOL = {"mu": 5.33348956690, "tau": 6.35459}


def framing(N, t):
    return cmath.exp(t * (N * N - 1) / 2)


def cut_brute(N, t, word, strands):
    Rc, K = rcheck(N, t)
    Ki = np.linalg.inv(K)  # pivotal element in this convention
    g = {}
    for i in range(1, strands):
        g[i] = np.kron(np.kron(np.eye(N ** (i - 1)), Rc), np.eye(N ** (strands - 1 - i)))
        g[-i] = np.linalg.inv(g[i])
    M = np.eye(N**strands, dtype=complex)
    for s in word:
        M = M @ g[s]
    piv = np.eye(1)
    for _ in range(strands - 1):
        piv = np.kron(piv, Ki)
    T = (np.kron(piv, np.eye(N)) @ M).reshape([N] * (2 * strands))
    letters = "abcdefg"[: strands - 1]
    cut = np.einsum(f"{letters}i{letters}j->ij", T)
    w = sum(1 if s > 0 else -1 for s in word)
    return cut * framing(N, t) ** (-w)


def cut_axis(N, t, word):
    Rc, K = rcheck(N, t)
    Rci = np.linalg.inv(Rc)
    n = N - 1
    wr = sum(1 if s > 0 else -1 for s in word)
    f = framing(N, t)
    groups = defaultdict(list)
    for p1 in range(N):
        for p2 in range(N):
            for p3 in range(N):
                groups[3 * n - 2 * (p1 + p2 + p3)].append((p1, p2, p3))
    T = {}
    for w2, S in groups.items():
        if w2 < 0:
            continue
        pos = {x: i for i, x in enumerate(S)}
        d = len(S)
        G = {}
        for s in set(word):
            gen, R = abs(s), (Rc if s > 0 else Rci)
            M = np.zeros((d, d), complex)
            for (p1, p2, p3), i in pos.items():
                if gen == 1:
                    tot = p1 + p2
                    for a in range(max(0, tot - n), min(n, tot) + 1):
                        M[pos[(a, tot - a, p3)], i] = R[a * N + tot - a, p1 * N + p2]
                else:
                    tot = p2 + p3
                    for a in range(max(0, tot - n), min(n, tot) + 1):
                        M[pos[(p1, a, tot - a)], i] = R[a * N + tot - a, p2 * N + p3]
            G[s] = M
        B = np.eye(d, dtype=complex)
        for s in word:
            B = B @ G[s]
        T[w2] = np.trace(B) * f ** (-wr)
    tot = 0
    for w2 in T:
        d = w2 + 1
        tot += (T[w2] - T.get(w2 + 2, 0)) * d * (-1) ** (d - 1)
    return tot * f ** (-6)


def main():
    for N in range(2, 7):
        t = 1j * math.pi / N
        c = cut_brute(N, t, [1, -2, 1, -2], 3)
        Q = cmath.exp(2j * math.pi / N)
        kas = sum(abs(np.prod([1 - Q**k for k in range(1, m + 1)])) ** 2 for m in range(N))
        check(f"4_1 cut = Kashaev sum at N={N}", abs(c[0, 0] - kas) < 1e-8 * kas)
        for nm, w in WORDS.items():
            cb = cut_brute(N, t, w + LOOP, 4)
            check(f"cut is scalar and weight formula matches brute force, N={N} {nm}",
                  np.abs(cb - cb[0, 0] * np.eye(N)).max() < 1e-8 * max(1, abs(cb[0, 0]))
                  and abs(cut_axis(N, t, w) - cb[0, 0]) < 1e-8 * max(1, abs(cb[0, 0])))
    rows = {}
    for N in range(2, 25):
        t = 1j * math.pi / N
        rows[N] = {nm: abs(cut_axis(N, t, w)) for nm, w in WORDS.items()}
    print("\n N   |c(e)|        |c(mu)|       |c(tau)|")
    for N in sorted(rows):
        print(f"{N:3d}  {rows[N]['e']:.5e}  {rows[N]['mu']:.5e}  {rows[N]['tau']:.5e}")
    check("e: |c_N| <= N^2 for N <= 24 (volume 0)", all(rows[N]["e"] <= N * N for N in rows))
    ests = []
    for N0 in range(17, 22):
        Ns = list(range(N0, N0 + 4))
        A = np.array([[N, math.log(N), 1, 1 / N] for N in Ns])
        y = np.array([math.log(rows[N]["mu"]) for N in Ns])
        sol = np.linalg.solve(A, y)
        ests.append((2 * math.pi * sol[0], sol[1]))
        print(f"mu window {N0}..{N0+3}: V = {2*math.pi*sol[0]:.4f}, log N coefficient {sol[1]:.3f}")
    check("mu: growth -> 5.33349 (within 0.01), one-loop 3/2 (within 0.05)",
          all(abs(v - VOL["mu"]) < 0.01 and abs(a - 1.5) < 0.05 for v, a in ests))
    tw = []
    for N in range(20, 25):
        k = 8
        v = 2 * math.pi * (math.log(rows[N]["tau"]) - math.log(rows[N - k]["tau"]) - 1.5 * math.log(N / (N - k))) / k
        tw.append(v)
        print(f"tau window ending N={N}: V = {v:.4f}")
    check("tau: window estimates within 0.1 of 6.35459", all(abs(v - VOL["tau"]) < 0.1 for v in tw))
    print(f"\n{sum(checks)}/{len(checks)} checks passed")
    raise SystemExit(0 if all(checks) else 1)


if __name__ == "__main__":
    main()
