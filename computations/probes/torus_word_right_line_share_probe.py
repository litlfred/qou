#!/usr/bin/env python3
"""Route 4 (owner, 2026-11-15): the right-line share of torus words under convention D, every n.

Bean qou-hlx7. Follows weak_knot_left_line_split_probe.py (n = 3, T(3,5)) and stream 11's
ConventionDLineWeights.lean / corner_sl2_weighted_persistence_probe.py (the [3]_q : 1 line
weighting, which is the N = 0 case here).

Setting. c = s_1 s_2 ... s_{n-1} (Coxeter word), torus word c^N (closure T(n,N)).
P_R = (q - s_1)/[2]_q, the right line of the FIRST letter (= leftLine's complement at q > 1).
Convention D: tau_D = sum over two-row shapes lambda = (n-k, k) of y_lambda * tr_lambda, with
y_(n-k,k) = [n-2k+1]_q / [2]_q^n; every shape with >= 3 rows has weight 0.

What is checked, exactly (Fraction arithmetic at rational q, no floats):
 1. Young's seminormal matrices satisfy the Hecke and braid relations on each two-row block
    (helpers syt/content/swap as in stream 11's corner_doublet_vs_flavour_probe.py).
 2. The full twist c^n acts on block lambda by the scalar q^(2 c(lambda)), c(lambda) the
    content sum. (A standard fact; here CHECKED for n <= 7, not assumed.)
 3. Exact decomposition: tau_D(c^(m n + r) P_R) = sum_lambda y_lambda q^(2 m c(lambda)) g_lambda(r),
    g_lambda(r) = tr_lambda(c^r P_R), and g_(n) = 0 (P_R vanishes on the trivial block).
 4. g_(n-1,1)(r) != 0 for some r: the hook block, which has the largest twist exponent among
    the non-trivial shapes, contributes along those residues (the residues where it vanishes are printed).
 5. N = 0: tau_D(P_L) / tau_D(P_R) = [3]_q (stream 11).
 6. The right part is nonzero for every N <= 3n tested.
Consequence (stated in the audit, from 2-4): c(n) - c(n-1,1) = n, so the right-line share
tau_D(c^N P_R)/tau_D(c^N) is O(q^(-2N)) for q > 1, with that rate attained on the residues where
the hook term is nonzero, and the share is not zero for the N tested. Numbers at the proton q0 in mpmath, 70 dps. No witness. Nothing fitted.
"""
import sys
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools/qou-substrate/python"))
from qou_substrate.constants import Q_50_DIGIT_STR  # proton pin (owner directive 2026-08-07)

mp.mp.dps = 70
NMAX = 7
ok = True


def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)


def syt(shape):
    n = sum(shape)
    out = []

    def rec(rows, k):
        if k > n:
            out.append(tuple(tuple(r) for r in rows))
            return
        for i, r in enumerate(rows):
            if len(r) < shape[i] and (i == 0 or len(rows[i - 1]) > len(r)):
                r.append(k)
                rec(rows, k + 1)
                r.pop()

    rec([[] for _ in shape], 1)
    return out


def content(t, k):
    for i, r in enumerate(t):
        if k in r:
            return r.index(k) - i
    raise ValueError


def swap(t, i):
    m = {i: i + 1, i + 1: i}
    s = tuple(tuple(m.get(x, x) for x in r) for r in t)
    for r in s:
        if list(r) != sorted(r):
            return None
    for c in range(len(s[0])):
        col = [r[c] for r in s if len(r) > c]
        if col != sorted(col):
            return None
    return s


