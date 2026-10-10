#!/usr/bin/env python3
"""Re-verify part (iii) (Rosso-Jones) of prop:rj-canonical-inner-product under
convention D, in exact arithmetic over Q(q).  Bean qou-q425.

Normalisation in force (the block's own, and AGENTS.md section 7a):
    Hecke relation  (sigma_i - q)(sigma_i + q^{-1}) = 0,
    [n]_q = (q^n - q^{-n})/(q - q^{-1}),
    Markov parameter z = q^2/[2]_q.
Algebraically q^2/[2]_q = q^3/(q^2+1) = z_D, the canonical convention-D value,
so the block's z IS z_D (checked symbolically below) -- no rescaling.

Method (no fitting, no floats):
  1. Build every irrep rho_lambda of H_r(q), lambda |- r, as the Hoefsmit
     seminormal representation on standard tableaux (sigma_i diagonal entry
     (q - q^{-1})/(1 - q^{-2d}), d = content(i+1) - content(i)); braid and Hecke
     relations are verified symbolically.
  2. Solve for the Ocneanu weights y_lambda of the Markov trace with parameter
     z from tr(1) = 1, restriction to H_{r-1}, and tr(x sigma_{r-1}) = z tr(x)
     on a spanning set of H_{r-1}; compare with the block's claim
     y_lambda = d_lambda/[2]^r, d_lambda = prod [2+c]/[h].
  3. For torus braids beta = (sigma_1...sigma_{r-1})^s compute
     tr_M(beta) = sum_lambda y_lambda Tr rho_lambda(beta) directly, and test
       (A) the block's printed form   sum_{lambda |- r} d_lambda q^{c_lambda s}
       (B) the same with the Hecke sign, sum d_lambda (eps_lambda q^{c_lambda})^s,
       (C) the Rosso-Jones form with the Adams/plethysm coefficients: for
           gcd(r,s)=1, [2]^r tr_M(beta) = sum over HOOKS lambda=(r-j,1^j) of
           (-1)^j d_lambda q^{2 s c_lambda / r}.
     (C) is the standard Rosso-Jones shape (Rosso-Jones 1993); it is tested,
     not assumed.
       (D) at s = r (the full twist Delta^2, a central element):
           [2]^r tr_M(Delta^2) = sum_lambda d_lambda f^lambda q^{2 c_lambda},
           i.e. Delta^2 acts on V_lambda by theta_lambda = q^{2 c_lambda}.
  4. Also check the unknot-normalised invariant [2]^{r-1} q^{-2e} tr_M(beta)
     (e = writhe) against the classical Jones polynomial of the trefoil at t = q^{-2}, to pin
     the variable convention.
Exit status 0 iff every check printed as PASS behaves as recorded.
"""
from __future__ import annotations

import itertools
import sys
from math import gcd

import sympy as sp

q = sp.symbols("q", positive=True)


def qint(n):
    return sp.cancel((q**n - q**(-n)) / (q - 1 / q))


Z_BLOCK = sp.cancel(q**2 / qint(2))
Z_D = q**3 / (q**2 + 1)


# ---------- partitions / tableaux ----------
def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def cells(lam):
    return [(i, j) for i, row in enumerate(lam) for j in range(row)]


def content(lam):
    return sum(j - i for i, j in cells(lam))


def hook(lam, i, j):
    conj = [sum(1 for r in lam if r > jj) for jj in range(lam[0])]
    return (lam[i] - j - 1) + (conj[j] - i - 1) + 1


def d_sl2(lam):
    """Block's d_lambda = prod [2 + c]/[h] (U_q(sl2) quantum dimension)."""
    val = sp.Integer(1)
    for i, j in cells(lam):
        val *= qint(2 + j - i) / qint(hook(lam, i, j))
    return sp.cancel(val)


def syt(lam):
    n = sum(lam)
    res = []

    def rec(filled, k):
        if k > n:
            res.append(dict(filled))
            return
        for i in range(len(lam)):
            row_len = sum(1 for (a, b) in filled if a == i)
            if row_len < lam[i]:
                j = row_len
                if i == 0 or (i - 1, j) in filled:
                    filled[(i, j)] = k
                    rec(filled, k + 1)
                    del filled[(i, j)]

    rec({}, 1)
    return res


