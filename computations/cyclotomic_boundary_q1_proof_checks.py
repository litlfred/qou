#!/usr/bin/env python3
"""cyclotomic_boundary_q1_proof_checks.py — symbolic (all-n) checks behind the q = 1 expansion of
D(n) in cyclotomic_boundary_q1_expansion.py, for conj:cyclotomic-boundary-at-keystone.

Each check is an identity of polynomials, so it holds for every n or every partition, not only
for a range:

  A. Hook power sums through beta-sets.  For a partition with beta-set {b_1 > ... > b_l},
     hooks are the pairs (b, g) with b in beta, g < b, g not in beta, h = b - g, so
       sum h^k = sum_b sum_{h=1}^{b} h^k - sum_{b > b'} (b - b')^k,
     and contents give sum c^k = sum_i [F_k(b_i - l) - F_k(-i)] with F_k(N) - F_k(N-1) = N^k.
     Both sides become polynomials in l and the power sums p_j = sum b^j; the identities
       sum h^2 = sum c^2 + n^2,
       sum h^4 = sum c^4 + 12 n sum c^2 + n^2 - 12 (sum c)^2,        n = p_1 - l(l-1)/2,
     hold as polynomial identities in (l, p_1, ..., p_4).
  B. Jucys-Murphy sums.  p_k(contents) is the central character of sum_t J_t^k, and
     sum_lam f^lam omega_lam(z) = sum_g z_g r(g) with r(g) = #{x : x^2 = g} (all irreducible
     characters of S_n are real).  Expanding a product of JM transpositions (a t), a < t, over
     the ordered set partitions of its symbols gives
       sum_lam f^lam F(lam) = sum_s poly_s(n) I_{n-s}
     with binomial(n, #blocks) counting the labellings.  The result matches CLASS_SUMS in
     cyclotomic_boundary_q1_expansion.py support by support, for symbolic n.
  C. d2 and d4 from A and B, symbolically in n, equal the closed forms used there, and
     Delta = a e - b cc is the polynomial stated there.
  D. Growth.  odd(d2) >= (n-6)(n^2-13) I_{n-8} / (6 * 2^((n+1)/4)) and |Delta| < 10 n^14 for
     n >= 9; the left side beats the right for 46 <= n <= 400 and the ratio grows (it gains a
     factor >= (n-7)/sqrt 2 > 2 every two steps while (1 + 2/n)^14 < 2), so for all n >= 46.

Exact arithmetic (sympy rationals); no floats, no fitting.
Usage: python3 computations/cyclotomic_boundary_q1_proof_checks.py
"""
from __future__ import annotations
import sys
from collections import defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
import cyclotomic_boundary_q1_expansion as q1  # noqa: E402

n = sp.Symbol("n")


# ---------- A. hook identities ----------
def check_hooks():
    b, l, m, i = sp.symbols("b l m i")
    P = sp.symbols("p0:9")

    def S(k, N):
        return sp.expand(sp.summation(m**k, (m, 1, N)))

    def psum(expr):
        e = sp.Poly(sp.expand(expr), b)
        return sp.expand(sum(c * (P[d[0]] if d[0] > 0 else l) for d, c in zip(e.monoms(), e.coeffs())))

    def content(k):
        return sp.expand(psum(S(k, b - l)) - sp.summation(S(k, -i), (i, 1, l)))

    def hook(k):  # k even
        pairs = 2 * l * P[k] + sum(sp.binomial(k, j) * (-1) ** j * P[k - j] * P[j] for j in range(1, k))
        return sp.expand(psum(S(k, b)) - pairs / 2)

    N_ = sp.expand(P[1] - l * (l - 1) / 2)
    c1, c2, c4, h2, h4 = content(1), content(2), content(4), hook(2), hook(4)
    assert sp.expand(h2 - (c2 + N_**2)) == 0
    assert sp.expand(h4 - (c4 + 12 * N_ * c2 + N_**2 - 12 * c1**2)) == 0
    # the beta-set model reproduces direct sums
    import cyclotomic_boundary_certificates as ex
    for lam in [(3, 1), (4, 2, 2, 1), (5, 3, 3, 2, 1, 1), (2, 2, 2), (7,)]:
        L = len(lam)
        beta = [lam[j] + L - (j + 1) for j in range(L)]
        sub = {l: L, **{P[k]: sum(x**k for x in beta) for k in range(1, 9)}}
        h = ex.hooks(lam)
        c = [jj - ii for ii, r in enumerate(lam) for jj in range(r)]
        assert h4.subs(sub) == sum(x**4 for x in h) and c4.subs(sub) == sum(x**4 for x in c)
        assert c1.subs(sub) == sum(c) and N_.subs(sub) == sum(lam)


# ---------- B. Jucys-Murphy sums ----------
def ordered_partitions(syms):
    if not syms:
        yield []
        return
    first, rest = syms[0], syms[1:]
    for op in ordered_partitions(rest):
        for j in range(len(op)):
            yield op[:j] + [op[j] | {first}] + op[j + 1:]
        for j in range(len(op) + 1):
            yield op[:j] + [{first}] + op[j:]


def cyc_type(perm):
    seen, t = set(), []
    for x in perm:
        if x in seen:
            continue
        L, y = 0, x
        while y not in seen:
            seen.add(y)
            y, L = perm[y], L + 1
        if L > 1:
            t.append(L)
    return tuple(sorted(t, reverse=True))


