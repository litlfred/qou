"""Temperley–Lieb quotient of `H_n(q)`: basis, Markov–Gram form, and its
genuine inverse — general `n`, exact, **additive** to `pyhecke.gram`.

Bean `qou-8iru` (the TL_n compute move) / `qou-cds2` (the Gram singularity).

## Why this module exists

Under trace convention D (`z = q³/(q²+1)`) the Markov–Gram form on the *full*
`H_n(q)` basis `{T_w : w ∈ S_n}` is **identically singular** — not
ill-conditioned, singular: `det G = 0` exactly over ℚ(q), because the Markov
weight `y_λ` vanishes for every partition with ≥ 3 rows
(`QOU.QBeta.WenzlWeight.conventionD_weight_eq_zero_iff`, sorry-free, all `n`).
The radical is exactly `ker(H_n → TL_n)`, of dimension `n! − Catalan(n)`.

Consumers have been working *around* that degeneracy rather than through it:

| site | workaround |
|---|---|
| `pyhecke.gram.G_PINV` (`gram.py`) | `np.linalg.pinv` at module import |
| `hecke-engine` `gram.rs` | rank-one-shift Moore–Penrose |
| `pyhecke.gram.gram_inverse` | raises `NotImplementedError` |
| `computations/confinement-operator-selection.py` | routes via `_pg_safe_inverse` |

**All four are unnecessary on the right basis.** The form descends to
`H_n/rad` (`QOU.QBeta.MarkovGramDegenerate.pairing_descends`) and is
non-degenerate there, so on a basis of the quotient it has an *inverse* — no
pseudo-, no shift, no `rcond`. At `n = 3` that is exact and closed-form: PR
#5572 established

    det G_TL = −(q⁴+1)(q²−q+1)⁴(q²+q+1)⁴ / (q²+1)¹⁰,

which has **no real roots**, so the quotient form is non-singular for *every*
real `q > 0`. This module builds that form for general `n`, and
`computations/qbeta/tl_quotient_gram_probe.py` re-derives the `n = 3`
determinant from this general-`n` code as a cross-implementation check.

## The basis

`tl_basis(n)` returns the **321-avoiding** (equivalently fully commutative)
permutations of `S_n`; there are `Catalan(n)` of them, and `{T_w}` over that
set is a basis of the quotient. This module does **not** take that on faith —
it is *verified* in the probe, exactly, by two facts that together force it:

1. `rank(G_full) = Catalan(n)` (measured exactly over ℚ: `n = 3, 4, 5` give
   ranks 5, 14, 42, i.e. coranks 1, 10, 78 — matching `qou-cds2`'s corank
   accounting `1`, `3²+1²`, `6²+5²+4²+1²`), so the radical has the stated
   dimension and the quotient has dimension `Catalan(n)`;
2. `det G_TL ≠ 0` on this set, so its `Catalan(n)` cosets are independent.

Independent + right cardinality = basis. Neither step cites a theorem this
repo has not checked.

At `n = 3` the 321-avoiding words are exactly the first five entries of
`pyhecke.gram.NF_BASIS` — which is *why* PR #5572's "take the first five NF
cosets" worked, and this module supplies the reason rather than the accident.

## Scalars — one implementation, three exact arithmetics

`tl_gram(n, q, ...)` is generic in the scalar type: it needs only `+ - * /`
and a `1`. That makes the same code exact over

* `fractions.Fraction` — a *rational* `q`; convention D's `z = q³/(q²+1)` is a
  rational function, so the whole Gram is exactly computable in ℚ (this is the
  only path that can *prove* singular vs. very-small);
* `sympy` — symbolic over ℚ(q), i.e. the pin-independent statement;
* `mpmath.mpf` — the true substrate `q₀`, which is not rational.

**There is no float64 path here, deliberately** (AGENTS.md "PROBES ARE NOT
EXEMPT", 2026-08-18). `pyhecke.gram`'s `q0`/`h`/`z` are float64 and are an
entry point into double precision with no signal; nothing in this module
touches them. The mpmath default `q` is the **proton**-pinned 50-digit
`Q_50_DIGIT_STR` (owner directive 2026-08-07), sourced exactly as
`pyhecke.gram._q0_50dps_str` sources it.

## What this module does NOT do

It adds names; it changes none. `pyhecke.gram`'s `G`, `G_PINV`, `RADICAL`,
`TR_M` and the raising `gram_inverse()` are untouched, and no consumer changes
behaviour by this file landing. Migrating the four workaround sites above onto
this form is separate, deliberate work — `G_PINV` is computed at *module
import*, so anything that reads it is affected the moment it changes, and
silently changing what an existing name means is how a wrong number keeps
circulating under a trusted label (`gram.py`'s own account of why `G_INV` was
deleted rather than rebound).
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import comb

__all__ = [
    "catalan",
    "tl_dim",
    "tl_basis",
    "tl_basis_words",
    "full_basis",
    "is_fully_commutative",
    "coxeter_length",
    "reduced_word",
    "hecke_mul_word",
    "markov_trace_basis",
    "markov_weights",
    "tl_gram",
    "tl_gram_exact",
    "gram_rank_exact",
    "tl_gram_mp",
    "tl_gram_inverse_exact",
    "tl_gram_inverse_mp",
    "tl_gram_solve_mp",
    "full_hecke_gram",
    "full_hecke_gram_exact",
]


# ══════════════════════════════════════════════════════════════
# Symmetric-group plumbing
# ══════════════════════════════════════════════════════════════
# A permutation `w ∈ S_n` is a tuple `p` of length `n` in one-line notation:
# `p[i] = w(i+1)`.  Generators are 0-indexed: `s_i` swaps *positions* i, i+1,
# so `s_0, …, s_{n-2}` generate `S_n` and `s_0, …, s_{n-3}` generate the
# parabolic `S_{n-1}` (the permutations fixing `n`).  Right multiplication by
# `s_i` is therefore a positional swap, which is the convention
# `pyhecke.gram.hm` and `computations/markov/markov_trace_recursive.py` both
# use; keeping it lets the `n = 3` cross-check below be an equality rather
# than a translation.


def catalan(n: int) -> int:
    """`C_n = binom(2n, n) / (n+1)` — the dimension of `TL_n`."""
    return comb(2 * n, n) // (n + 1)


def tl_dim(n: int) -> int:
    """`dim TL_n = Catalan(n)`; `dim rad = n! − Catalan(n)`."""
    return catalan(n)


def _identity(n: int) -> tuple[int, ...]:
    return tuple(range(1, n + 1))


def _swap(p: tuple[int, ...], i: int) -> tuple[int, ...]:
    lst = list(p)
    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return tuple(lst)


def coxeter_length(p: tuple[int, ...]) -> int:
    """Number of inversions of `p` — the Coxeter length `ℓ(w)`."""
    n = len(p)
    return sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])


def reduced_word(p: tuple[int, ...]) -> tuple[int, ...]:
    """A reduced word for `p` in the 0-indexed generators.

    Greedy descent: strip a descent at a time, then reverse.  Each strip drops
    the length by exactly one, so the result has length `ℓ(p)` and is reduced.
    """
    word: list[int] = []
    lst = list(p)
    n = len(lst)
    while True:
        for i in range(n - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                word.append(i)
                break
        else:
            break
    return tuple(reversed(word))


def is_fully_commutative(p: tuple[int, ...]) -> bool:
    """True iff `p` is 321-avoiding, i.e. fully commutative.

    `w` is fully commutative iff no reduced word for it contains a braid
    factor `s_i s_{i+1} s_i`, and (Billey–Jockusch–Stanley) that is equivalent
    to avoiding the pattern 321.  The pattern test is what is implemented,
    because it is `O(n³)` and needs no word enumeration.
    """
    n = len(p)
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] > p[j]:
                for k in range(j + 1, n):
                    if p[j] > p[k]:
                        return False
    return True


def _sorted_perms(n: int) -> tuple[tuple[int, ...], ...]:
    return tuple(sorted(permutations(range(1, n + 1)),
                        key=lambda p: (coxeter_length(p), p)))


@lru_cache(maxsize=None)
def full_basis(n: int) -> tuple[tuple[int, ...], ...]:
    """All of `S_n`, ordered by length then lexicographically — the basis of
    the *full* `H_n(q)`, on which the convention-D form is singular."""
    return _sorted_perms(n)


@lru_cache(maxsize=None)
def tl_basis(n: int) -> tuple[tuple[int, ...], ...]:
    """The `Catalan(n)` fully commutative permutations, length-ordered.

    At `n = 3` this is `[(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2)]` — the
    five NF words of `pyhecke.gram.NF_BASIS` other than `(0,1,0)`, whose
    permutation `(3,2,1)` is the one 321-pattern in `S_3`.
    """
    return tuple(p for p in full_basis(n) if is_fully_commutative(p))


@lru_cache(maxsize=None)
def tl_basis_words(n: int) -> tuple[tuple[int, ...], ...]:
    """`tl_basis(n)` as reduced words in the 0-indexed generators."""
    return tuple(reduced_word(p) for p in tl_basis(n))


# ══════════════════════════════════════════════════════════════
# Hecke multiplication (generic scalars)
# ══════════════════════════════════════════════════════════════
# `T_w T_i = T_{w s_i}` when `ℓ(w s_i) > ℓ(w)`, else `T_{w s_i} + h · T_w`,
# with `h = q − q⁻¹` — the AGENTS.md §7a Hecke relation
# `σ_i² = (q − q⁻¹) σ_i + 1` in the `T_w` basis.


def _mul_gen(elem: dict, i: int, h):
    out: dict = {}
    for p, c in elem.items():
        t = _swap(p, i)
        out[t] = out.get(t, 0) + c
        if p[i] > p[i + 1]:            # length drops ⇒ the quadratic term
            out[p] = out.get(p, 0) + c * h
    return {k: v for k, v in out.items() if v != 0}


def hecke_mul_word(elem: dict, word, h) -> dict:
    """Right-multiply a `{perm: scalar}` element by `T_{s_{i₁}} ⋯ T_{s_{i_k}}`."""
    for i in word:
        elem = _mul_gen(elem, i, h)
    return elem


# ══════════════════════════════════════════════════════════════
# The Ocneanu / Markov trace on the T_w basis (generic scalars)
# ══════════════════════════════════════════════════════════════


def _coset_rep(n: int, k: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Minimal-length representative of the coset `S_{n-1} w` with `w⁻¹(n) = k`.

    One-line `(1, …, k−1, n, k, …, n−1)`; reduced word `[n−2, n−3, …, k−1]`,
    of length `n − k`.  These `n` permutations (one per position `k`) are a
    transversal: two elements lie in the same coset iff they place `n` in the
    same position, because a `u ∈ S_{n-1}` fixes `n`.
    """
    d = tuple(list(range(1, k)) + [n] + list(range(k, n)))
    word = tuple(range(n - 2, k - 2, -1))
    return d, word


