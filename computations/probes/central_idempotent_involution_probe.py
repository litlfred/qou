#!/usr/bin/env python3
"""Which involution does the conjecture's star mean? (bean qou-2150)

conj:explicit-central-idempotent asks for an involution `*` with
  (3) *(e_lam) = e_lam  for self-conjugate lam,
  (4) *(e_lam) = e_lam' for chiral lam != lam'.
The block never defines `*`. This probe tests the candidate involutions on the
Murphy-Lagrange central idempotents e_lam of H_n(q), n = 2, 3, 4, in the
(faithful) left-regular representation on the T_w basis.

Candidates:
  bar   : sigma -> sigma^-1, q -> q^-1          (antilinear automorphism; mirror image)
  stokes: sigma_{i1}..sigma_{ik} -> sigma_{ik}^-1..sigma_{i1}^-1, q -> q^-1
          (antilinear ANTI-automorphism; non-abelian Stokes path reversal,
           hol(gamma^-1) = hol(gamma)^-1)
  rev   : word reversal, q fixed                (linear anti-automorphism)
  hash  : sigma -> -sigma^-1, q fixed           (linear automorphism; sign twist)

Each e_lam is a polynomial in the commuting Murphy elements L_k with coefficients
rational in q, so the image under an involution is obtained by mapping L_k and
the coefficients. Exact rational arithmetic at two generic values of q (no
float anywhere). Report-only; writes no witness; decides nothing.

-- Ref: [leitner2026] mass-endomorphism/conj-explicit-central-idempotent.md
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction

import sympy as sp


def perms(n):
    return list(itertools.permutations(range(n)))


def length(w):
    return sum(1 for i in range(len(w)) for j in range(i + 1, len(w)) if w[i] > w[j])


def regular_rep(n, q):
    """Left multiplication by sigma_i on basis T_w: T_s T_w = T_{sw} if l(sw) > l(w),
    else (q - q^-1) T_w + T_{sw}."""
    W = perms(n)
    idx = {w: a for a, w in enumerate(W)}
    h = q - 1 / q
    gens = []
    for i in range(n - 1):
        M = sp.zeros(len(W), len(W))
        for w in W:
            sw = list(w)
            # left multiplication by s_i acts on values i <-> i+1
            sw = tuple(i + 1 if x == i else i if x == i + 1 else x for x in w)
            if length(sw) > length(w):
                M[idx[sw], idx[w]] += 1
            else:
                M[idx[w], idx[w]] += h
                M[idx[sw], idx[w]] += 1
        gens.append(M)
    return gens


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def syts(lam):
    n = sum(lam)
    cells = [(i, j) for i, r in enumerate(lam) for j in range(r)]
    out = []

    def rec(filled, k):
        if k == n:
            out.append(dict(filled))
            return
        for (i, j) in cells:
            if (i, j) in filled:
                continue
            if (j == 0 or (i, j - 1) in filled) and (i == 0 or (i - 1, j) in filled):
                filled[(i, j)] = k
                rec(filled, k + 1)
                del filled[(i, j)]

    rec({}, 0)
    # content vector: k -> content of the cell holding k
    return [[next(j - i for (i, j), v in T.items() if v == k) for k in range(n)] for T in out]


def conj(lam):
    return tuple(sum(1 for r in lam if r > j) for j in range(lam[0])) if lam else ()


def murphy(gens, n):
    I = sp.eye(gens[0].shape[0]) if gens else sp.eye(1)
    L = [I]
    for k in range(1, n):
        L.append(gens[k - 1] * L[-1] * gens[k - 1])
    return L


def e_lam(lam, qc, L, n):
    """Murphy-Lagrange e_lam: coefficients use scalar qc, Murphy elements L."""
    I = L[0] * 0 + sp.eye(L[0].shape[0])
    total = I * 0
    spec = list(range(-(n - 1), n))
    for cv in syts(lam):
        P = I
        for k in range(n):
            c = cv[k]
            for d in spec:
                if d == c:
                    continue
                P = P * (L[k] - qc ** (2 * d) * I) / (qc ** (2 * c) - qc ** (2 * d))
        total = total + P
    return total


def run(n, q):
    gens = regular_rep(n, q)
    ginv = [g.inv() for g in gens]
    L = murphy(gens, n)
    lams = list(partitions(n))
    E = {lam: e_lam(lam, q, L, n) for lam in lams}
    # sanity: idempotent, central, sum to 1
    ok = all((E[l] * E[l] - E[l]).is_zero_matrix for l in lams)
    ok &= all((E[l] * g - g * E[l]).is_zero_matrix for l in lams for g in gens)
    ok &= (sum(E.values(), sp.zeros(*E[lams[0]].shape)) - sp.eye(E[lams[0]].shape[0])).is_zero_matrix
    # bar: L_k -> word in sigma^-1 (an automorphism), coefficients at 1/q
    Lbar = murphy(ginv, n)
    # stokes = bar o rev; rev fixes each L_k (palindromic word), so stokes acts on
    # e_lam like bar. hash: sigma -> -sigma^-1, coefficients at q.
    Lhash = murphy([-g for g in ginv], n)
    res = {}
    for lam in lams:
        bar_e = e_lam(lam, 1 / q, Lbar, n)
        hash_e = e_lam(lam, q, Lhash, n)
        res[lam] = dict(
            bar_fixes=(bar_e - E[lam]).is_zero_matrix,
            hash_is_conj=(hash_e - E[conj(lam)]).is_zero_matrix,
            hash_fixes=(hash_e - E[lam]).is_zero_matrix,
        )
    return ok, res


def main():
    failures = 0
    for q in (sp.Rational(3, 2), sp.Rational(5, 7)):
        for n in (2, 3, 4):
            ok, res = run(n, q)
            print(f"n={n} q={q}: e_lam idempotent+central+sum=1: {ok}")
            failures += (not ok)
            for lam, r in res.items():
                tag = "self-conj" if conj(lam) == lam else f"chiral (lam'={conj(lam)})"
                print(f"   {lam!s:14} {tag:24} bar fixes: {r['bar_fixes']!s:5}  "
                      f"hash -> e_lam': {r['hash_is_conj']!s:5}  hash fixes: {r['hash_fixes']}")
                failures += (not r["bar_fixes"]) + (not r["hash_is_conj"])
    # z under hash at n = 2: tr(hash(sigma)) = tr(-sigma^-1) = -(z - h) = h - z
    qs = sp.symbols("q", positive=True)
    zD = qs**3 / (qs**2 + 1)
    h = qs - 1 / qs
    zD_at_minus_qinv = zD.subs(qs, -1 / qs)
    check = sp.simplify((h - zD) - zD_at_minus_qinv)
    print(f"\nconvention D: h - z_D(q) - z_D(-1/q) = {check}  (0 => hash maps tr_D(q) to tr_D(-1/q))")
    failures += (check != 0)
    # Downstream: the convention-D (Jones/TL) Ocneanu weights. Each two-row weight is
    # d_lam/[2]^n with d_lam = prod_cells [2+c]/[hook] (bean qou-q425); rows >= 3 get 0.
    # Since bar fixes every e_lam and tr_D(e_lam) = y_lam * f^lam, bar-equivariance of tr_D
    # (markov_bar_equivariant_zD) predicts each y_lam is invariant under q -> 1/q.
    def qint(k):
        return (qs**k - qs**-k) / (qs - 1 / qs)
    print("\nD weights y_lam(q) - y_lam(1/q):")
    for n in (2, 3, 4, 5):
        for lam in partitions(n):
            if len(lam) > 2:
                continue
            cells = [(i, j) for i, r in enumerate(lam) for j in range(r)]
            cl = conj(lam)
            num = sp.prod([qint(2 + j - i) for i, j in cells])
            den = sp.prod([qint(lam[i] - j + cl[j] - i - 1) for i, j in cells])
            y = num / den / qint(2) ** n
            diff = sp.simplify(y - y.subs(qs, 1 / qs))
            print(f"   n={n} {lam!s:10} {diff}")
            failures += (diff != 0)
    print(f"\n{failures} failures")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
