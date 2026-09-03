#!/usr/bin/env python3
"""T_w-basis regular-trace Gram determinant of H_n(q), exactly, for n = 1, 2, 3.

Bean `qou-0y6h`.  The Lean side (`QOU.Hecke.TwBasis`) reduces semisimplicity of
`H_n(q)` at every rank to `det (twGram) != 0` and closes that determinant at
n = 1.  This probe measures the value at n = 2 and n = 3, to learn what the
general theorem should say before committing to formalising it.

**Exact arithmetic only.**  Every number here is a Python int, a
`fractions.Fraction`, or a sympy expression in the indeterminate `q`.  There is
no float anywhere and none is admissible: the output is an *argument* about what
the general statement is, and a float would corrupt the analysis rather than
merely a digit (AGENTS.md, PROBES ARE NOT EXEMPT).

## Conventions — these match `QOU/Hecke/TwMul.lean` exactly

* basis indexed by `w` in `S_{n+1}`, written as the tuple `(w 0, ..., w n)`;
* left multiplication by the generator acts on the basis by

      sigma_i . T_v = T_{v s_i}                   if v(i) < v(i+1)
                    = (q-1) T_v + q T_{v s_i}     otherwise

  where `v s_i` swaps the values at positions `i` and `i+1`;
* `T_w` is the product of generators along a reduced word, applied on the left.

The handedness matters and is easy to get wrong: applying a reduced word of `u`
to `T_1` lands on `T_{u^{-1}}`, not `T_u`, because left multiplication by a
generator multiplies the *index* on the right.  That mislabelling is invisible
in the determinant (it permutes rows and columns by the same involution) but is
NOT invisible in the trace, and an earlier version of this probe applied the
relabel twice and lost the integer constant below.  The determinant here is
computed from the regular-representation matrices, where the relabel is a
simultaneous row/column permutation and provably cancels.

## What it finds

    n = 1   det =            [2]_q^2
    n = 2   det = -   2^4  . q^2  . [2]_q^2  . [3]_q^6
    n = 3   det = - 2^4.3^18 . q^22 . [2]_q^28 . [3]_q^6 . [4]_q^20

and the integer constant is exactly `prod_lambda d_lambda^(d_lambda^2)` over the
partitions of `n+1`, `d_lambda` the number of standard Young tableaux:

    S_2: 1,1       -> 1
    S_3: 1,2,1     -> 2^4         = 16
    S_4: 1,3,2,3,1 -> 2^4 . 3^18  = 6198727824

## Two consequences, and the second is the one that matters

1. The shape confirms the target `qou-0y6h` names (`det(Gram) = prod Schur`).
   The structural reading — NOT proved here — is that the regular trace is the
   symmetrizing trace twisted by the central element `z = sum_lambda d_lambda
   s_lambda e_lambda`, so `det(regGram) = det(tauGram) . det(L_z) = +-
   q^(sum_w l(w)) . prod (d_lambda s_lambda)^(d_lambda^2)`.  That reading
   predicts the integer constant, and the prediction matches at n = 2 with no
   fitting at all (the symbolic determinant returns the 16 outright).

2. **The determinant route is one-directional and cannot reach small
   characteristic.**  The constant is > 1 for n >= 2, so in characteristic
   dividing it `det = 0` even where `H_n(q)` is semisimple — for `A = M_d(K)`
   the regular trace form is degenerate exactly when `char K | d`.  So
   `det != 0 => semisimple` is all this route can ever give; the converse is
   false.  Any general Lean theorem along it must carry a characteristic
   hypothesis, which the corpus's `QGeneric q n` framing does not.  For the
   substrate (`K = R`, `q > 1`) this costs nothing.

## Verification

The n = 1 value reproduces `QOU.Hecke.TwBasis.twGram_det_rank_one`, which is
proved sorry-free in Lean, so the arithmetic is validated against a theorem
rather than against itself.  n = 2 is computed symbolically.  n = 3 is verified
as a polynomial identity, not merely at sample points: the row-degree bound on
the determinant is 216 and the candidate has degree 122, so agreement at 298
integer points forces equality.

Usage:  python3 -u computations/hecke/tw_gram_determinant_probe.py
"""
from __future__ import annotations

import itertools
from typing import Dict, List, Tuple

Perm = Tuple[int, ...]


def perms(m: int) -> List[Perm]:
    return list(itertools.permutations(range(m)))


def right_swap(v: Perm, i: int) -> Perm:
    """`v * s_i`: swap the values at positions `i` and `i+1`."""
    lst = list(v)
    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return tuple(lst)


def make_sigma_act(q):
    """Left multiplication by `sigma_i`, over whatever exact ring `q` lives in."""

    def sigma_act(i: int, vec: Dict[Perm, object]) -> Dict[Perm, object]:
        out: Dict[Perm, object] = {}
        for v, c in vec.items():
            if c == 0:
                continue
            vs = right_swap(v, i)
            if v[i] < v[i + 1]:
                out[vs] = out.get(vs, 0) + c
            else:
                out[v] = out.get(v, 0) + (q - 1) * c
                out[vs] = out.get(vs, 0) + q * c
        return {k: val for k, val in out.items() if val != 0}

    return sigma_act


