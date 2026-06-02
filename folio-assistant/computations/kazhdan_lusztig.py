#!/usr/bin/env python3
"""Kazhdan–Lusztig polynomials and the canonical basis of ``H_n(q)``.

Phase 1.5 of the S-poly → crystal-basis migration: provides the
change-of-basis between the standard ``T_w`` basis and the canonical
``C_w`` basis of the Iwahori–Hecke algebra ``H_n(q)``.

For ``n ≤ 4`` the symmetric group ``S_n`` has Coxeter rank ≤ 3.  At
rank ≤ 3, the Kazhdan–Lusztig polynomials satisfy

    P_{x, w}(q) = 1   for every  x ≤ w  in Bruhat order

(Brenti, *Combinatorics of Coxeter groups* §5.1; the first
non-trivial KL polynomial appears at rank 4 / ``S_5``).

Consequently the canonical basis element ``C_w`` (Lusztig's ``q^½``
normalisation) collapses to a closed form

    C_w  =  q^{-ℓ(w)/2}  ∑_{x ≤ w}  q^{ℓ(x)}  T_x         (rank ≤ 3)

This module provides

* ``permutations_S_n(n)`` — enumerate ``S_n`` as one-line tuples.
* ``length(perm)`` — Coxeter length ``ℓ(w)`` (number of inversions).
* ``bruhat_le(x, w)`` — Bruhat order ``x ≤ w`` via the
  **tableau (rank) criterion** (Bjorner–Brenti §2.6): for every
  prefix length ``k``, the sorted first-``k`` entries of ``x``
  are component-wise ≤ those of ``w``.  ``O(n²)``.
* ``kl_polynomial(x, w)`` — KL polynomial ``P_{x, w}(q)`` returned
  as a sympy ``Integer``; for n ≤ 4 it is ``Integer(1)`` whenever
  ``x ≤ w`` and ``Integer(0)`` otherwise.  For n ≥ 5 raises with a
  pointer to the deferred KL recursion work.
* ``canonical_basis_C_w(perm, n)`` — return ``C_w`` as a sympy
  ``SymbolicHeckeElement`` in the ``T_x`` basis for ``x ∈ S_n``.
* ``T_basis_to_C_basis(elem, n)`` / ``C_basis_to_T_basis(elem, n)`` —
  full change-of-basis (n ≤ 4 only).

Run ``python3 kazhdan_lusztig.py`` to validate ``n ∈ {2, 3, 4}``:

  - Bruhat order matches the standard interval count
    (``|[e, w_0]| = n!`` for the longest element).
  - Round-trip ``T → C → T`` is the identity.
  - At ``w = w_0`` the canonical basis element is bar-invariant
    (``q ↔ q^{-1}`` preserves it).

References
----------
- Kazhdan, Lusztig, "Representations of Coxeter groups and Hecke
  algebras", Inventiones Math. 53 (1979), 165–184.
- Brenti, *Combinatorics of Coxeter groups*, GTM 231 (2005), §5.1.
- Lusztig, "Hecke algebras with unequal parameters", CRM Monograph
  Series 18 (2003) — for the canonical-basis normalisation used here.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from itertools import permutations
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from hecke_symbolic import SymbolicHeckeElement, q  # noqa: E402


# ── Symmetric group basics ─────────────────────────────────────────


def permutations_S_n(n: int) -> list[tuple[int, ...]]:
    """All ``n!`` permutations of ``S_n`` as one-line tuples
    ``(σ(1), σ(2), …, σ(n))`` (1-indexed values)."""
    return [tuple(p) for p in permutations(range(1, n + 1))]


def length(perm: tuple[int, ...]) -> int:
    """Coxeter length ``ℓ(w)`` = number of inversions of ``w``."""
    n = len(perm)
    return sum(
        1 for i in range(n) for j in range(i + 1, n) if perm[i] > perm[j]
    )


def reduced_word(perm: tuple[int, ...]) -> tuple[int, ...]:
    """A reduced expression for ``perm`` via insertion sort —
    bubble-sort the one-line form left-to-right and record the
    simple reflections used.

    Returns a tuple of 0-indexed simple-reflection indices
    (``s_i`` swaps positions ``i`` and ``i+1`` in the *one-line*
    representation; equivalently swaps the values at adjacent
    positions).  Length equals ``length(perm)`` by construction.
    """
    arr = list(perm)
    out: list[int] = []
    n = len(arr)
    # Bubble-sort: pass left-to-right; on each adjacent inversion
    # swap and record the index.  Repeat until sorted.
    sorted_flag = False
    while not sorted_flag:
        sorted_flag = True
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                out.append(i)
                sorted_flag = False
    return tuple(out)


def apply_simple_reflection(perm: tuple[int, ...], i: int) -> tuple[int, ...]:
    """Right-multiplication by ``s_i``: swap positions ``i`` and
    ``i+1`` in the one-line word."""
    arr = list(perm)
    arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return tuple(arr)


# ── Bruhat order ───────────────────────────────────────────────────


def bruhat_le(x: tuple[int, ...], w: tuple[int, ...]) -> bool:
    """Test ``x ≤ w`` in Bruhat order.

    Uses the **tableau criterion** (Bjorner–Brenti §2.6):
    ``x ≤ w`` iff for every ``k = 1, …, n−1`` the sorted list of
    the first ``k`` entries of ``x`` is component-wise ≤ the sorted
    list of the first ``k`` entries of ``w``.

    O(n²) — fast enough for n ≤ 6.
    """
    if len(x) != len(w):
        raise ValueError(f"length mismatch: |x|={len(x)} vs |w|={len(w)}")
    n = len(x)
    for k in range(1, n):
        xk = sorted(x[:k])
        wk = sorted(w[:k])
        for j in range(k):
            if xk[j] > wk[j]:
                return False
    return True


# ── Kazhdan–Lusztig polynomials ────────────────────────────────────


def kl_polynomial(x: tuple[int, ...], w: tuple[int, ...]) -> sp.Expr:
    """Kazhdan–Lusztig polynomial ``P_{x, w}(q)``.

    The closed-form ``P_{x, w} = 1 for all x ≤ w`` holds only at
    **Coxeter rank ≤ 2** (dihedral groups, i.e. ``S_n`` for n ≤ 3).
    The famous "3412" example shows ``P_{e, (3,4,1,2)}(q) = 1 + q``
    is already non-trivial at S_4 (rank 3); see e.g. Bjorner-Brenti
    §5.1 (the lattice of non-trivial KL polynomials in low rank).

    Implementation:

    - ``n ≤ 3``: closed-form (``P = 1`` whenever ``x ≤ w``).
    - ``n ≥ 4``: route to the K-L 1979 §1.1 recursion via
      :func:`kl_polynomial_recursive`.
    - Cap raised to ``n ≤ 6`` (covers the deuteron H_6 PROBE 4
      need); ``n ≥ 7`` raises ``NotImplementedError`` until the
      recursion is optimised (sympy at S_7 takes hours).

    Historical note: prior to this branch, the closed form was
    incorrectly applied at n=4, returning ``1`` for 6 Bruhat pairs
    that should have been ``1 + q``. Fixed by routing through the
    recursion.
    """
    if len(x) != len(w):
        raise ValueError(f"length mismatch: |x|={len(x)} vs |w|={len(w)}")
    n = len(x)
    if n > 6:
        raise NotImplementedError(
            f"kl_polynomial(x, w): n={n} exceeds the current "
            f"recursion cap (n ≤ 6).  The pure-Python sympy "
            f"recursion at n ≥ 7 is slow (hours for S_7, days for "
            f"S_8); deferred to a follow-up (C/Rust port or external "
            f"Sage/Magma backend).  Tracking: "
            f"`docs/audits/2026-06-02-kl-recursion-s6-scaffold-design.md`."
        )
    if not bruhat_le(x, w):
        return sp.Integer(0)
    if n <= 3:
        # Coxeter rank ≤ 2 closed form: every Bruhat-comparable
        # pair has P_{x, w} = 1 (Brenti §5.1 for dihedral groups).
        return sp.Integer(1)
    # n ∈ {4, 5, 6}: route to the full K-L recursion.
    return kl_polynomial_recursive(x, w)


# ── Memoized Kazhdan–Lusztig recursion (K-L 1979 §1.1) ────────────
#
# For n ≥ 4 the closed form fails (first non-trivial P_{e, (3,4,1,2)}
# = 1 + q is already in S_4 — the famous "3412" example, NOT S_5 as
# previously mis-stated here per Brenti §5.1 mis-reading; see
# `kl_polynomial` docstring + commit message for details).
#
# The standard recursion (K-L 1979 §1.1, Brenti §5.2): pick a right
# descent s of w (i.e. ws < w), then per Bjorner-Brenti Theorem
# 5.1.4:
#
#   c(x, w; s) := q · P_{xs, ws} + P_{x, ws}        if xs > x (c=0)
#               := P_{xs, ws} + q · P_{x, ws}        if xs < x (c=1)
#
#   P_{x, w} = c(x, w; s) − Σ_{x ≤ z < ws, zs < z}
#                              μ(z, ws) · q^{(ℓ(w) − ℓ(z))/2} · P_{x, z}
#
# where μ(z, w') is the coefficient of q^{(ℓ(w') − ℓ(z) − 1)/2} in
# P_{z, w'}(q) — zero unless ℓ(w') − ℓ(z) is odd.
#
# Base cases: P_{w, w} = 1; P_{x, w} = 0 when x ̸≤ w.

_kl_cache: dict[
    tuple[tuple[int, ...], tuple[int, ...]],
    sp.Expr,
] = {}


# Cache permutations_S_n results — the inner correction loop hits
# permutations_S_n(n) on every recursive call; without caching this
# allocates a fresh n!-element list each time (e.g. 720 elements per
# call at S_6, ~70 MB of allocations across 97k cache entries).  Per
# Copilot review on PR #1714 line 289.
_perms_cache: dict[int, list[tuple[int, ...]]] = {}


def _perms_n(n: int) -> list[tuple[int, ...]]:
    """Cached `permutations_S_n(n)` for hot-loop use inside the
    KL recursion's correction sum."""
    cached = _perms_cache.get(n)
    if cached is not None:
        return cached
    result = permutations_S_n(n)
    _perms_cache[n] = result
    return result


