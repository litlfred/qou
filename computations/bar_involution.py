#!/usr/bin/env python3
"""
Bar involution and crystal-graph kernel for the Iwahori–Hecke algebra.

Mathematical objects
--------------------
The bar involution is the $\\mathbb{Z}/2\\mathbb{Z}$ ring automorphism

    bar :  H_n(q) -> H_n(q),    q ↦ q^{-1},    T_w ↦ T_{w^{-1}}^{-1}

(Lusztig's convention; see Kazhdan–Lusztig 1979).  Its fixed points are
the Kazhdan–Lusztig basis ``C_w``.  In QOU language the bar-invariant
elements of ``H_n(q)`` correspond to *charge-conjugation symmetric*
multi-particle states:  applying bar swaps over- and under-crossings,
i.e. an electron worldline with a positron worldline.

This module provides the smallest functional kernel needed by other
compute scripts:

* ``bar_polynomial`` — apply ``q ↦ q^{-1}`` to a sympy polynomial in q
  (Laurent or ordinary).
* ``bar_T_word`` — given ``w = (i_1, …, i_L)``, return ``w^{-1}``
  (reversal) and the Lusztig sign factor ``(-q)^{-L}``.
* ``is_bar_invariant`` / ``bar_symmetric_part`` — symmetric / anti-
  symmetric projections of an H_n(q) element written as a coefficient
  dictionary ``{word: poly_in_q}``.
* ``s1_phase`` and ``unitary_q`` — substitute ``q = e^{iθ}`` to wrap
  the deformation parameter onto the unit circle (the
  $S^1$ + $i$ "physical boundary" dial).
* ``root_of_unity_truncate`` — truncate a polynomial in q at a
  primitive ``k``-th root of unity, the modular-tensor-category
  truncation that enforces finite particle generations.
* ``crystal_paths`` — minimal BFS over the Kashiwara crystal of a
  partition (skeleton; see CLAUDE.md §7b for the symmetric-crystal /
  Type-B-folding shortcut).

The module is self-contained and pure-Python except for sympy.
"""
from __future__ import annotations

import math
from typing import Iterable

import sympy as sp

# ── 1.  Bar on polynomials in q  ─────────────────────────────

q = sp.symbols("q")


def bar_polynomial(P) -> sp.Expr:
    """Apply the bar involution ``q ↦ q^{-1}`` to a sympy expression
    in the symbol ``q`` (defined module-locally).  Laurent monomials
    are handled correctly via ``sp.together``.
    """
    P = sp.sympify(P)
    return sp.together(P.subs(q, 1 / q))


def is_bar_invariant_poly(P, *, tol: float = 1e-12) -> bool:
    """True iff ``bar(P) = P`` symbolically (or within numerical tol
    after substituting random q values)."""
    diff = sp.cancel(bar_polynomial(P) - sp.sympify(P))
    if diff.equals(0):
        return True
    # Numerical fallback for messy expressions
    for sample in (sp.Rational(7, 5), sp.Rational(3, 2), sp.Rational(11, 7)):
        try:
            v = float(diff.subs(q, sample))
            if abs(v) > tol:
                return False
        except (TypeError, ValueError):
            return False
    return True


# ── 2.  Bar on T_w basis elements (combinatorial)  ───────────

def bar_T_word(word: tuple[int, ...]) -> tuple[tuple[int, ...], sp.Expr]:
    """Return ``(w_inv, prefactor)`` such that ``bar(T_w) = prefactor *
    (T_{w_inv})^{-1}``.

    For the seminormal expansion this means:

        bar(T_w) ≈ (-q)^{-ℓ(w)} · T_{w^{-1}}    (mod higher KL terms)

    The exact relation involves Kazhdan–Lusztig polynomials; this
    helper returns the leading-order combinatorics needed by the
    ``is_bar_invariant`` projector below.  Callers that need the full
    KL expansion should use the symmetric-crystal shortcut
    (CLAUDE.md §7b, item 1) rather than expanding by hand.
    """
    w_inv = tuple(reversed(word))
    L = len(word)
    return w_inv, (-q) ** (-L)


def bar_coeff_dict(coeffs: dict[tuple[int, ...], sp.Expr]) -> dict[
        tuple[int, ...], sp.Expr]:
    """Apply bar to a Hecke element written as ``{word: coeff_in_q}``.

    Returns a new dict (does not mutate input).  Coefficients are
    bar-applied; words are inverted; the Lusztig prefactor is
    absorbed into the new coefficient.
    """
    out: dict[tuple[int, ...], sp.Expr] = {}
    for word, c in coeffs.items():
        w_inv, pref = bar_T_word(word)
        new_c = sp.expand(bar_polynomial(c) * pref)
        out[w_inv] = sp.expand(out.get(w_inv, sp.S.Zero) + new_c)
    # Drop zero entries to keep the basis sparse
    return {w: c for w, c in out.items() if not sp.sympify(c).equals(0)}