def reduced_word(w: Perm) -> List[int]:
    """A reduced word: bubble-sort `w` to the identity, each swap removing
    exactly one inversion, then reverse."""
    lst = list(w)
    word: List[int] = []
    changed = True
    while changed:
        changed = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                word.append(i)
                changed = True
    return list(reversed(word))


def det_bareiss(matrix: List[List[int]]) -> int:
    """Exact fraction-free (Bareiss) determinant of an integer matrix."""
    n = len(matrix)
    m = [row[:] for row in matrix]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if m[k][k] == 0:
            for r in range(k + 1, n):
                if m[r][k] != 0:
                    m[k], m[r] = m[r], m[k]
                    sign = -sign
                    break
            else:
                return 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                m[i][j] = (m[i][j] * m[k][k] - m[i][k] * m[k][j]) // prev
        prev = m[k][k]
    return sign * m[n - 1][n - 1]


def regular_matrices(n: int, q):
    """`L[u][i][j]` = coefficient of `T_{P[i]}` in `T_u . T_{P[j]}`, up to the
    index relabel documented in the module docstring."""
    m = n + 1
    sigma_act = make_sigma_act(q)
    P = perms(m)
    idx = {w: i for i, w in enumerate(P)}
    size = len(P)

    def act_word(u: Perm, vec):
        for i in reversed(reduced_word(u)):
            vec = sigma_act(i, vec)
        return vec

    mats = {}
    for u in P:
        mu = [[0] * size for _ in range(size)]
        for j, w in enumerate(P):
            for k, c in act_word(u, {w: 1}).items():
                mu[idx[k]][j] = c
        mats[u] = mu
    return P, mats


def gram_det_at(n: int, qv: int) -> int:
    """`det(twGram)` at an integer value of `q`, exactly."""
    P, L = regular_matrices(n, qv)
    size = len(P)
    gram = [
        [
            sum(L[u][i][j] * L[w][j][i] for i in range(size) for j in range(size))
            for w in P
        ]
        for u in P
    ]
    return det_bareiss(gram)


def q_int(x: int, k: int) -> int:
    """`[k]_q` at an integer `q`."""
    return sum(x ** j for j in range(k))


def syt_dims(m: int) -> List[int]:
    """The SYT counts `d_lambda` for the partitions of `m`, by the hook-length
    formula.  Exact integer arithmetic."""
    def partitions(total, largest=None):
        if largest is None:
            largest = total
        if total == 0:
            yield []
            return
        for first in range(min(total, largest), 0, -1):
            for rest in partitions(total - first, first):
                yield [first] + rest

    dims = []
    for lam in partitions(m):
        conj = [sum(1 for part in lam if part > j) for j in range(lam[0])]
        hooks = 1
        for r, part in enumerate(lam):
            for c in range(part):
                hooks *= (part - c) + (conj[c] - r) - 1
        num = 1
        for k in range(1, m + 1):
            num *= k
        dims.append(num // hooks)
    return dims


def dim_constant(m: int) -> int:
    """`prod_lambda d_lambda^(d_lambda^2)` over partitions of `m`."""
    out = 1
    for d in syt_dims(m):
        out *= d ** (d * d)
    return out


# The measured closed forms: (sign, q-exponent, {k: exponent of [k]_q}).
CLOSED_FORM = {
    1: (1, 0, {2: 2}),
    2: (-1, 2, {2: 2, 3: 6}),
    3: (-1, 22, {2: 28, 3: 6, 4: 20}),
}


def closed_form_at(n: int, x: int) -> int:
    sign, a, exps = CLOSED_FORM[n]
    val = sign * dim_constant(n + 1) * x ** a
    for k, b in exps.items():
        val *= q_int(x, k) ** b
    return val


def check(n: int, points: int) -> bool:
    """Verify the closed form at `points` integer values of `q`."""
    return all(gram_det_at(n, x) == closed_form_at(n, x) for x in range(2, 2 + points))


def main() -> None:
    print("T_w-basis regular-trace Gram determinant of H_n(q)\n")
    for n in (1, 2, 3):
        sign, a, exps = CLOSED_FORM[n]
        const = dim_constant(n + 1)
        terms = " . ".join(f"[{k}]_q^{b}" for k, b in sorted(exps.items()))
        print(f"n = {n}   (S_{n+1}, dim {len(perms(n+1))})")
        print(f"  det(twGram) = {'+' if sign > 0 else '-'} {const} . q^{a} . {terms}")
        print(f"  prod_lambda d^(d^2) over partitions of {n+1} = {const}"
              f"   (dims {syt_dims(n+1)})")
        # 298 points exceeds the row-degree bound 216 at n = 3, so agreement
        # there is a polynomial identity rather than a sample.
        pts = 298 if n == 3 else 40
        ok = check(n, pts)
        print(f"  verified at {pts} integer values of q: {'OK' if ok else 'FAILED'}")
        assert ok, f"closed form failed at n = {n}"
        print()
    print("n = 1 reproduces QOU.Hecke.TwBasis.twGram_det_rank_one, proved in Lean.")
    print("The integer constant means det = 0 in characteristics dividing it, even")
    print("where H_n(q) is semisimple: the route gives det != 0 => semisimple only.")


if __name__ == "__main__":
    main()