def _right_descent(w: tuple[int, ...]) -> int | None:
    """Return the smallest 0-indexed simple-reflection index ``i``
    such that ``s_i`` is a right descent of ``w`` (equivalently,
    ``w[i] > w[i+1]``).  Returns ``None`` if ``w`` is the identity
    (no descents)."""
    for i in range(len(w) - 1):
        if w[i] > w[i + 1]:
            return i
    return None


def _mu(z: tuple[int, ...], w: tuple[int, ...]) -> sp.Expr:
    """Kazhdan–Lusztig μ-coefficient: the coefficient of
    ``q^{(ℓ(w) − ℓ(z) − 1)/2}`` in ``P_{z, w}(q)``.  Zero unless
    ``ℓ(w) − ℓ(z)`` is odd.

    Implementation note: extracts the coefficient via
    ``as_coefficients_dict()`` (O(#terms) dict lookup) rather than
    ``sp.Poly(...).coeff_monomial(...)`` (which constructs a full
    polynomial representation).  Per Gemini review on PR #1714, the
    dict form is ~10× faster on this hot path.
    """
    diff = length(w) - length(z)
    if diff < 1 or diff % 2 == 0:
        return sp.S.Zero
    target_power = (diff - 1) // 2
    P_zw = kl_polynomial_recursive(z, w)
    if P_zw == 0:
        return sp.S.Zero
    coeff_dict = P_zw.as_coefficients_dict()
    key = q ** target_power if target_power > 0 else sp.S.One
    return coeff_dict.get(key, sp.S.Zero)