def seminormal(lam):
    """Hoefsmit seminormal matrices for sigma_1..sigma_{n-1}."""
    n = sum(lam)
    tabs = syt(lam)
    pos = [{v: c for c, v in T.items()} for T in tabs]
    key = [tuple(sorted(T.items())) for T in tabs]
    index = {k: a for a, k in enumerate(key)}
    N = len(tabs)
    mats = []
    for i in range(1, n):
        M = sp.zeros(N, N)
        for a, T in enumerate(tabs):
            (r1, c1), (r2, c2) = pos[a][i], pos[a][i + 1]
            d = (c2 - r2) - (c1 - r1)
            diag = sp.cancel((q - 1 / q) / (1 - q**(-2 * d)))
            M[a, a] = diag
            if abs(d) >= 2:
                T2 = dict(T)
                T2[(r1, c1)], T2[(r2, c2)] = i + 1, i
                b = index[tuple(sorted(T2.items()))]
                if d > 0:
                    M[b, a] = 1
                else:
                    other = sp.cancel((q - 1 / q) / (1 - q**(2 * d)))
                    M[b, a] = sp.cancel(diag * other + 1)
        mats.append(M)
    return mats


def check_relations(mats):
    ok = True
    one = sp.eye(mats[0].shape[0]) if mats else None
    for a, A in enumerate(mats):
        R = (A - q * one) * (A + one / q)
        ok &= R.applyfunc(sp.cancel).is_zero_matrix
        for b, B in enumerate(mats):
            if abs(a - b) == 1:
                ok &= (A * B * A - B * A * B).applyfunc(sp.cancel).is_zero_matrix
            elif abs(a - b) >= 2:
                ok &= (A * B - B * A).applyfunc(sp.cancel).is_zero_matrix
    return ok


def word_matrix(mats, word, dim):
    M = sp.eye(dim)
    for g in word:
        M = M * mats[g - 1]
    return M


# ---------- Markov weights ----------
_weights_cache = {}


def markov_weights(n, z):
    if n in _weights_cache:
        return _weights_cache[n]
    lams = list(partitions(n))
    if n == 1:
        _weights_cache[n] = {(1,): sp.Integer(1)}, {(1,): []}
        return _weights_cache[n]
    reps = {lam: seminormal(lam) for lam in lams}
    for lam in lams:
        if reps[lam]:
            assert check_relations(reps[lam]), lam
    prev, _ = markov_weights(n - 1, z)
    ys = sp.symbols(f"y0:{len(lams)}")
    yv = dict(zip(lams, ys))
    eqs = []
    # spanning words of H_{n-1}: all words of length <= n-1 in sigma_1..sigma_{n-2}
    gens = list(range(1, n - 1))
    words = [()]
    for L in range(1, n):
        words += list(itertools.product(gens, repeat=L))
    prev_reps = {mu: seminormal(mu) for mu in prev}
    for w in words:
        lhs_prev = sum(
            prev[mu] * word_matrix(prev_reps[mu], w, len(syt(mu))).trace()
            for mu in prev
        )
        tr_x = sum(yv[l] * word_matrix(reps[l], w, len(syt(l))).trace() for l in lams)
        tr_xs = sum(
            yv[l] * word_matrix(reps[l], w + (n - 1,), len(syt(l))).trace() for l in lams
        )
        eqs.append(sp.cancel(tr_x - lhs_prev))
        eqs.append(sp.cancel(tr_xs - z * lhs_prev))
    sol = sp.solve(eqs, ys, dict=True)
    assert len(sol) == 1, sol
    w = {l: sp.cancel(sol[0][yv[l]]) for l in lams}
    _weights_cache[n] = (w, reps)
    return _weights_cache[n]


def tr_M(r, word, z):
    w, reps = markov_weights(r, z)
    if r == 1:
        return sp.Integer(1)
    return sp.cancel(
        sum(w[l] * word_matrix(reps[l], word, len(syt(l))).trace() for l in w)
    )


def eps(lam):
    """Hecke sign of the full-twist/Coxeter eigenvalue phase: (-1)^{leg} on hooks."""
    return (-1) ** (len(lam) - 1)