def _trace_basis(p: tuple[int, ...], n: int, h, z, one, cache: dict):
    key = (p, n)
    hit = cache.get(key)
    if hit is not None:
        return hit
    if n <= 1 or p == _identity(n):
        cache[key] = one
        return one
    k = p.index(n) + 1
    if k == n:                          # w fixes n ⇒ T_w ∈ H_{n-1}
        r = _trace_basis(p[:n - 1], n - 1, h, z, one, cache)
        cache[key] = r
        return r
    d, word = _coset_rep(n, k)
    # u = w d⁻¹, read off from u[d[m]-1] = p[m].
    u_lst: list = [None] * n
    for m in range(n):
        u_lst[d[m] - 1] = p[m]
    u = tuple(u_lst)
    # Minimal coset reps make the lengths additive; assert rather than assume,
    # since the whole recursion rests on `T_w = T_u T_d`.
    assert u[n - 1] == n, (p, n, u)
    assert coxeter_length(u) + coxeter_length(d) == coxeter_length(p), (p, n, u, d)
    # T_w = T_u · T_{n-2} T_{n-3} ⋯ T_{k-1} = (T_u) · T_{n-2} · (T_{n-3} ⋯ T_{k-1}),
    # i.e. `a T_{n-2} b` with a, b ∈ H_{n-1}.  The Markov axiom
    # tr(a T_{n-2} b) = z · tr(a b) then applies, and `a b` is computed inside
    # H_{n-1} — the recursion never applies the axiom outside the subalgebra.
    inner = hecke_mul_word({u[:n - 1]: one}, word[1:], h)
    total = 0 * one
    for w2, c in inner.items():
        total = total + c * _trace_basis(w2, n - 1, h, z, one, cache)
    r = z * total
    cache[key] = r
    return r


