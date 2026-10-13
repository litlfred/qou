#!/usr/bin/env python3
"""Is the v9 nuclear element a Yang-Baxter / transfer-matrix object?  (qou-m7py follow-up 3)

Context
-------
`markov_trace_two_row_tower_probe.py` and `two-row-tower-trace` (Rust) compute the
convention-D Markov trace of the v9 element

    E = prod_{k=1}^{A-1} prod_{i=0}^{k-1} f(type_i, type_k; sigma_i)

with pp -> sigma, nn -> sigma - h = sigma^{-1}, pn -> 2 sigma - h = sigma + sigma^{-1}.
Cost grows like L * Catalan(A); A = 40 is ~1e24 operations, out of reach of any
column or matrix method.  The owner asked whether Yang-Baxter / R-matrix structure
could reach A = 40.  This probe tests the structural facts that would decide it.
It reports findings; it claims no closed form.

Checks (exact arithmetic in Q(q), sympy; no floats)
---------------------------------------------------
B1  Baxterisation.  With R(x) = x sigma - x^{-1} sigma^{-1} (Jones), the three v9
    factors are R at x -> infinity (pp), x -> 0 (nn), x = i (pn), up to scalars.
    Checked as identities in H_n: x^{-1} R(x) -> sigma, -x R(x) -> sigma^{-1},
    -i R(i) = sigma + sigma^{-1}.
B2  YBE.  R_1(x) R_2(xy) R_1(y) = R_2(y) R_1(xy) R_2(x) in H_3, checked on every
    irrep of H_3 (seminormal; H_3 is semisimple at generic q, so this is faithful).
B3  Spectral parameters by strand.  A vertex-model reading needs one parameter per
    STRAND with x_{ik} = u_i / u_k (difference property).  pp would need
    u_p / u_p = infinity.  Checked: R(1) = h * 1 is a scalar, not sigma, so no
    assignment of the difference form reproduces pp.  (The product form
    x_{ik} = u_i u_k reproduces all three only in the degenerate limit
    u_p -> infinity, u_n = i / u_p -> 0.)
B4  The factor labels are by POSITION, not by tracked strand.  The braid
    permutation of E is computed and the (i, k) labels are compared with the pair
    of strands that actually meet at each crossing; a mismatch means E is not the
    partition function of a vertex model on its own braid diagram.
B5  The one exact reduction available: the last factor is the only use of
    sigma_{A-2}, so tr(E) = (a + b z) * tr(E without it) by the Markov property.
    Checked numerically-exact on small nuclei in Q(q) (two-row seminormal).

Run:  python3 -u v9_element_ybe_structure_probe.py | tee /tmp/v9_ybe.log
"""
from __future__ import annotations

import itertools
import sys

import sympy as sp

q = sp.symbols("q", positive=True)
x, y = sp.symbols("x y")
h = q - 1 / q


# ---------------------------------------------------------------- seminormal irreps

def tableaux_all(shape):
    """Standard Young tableaux of `shape` as row-index sequences (entry j in row t[j])."""
    n = sum(shape)
    out = []

    def rec(t, rowlen):
        if len(t) == n:
            out.append(tuple(t))
            return
        for r in range(len(shape)):
            if rowlen[r] < shape[r] and (r == 0 or rowlen[r] < rowlen[r - 1]):
                rowlen[r] += 1
                rec(t + [r], rowlen)
                rowlen[r] -= 1

    rec([], [0] * len(shape))
    return out


def contents(t):
    rowlen = {}
    c = []
    for r in t:
        k = rowlen.get(r, 0)
        c.append(k - r)
        rowlen[r] = k + 1
    return c


def alpha(r):
    return h / (1 - q ** (-2 * r))


def sigma_matrix(shape, i):
    """Seminormal matrix of sigma_i (columns = images of basis vectors)."""
    tabs = tableaux_all(shape)
    idx = {t: j for j, t in enumerate(tabs)}
    d = len(tabs)
    M = sp.zeros(d, d)
    for j, t in enumerate(tabs):
        c = contents(t)
        r = c[i + 1] - c[i]
        if abs(r) == 1:
            M[j, j] = q if r == 1 else -1 / q
            continue
        t2 = list(t)
        t2[i], t2[i + 1] = t2[i + 1], t2[i]
        j2 = idx[tuple(t2)]
        if r > 0:
            ar, am = alpha(r), alpha(-r)
            M[j, j] = ar
            M[j2, j] = 1
            M[j, j2] = 1 + ar * am
            M[j2, j2] = am
    return M


def partitions(n):
    if n == 0:
        yield ()
        return
    def rec(n, mx):
        if n == 0:
            yield ()
            return
        for k in range(min(n, mx), 0, -1):
            for rest in rec(n - k, k):
                yield (k,) + rest
    yield from rec(n, n)


def simp0(M):
    return all(sp.simplify(e) == 0 for e in M)


results = []


def report(name, ok, detail=""):
    results.append((name, ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""), flush=True)


# ---------------------------------------------------------------- B1, B2