def main():
    fails = 0

    def report(name, ok):
        nonlocal fails
        print(("PASS " if ok else "FAIL ") + name)
        if not ok:
            fails += 1

    report("z_block = q^2/[2]_q equals z_D = q^3/(q^2+1)",
           sp.simplify(Z_BLOCK - Z_D) == 0)

    for r in (2, 3, 4):
        w, _ = markov_weights(r, Z_BLOCK)
        for lam in w:
            ok = sp.simplify(w[lam] - d_sl2(lam) / qint(2) ** r) == 0
            report(f"y_{lam} = d_lambda/[2]^{r}  (y={sp.factor(w[lam])})", ok)

    # torus braids
    print("\n-- torus braids beta=(sigma_1..sigma_{r-1})^s, value [2]^r tr_M(beta) --")
    rows = []
    fulltwist = []
    for r, srange in ((2, range(1, 8)), (3, range(1, 8)), (4, range(1, 6))):
        cox = tuple(range(1, r))
        for s in srange:
            val = sp.factor(sp.cancel(qint(2) ** r * tr_M(r, cox * s, Z_BLOCK)))
            lams = list(partitions(r))
            A = sp.cancel(sum(d_sl2(l) * q ** (content(l) * s) for l in lams))
            B = sp.cancel(sum(d_sl2(l) * (eps(l) * q ** content(l)) ** s for l in lams))
            okA = sp.simplify(val - A) == 0
            okB = sp.simplify(val - B) == 0
            okC = None
            if gcd(r, s) == 1:
                hooks = [l for l in lams if all(x == 1 for x in l[1:])]
                C = sp.cancel(
                    sum(eps(l) * d_sl2(l) * q ** sp.Rational(2 * s * content(l), r)
                        for l in hooks)
                )
                okC = sp.simplify(val - C) == 0
            okD = None
            if s == r:
                # full twist Delta^2 = (sigma_1..sigma_{r-1})^r acts on V_lambda
                # by theta_lambda = q^{2 c_lambda}; f^lambda = #SYT
                D = sp.cancel(sum(d_sl2(l) * len(syt(l)) * q ** (2 * content(l))
                                  for l in lams))
                okD = sp.simplify(val - D) == 0
                fulltwist.append(okD)
            rows.append((r, s, okA, okB, okC))
            print(f"r={r} s={s}: (A) {okA}  (B) {okB}  (C) {okC}  (D) {okD}   value={val}")

    # recorded expectations
    report("(A) printed form holds only for r=2, s even",
           all(okA == (r == 2 and s % 2 == 0) for r, s, okA, _, _ in rows))
    report("(B) sign-corrected form holds for every r=2 case",
           all(okB for r, s, _, okB, _ in rows if r == 2))
    report("(B) fails for some r=3 case",
           any(not okB for r, s, _, okB, _ in rows if r == 3))
    report("(C) Rosso-Jones hook form holds for every gcd(r,s)=1 case",
           all(okC for *_, okC in rows if okC is not None))

    report("(D) full twist: [2]^r tr_M(Delta^2) = sum d_lambda f^lambda q^{2c_lambda}, r=2,3,4",
           len(fulltwist) == 3 and all(fulltwist))

    report("closed form: d_(r) = [r+1], d_(r-1,1) = [r-1] for r = 2..7",
           all(sp.simplify(d_sl2((r,)) - qint(r + 1)) == 0
               and sp.simplify(d_sl2((r - 1, 1)) - qint(r - 1)) == 0
               for r in range(2, 8)))

    # trefoil pin: T(2,3), writhe 3, invariant [2]^{r-1} q^{-2e} tr_M
    V = sp.expand(sp.cancel(qint(2) * q ** (-6) * tr_M(2, (1, 1, 1), Z_BLOCK)))
    print("\ntrefoil normalised invariant:", V)
    t = sp.symbols("t")
    jones_trefoil = t + t**3 - t**4  # right-handed trefoil
    report("trefoil invariant = Jones V(t) at t = q^{-2}",
           sp.simplify(V - jones_trefoil.subs(t, q ** (-2))) == 0)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
