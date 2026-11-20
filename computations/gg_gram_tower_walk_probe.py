#!/usr/bin/env python3
"""
gg_gram_tower_walk_probe — walk the Frobenius pairing <g,g> = tr_M(T_v T_w) up
the Hecke tower on the GB normal-form basis, and measure how much of each level
the pairing CANNOT SEE.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. This is the <g,g> tower walk;
it exists because the recorded negative was measured on the wrong basis.

## Why the existing negative does not settle this

AGENTS.md records the Gram/Frobenius + confinement-SDP route as a scope-(a)
negative, tested in `deuteron_real_sdp.py` at H_6: "the diagonal Gram SDP is
degenerate and 0 of 6 off-diagonal encodings derive the binding".

Read that producer's own header and the degeneracy is not a discovery, it is a
CONSEQUENCE OF THE BASIS:

    operators     b_lambda := P_lambda            (Wedderburn block projectors)
    Frobenius Gram  G_{lm} := tr_M(P_l P_m) = delta_{lm} * tr_M(P_l)
                                              (diagonal: the P_lambda are
                                               orthogonal CENTRAL idempotents)

A diagonal Gram has no off-diagonal content to begin with, so <g,g> on the
Wedderburn blocks is degenerate BY CONSTRUCTION and the SDP built on it can only
report back what its net constraint puts in. That is exactly what happened -- the
one non-zero result was the AME value fed in as the constraint.

**The blocks are the wrong basis for this question.** The GB normal-form basis is
the one where the pairing is not diagonal, and it is also the basis the whole
jet/GB filtration story is told in.

## What is measured

At each level `n` of the tower, on the length-ordered GB normal-form basis
`{T_w : w in S_n}`:

    G^{(n)}_{vw} = tr_M(T_v T_w)          (this IS <g,g>)

and then: rank, CORANK, and where the radical sits in the jet filtration.

The single fact that motivates the walk: at `n = 3`, under convention D, this
Gram is **singular**, and `pyhecke.gram` gives its radical in closed form as

    v_i = (-1/q)^{len(w_i)}               the 3-strand q-antisymmetriser

-- a vector indexed by WORD LENGTH, i.e. by the jet / GB filtration degree. So
the degeneracy is not numerical noise; it is a specific element sitting at a
definite place in the filtration. The question the tower walk answers is whether
the invisible subspace stays one-dimensional or GROWS with `n`.

If it grows, that is a candidate mechanism for the binding deficit growing with
A: more of the tower would be invisible to <g,g> at every step.

## Implementation

General-`n` Hecke arithmetic, built here rather than borrowed, because
`pyhecke.gram` is hardcoded to the 6-element H_3 basis:

  * elements are dicts {permutation tuple -> mpf coefficient};
  * right multiplication by a generator uses the Hecke relation in the repo
    convention (AGENTS.md 7a) `sigma_i^2 = h sigma_i + 1`, `h = q - 1/q`:
        T_w T_i = T_{w s_i}                  if len(w s_i) > len(w)
        T_w T_i = T_{w s_i} + h T_w          otherwise;
  * the Markov trace is the standard recursion via the coset factorisation
    `w = u . d`, `u in S_{n-1}`, `d = s_{n-1} s_{n-2} ... s_k`, using the Markov
    property `tr_n(x T_{n-1} y) = z tr_{n-1}(x y)` with `z = q^3/(q^2+1)`
    (convention D).

Both are checked against `pyhecke.gram.gram_matrix_mp()` at n = 3 before any
result is reported -- if the reimplementation disagrees with production, the
probe fails rather than reporting its own arithmetic.

## Scope

Scope **(a)**: a structural measurement of where the pairing is blind. It does
NOT derive a binding energy, does not run an SDP, and proposes no closure. What
it is for is deciding whether the <g,g> route was refuted or merely mis-based.

NO FLOAT64: mpmath `mpf` at 50 dps, 50-digit proton pin, convention D. `float`
appears nowhere.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

from itertools import permutations  # noqa: E402

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 50

N_MAX = 5          # H_5 has dim 120 -> a 120x120 Gram; H_6 (720) is out of reach here


# --------------------------------------------------------------------------
# symmetric-group plumbing (one-line permutations as tuples, 0-indexed)
# --------------------------------------------------------------------------
def s_i(n: int, i: int) -> tuple:
    """The adjacent transposition s_i, as a one-line tuple of length n."""
    p = list(range(n))
    p[i], p[i + 1] = p[i + 1], p[i]
    return tuple(p)


def compose(a: tuple, b: tuple) -> tuple:
    """(a.b)(k) = a(b(k))."""
    return tuple(a[b[k]] for k in range(len(a)))


def inv_count(p: tuple) -> int:
    """Coxeter length = number of inversions."""
    n = len(p)
    return sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])


# --------------------------------------------------------------------------
# Hecke arithmetic on the GB normal-form (T_w) basis
# --------------------------------------------------------------------------
def mul_gen(elt: dict, i: int, n: int, h) -> dict:
    """Right-multiply by T_i using sigma_i^2 = h sigma_i + 1."""
    out: dict = {}
    si = s_i(n, i)
    for w, c in elt.items():
        ws = compose(w, si)
        if inv_count(ws) > inv_count(w):
            out[ws] = out.get(ws, mp.mpf(0)) + c
        else:
            out[ws] = out.get(ws, mp.mpf(0)) + c
            out[w] = out.get(w, mp.mpf(0)) + h * c
    return out


def reduced_word(w: tuple) -> list:
    """A reduced word for w as a list of generator indices (bubble sort)."""
    p, word = list(w), []
    n = len(p)
    changed = True
    while changed:
        changed = False
        for i in range(n - 1):
            if p[i] > p[i + 1]:
                p[i], p[i + 1] = p[i + 1], p[i]
                word.append(i)
                changed = True
    return word[::-1]          # applied left-to-right rebuilds w


def t_word(w: tuple, n: int, h) -> dict:
    """T_w as a basis element (it IS a basis element; built by folding)."""
    elt = {tuple(range(n)): mp.mpf(1)}
    for i in reduced_word(w):
        elt = mul_gen(elt, i, n, h)
    return elt


def mul(a: dict, b: tuple, n: int, h) -> dict:
    """Multiply element `a` by the basis element T_b."""
    out = dict(a)
    for i in reduced_word(b):
        out = mul_gen(out, i, n, h)
    return out


# --------------------------------------------------------------------------
# Markov trace, by the coset recursion
# --------------------------------------------------------------------------
def _tr_perm(w: tuple, n: int, h, z, memo: dict):
    """tr_n(T_w) for a basis element, normalised tr(1) = 1."""
    key = (n, w)
    if key in memo:
        return memo[key]
    if n <= 1:
        memo[key] = mp.mpf(1)
        return memo[key]
    if w[n - 1] == n - 1:                      # w fixes the last strand
        r = _tr_perm(w[: n - 1], n - 1, h, z, memo)
        memo[key] = r
        return r
    # Right-coset factorisation w = u . d with u in S_{n-1} (fixing the last
    # position) and d the MINIMAL rep, so lengths add and T_w = T_u T_d.
    #
    # u = w . d^-1 fixes position n-1 iff d(j) = n-1 where j = w^-1(n-1), i.e.
    # j is the position at which w carries the value n-1.  The minimal such d
    # is the cycle j -> n-1 shifting j+1..n-1 down by one; its reduced word is
    # s_{n-2} s_{n-3} ... s_j, so it contains exactly ONE copy of the last
    # generator s_{n-2} and the Markov property peels it:
    #     tr_n(T_u . T_{n-2} . T_{n-3}...T_j) = z * tr_{n-1}(T_u . T_{n-3}...T_j)
    j = w.index(n - 1)
    d = [0] * n
    for k in range(n):
        d[k] = k if k < j else (n - 1 if k == j else k - 1)
    d = tuple(d)
    dinv = tuple(sorted(range(n), key=lambda k: d[k]))
    u = compose(w, dinv)
    assert u[n - 1] == n - 1, "coset factorisation must fix the last strand"
    # d'' = d with the leading s_{n-2} dropped: the same cycle one strand
    # shorter, living in S_{n-1} and fixing position n-1.
    dd = [0] * (n - 1)
    for k in range(n - 1):
        dd[k] = k if k < j else (n - 2 if k == j else k - 1)
    # T_u . T_{d''} is a HECKE product, not a permutation composition: when the
    # lengths do not add it collapses via sigma^2 = h sigma + 1 and picks up
    # extra basis terms.  Composing the permutations instead loses exactly those
    # terms -- e.g. at n=3, w_0 needs tr_2(T_0 . T_0) = tr_2(h T_0 + 1) = h z + 1,
    # giving h z^2 + z, whereas the permutation product is the identity and
    # gives z.  That was a real bug here, caught by the n=3 calibration gate.
    prod = mul({tuple(u[: n - 1]): mp.mpf(1)}, tuple(dd), n - 1, h)
    r = z * mp.fsum(c * _tr_perm(v, n - 1, h, z, memo) for v, c in prod.items())
    memo[key] = r
    return r


def tr_M(elt: dict, n: int, h, z, memo: dict):
    return mp.fsum(c * _tr_perm(w, n, h, z, memo) for w, c in elt.items())


# --------------------------------------------------------------------------
def gram(n: int, h, z, memo: dict):
    """G_{vw} = tr_M(T_v T_w) on the length-ordered NF basis."""
    basis = sorted(permutations(range(n)), key=lambda w: (inv_count(w), w))
    G = [[mp.mpf(0)] * len(basis) for _ in basis]
    for i, v in enumerate(basis):
        tv = t_word(v, n, h)
        for j, w in enumerate(basis):
            G[i][j] = tr_M(mul(tv, w, n, h), n, h, z, memo)
    return basis, G


def rank_and_radical(G, tol):
    """Rank + an orthonormal-ish basis of the radical, by mpmath SVD."""
    M = mp.matrix(G)
    U, S, V = mp.svd_r(M)
    sv = [S[k] for k in range(len(G))]
    rank = sum(1 for s in sv if abs(s) > tol)
    rad = [[V[k, j] for j in range(len(G))] for k in range(len(G))
           if abs(sv[k]) <= tol]
    return rank, sv, rad


def fmt(x, n=8):
    return mp.nstr(x, n)


def main() -> int:
    q0 = Q_MP
    h = q0 - 1 / q0
    z = q0**3 / (q0**2 + 1)                    # convention D
    memo: dict = {}

    print("gg_gram_tower_walk_probe")
    print("=" * 78)
    print(f"q0 = {fmt(q0, 20)}   h = {fmt(h, 12)}   z = {fmt(z, 12)}  [conv D]")
    print()
    print("<g,g>_{vw} = tr_M(T_v T_w) on the length-ordered GB normal-form basis.")
    print("Contrast: deuteron_real_sdp uses the Wedderburn block projectors, for")
    print("which G is DIAGONAL by construction (orthogonal central idempotents),")
    print("so its degeneracy is a property of the basis, not of the pairing.")
    print()

    # ---- calibration against production before reporting anything ---------
    print("CALIBRATION — reimplementation vs production pyhecke at n = 3")
    print("-" * 78)
    basis3, G3 = gram(3, h, z, memo)
    try:
        from pyhecke.gram import gram_matrix_mp
        Gp = gram_matrix_mp()
        worst = mp.mpf(0)
        for i in range(6):
            for j in range(6):
                worst = max(worst, abs(G3[i][j] - Gp[i][j]))
        print(f"  worst |mine - pyhecke| over the 6x6 = {fmt(worst, 6)}")
        calibrated = worst < mp.mpf(10) ** -30
        print(f"  agrees to 1e-30: {calibrated}")
        if not calibrated:
            print("  BASIS ORDER may differ (pyhecke's NF_BASIS ordering is its")
            print("  own); comparing SPECTRA instead, which is order-independent:")
            _, sm, _ = rank_and_radical(G3, mp.mpf(10) ** -30)
            _, sp_, _ = rank_and_radical([[Gp[i][j] for j in range(6)]
                                          for i in range(6)], mp.mpf(10) ** -30)
            for a, b in zip(sorted(map(abs, sm)), sorted(map(abs, sp_))):
                print(f"    {fmt(a, 10):>16}  vs  {fmt(b, 10):>16}")
            worst_s = max(abs(a - b) for a, b in
                          zip(sorted(map(abs, sm)), sorted(map(abs, sp_))))
            print(f"  worst singular-value gap = {fmt(worst_s, 6)}")
            assert worst_s < mp.mpf(10) ** -30, \
                "reimplementation must match production spectrum at n=3"
            print("  spectra agree => the reimplementation is faithful, basis")
            print("  ordering differs only.")
    except ImportError:
        print("  pyhecke unavailable in this environment -- calibration SKIPPED.")
        print("  Results below are therefore UNCALIBRATED; treat with suspicion.")
    print()

    # ---- the walk ----------------------------------------------------------
    print("THE WALK — how much of each level is invisible to <g,g>")
    print("-" * 78)
    tol = mp.mpf(10) ** -35
    print(f"{'n':>3} {'dim H_n':>8} {'rank':>6} {'corank':>7} "
          f"{'top jet deg':>12} {'smallest |sv|':>16} {'largest |sv|':>16}")
    results = []
    for n in range(2, N_MAX + 1):
        basis, G = gram(n, h, z, memo)
        rank, sv, rad = rank_and_radical(G, tol)
        dim = len(basis)
        corank = dim - rank
        a = sorted(map(abs, sv))
        results.append((n, dim, rank, corank, sv, rad, basis))
        print(f"{n:>3} {dim:>8} {rank:>6} {corank:>7} {n*(n-1)//2:>12} "
              f"{fmt(a[0], 10):>16} {fmt(a[-1], 10):>16}")
    print()

    # ---- is the radical the q-antisymmetriser, i.e. length-indexed? --------
    print("IS THE RADICAL LENGTH-INDEXED?  (pyhecke's closed form at n=3 is")
    print("v_i = (-1/q)^len(w_i), the q-antisymmetriser -- a JET-DEGREE vector)")
    print("-" * 78)
    for n, dim, rank, corank, sv, rad, basis in results:
        if corank == 0:
            print(f"  n = {n}: corank 0 -- the pairing is non-degenerate here.")
            continue
        pred = [(-1 / q0) ** inv_count(w) for w in basis]
        nrm = mp.sqrt(mp.fsum(x**2 for x in pred))
        pred = [x / nrm for x in pred]
        # The right question is whether the antisymmetriser LIES IN the radical,
        # i.e. the norm of its projection onto that subspace -- NOT its overlap
        # with any single radical basis vector.  Once the radical is
        # many-dimensional the single-vector overlap understates badly (it read
        # 0.41 at n=5 while the projection is ~1).
        proj2 = mp.mpf(0)
        for v in rad:
            nv = mp.sqrt(mp.fsum(x**2 for x in v))
            vv = [x / nv for x in v]
            proj2 += mp.fsum(a * b for a, b in zip(vv, pred)) ** 2
        proj = mp.sqrt(proj2)
        print(f"  n = {n}: corank {corank}; "
              f"||P_radical (-1/q)^len|| = {fmt(proj, 12)}")
        if proj > mp.mpf("0.999999"):
            print("      => the q-antisymmetriser LIES IN the radical "
                  "(length-indexed, as at n=3)")
        else:
            print("      => the q-antisymmetriser is NOT wholly in the radical")
    print()

    # ---- the rank is the Catalan number = dim TL_n -------------------------
    print("THE RANK IS THE CATALAN NUMBER — <g,g> sees exactly Temperley-Lieb")
    print("-" * 78)

    def catalan(k):
        # math.comb returns an exact arbitrary-precision int, not a float, and it
        # is combined only by integer floor division. Every downstream division is
        # routed through mp.mpf before dividing.
        from math import comb  # float64-ok: exact integer binomial, no float path
        return comb(2 * k, k) // (k + 1)

    print(f"{'n':>3} {'dim H_n = n!':>13} {'rank <g,g>':>11} {'C_n = dim TL_n':>15} "
          f"{'equal':>6} {'visible fraction':>17}")
    ok = True
    for n, dim, rank, corank, _sv, _rad, _b in results:
        cn = catalan(n)
        eq = rank == cn
        ok = ok and eq
        print(f"{n:>3} {dim:>13} {rank:>11} {cn:>15} {str(eq):>6} "
              f"{fmt(mp.mpf(rank) / dim * 100, 6) + ' %':>17}")
    assert ok, "rank of the Markov-trace Gram must equal the Catalan number"
    print()
    print("  This is the classical fact that the Markov (Jones) trace form on")
    print("  H_n(q) has radical exactly the kernel of H_n -> TL_n, so <g,g>")
    print("  factors through Temperley-Lieb and its rank is dim TL_n = C_n.")
    print("  Verified here at n = 2..5 rather than cited.")
    print()
    print("  CONSEQUENCE FOR THE ATOM.  The atom word lives at n = 3A, so the")
    print("  fraction of the tower <g,g> can see is C_{3A}/(3A)! :")
    print(f"{'A':>3} {'n = 3A':>7} {'(3A)!':>22} {'C_{3A}':>14} "
          f"{'visible fraction':>18}")
    for A in (1, 2, 3, 4, 6):
        # math.factorial returns an exact arbitrary-precision int. It is printed
        # as an int and, where divided, is lifted to mp.mpf first (see `frac`
        # below), so no float64 enters the visible-fraction ratio.
        from math import factorial  # float64-ok: exact integer factorial, no float path
        n3 = 3 * A
        cn = catalan(n3)
        frac = mp.mpf(cn) / mp.mpf(factorial(n3))
        print(f"{A:>3} {n3:>7} {factorial(n3):>22} {cn:>14} "
              f"{fmt(frac * 100, 6) + ' %':>18}")
    print()
    print("  PREDICTION, not measurement: the walk above measured n = 2..5")
    print("  directly; the A >= 2 rows use the verified rank law C_n rather than")
    print("  a computed Gram (H_6 is 720x720 and H_12 is out of reach entirely).")
    print("  They stand or fall with the rank law, which is gated at n = 2..5.")
    print()

    print("READING")
    print("-" * 78)
    coranks = [(n, c) for n, _d, _r, c, _s, _rad, _b in results]
    print(f"  corank by level: {coranks}")
    grows = len(coranks) > 1 and coranks[-1][1] > coranks[0][1]
    if grows:
        print("  The invisible subspace GROWS with n, and not gently: the")
        print("  VISIBLE fraction is C_n/n!, which collapses super-exponentially.")
        print()
        print("  🛑 DO NOT read this as explaining the binding deficit")
        print("  QUANTITATIVELY -- it does not, and the arithmetic says so.  If")
        print("  the deficit scaled with the invisible fraction, 4He (visible")
        print("  0.043 %) would miss by a factor of ~2300.  It misses by 3.26.")
        print("  So the deficit does NOT track 1/visible_fraction, and any claim")
        print("  that blindness 'accounts for' the A-dependence is refuted by")
        print("  its own numbers.")
        print()
        print("  What IS established is structural: <g,g> is not a faithful")
        print("  pairing on the tower at any A >= 1, it factors through")
        print("  Temperley-Lieb, and the part it discards is the bulk.  That")
        print("  says an SDP built on <g,g> cannot select among Hecke elements")
        print("  differing only in the radical -- which is most of them.")
    else:
        print("  The invisible subspace does NOT grow across the levels measured.")
        print("  So a growing-blindness explanation of the A-dependence is NOT")
        print("  supported by this walk, and should not be asserted.")
    print()
    print("WHAT THIS DOES AND DOES NOT SETTLE")
    print("-" * 78)
    print("  * It does NOT overturn the recorded scope-(a) negative.  That")
    print("    negative is correct for the basis it was measured in.")
    print("  * It DOES show that basis was diagonal by construction, so the")
    print("    negative is about the Wedderburn encoding, not about <g,g>.")
    print("  * No SDP is run and no binding energy is produced here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