def markov_trace_basis(p: tuple[int, ...], n: int, h, z, one=1, cache=None):
    """`tr_M(T_p)` for `p ∈ S_n`, by the Ocneanu recursion, in any scalar type.

    Verified against the authoritative hard-coded `pyhecke.gram.TR_M` at
    `n = 3`: `[1, z, z, z², z², h z² + z]` on `NF_BASIS`, exactly.
    """
    return _trace_basis(p, n, h, z, one, {} if cache is None else cache)


def markov_weights(q, one=1):
    """`(h, z)` for convention D: `h = q − q⁻¹`, `z = q³/(q² + 1)`.

    Convention D is canonical (owner ruling 2026-08-15).  It is *because* of
    this `z` that the form is singular on the full basis and Temperley–Lieb on
    the quotient — the degeneracy is what convention D means, not a defect it
    introduced (`qou-8iru`).
    """
    return q - one / q, q ** 3 / (q ** 2 + one)


# ══════════════════════════════════════════════════════════════
# The Gram forms
# ══════════════════════════════════════════════════════════════


def _gram(basis, n: int, h, z, one):
    m = len(basis)
    cache: dict = {}
    words = [reduced_word(v) for v in basis]
    rows = []
    for u in basis:
        row = []
        for wv in words:
            prod = hecke_mul_word({u: one}, wv, h)
            acc = 0 * one
            for w2, c in prod.items():
                acc = acc + c * _trace_basis(w2, n, h, z, one, cache)
            row.append(acc)
        rows.append(row)
    assert len(rows) == m
    return rows


