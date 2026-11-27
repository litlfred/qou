"""Closure ∪ axis: the braid axis as a convolution operator (no fitting, no data comparison).

Owner card 2026-11-27: "Convolution op of closure ∪ axis". Least-trace ladder (owner ruling
23:35Z): e = s1 s2 s1, mu = s1^2 s2^-1, tau = s1^4 s2^-1. e and mu close to the same link
(Hopf), so closure invariants agree; the axis is an unknot encircling the three strands, i.e. the
4-strand closure of beta * s3 s2 s1 s1 s2 s3.

Checks:
1. m_N(beta ∪ A) = f^-6 * sum_J chi_J(beta) * [N(2J+1)]/[2J+1], with chi_J the framed isotypic
   trace of beta on the spin-J part of V_j^{x3} (projectors from the full twist Delta^2).
2. Hopf fusion sum: sum_K [d_K] theta_K = theta_J theta_j [d_J d_j], theta = q^{2J(J+1)}.
3. The axis is invisible at q = 1 (scalar N on every block): U(1) of beta ∪ A is closure U(1)
   plus the axis linking term.
4. The axis separates e and mu at q != 1.
Lean: QOU/Observations/AxisConvolutionOperator.lean. Audit §16.
"""
import numpy as np

Q0 = 1.1099785827513808  # display only
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


def gens(N, q, n):
    Rc, K = rcheck(N, q)
    g = {}
    for i in range(1, n):
        g[i] = np.kron(np.kron(np.eye(N ** (i - 1)), Rc), np.eye(N ** (n - 1 - i)))
        g[-i] = np.linalg.inv(g[i])
    return g, Rc, K


def word_mat(g, word, dim):
    M = np.eye(dim)
    for s in word:
        M = M @ g[s]
    return M


def kron_n(K, n):
    out = np.eye(1)
    for _ in range(n):
        out = np.kron(out, K)
    return out


def framing(N, q):
    Rc, K = rcheck(N, q)
    return np.trace(np.kron(K, K) @ Rc) / qint(N, q)


def mass(N, q, word, n):
    g, Rc, K = gens(N, q, n)
    M = word_mat(g, word, N**n)
    w = sum(1 if s > 0 else -1 for s in word)
    return (np.trace(kron_n(K, n) @ M) * framing(N, q) ** (-w)).real


def theta(J, q):
    return q ** (2 * J * (J + 1))


def isotypic(N, q, word):
    j = (N - 1) / 2
    g, Rc, K = gens(N, q, 3)
    D2 = word_mat(g, [1, 2, 1, 1, 2, 1], N**3)
    Js = [3 * j - k for k in range(int(3 * j) + 1)]
    lam = {J: theta(J, q) / theta(j, q) ** 3 for J in Js}
    ev = np.linalg.eigvals(D2)
    assert all(np.min(np.abs(ev - lam[J])) < 1e-6 * abs(lam[J]) for J in Js)

    def P(J):
        Pm = np.eye(N**3)
        for J2 in Js:
            if J2 != J:
                Pm = Pm @ (D2 - lam[J2] * np.eye(N**3)) / (lam[J] - lam[J2])
        return Pm

    M = word_mat(g, word, N**3)
    w = sum(1 if s > 0 else -1 for s in word)
    return {J: (np.trace(kron_n(K, 3) @ M @ P(J)) * framing(N, q) ** (-w)).real for J in Js}


def axis_scalar(J, N, q):
    a = int(round(2 * J + 1))
    return qint(a * N, q) / qint(a, q)


LOOP = [3, 2, 1, 1, 2, 3]
WORDS = {"e": [1, 2, 1], "mu": [1, 1, -2], "tau": [1, 1, 1, 1, -2]}


def U(fn, q, h=1e-6):
    return -(np.log(fn(q * (1 + h))) - np.log(fn(q * (1 - h)))) / (2 * h)


def main():
    for q in (Q0, 0.83):
        for N in (2, 3, 4):
            j = (N - 1) / 2
            f = framing(N, q)
            check(f"framing f = q^(2j(j+1)) at N={N}, q={q:.3f}", abs(f - q ** (2 * j * (j + 1))) < 1e-9 * f)
            for nm, w in WORDS.items():
                chi = isotypic(N, q, w)
                ax = mass(N, q, w + LOOP, 4)
                pred = f ** -6 * sum(chi[J] * axis_scalar(J, N, q) for J in chi)
                check(f"axis decomposition N={N} {nm} q={q:.3f}", abs(ax - pred) < 1e-8 * max(1, abs(ax)))
    for a in range(1, 7):
        for b in range(1, 6):
            q = Q0
            lhs = sum(qint(a + b - 1 - 2 * k, q) * q ** (((a + b - 1 - 2 * k) ** 2 - 1) / 2) for k in range(b))
            rhs = q ** ((a * a - 1) / 2) * q ** ((b * b - 1) / 2) * qint(a * b, q)
            if abs(lhs - rhs) > 1e-9 * abs(rhs):
                check(f"Hopf fusion sum a={a} b={b}", False)
    check("Hopf fusion sum a<=6, b<=5", True)
    print("\nReadings at q0 (display only, not compared with any measurement):")
    for N in (2, 3, 4):
        j = (N - 1) / 2
        row = {}
        for nm, w in WORDS.items():
            row[nm] = mass(N, Q0, w + LOOP, 4)
            u1 = U(lambda q: mass(N, q, w + LOOP, 4), 1.0)
            uc = U(lambda q: mass(N, q, w, 3), 1.0)
            print(f"  N={N} {nm:3s} m(closure∪A)={row[nm]:.6f}  U(1)={u1:.3f}  closure U(1)={uc:.3f}")
            check(f"axis adds 6*2j(j+1) to U(1), N={N} {nm}", abs(u1 - uc - 12 * j * (j + 1)) < 1e-3)
        check(f"closures of e, mu agree at N={N}", abs(mass(N, Q0, WORDS['e'], 3) - mass(N, Q0, WORDS['mu'], 3)) < 1e-9)
        check(f"axis separates e, mu at N={N}", abs(row["e"] - row["mu"]) > 1e-3)
        print(f"  N={N} ratios mu/e={row['mu']/row['e']:.5f} tau/e={row['tau']/row['e']:.5f}")
    print(f"\n{sum(checks)}/{len(checks)} checks passed")
    raise SystemExit(0 if all(checks) else 1)


if __name__ == "__main__":
    main()
