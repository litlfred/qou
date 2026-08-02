#!/usr/bin/env python3
"""Option-B-hard bridge test: is the QOU atom module a symmetric power S^k V_n?

Bean qou-0rp2. The only surviving route to derive ρ_F = ν_SDP via the spherical
partition algebra (arXiv:2402.01890) needs the QOU atom's H_{3A}(q) module to be
(a summand of) the k-th symmetric power S^k V_n of the S_n defining module — the
Schur-Weyl dual pair (CS_n, SP_k(n)) acts on S^k V_n (paper eq 1.2), and then
ν_SDP = dim G_k(λ). Note SP_k(n) and the QOU Hecke algebra H_n(q) are centralizers
of DIFFERENT dual pairs (CS_n on S^k V_n vs U_q(gl_m) on tensor space), so the
bridge is not routine.

This probe tests a NECESSARY condition at q=1 (H_{3A}(1)=CS_{3A}): the atom's
Wedderburn-block support must equal the S_{3A}-irreducible support of some
S^k(V_{3A}). It computes S^k(V_n) decompositions via the Murnaghan-Nakayama rule
and compares to the deuteron's SDP-active blocks (n = 3A = 6, canonical strand
count).

RESULT (scope-(a) refutation, deuteron): the bridge is CONCRETELY FALSE. The
deuteron active support is {(6),(5,1),(4,2),(4,1,1),(3,3),(2,2,2),(2,1,1,1,1)}.
In Sym^k(C^6): (2,1^4) appears only for k≥10, while (3,2,1) appears for all k≥4;
so every symmetric power containing (2,1^4) also contains (3,2,1). But the
deuteron contains (2,1^4) and EXCLUDES (3,2,1) (its forbidden self-conjugate
block). No k satisfies both ⇒ the deuteron module is not any S^k V_6. Under the
canonical n=3A this refutes the SP_k(n) route to ν_SDP; a non-canonical n would
be a fit. (Combined with Option A refuted and Option-B-coarse refuted, all known
bridges to ρ_F=ν_SDP are now closed; the conjecture stays honestly open.)

Requires: numpy, sympy. Self-contained (MN rule implemented inline).
"""
from __future__ import annotations
from functools import lru_cache
from itertools import combinations_with_replacement as cwr
from math import factorial
from collections import Counter
import cmath
import numpy as np
from sympy.utilities.iterables import partitions as _parts


def partitions_of(n):
    out = []
    for p in _parts(n):
        lam = []
        for part, mult in sorted(p.items(), reverse=True):
            lam += [part] * mult
        out.append(tuple(lam))
    return out


@lru_cache(maxsize=None)
def chi(lam, mu):
    """S_n irreducible character χ^λ(μ) via Murnaghan-Nakayama."""
    lam = tuple(x for x in lam if x > 0)
    mu = tuple(mu)
    if len(mu) == 0:
        return 1 if sum(lam) == 0 else 0
    r, rest = mu[0], mu[1:]
    total = 0
    L = len(lam)
    beta = [lam[i] + (L - 1 - i) for i in range(L)]
    bset = set(beta)
    for b in list(beta):
        if b - r >= 0 and (b - r) not in bset:
            nb = sorted([x for x in beta if x != b] + [b - r], reverse=True)
            ht = sum(1 for x in beta if b - r < x < b)
            m = len(nb)
            nl = tuple(x for x in (nb[i] - (m - 1 - i) for i in range(m)) if x > 0)
            total += (-1) ** ht * chi(nl, rest)
    return total


def _ccsize(mu, n):
    c = Counter(mu)
    z = 1
    for part, mult in c.items():
        z *= (part ** mult) * factorial(mult)
    return factorial(n) // z


def _perm_eigs(mu):
    e = []
    for d in mu:
        e += [cmath.exp(2j * cmath.pi * t / d) for t in range(d)]
    return e  # full n-dim permutation module C^n


def _symk_char(mu, k):
    e = _perm_eigs(mu)
    if k == 0:
        return 1.0
    return sum(np.prod([e[i] for i in idx]) for idx in cwr(range(len(e)), k))


def symk_support(n, k):
    mus = partitions_of(n)
    order = factorial(n)
    S = set()
    for lam in partitions_of(n):
        s = sum(_ccsize(mu, n) * _symk_char(mu, k) * chi(lam, mu) for mu in mus)
        if round((s / order).real) != 0:
            S.add(lam)
    return S


def main() -> int:
    n = 6
    deut = {(6,), (5, 1), (4, 2), (4, 1, 1), (3, 3), (2, 2, 2), (2, 1, 1, 1, 1)}
    print(f"Deuteron (n=3A=6) active Wedderburn support: {sorted(deut, reverse=True)}")
    print("\nSym^k(C^6) support test for the (2,1^4)-present / (3,2,1)-absent window:")
    ok = False
    for k in range(0, 16):
        S = symk_support(n, k)
        has214 = (2, 1, 1, 1, 1) in S
        has321 = (3, 2, 1) in S
        exact = S == deut
        if exact:
            ok = True
        print(f"  k={k:2d}: (2,1^4)={has214!s:5} (3,2,1)={has321!s:5} "
              f"exact_match={exact}")
    print("\nVerdict: no k reproduces the deuteron support. (2,1^4)∈S only for k≥10, "
          "(3,2,1)∈S for k≥4 ⇒ the two never occur as (present, absent). The "
          "deuteron needs (2,1^4) present AND (3,2,1) absent ⇒ NOT a symmetric "
          "power. Option-B-hard bridge REFUTED for the deuteron (canonical n=3A).")
    return 0 if not ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