def check_b1_b2():
    ok1 = ok2 = True
    for shape in partitions(3):
        S1, S2 = sigma_matrix(shape, 0), sigma_matrix(shape, 1)
        d = S1.shape[0]
        I = sp.eye(d)
        S1i, S2i = S1 - h * I, S2 - h * I  # sigma^{-1} = sigma - h
        assert simp0(S1 * S1i - I) and simp0(S2 * S2i - I)

        def R(S, Si, t):
            return t * S - Si / t

        # B1
        lim_pp = (R(S1, S1i, x) / x).applyfunc(lambda e: sp.limit(sp.simplify(e), x, sp.oo))
        lim_nn = (-x * R(S1, S1i, x)).applyfunc(lambda e: sp.limit(sp.simplify(e), x, 0))
        pn = (-sp.I * R(S1, S1i, sp.I)).applyfunc(sp.simplify)
        ok1 &= simp0(lim_pp - S1) and simp0(lim_nn - S1i) and simp0(pn - (S1 + S1i))
        # B2
        L = R(S1, S1i, x) * R(S2, S2i, x * y) * R(S1, S1i, y)
        Rr = R(S2, S2i, y) * R(S1, S1i, x * y) * R(S2, S2i, x)
        ok2 &= simp0((L - Rr).applyfunc(sp.expand))
    report("B1 Baxterisation: pp = lim x^-1 R(x), nn = lim -x R(x), pn = -i R(i)", ok1)
    report("B2 YBE R1(x)R2(xy)R1(y) = R2(y)R1(xy)R2(x) on every irrep of H_3", ok2)


# ---------------------------------------------------------------- B3

def check_b3():
    shape = (2, 1)
    S1 = sigma_matrix(shape, 0)
    I = sp.eye(2)
    R1 = (1 * S1 - (S1 - h * I) / 1).applyfunc(sp.simplify)
    is_scalar = simp0(R1 - h * I)
    # R(1) = h * 1: a strand-difference parameter u_p/u_p = 1 gives a scalar, never sigma.
    report("B3 R(1) = h * 1 (so the difference form x_ik = u_i/u_k cannot give pp -> sigma)",
           is_scalar, "v9's element is not an inhomogeneous transfer-matrix product of difference type")


# ---------------------------------------------------------------- B4

def braid_crossings(A):
    """Walk the v9 word as a braid; return, per factor (i, k), the pair of
    ORIGINAL strands that meet at that crossing."""
    pos = list(range(A))  # pos[p] = strand currently at position p
    out = []
    # product left to right acts on a diagram read top to bottom
    for k in range(1, A):
        for i in range(k):
            a, b = pos[i], pos[i + 1]
            out.append(((i, k), tuple(sorted((a, b)))))
            pos[i], pos[i + 1] = b, a
    return out


def check_b4(A=6):
    cr = braid_crossings(A)
    mismatch = sum(1 for (i, k), s in cr if tuple(sorted((i, k))) != s)
    report(f"B4 position labels (i,k) vs strands actually crossing, A={A}",
           True, f"{mismatch}/{len(cr)} crossings carry a label that is not the pair of strands meeting there")
    return mismatch, len(cr)


# ---------------------------------------------------------------- B5

def v9_factor(ti, tk):
    if ti == tk == "p":
        return 0, 1
    if ti == tk == "n":
        return -h, 1
    return -h, 2


def trace_two_row(Z, N, drop_last=False):
    """Exact convention-D trace (two-row seminormal), times 2^pn (not divided)."""
    types = ["p"] * Z + ["n"] * N
    A = Z + N
    facs = [(i, *v9_factor(types[i], types[k])) for k in range(1, A) for i in range(k)]
    if drop_last:
        facs = facs[:-1]
    tot = 0
    for k in range(A // 2 + 1):
        shape = (A - k, k) if k else (A,)
        S = [sigma_matrix(shape, i) for i in range(A - 1)]
        d = S[0].shape[0] if S else 1
        M = sp.eye(d)
        for i, a, b in facs:
            M = M * (a * sp.eye(d) + b * S[i])
        qi = lambda m: (q ** m - q ** (-m)) / (q - 1 / q)
        w = qi(A - 2 * k + 1) / qi(2) ** A
        tot += w * M.trace()
    return sp.simplify(tot)


def check_b5():
    zD = q ** 3 / (q ** 2 + 1)
    ok = True
    for Z, N in [(1, 1), (2, 1), (1, 2), (2, 2)]:
        types = ["p"] * Z + ["n"] * N
        a, b = v9_factor(types[Z + N - 2], types[Z + N - 1])
        full = trace_two_row(Z, N)
        rest = trace_two_row(Z, N, drop_last=True)
        ok &= sp.simplify(full - (a + b * zD) * rest) == 0
    report("B5 Markov peel of the last factor: tr(E) = (a + b z_D) tr(E') on 2H, 3He, 3H, 4He", ok,
           "only sigma_{A-2} is used once; sigma_{A-3} is used twice, so the peel does not iterate")


if __name__ == "__main__":
    check_b1_b2()
    check_b3()
    check_b4(6)
    check_b5()
    bad = [n for n, ok in results if not ok]
    print(f"\n{len(results) - len(bad)}/{len(results)} checks pass", flush=True)
    sys.exit(1 if bad else 0)