def is_bar_invariant(coeffs: dict[tuple[int, ...], sp.Expr],
                       *, tol: float = 1e-12) -> bool:
    """True iff applying ``bar_coeff_dict`` returns the same element."""
    barred = bar_coeff_dict(coeffs)
    keys = set(coeffs) | set(barred)
    for k in keys:
        a = sp.expand(coeffs.get(k, sp.S.Zero))
        b = sp.expand(barred.get(k, sp.S.Zero))
        if not is_bar_invariant_poly(a - b, tol=tol):
            return False
    return True


def bar_symmetric_part(coeffs: dict[tuple[int, ...], sp.Expr]) -> dict[
        tuple[int, ...], sp.Expr]:
    """Project onto the bar-symmetric ($\\mathbb{Z}/2\\mathbb{Z}$
    fixed-point) subspace:  ½ (P + bar(P))."""
    barred = bar_coeff_dict(coeffs)
    keys = set(coeffs) | set(barred)
    half = sp.Rational(1, 2)
    return {
        k: sp.expand(half * (coeffs.get(k, sp.S.Zero)
                              + barred.get(k, sp.S.Zero)))
        for k in keys
        if not (coeffs.get(k, sp.S.Zero)
                        + barred.get(k, sp.S.Zero)).equals(0)
    }


def bar_antisymmetric_part(coeffs: dict[tuple[int, ...], sp.Expr]) -> dict[
        tuple[int, ...], sp.Expr]:
    """Project onto the bar-antisymmetric subspace:  ½ (P − bar(P))."""
    barred = bar_coeff_dict(coeffs)
    keys = set(coeffs) | set(barred)
    half = sp.Rational(1, 2)
    return {
        k: sp.expand(half * (coeffs.get(k, sp.S.Zero)
                              - barred.get(k, sp.S.Zero)))
        for k in keys
        if not (coeffs.get(k, sp.S.Zero)
                        - barred.get(k, sp.S.Zero)).equals(0)
    }


# ── 3.  $S^1$ + $i$ — unitarity dial  ────────────────────────

def s1_phase(theta) -> sp.Expr:
    """Return ``q = exp(i θ)`` on the unit circle.  ``theta`` may be
    sympy or numeric."""
    return sp.exp(sp.I * sp.sympify(theta))


def unitary_q(P, theta) -> sp.Expr:
    """Substitute ``q = e^{iθ}`` into a polynomial / rational in q.

    Returns the value as a complex sympy expression; use
    ``complex(.)`` for a numeric result.
    """
    return sp.cancel(sp.sympify(P).subs(q, s1_phase(theta)))


def root_of_unity_truncate(P, k: int) -> sp.Expr:
    """Evaluate ``P`` at the primitive ``k``-th root of unity
    ``q = e^{2πi/k}`` — the Witten–Reshetikhin–Turaev modular-tensor
    truncation that shatters the infinite crystal graph into a finite
    spectrum (CLAUDE.md §7b, item 2 motivation).
    """
    if k <= 0:
        raise ValueError("k must be a positive integer")
    return sp.cancel(sp.sympify(P).subs(q, sp.exp(sp.I * 2 * sp.pi / k)))


# ── 4.  Crystal graph (skeleton)  ────────────────────────────
#
# This is intentionally a thin scaffold. Full Kashiwara $f_i, e_i$
# operators on tableaux belong in a dedicated module if downstream
# compute scripts ever need them; for now the BFS over partition
# children is enough to drive a "crystal-prefix" pruning loop in the
# GS engine. See CLAUDE.md §7b for symmetric-crystal shortcuts that
# avoid implementing Kashiwara operators by hand.

def _partition_children(lam: tuple[int, ...]) -> list[tuple[int, ...]]:
    """One-cell extensions of ``lam`` that remain a partition.
    Mirrors the addable-cell rule in the Young-graph crystal."""
    out: list[tuple[int, ...]] = []
    rows = list(lam)
    # Add to existing rows
    for i in range(len(rows)):
        if i == 0 or rows[i] < rows[i - 1]:
            new = list(rows)
            new[i] += 1
            out.append(tuple(new))
    # Add a new bottom row
    if not rows or rows[-1] >= 1:
        out.append(tuple(rows) + (1,))
    return out