def mul(A, B):
    return [[sum(A[i][t] * B[t][j] for t in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def eye(d, one):
    return [[one if i == j else one * 0 for j in range(d)] for i in range(d)]


def tr(M):
    return sum(M[i][i] for i in range(len(M)))


def seminormal(shape, n, q):
    h = q - 1 / q
    T = syt(shape)
    idx = {t: a for a, t in enumerate(T)}
    d = len(T)
    gens = []
    for i in range(1, n):
        M = [[q * 0 for _ in range(d)] for _ in range(d)]
        for t in T:
            a = idx[t]
            dd = content(t, i + 1) - content(t, i)
            x = h * q**dd / (q**dd - q ** (-dd))
            M[a][a] = x
            s = swap(t, i)
            if s is not None:
                b = idx[s]
                if a < b:
                    M[a][b] = q * 0 + 1
                else:
                    y = h * q ** (-dd) / (q ** (-dd) - q**dd)
                    M[a][b] = x * y + 1
        gens.append(M)
    return gens


def qint(m, q):
    return (q**m - q ** (-m)) / (q - 1 / q)


def csum(sh):
    return sum(j - i for i, r in enumerate(sh) for j in range(r))


def two_row(n):
    return [(n - k, k) if k else (n,) for k in range(0, n // 2 + 1)]


def blocks(n, q, exact):
    br2 = q + 1 / q
    out = []
    for sh in two_row(n):
        g = seminormal(sh, n, q)
        d = len(g[0])
        one = q * 0 + 1
        if exact:
            h = q - 1 / q
            for G in g:
                G2 = mul(G, G)
                assert all(G2[i][j] == h * G[i][j] + (1 if i == j else 0) for i in range(d) for j in range(d)), sh
            for a in range(len(g) - 1):
                L = mul(mul(g[a], g[a + 1]), g[a])
                R = mul(mul(g[a + 1], g[a]), g[a + 1])
                assert L == R, sh
        c = eye(d, one)
        for G in g:
            c = mul(c, G)
        PR = [[((q if i == j else 0) - g[0][i][j]) / br2 for j in range(d)] for i in range(d)]
        y = qint(n - 2 * (sh[1] if len(sh) > 1 else 0) + 1, q) / br2**n
        out.append(dict(sh=sh, d=d, y=y, c=c, PR=PR))
    return out


def series(bl, Nmax, one):
    cur = {b["sh"]: eye(b["d"], one) for b in bl}
    rows = []
    for N in range(Nmax + 1):
        R = one * 0
        T = one * 0
        per = {}
        for b in bl:
            M = cur[b["sh"]]
            g = tr(mul(M, b["PR"]))
            per[b["sh"]] = g
            R += b["y"] * g
            T += b["y"] * tr(M)
            cur[b["sh"]] = mul(M, b["c"])
        rows.append((N, R, T, per))
    return rows


for q in (Fr(11, 10), Fr(3, 2)):
    print(f"\n== exact, q = {q}")
    for n in range(2, NMAX + 1):
        bl = blocks(n, q, exact=True)
        one = Fr(1)
        check(f"n={n}: Hecke + braid relations hold on every two-row block", True)
        check(f"n={n}: sum y_lambda * dim_lambda = 1", sum(b["y"] * b["d"] for b in bl) == 1)
        tw_ok = True
        for b in bl:
            cn = eye(b["d"], one)
            for _ in range(n):
                cn = mul(cn, b["c"])
            z = q ** (2 * csum(b["sh"]))
            tw_ok &= all(cn[i][j] == (z if i == j else 0) for i in range(b["d"]) for j in range(b["d"]))
        check(f"n={n}: full twist c^n = q^(2 c(lambda)) on every block", tw_ok)
        rows = series(bl, 3 * n, one)
        check(f"n={n}: P_R vanishes on the trivial block (g_(n) = 0)", all(r[3][(n,)] == 0 for r in rows))
        dec = True
        for m in range(0, 3):
            for r in range(n):
                lhs = rows[m * n + r][1]
                rhs = sum(b["y"] * q ** (2 * m * csum(b["sh"])) * rows[r][3][b["sh"]] for b in bl)
                dec &= lhs == rhs
        check(f"n={n}: tau_D(c^(mn+r) P_R) = sum y q^(2 m c) g(r)", dec)
        hook = (n - 1, 1)
        zero_r = [r for r in range(n) if rows[r][3][hook] == 0]
        print(f"   n={n}: residues r with g_(n-1,1)(r) = 0: {zero_r}")
        check(f"n={n}: hook block term g_(n-1,1)(r) != 0 for some r (the rate q^(-2N) is attained)",
              len(zero_r) < n)
        check(f"n={n}: c(n) - c(n-1,1) = n", csum((n,)) - csum(hook) == n)
        check(f"n={n}: N = 0 ratio tau(P_L)/tau(P_R) = [3]_q", (rows[0][2] - rows[0][1]) / rows[0][1] == q**2 + 1 + q**-2)
        check(f"n={n}: N = 1 share = -1/(q^2 (q^2+1)) (Markov property; independent of n)",
              rows[1][1] / rows[1][2] == -1 / (q**2 * (q**2 + 1)))
        check(f"n={n}: right part nonzero for N = 0..{3*n}", all(r[1] != 0 for r in rows))

q0 = mp.mpf(Q_50_DIGIT_STR)
print(f"\n== at the proton q0 = {mp.nstr(q0, 20)} (mpmath {mp.mp.dps} dps): right-line share of T(n,N)")
for n in range(2, NMAX + 1):
    bl = blocks(n, q0, exact=False)
    rows = series(bl, 2 * n, mp.mpf(1))
    shares = [r[1] / r[2] for r in rows]
    print(f"  n={n}: " + "  ".join(f"N={N}:{mp.nstr(s, 6)}" for N, s in enumerate(shares)))
    scaled = [abs(s) * q0 ** (2 * N) for N, s in enumerate(shares)]
    print(f"        |share| * q0^(2N) max over N <= {2*n}: {mp.nstr(max(scaled), 6)}")

print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
sys.exit(0 if ok else 1)