def roots(t):
    """Square roots of a permutation of nontrivial cycle type t (fixed points excluded)."""
    res = 1
    for k in set(t):
        c = t.count(k)
        if k % 2:
            res *= sum(comb(c, 2 * j) * sp.factorial2(2 * j - 1) * k**j for j in range(c // 2 + 1))
        elif c % 2:
            return 0
        else:
            res *= sp.factorial2(c - 1) * k ** (c // 2)
    return res


def jm_sum(word):
    syms = sorted({s for p in word for s in p})
    res = defaultdict(lambda: 0)
    for op in ordered_partitions(syms):
        val = {s: j for j, blk in enumerate(op) for s in blk}
        if any(val[a] >= val[t] for a, t in word):
            continue
        perm = {j: j for j in range(len(op))}
        for a, t in word:
            x, y = val[a], val[t]
            perm[x], perm[y] = perm[y], perm[x]
        ty = cyc_type(perm)
        res[sum(ty)] += sp.binomial(n, len(op)) * roots(ty)
    return {s: sp.expand(sp.expand_func(v)) for s, v in res.items() if sp.expand(sp.expand_func(v)) != 0}


def JM(top, pw, tag):
    return [(f"{tag}{j}", top) for j in range(pw)]


WORDS = {"p2": JM("t", 2, "a"), "p4": JM("t", 4, "a"),
         "p1sq": JM("t", 1, "a") + JM("u", 1, "b"), "p2sq": JM("t", 2, "a") + JM("u", 2, "b")}


def check_jm():
    """Both sides are polynomials in n of degree <= 6 for each support s, so agreement at
    12 integer points is equality of polynomials."""
    sums = {}
    for key, word in WORDS.items():
        got = jm_sum(word)
        sums[key] = got
        supports = set(got) | {q1.ROOTS[t][1] for t in q1.CLASS_SUMS[key]}
        for s_ in supports:
            for nn in range(6, 18):
                lhs = got[s_].subs(n, nn) if s_ in got else 0
                rhs = sum(q1.ROOTS[t][0] * q1.CLASS_SUMS[key][t](nn)
                          for t in q1.CLASS_SUMS[key] if q1.ROOTS[t][1] == s_)
                assert lhs == rhs, (key, s_, nn)
    return sums


# ---------- C. closed forms for d2, d4 ----------
def check_closed(sums):
    x, y = sp.symbols("x y")  # x = I_{n-8}, y = I_{n-9}
    seq = {9: y, 8: x}
    for j in range(7, -1, -1):
        seq[j] = sp.expand(seq[j + 1] + (n - j - 1) * seq[j + 2])  # I_{n-j} = I_{n-j-1} + (n-j-1) I_{n-j-2}

    def M(key, n0):
        if key == "1":
            return seq[n0]
        return sum(v.subs(n, n - n0) * seq[n0 + s_] for s_, v in sums[key].items())

    i = sp.Symbol("i")

    def T(k, mm):
        return sp.summation(i**k, (i, 1, mm))

    def s2(n0):
        mm = n - n0
        return (T(2, mm) - mm**2) / 6 * M("1", n0) - M("p2", n0) / 6

    def s4(n0):
        mm = n - n0
        A = T(2, mm) - mm**2
        return (-((T(4, mm) - mm**2) * M("1", n0) - M("p4", n0) - 12 * mm * M("p2", n0) + 12 * M("p1sq", n0)) / 180
                + (A * A * M("1", n0) - 2 * A * M("p2", n0) + M("p2sq", n0)) / 72)

    k = n - 1
    k2, k4 = k * (k * k - 1) / 6, k * (k * k - 1) * (3 * k * k - 7) / 360
    d2 = sp.expand(s2(0) - s2(1) - (k * s2(2) + k2 * M("1", 2)))
    d4 = sp.expand(s4(0) - s4(1) - (k * s4(2) + k2 * s2(2) + k4 * M("1", 2)))
    c = (n - 1) * (n - 2) * (n - 3)
    a, b = c * (n - 6) * (n**2 - 13), 2 * c * (n - 8) * (n - 5) * (2 * n - 5)
    cc = c * (n - 6) * (10 * n**5 - 51 * n**4 - 86 * n**3 + 774 * n**2 - 536 * n - 1695)
    e = 2 * c * (n - 8) * (n - 5) * (20 * n**4 - 157 * n**3 + 419 * n**2 - 333 * n - 219)
    assert sp.expand(6 * d2 - (a * x + b * y)) == 0
    assert sp.expand(1080 * d4 - (cc * x + e * y)) == 0
    assert sp.expand(a * e - b * cc - q1.delta_poly(n)) == 0


# ---------- D. growth ----------
def check_growth():
    for nn in range(46, 401):
        lhs = Fraction((nn - 6) * (nn * nn - 13) * q1.I(nn - 8), 6)
        assert lhs**4 > (10 * nn**14) ** 4 * 2 ** (nn + 1), nn
    for nn in range(9, 401):
        assert abs(q1.delta_poly(nn)) < 10 * nn**14 and q1.delta_poly(nn) != 0


def main() -> int:
    check_hooks()
    print("A. hook identities: polynomial identities in (l, p_1..p_4)  OK")
    sums = check_jm()
    print("B. Jucys-Murphy sums equal CLASS_SUMS support by support  OK")
    check_closed(sums)
    print("C. d2, d4 and Delta equal the closed forms, symbolically in n  OK")
    check_growth()
    print("D. growth bound holds for 46 <= n <= 400  OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