def crystal_paths(start: tuple[int, ...], depth: int) -> list[
        tuple[tuple[int, ...], ...]]:
    """Enumerate every length-``depth`` path of one-cell additions
    starting at ``start``.

    Returns a list of paths; each path is a tuple of partitions
    ``(start, λ_1, λ_2, …, λ_{depth})``.  This is the BFS used by
    the GS engine to enumerate crystal-graph prefixes (cf.
    `def:cemetery-group`); apply the cemetery-group filter to prune.
    """
    if depth < 0:
        raise ValueError("depth must be ≥ 0")
    paths: list[tuple[tuple[int, ...], ...]] = [(tuple(start),)]
    for _ in range(depth):
        next_paths: list[tuple[tuple[int, ...], ...]] = []
        for p in paths:
            for child in _partition_children(p[-1]):
                next_paths.append(p + (child,))
        paths = next_paths
    return paths


def crystal_path_count(start: tuple[int, ...], depth: int) -> int:
    """Cardinality of ``crystal_paths(start, depth)`` without
    materializing the list — useful for the cemetery-group pruning
    statistics in the GS engine."""
    layer = {tuple(start): 1}
    for _ in range(depth):
        nxt: dict[tuple[int, ...], int] = {}
        for lam, mult in layer.items():
            for child in _partition_children(lam):
                nxt[child] = nxt.get(child, 0) + mult
        layer = nxt
    return sum(layer.values())


# ── 5.  CLI: self-test  ─────────────────────────────────────

if __name__ == "__main__":
    print("=" * 72)
    print("BAR INVOLUTION + CRYSTAL KERNEL — self-test")
    print("=" * 72)

    # 1. Bar on a polynomial: q + q^-1 is bar-invariant
    P = q + 1 / q
    print(f"\n  bar({P}) = {bar_polynomial(P)}    invariant? "
          f"{is_bar_invariant_poly(P)}")
    assert is_bar_invariant_poly(P)

    # 2. q is NOT bar-invariant
    assert not is_bar_invariant_poly(q)
    print(f"  bar(q)   = {bar_polynomial(q)}    invariant? "
          f"{is_bar_invariant_poly(q)}")

    # 3. Bar on a Hecke element
    elem: dict[tuple[int, ...], sp.Expr] = {
        (0,): q,
        (1, 0): sp.S.One,
    }
    print(f"\n  Element: {elem}")
    print(f"  bar:     {bar_coeff_dict(elem)}")

    # 4. Symmetric / antisymmetric projections sum back to original
    sym = bar_symmetric_part(elem)
    asym = bar_antisymmetric_part(elem)
    print(f"  sym:     {sym}")
    print(f"  asym:    {asym}")
    rebuilt = {}
    for k in set(sym) | set(asym):
        rebuilt[k] = sp.expand(sym.get(k, 0) + asym.get(k, 0))
    print(f"  sum:     {rebuilt}")
    for k in set(elem) | set(rebuilt):
        a = sp.expand(elem.get(k, 0))
        b = sp.expand(rebuilt.get(k, 0))
        assert sp.simplify(a - b) == 0, f"Reassembly fails at {k}"
    print("  ✓ sym + antisym = original (Z/2Z decomposition)")

    # 5. S^1 phase: |q| = 1 at q = exp(iθ)
    val = complex(unitary_q(q, sp.pi / 4))
    print(f"\n  q at θ=π/4:  {val}    |q|={abs(val):.6f}")
    assert abs(abs(val) - 1) < 1e-12, "S^1 phase not unitary"

    # 6. Root-of-unity truncation: q^k = 1 at k-th primitive root
    for k in (3, 4, 6):
        val = complex(root_of_unity_truncate(q ** k, k))
        print(f"  q^{k} at primitive {k}-th root: {val:+.6f}")
        assert abs(val - 1) < 1e-9, f"Root-of-unity check failed at k={k}"

    # 7. Crystal graph: Catalan-style growth from empty partition
    counts = [crystal_path_count((), d) for d in range(6)]
    print(f"\n  Crystal-path counts from () at depths 0..5: {counts}")
    # From empty: depth d = number of SYT of total size d = sum of
    # # SYT(λ) over partitions of d ; this is the involution number
    # 1, 1, 2, 4, 10, 26 (OEIS A000085).
    assert counts == [1, 1, 2, 4, 10, 26], \
        f"Crystal path counts disagree with A000085: {counts}"
    print("  ✓ Crystal-path counts match OEIS A000085 (involution numbers)")

    print("\n  ✓ All bar-involution / crystal-kernel self-tests passed.")