def tl_gram(n: int, q, one=1):
    """`G_TL[i][j] = tr_M(T_u T_v)` over `tl_basis(n)` — the descended form.

    Generic in the scalar type of `q` (`Fraction`, `sympy`, `mpmath.mpf`).
    The entries depend only on the *cosets* of `T_u`, `T_v` mod the radical
    (`pairing_descends`), so this genuinely is the quotient form and not a
    corner of the singular one.
    """
    h, z = markov_weights(q, one)
    return _gram(tl_basis(n), n, h, z, one)


def full_hecke_gram(n: int, q, one=1):
    """The *singular* Markov–Gram form on all of `S_n` — kept for audit.

    This is the object whose degeneracy the `pinv` / Moore–Penrose / raising
    workarounds exist for.  Its rank is `Catalan(n)`, so its corank is
    `n! − Catalan(n)`: 1, 10, 78 at `n = 3, 4, 5`.
    """
    h, z = markov_weights(q, one)
    return _gram(full_basis(n), n, h, z, one)


# ── exact ℚ ───────────────────────────────────────────────────


def _as_fraction(q) -> Fraction:
    if isinstance(q, Fraction):
        return q
    if isinstance(q, int):
        return Fraction(q)
    if isinstance(q, str):
        return Fraction(q)
    raise TypeError(
        "tl_gram_exact needs a RATIONAL q (Fraction / int / str). A float q "
        "would make the whole 'exact' claim false at digit 17; use "
        "tl_gram_mp() for the true substrate q₀, which is not rational."
    )


def tl_gram_exact(n: int, q=Fraction(111, 100)):
    """`tl_gram` in exact ℚ at a rational `q` — no floating point anywhere.

    The default `q = 111/100` matches `pyhecke.gram`'s exact-rational block.
    Exactness is what makes "singular" distinguishable from "very small": on
    the full basis this path gives `det = 0` on the nose, where float64 can
    only report `3.998e-17` and mpmath a smaller epsilon.
    """
    return tl_gram(n, _as_fraction(q), Fraction(1))


def full_hecke_gram_exact(n: int, q=Fraction(111, 100)):
    """`full_hecke_gram` in exact ℚ — `det` is exactly `0`."""
    return full_hecke_gram(n, _as_fraction(q), Fraction(1))


def _inverse_exact(rows):
    """Gauss–Jordan over an exact field. Raises if the matrix is singular.

    Unlike `np.linalg.inv` this *does* raise — the whole reason `gram.py` had
    to add `safe_inverse` is that numpy silently returns inverted rounding
    noise on the degenerate form.  Here a zero pivot is exactly zero.
    """
    m = len(rows)
    a = [list(r) + [1 if i == j else 0 for j in range(m)] for i, r in enumerate(rows)]
    zero = rows[0][0] * 0
    for col in range(m):
        piv = next((r for r in range(col, m) if a[r][col] != zero), None)
        if piv is None:
            raise ZeroDivisionError(
                f"the form is singular at column {col} of {m} — this is the "
                "convention-D degeneracy; use tl_gram_exact (the quotient), "
                "not full_hecke_gram_exact"
            )
        a[col], a[piv] = a[piv], a[col]
        pv = a[col][col]
        a[col] = [x / pv for x in a[col]]
        for r in range(m):
            if r != col and a[r][col] != zero:
                f = a[r][col]
                a[r] = [x - f * y for x, y in zip(a[r], a[col])]
    return [row[m:] for row in a]