def kl_polynomial_recursive(
    x: tuple[int, ...],
    w: tuple[int, ...],
) -> sp.Expr:
    """Memoized Kazhdan–Lusztig polynomial ``P_{x, w}(q)`` via the
    standard recursion (K-L 1979 §1.1, Brenti §5.2).

    Works for any ``n ≥ 1``.  Memoizes in ``_kl_cache`` keyed by
    ``(x, w)``; cache persists across calls within a process.
    """
    if len(x) != len(w):
        raise ValueError(f"length mismatch: |x|={len(x)} vs |w|={len(w)}")

    # Base case: x = w.
    if x == w:
        return sp.Integer(1)
    # Base case: x ̸≤ w → 0.
    if not bruhat_le(x, w):
        return sp.Integer(0)

    key = (x, w)
    cached = _kl_cache.get(key)
    if cached is not None:
        return cached

    # Choose a right descent s of w (exists because w ≠ identity).
    s = _right_descent(w)
    assert s is not None, "internal: w should be non-identity here"

    ws = apply_simple_reflection(w, s)
    xs = apply_simple_reflection(x, s)
    # xs < x ⇔ s is a right descent of x ⇔ x[s] > x[s+1].
    x_has_s_descent = (x[s] > x[s + 1])

    # c(x, w; s) per Bjorner-Brenti Theorem 5.1.4:
    #   c = 0 if xs > x (s is right ASCENT of x): main = q·P_{xs,ws} + P_{x,ws}
    #   c = 1 if xs < x (s is right DESCENT of x): main = P_{xs,ws} + q·P_{x,ws}
    # Both branches keep BOTH terms (the missing-term version gives the
    # wrong base case: P_{e, s} should be 1, not q).
    if x_has_s_descent:
        c = kl_polynomial_recursive(xs, ws) \
            + q * kl_polynomial_recursive(x, ws)
    else:
        c = q * kl_polynomial_recursive(xs, ws) \
            + kl_polynomial_recursive(x, ws)

    # Correction: Σ_{x ≤ z < ws, zs < z} μ(z, ws) · q^{(ℓ(w) − ℓ(z))/2}
    #              · P_{x, z}.
    # Per Gemini review on PR #1714, the inner-loop filters are
    # ordered cheap-to-expensive: descent check (O(1) tuple compare)
    # first, then parity (cheap arithmetic), then the two O(n²)
    # Bruhat checks, then the recursive _mu call.  Since _mu is
    # non-zero only when (ℓ(ws) − ℓ(z)) is odd, equivalently
    # (lw − lz) is even, the parity gate skips ~50 % of candidates
    # before any expensive check.
    lw = length(w)
    correction = sp.S.Zero
    n = len(w)
    for z in _perms_n(n):
        # zs < z ⇔ s is a right descent of z (cheap; ~50% filter).
        if not (z[s] > z[s + 1]):
            continue
        if z == ws:
            continue
        lz = length(z)
        # Parity gate: _mu is zero unless (lw − lz) is even.
        if (lw - lz) % 2 != 0:
            continue
        if not bruhat_le(z, ws):
            continue
        if not bruhat_le(x, z):
            continue
        mu = _mu(z, ws)
        if mu.equals(0):
            continue
        # (lw − lz) is even here, so integer division is exact and
        # cheaper than sp.Rational.
        correction += mu * q ** ((lw - lz) // 2) \
            * kl_polynomial_recursive(x, z)

    result = sp.expand(c - correction)
    _kl_cache[key] = result
    return result


def _kl_cache_size() -> int:
    """Number of memoized ``P_{x, w}`` entries; used by tests."""
    return len(_kl_cache)


def _kl_cache_clear() -> None:
    """Reset the memoization cache (used by tests / re-runs)."""
    _kl_cache.clear()


# ── Canonical-basis element C_w ────────────────────────────────────


def canonical_basis_C_w(w: tuple[int, ...]) -> SymbolicHeckeElement:
    """Lusztig's canonical-basis element ``C_w`` of ``H_n(q)`` for
    the permutation ``w ∈ S_n``, expressed in the standard ``T_x``
    basis.

    Convention (Lusztig "Hecke algebras with unequal parameters",
    §5):

        C_w  =  q^{-ℓ(w)/2}  ∑_{x ≤ w}  P_{x, w}(q)·q^{ℓ(x)}  T_x

    At ``n ≤ 3`` (Coxeter rank ≤ 2 = dihedral), every ``P_{x, w} = 1``
    so this collapses to the closed form

        C_w  =  q^{-ℓ(w)/2}  ∑_{x ≤ w}  q^{ℓ(x)}  T_x.

    At ``n ≥ 4`` the KL polynomials are non-trivial (P_{e, 3412} = 1+q
    is the famous minimal example in S_4); the per-``x`` coefficient
    is computed via :func:`kl_polynomial`.

    The ``T_x`` words are produced via ``reduced_word(x)``; any
    reduced expression yields the same ``T_x`` because the braid
    relations are quotiented in ``H_n``.
    """
    n = len(w)
    if n > 6:
        raise NotImplementedError(
            f"canonical_basis_C_w: n={n} exceeds the current KL-"
            f"recursion cap (n ≤ 6).  See kl_polynomial() for the "
            f"S_7+ deferral rationale."
        )
    lw = length(w)
    q_neg_half_lw = q ** sp.Rational(-lw, 2)
    terms: dict[tuple[int, ...], sp.Expr] = {}
    for x in permutations_S_n(n):
        if not bruhat_le(x, w):
            continue
        lx = length(x)
        P_xw = kl_polynomial(x, w)
        coeff = sp.expand(q_neg_half_lw * P_xw * q ** lx)
        word = reduced_word(x)
        terms[word] = sp.expand(terms.get(word, sp.S.Zero) + coeff)
    return SymbolicHeckeElement(terms)


# ── T-basis ↔ C-basis change-of-basis ──────────────────────────────


def _T_basis_index(n: int) -> dict[tuple[int, ...], tuple[int, ...]]:
    """Map ``perm → reduced_word(perm)`` for every ``perm ∈ S_n``.
    Used as the canonical word for each Bruhat element (the words
    produced by ``reduced_word`` are unique per permutation
    because bubble sort is deterministic)."""
    return {p: reduced_word(p) for p in permutations_S_n(n)}


def C_basis_to_T_basis(
    coeffs: dict[tuple[int, ...], sp.Expr],
    n: int,
) -> SymbolicHeckeElement:
    """Convert an element written in the C-basis ``{C_w : w ∈ S_n}``
    to the T-basis.  ``coeffs`` is ``{perm: coefficient_in_q}``.
    """
    if n > 6:
        raise NotImplementedError(
            f"C_basis_to_T_basis: n={n} exceeds the current KL-"
            f"recursion cap (n ≤ 6)."
        )
    out = SymbolicHeckeElement.zero()
    for w_perm, c in coeffs.items():
        Cw = canonical_basis_C_w(w_perm)
        out = out + Cw.scale(c)
    return out


def T_basis_to_C_basis(
    elem: SymbolicHeckeElement,
    n: int,
) -> dict[tuple[int, ...], sp.Expr]:
    """Convert a T-basis element back to the C-basis as
    ``{perm: coefficient_in_q}``.

    Because the C-basis is upper-triangular in Bruhat order with
    diagonal coefficient ``q^{ℓ(w)/2}`` (which holds for any KL
    polynomial values since ``P_{w, w} = 1`` always), we can solve
    by back-substitution top-down (longest perms first).  The
    non-trivial KL polynomials at n ≥ 4 affect off-diagonal entries
    only; the diagonal stays ``q^{ℓ(w)/2}`` and the back-substitution
    remains well-defined.
    """
    if n > 6:
        raise NotImplementedError(
            f"T_basis_to_C_basis: n={n} exceeds the current KL-"
            f"recursion cap (n ≤ 6)."
        )
    word_of: dict[tuple[int, ...], tuple[int, ...]] = _T_basis_index(n)
    perm_of_word: dict[tuple[int, ...], tuple[int, ...]] = {
        word: perm for perm, word in word_of.items()
    }

    # Working copy of the T-basis coefficients keyed by permutation.
    T_coeffs: dict[tuple[int, ...], sp.Expr] = {}
    for word, c in elem.terms.items():
        if word not in perm_of_word:
            raise ValueError(
                f"T_basis_to_C_basis: word {word} is not the canonical "
                f"reduced expression of any element of S_{n}; the input "
                f"must be in normal form (all braid relations resolved)."
            )
        T_coeffs[perm_of_word[word]] = sp.expand(
            T_coeffs.get(perm_of_word[word], sp.S.Zero) + sp.sympify(c)
        )

    # Solve for C-basis coefficients in decreasing Bruhat order
    # (longest first).  Each C_w contributes only to T_x for x ≤ w,
    # so processing w from longest to shortest peels off C_w's
    # contribution at T_w (where the diagonal is q^{-ℓ(w)/2}).
    perms_by_length = sorted(
        permutations_S_n(n), key=lambda p: -length(p)
    )
    C_coeffs: dict[tuple[int, ...], sp.Expr] = {}
    for w_perm in perms_by_length:
        T_w_coef = T_coeffs.get(w_perm, sp.S.Zero)
        if sp.simplify(T_w_coef) == 0:
            continue
        lw = length(w_perm)
        # Diagonal: T_w in C_w has coefficient q^{-ℓ(w)/2} · q^{ℓ(w)}
        #          = q^{ℓ(w)/2}.
        diag = q ** sp.Rational(lw, 2)
        c_w = sp.cancel(T_w_coef / diag)
        if sp.simplify(c_w) == 0:
            continue
        C_coeffs[w_perm] = c_w
        # Subtract c_w · C_w from the working T_coeffs.
        Cw = canonical_basis_C_w(w_perm)
        for word, coef in Cw.terms.items():
            x = perm_of_word[word]
            T_coeffs[x] = sp.expand(
                T_coeffs.get(x, sp.S.Zero) - c_w * coef
            )

    return C_coeffs


# ── Self-test / witness ────────────────────────────────────────────


def _self_test() -> dict:
    """Self-test sweep across n ∈ {2, 3, 4, 5} (full) + n = 6 spot
    (longest-50 round-trip + literature cross-checks).  The full S_6
    sweep takes ~3.5 min; the spot subset takes ~30s and is the right
    balance for CI."""
    from bar_involution import bar_polynomial

    cases: list[dict] = []

    # Full sweep up to n=5.
    for n in (2, 3, 4, 5):
        perms = permutations_S_n(n)
        identity = tuple(range(1, n + 1))
        w0 = tuple(reversed(identity))
        bruhat_below_w0 = sum(1 for p in perms if bruhat_le(p, w0))
        bruhat_ok = (bruhat_below_w0 == len(perms))

        roundtrip_ok = True
        for w_perm in perms:
            Cw = canonical_basis_C_w(w_perm)
            recovered = T_basis_to_C_basis(Cw, n)
            nz = {p: sp.simplify(c) for p, c in recovered.items()
                  if sp.simplify(c) != 0}
            if set(nz) != {w_perm} or sp.simplify(nz[w_perm] - 1) != 0:
                roundtrip_ok = False
                break

        # Coefficient-sum bar-invariance of C_{w_0} (necessary
        # condition for the full bar-invariance of C_{w_0}; see note
        # in the original self-test comment).
        Cw0 = canonical_basis_C_w(w0)
        sum_coef = sum(Cw0.terms.values(), start=sp.S.Zero)
        sum_bar = bar_polynomial(sum_coef)
        sum_bar_invariant = sp.simplify(sum_coef - sum_bar) == 0

        cases.append({
            "n": n,
            "factorial": len(perms),
            "bruhat_below_w0": bruhat_below_w0,
            "bruhat_count_ok": bruhat_ok,
            "roundtrip_T_C_T_ok": roundtrip_ok,
            "Cw0_coef_sum_bar_invariant": sum_bar_invariant,
            "ok": bruhat_ok and roundtrip_ok and sum_bar_invariant,
        })

    # n=6 spot test: Bruhat count + round-trip on the longest 50
    # elements (skip full 720-element sweep which takes ~3.5 min).
    n = 6
    perms6 = permutations_S_n(n)
    identity = tuple(range(1, n + 1))
    w0 = tuple(reversed(identity))
    bruhat_below_w0 = sum(1 for p in perms6 if bruhat_le(p, w0))
    bruhat_ok = (bruhat_below_w0 == len(perms6))

    # Round-trip on a representative subset: identity, the 14 simple
    # reflections + length-2 elements, and the 35 longest elements.
    # Total ~50 perms; covers low + high + a few mid representatives.
    test_perms6 = (
        [identity]
        + [p for p in perms6 if length(p) == 1]
        + [p for p in perms6 if length(p) == 2][:8]
        + sorted(perms6, key=lambda p: -length(p))[:35]
    )
    # De-dup while preserving order.
    seen: set[tuple[int, ...]] = set()
    test_perms6 = [p for p in test_perms6 if not (p in seen or seen.add(p))]

    roundtrip_ok = True
    for w_perm in test_perms6:
        Cw = canonical_basis_C_w(w_perm)
        recovered = T_basis_to_C_basis(Cw, n)
        nz = {p: sp.simplify(c) for p, c in recovered.items()
              if sp.simplify(c) != 0}
        if set(nz) != {w_perm} or sp.simplify(nz[w_perm] - 1) != 0:
            roundtrip_ok = False
            break

    Cw0 = canonical_basis_C_w(w0)
    sum_coef = sum(Cw0.terms.values(), start=sp.S.Zero)
    sum_bar = bar_polynomial(sum_coef)
    sum_bar_invariant = sp.simplify(sum_coef - sum_bar) == 0

    cases.append({
        "n": n,
        "factorial": len(perms6),
        "bruhat_below_w0": bruhat_below_w0,
        "bruhat_count_ok": bruhat_ok,
        "roundtrip_T_C_T_ok": roundtrip_ok,
        "roundtrip_subset_size": len(test_perms6),
        "Cw0_coef_sum_bar_invariant": sum_bar_invariant,
        "ok": bruhat_ok and roundtrip_ok and sum_bar_invariant,
    })

    # Literature cross-checks.
    lit_checks: list[dict] = []
    # The famous "3412" example — minimal non-trivial KL polynomial
    # in any symmetric group (Bjorner-Brenti §5.1).
    e_4 = (1, 2, 3, 4)
    w_3412 = (3, 4, 1, 2)
    P_3412 = kl_polynomial(e_4, w_3412)
    expected_3412 = 1 + q
    P_3412_ok = sp.simplify(P_3412 - expected_3412) == 0
    lit_checks.append({
        "name": "P_e_3412_equals_1_plus_q",
        "computed": str(P_3412),
        "expected": "q + 1",
        "ok": P_3412_ok,
    })
    # A second S_5 reference: P_{e, 4231} = 1 + q (Bjorner-Brenti §5.1).
    e_5 = (1, 2, 3, 4, 5)
    w_4231 = (4, 2, 3, 1, 5)
    P_4231 = kl_polynomial(e_5, w_4231)
    P_4231_ok = sp.simplify(P_4231 - (1 + q)) == 0
    lit_checks.append({
        "name": "P_e_4231_equals_1_plus_q_in_S5",
        "computed": str(P_4231),
        "expected": "q + 1",
        "ok": P_4231_ok,
    })
    # Third reference: P_{e, w_0(S_n)} = 1 always (longest element
    # gives the trivial KL polynomial).  Check at S_6 — exercises
    # the deepest recursion depth in the self-test.
    e_6 = (1, 2, 3, 4, 5, 6)
    w0_6 = (6, 5, 4, 3, 2, 1)
    P_e_w0_6 = kl_polynomial(e_6, w0_6)
    P_e_w0_6_ok = sp.simplify(P_e_w0_6 - 1) == 0
    lit_checks.append({
        "name": "P_e_w0_equals_1_in_S6",
        "computed": str(P_e_w0_6),
        "expected": "1",
        "ok": P_e_w0_6_ok,
    })
    # Fourth reference: KL-multiplicativity for direct products.
    # P_{e, (3,4,1,2,6,5)} = P_{e, 3412} · P_{e, s_5} = (1+q) · 1
    # = 1 + q.  Confirms the recursion respects the parabolic
    # direct-product structure of S_4 × S_2 ⊂ S_6.
    w_prod = (3, 4, 1, 2, 6, 5)
    P_prod = kl_polynomial(e_6, w_prod)
    P_prod_ok = sp.simplify(P_prod - (1 + q)) == 0
    lit_checks.append({
        "name": "P_e_3412xS2_equals_1_plus_q_in_S6",
        "computed": str(P_prod),
        "expected": "q + 1",
        "ok": P_prod_ok,
    })

    lit_ok = all(c["ok"] for c in lit_checks)

    # Cache-size sanity (per Copilot review on PR #1714 line 678 +
    # design doc acceptance criteria): S_6 fully-sweep cache should
    # stay well under 300k entries.  This catches accidental cache
    # blow-ups (e.g. if a future change keys on something coarser
    # than the (x, w) tuple).  Note: the self-test only ran a 49-
    # element subset of S_6, so the cache here is well below the
    # full-S_6 baseline of ~97k entries.
    kl_cache_size = _kl_cache_size()
    cache_ok = (kl_cache_size <= 300_000)

    return {
        "cases": cases,
        "literature_checks": lit_checks,
        "literature_all_ok": lit_ok,
        "kl_cache_size": kl_cache_size,
        "kl_cache_size_sanity_ok": cache_ok,
        "all_passed": (
            all(c["ok"] for c in cases) and lit_ok and cache_ok
        ),
    }


if __name__ == "__main__":
    # Instantiate the WitnessBuilder *before* the expensive work so
    # its duration measurement covers _self_test() itself, not just
    # the post-test assertion plumbing.
    from witness_base import WitnessBuilder

    w_builder = (WitnessBuilder("kazhdan-lusztig-canonical-basis",
                                 engine="sympy")
                 .set_description(
                    "Kazhdan–Lusztig polynomials and the canonical "
                    "basis C_w of H_n(q) for n ≤ 6.  Closed form at "
                    "n ≤ 3 (dihedral / Brenti §5.1); full K-L 1979 "
                    "§1.1 recursion at n ∈ {4, 5, 6}.  Validates "
                    "Bruhat-order cardinality, T→C→T round-trip, "
                    "bar-invariance of C_{w_0} coefficient sum, and "
                    "two literature cross-checks (P_{e, 3412} = 1+q "
                    "and P_{e, 4231 in S_5} = 1+q)."
                 ))

    print("=" * 72)
    print("KAZHDAN–LUSZTIG / CANONICAL BASIS — self-test (n ≤ 6)")
    print("=" * 72)

    summary = _self_test()

    for c in summary["cases"]:
        flag = "✓" if c["ok"] else "✗"
        extra = (f" ({c.get('roundtrip_subset_size')} subset)"
                 if "roundtrip_subset_size" in c else "")
        print(
            f"  {flag}  n={c['n']}: |S_n|={c['factorial']}, "
            f"|[e,w_0]|={c['bruhat_below_w0']} ({'OK' if c['bruhat_count_ok'] else 'FAIL'}); "
            f"T→C→T roundtrip {'OK' if c['roundtrip_T_C_T_ok'] else 'FAIL'}{extra}; "
            f"C_{{w_0}} bar-invariant coef sum "
            f"{'OK' if c['Cw0_coef_sum_bar_invariant'] else 'FAIL'}"
        )

    print()
    print("  Literature cross-checks:")
    for lc in summary["literature_checks"]:
        flag = "✓" if lc["ok"] else "✗"
        print(f"    {flag}  {lc['name']}: got {lc['computed']}, "
              f"expected {lc['expected']}")

    if not summary["all_passed"]:
        sys.exit(1)
    print("\n  ✓ All KL / canonical-basis tests passed (n ≤ 6).")

    for c in summary["cases"]:
        w_builder.add_assertion(
            name=f"bruhat_count_n={c['n']}",
            computed=c["bruhat_below_w0"],
            expected=c["factorial"],
            tolerance=0,
            source="Bjorner-Brenti, Combinatorics of Coxeter Groups §2.6",
        )
        w_builder.add_assertion(
            name=f"roundtrip_T_to_C_to_T_n={c['n']}",
            computed="1" if c["roundtrip_T_C_T_ok"] else "0",
            expected="1",
            source=(
                f"canonical-basis change-of-basis is invertible"
                f"{' (longest-50 subset)' if 'roundtrip_subset_size' in c else ''}"
            ),
        )
        w_builder.add_assertion(
            name=f"bar_invariant_coef_sum_w0_n={c['n']}",
            computed="1" if c["Cw0_coef_sum_bar_invariant"] else "0",
            expected="1",
            source="Lusztig, Hecke algebras with unequal parameters §5",
        )
    for lc in summary["literature_checks"]:
        w_builder.add_assertion(
            name=f"literature_{lc['name']}",
            computed=lc["computed"],
            expected=lc["expected"],
            source="Bjorner-Brenti, Combinatorics of Coxeter Groups §5.1",
        )
    # Cache-size sanity assertion (per Copilot review on PR #1714).
    # Boolean form so the inequality semantics work with the
    # equality-based `Assertion.passed`.
    w_builder.add_data("kl_cache_size", summary["kl_cache_size"])
    w_builder.add_assertion(
        name="kl_cache_size_below_300k_sanity",
        computed="1" if summary["kl_cache_size_sanity_ok"] else "0",
        expected="1",
        source=(
            f"design-doc acceptance criterion: S_6 KL cache ≤ 300k. "
            f"Self-test recorded {summary['kl_cache_size']} entries "
            f"(actual size in `data.kl_cache_size`)."
        ),
    )
    out_path = w_builder.save()
    print(f"  Witness written → {out_path.name}")