def _rank_exact(rows) -> int:
    """Rank by Gaussian elimination over an exact field.

    Written out rather than delegated to `sympy.Matrix.rank()` because that
    call is the only slow step in the whole audit — 1.5 s to *build* the
    120×120 `n = 5` form, then minutes to rank it.  Over `Fraction` a pivot is
    zero or it is not, so the elimination needs no tolerance and admits no
    rank-decision heuristic; that exactness is the entire point of measuring
    the corank here rather than numerically.
    """
    a = [list(r) for r in rows]
    m = len(a)
    ncols = len(a[0]) if m else 0
    zero = a[0][0] * 0 if m else 0
    rank = 0
    for col in range(ncols):
        piv = next((r for r in range(rank, m) if a[r][col] != zero), None)
        if piv is None:
            continue
        a[rank], a[piv] = a[piv], a[rank]
        pv = a[rank][col]
        a[rank] = [x / pv for x in a[rank]]
        for r in range(m):
            if r != rank and a[r][col] != zero:
                f = a[r][col]
                a[r] = [x - f * y for x, y in zip(a[r], a[rank])]
        rank += 1
        if rank == m:
            break
    return rank


def gram_rank_exact(n: int, q=Fraction(111, 100)) -> int:
    """Exact rank of the *full* `H_n(q)` Markov–Gram form at a rational `q`.

    Equals `Catalan(n)`; the corank `n! − Catalan(n)` is the dimension of the
    radical.  Because this is exact in ℚ, a rank measured here is a lower
    bound on the generic rank over ℚ(q) — rank can only drop at special
    points, never rise.
    """
    return _rank_exact(full_hecke_gram_exact(n, q))


def tl_gram_inverse_exact(n: int, q=Fraction(111, 100)):
    """The **inverse** — not a pseudoinverse — of the quotient form, in ℚ.

    `G · G⁻¹ = I` holds entry-by-entry with exact `1`s and `0`s.  Contrast
    `pyhecke.gram.G_PINV`, where the corresponding residual on the singular
    6×6 form is `‖G · G_INV − I‖ = 1.64` (measured, `qou-cds2`).
    """
    return _inverse_exact(tl_gram_exact(n, q))


# ── mpmath at the substrate q₀ ────────────────────────────────

_MP_DPS = 60  # 50-dps target + 10 guard digits (compute-author §1)


def _q0_50dps_str() -> str:
    """The proton-pinned 50-digit substrate `q₀` as a decimal string.

    Same source and same fallback chain as `pyhecke.gram._q0_50dps_str`; the
    proton pin is the standing default for all new compute (owner directive
    2026-08-07).  Never `float(q0)` — that is the documented entry point into
    double precision with no signal.
    """
    try:
        from q_parameter import Q_50_DIGIT_STR  # type: ignore[import-not-found]
        return Q_50_DIGIT_STR
    except ImportError:
        from qou_substrate import Q_50_DIGIT_STR  # type: ignore[import-not-found]
        return Q_50_DIGIT_STR


def tl_gram_mp(n: int, dps: int = _MP_DPS, q=None):
    """`tl_gram` in `mpmath.mpf` at the true substrate `q₀` (no float64).

    `q` defaults to the 50-digit proton-pinned `q₀`, parsed from its decimal
    string inside `workdps` so no value ever passes through a float.
    """
    import mpmath as mp
    with mp.workdps(dps):
        qq = mp.mpf(_q0_50dps_str()) if q is None else mp.mpf(q)
        return [[+x for x in row] for row in tl_gram(n, qq, mp.mpf(1))]


def tl_gram_inverse_mp(n: int, dps: int = _MP_DPS, q=None):
    """Inverse of the quotient form at `q₀`, at `dps` digits."""
    import mpmath as mp
    with mp.workdps(dps):
        G = mp.matrix(tl_gram_mp(n, dps, q))
        return mp.inverse(G)


def tl_gram_solve_mp(rhs, n: int, dps: int = _MP_DPS, q=None):
    """Solve `G_TL x = rhs` on the quotient at `q₀`.

    A genuine solve: the quotient form is non-singular, so there is no
    least-squares fallback and no `rcond` to tune.
    """
    import mpmath as mp
    with mp.workdps(dps):
        G = mp.matrix(tl_gram_mp(n, dps, q))
        return mp.lu_solve(G, mp.matrix(list(rhs)))
