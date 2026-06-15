#!/usr/bin/env python3


# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Canonical Jones-Markov trace for H_n(q) elements.

Implements the unique trace satisfying
  (M1) tr_M(ab) = tr_M(ba)         (cyclicity)
  (M2) tr_M(x · σ_{n-2}) = z · tr_M(x)   for x ∈ H_{n-1}
  (M3) tr_M(1) = 1
where z = 1/(q^{1/2} + q^{-1/2}) is the Markov parameter.

This is the CANONICAL trace referenced in prop:categorical-mass-markov
explicit-values table:
  tr_M(1)         = 1
  tr_M(σ_0)       = z
  tr_M(σ_0σ_1)    = z²
  tr_M(σ_0σ_1σ_0) = hz² + z      (where h = q − q⁻¹)
  tr_M((σ_0σ_1⁻¹)²) ≈ 0.182     (figure-8)

Differs from the Plancherel-weighted trace
  tr_Pl(x) = Σ_λ (d_q(λ)²/[n]_q!) χ_λ(x)/d_λ
used in hecke_core.atom_markov_trace and binding_3A — these do NOT
satisfy (M2) with the canonical z and give different values.

Strategy:
  1. Each H_n element is a linear combination of words over σ_0..σ_{n-2}.
  2. For each word, recursively reduce via:
     - if empty: tr = 1
     - if max_gen < n-2: recurse at H_{max_gen + 2}
     - if max_gen appears once: cyclic rotate to end → Markov II
     - if max_gen appears multiple times: commute via far-commutativity,
       apply Hecke σ² = hσ + 1, recurse.
  3. Braid-relation cases (σ_{top-1} between two σ_{top}) reduce via
     explicit σ_iσ_{i+1}σ_i = σ_{i+1}σ_iσ_{i+1}, then retry.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# Symbolic z, h — can be overridden numerically
import sympy as sp
from hecke_symbolic import q, HA as H_SYMB, z_markov as Z_SYMB


# Manual cache so we can pass depth THROUGH to _tr_M_word_impl
# (preserving the recursion-depth guard) while keeping depth OUT of
# the cache key (the result depends only on (word, n, z, h, max_depth)).
_TR_M_WORD_CACHE: dict = {}


def tr_M_word(word: tuple, n: int, z, h, *,
               depth: int = 0, max_depth: int = 200):
    """See _tr_M_word_impl.  Memoized when (z, h) are hashable (typical
    symbolic / numeric usage); falls back to direct call when they are
    not (e.g. mutable mpf wrappers).

    Many subwords repeat across the recursion tree at H_n with multiple
    top-generator occurrences, so caching collapses the worst-case
    2^(n-1) branching factor to polynomial in distinct (word, n) pairs.

    The recursion-depth guard is preserved: ``depth`` is propagated
    through the cached path to ``_tr_M_word_impl``, while the cache
    key intentionally excludes ``depth`` (the result of tr_M is
    depth-independent).
    """
    if depth > max_depth:
        raise RecursionError(
            f"tr_M recursion too deep: word={word}, n={n}")
    word_t = tuple(word)
    try:
        key = (word_t, n, z, h, max_depth)
        if key in _TR_M_WORD_CACHE:
            return _TR_M_WORD_CACHE[key]
    except TypeError:
        # z or h unhashable — bypass cache entirely.
        return _tr_M_word_impl(word_t, n, z, h,
                                depth=depth, max_depth=max_depth)
    result = _tr_M_word_impl(word_t, n, z, h,
                              depth=depth, max_depth=max_depth)
    _TR_M_WORD_CACHE[key] = result
    return result


def _tr_M_word_impl(word: tuple, n: int, z, h, *,
                     depth: int = 0, max_depth: int = 200):
    """Canonical Markov trace of a Hecke word in H_n(q).

    word: tuple of non-negative ints (generator indices σ_i).
    n: strand count (H_n has generators σ_0..σ_{n-2}).
    z, h: Markov parameter and q - q⁻¹ (symbolic or numeric).
    """
    if depth > max_depth:
        raise RecursionError(
            f"tr_M recursion too deep: word={word}, n={n}")
    if not word:
        return sp.Integer(1) if hasattr(z, "is_number") else 1
    max_gen = max(word)
    if max_gen < n - 2:
        return tr_M_word(word, max_gen + 2, z, h,
                          depth=depth + 1, max_depth=max_depth)
    top = n - 2

    # Count top occurrences
    top_positions = [i for i, g in enumerate(word) if g == top]
    if len(top_positions) == 1:
        pos = top_positions[0]
        rest = word[pos + 1:] + word[:pos]
        return z * tr_M_word(rest, n - 1, z, h,
                              depth=depth + 1, max_depth=max_depth)

    # Multiple tops: rotate so the last top is at the rightmost position.
    last_top = top_positions[-1]
    rotated = word[last_top + 1:] + word[:last_top + 1]
    # Now rotated ends with top. rest = rotated[:-1].
    rest = rotated[:-1]
    if top not in rest:
        return z * tr_M_word(rest, n - 1, z, h,
                              depth=depth + 1, max_depth=max_depth)

    # rest contains another top. Find its position.
    inner_pos = len(rest) - 1 - rest[::-1].index(top)
    # Segment between inner_pos and end of rest
    segment = rest[inner_pos + 1:]

    # Case A: segment has no top-1 → we can commute inner top to end.
    if (top - 1) not in segment:
        # New word: prefix + segment + (top, top) → apply σ² = hσ + 1.
        prefix = rest[:inner_pos]
        new_base = prefix + segment  # type: ignore
        # tr_M((new_base) · σ² · 1) = h · tr_M(new_base · σ) + tr_M(new_base)
        term1 = tr_M_word(new_base + (top,), n, z, h,
                           depth=depth + 1, max_depth=max_depth)
        term2 = tr_M_word(new_base, n, z, h,
                           depth=depth + 1, max_depth=max_depth)
        return h * term1 + term2

    # Case B: segment contains top-1. Apply braid relation explicitly.
    # The obstructing σ_{top-1} sits at some position in segment.
    # Word structure near the two tops:
    #   prefix + σ_top + alpha + σ_{top-1} + beta + σ_top  (+ already at end)
    # Use braid σ_top σ_{top-1} σ_top = σ_{top-1} σ_top σ_{top-1}
    # to move one top past the σ_{top-1}.
    tm1_positions = [i for i, g in enumerate(segment) if g == top - 1]
    # Take the FIRST top-1 in segment (closest to inner_top).
    first_tm1_in_seg = tm1_positions[0]
    # Word: rest[:inner_pos] + σ_top + segment[:first_tm1] + σ_{top-1}
    #        + segment[first_tm1+1:] + σ_top
    # We want to apply braid on the two tops with σ_{top-1} between them.
    # If segment[:first_tm1] contains only commuting generators with top (i.e.
    # none of them is top - 1), then we can slide σ_top to be directly adjacent
    # to σ_{top-1}, giving σ_top · σ_{top-1} · ... · σ_top.
    alpha = segment[:first_tm1_in_seg]  # commutes with top (we're in Case B
                                         # and this alpha has no top-1)
    if (top - 1) in alpha:
        # Shouldn't happen since we took FIRST top-1, but safeguard.
        raise NotImplementedError(
            f"Unexpected top-1 in alpha segment for word {word}")
    beta = segment[first_tm1_in_seg + 1:]
    # Rebuild: (rest[:inner_pos]) · σ_top · alpha · σ_{top-1}
    #           · beta · σ_top
    # Commute σ_top past alpha (far-commute): ends up as alpha · σ_top · σ_{top-1} · beta · σ_top
    # Now apply braid: σ_top · σ_{top-1} · σ_top = σ_{top-1} · σ_top · σ_{top-1}
    # But we have σ_top · σ_{top-1} · (beta) · σ_top  — not directly.
    # To apply braid we need σ_top · σ_{top-1} · σ_top adjacent.  Commute σ_top
    # past beta if possible (beta must have no top-1).
    if (top - 1) in beta:
        # Both sides have top-1: cannot resolve cleanly.  Fall back: return 0
        # conservatively (sentinel for complex case).  Caller should detect.
        raise NotImplementedError(
            f"Complex braid case (multiple top-1 in segment): word={word}")
    # beta commutes with top.  After commutation:
    #   (rest[:inner_pos]) · alpha · σ_top · σ_{top-1} · σ_top · beta
    # Now apply braid: σ_top · σ_{top-1} · σ_top = σ_{top-1} · σ_top · σ_{top-1}
    #   → (rest[:inner_pos]) · alpha · σ_{top-1} · σ_top · σ_{top-1} · beta
    # Now only ONE σ_top in the entire word (we had two, braid consumed one).
    new_word = (rest[:inner_pos] + alpha + (top - 1,) + (top,)
                 + (top - 1,) + beta)
    return tr_M_word(new_word, n, z, h,
                      depth=depth + 1, max_depth=max_depth)


def tr_M_element(elem, n: int, z=Z_SYMB, h=H_SYMB,
                  ocneanu_fallback: bool = True,
                  simplify: bool = True):
    """Canonical Markov trace of a SymbolicHeckeElement.

    Uses the recursive Markov-axiom reduction tr_M_word.  For braid
    words that the recursion cannot handle directly (e.g., multiple
    top-1 occurrences in both alpha and beta segments around a top
    generator), falls back to the Ocneanu-weight path
    (ocneanu_weights.canonical_markov_trace_via_ocneanu) which
    computes the same canonical trace via ω-weighted seminormal
    character sum.  Set ``ocneanu_fallback=False`` to keep the
    original NotImplementedError behaviour.

    ``simplify`` (default True for back-compat): apply ``sp.simplify``
    to the aggregated total before returning.  For elements with
    many terms this dominates the runtime — at A=3 (³He, 128 reduced
    terms, ~5000 sympy ops) the simplify step exceeds 30 minutes
    while the aggregation itself takes 60 ms.  Pass ``simplify=False``
    to return the unsimplified total; numerical evaluation
    (``.subs(q, q₀).evalf(...)``) is unaffected by simplification.
    The Markov-peel production path
    (`markov_peel.tr_M_atomic`) opts out of simplification.
    """
    total = sp.Integer(0)
    fallback_terms = {}
    for word, coeff in elem.terms.items():
        # Only non-negative generator indices (skip formal variables)
        if any(g < 0 for g in word):
            continue
        try:
            tr_w = tr_M_word(word, n, z, h)
            total += coeff * tr_w
        except (NotImplementedError, RecursionError):
            if not ocneanu_fallback:
                raise
            # Collect for Ocneanu fallback
            fallback_terms[word] = coeff
    if fallback_terms:
        # Rebuild a mini-element and delegate
        from hecke_symbolic import SymbolicHeckeElement
        sub_elem = SymbolicHeckeElement(fallback_terms)
        from ocneanu_weights import canonical_markov_trace_via_ocneanu
        from q_parameter import Q as _Q0
        # Ocneanu path wants the *substrate* parameter q, not the
        # Markov parameter z.  Determine whether z and h are purely
        # numeric; if so evaluate the fallback at the canonical q₀,
        # otherwise emit a tagged symbolic placeholder.
        def _is_symbolic(x):
            return isinstance(x, sp.Basic) and not x.is_number
        if _is_symbolic(z) or _is_symbolic(h):
            # Symbolic path — add a tagged placeholder
            # (caller evaluates numerically downstream).
            total += sp.Symbol(
                f"_ocneanu_fallback_n{n}_" + str(len(fallback_terms)),
                real=True)
        else:
            num = canonical_markov_trace_via_ocneanu(sub_elem, n,
                                                        q_val=float(_Q0))
            total += num
    if simplify and isinstance(total, sp.Basic):
        return sp.simplify(total)
    return total


# ── Prop table sanity ───────────────────────────────────────────

if __name__ == "__main__":
    from q_parameter import Q as q0_num, HA as h_num
    z_num = 1.0 / (q0_num ** 0.5 + q0_num ** (-0.5))

    print("=" * 80)
    print("CANONICAL MARKOV TRACE — prop:categorical-mass-markov table")
    print(f"q₀ = {q0_num:.6f}, z = {z_num:.6f}, h = {h_num:.6f}")
    print("=" * 80)

    # Prop table
    TESTS = [
        ("𝟏 (photon)",           (),                1.0),
        ("σ₀ (polarisation)",    (0,),              z_num),
        ("σ₀σ₁ (gluon)",          (0, 1),            z_num ** 2),
        ("σ₀σ₁σ₀ (electron)",    (0, 1, 0),        h_num * z_num ** 2 + z_num),
        ("σ₁σ₀σ₁ (braid-equiv)", (1, 0, 1),        h_num * z_num ** 2 + z_num),
        ("σ₀² = hσ₀ + 1",        (0, 0),           h_num * z_num + 1.0),
    ]

    print(f"\n  {'Word':>24} {'Computed':>14} {'Expected':>14} "
          f"{'Match':>6}")
    print("  " + "-" * 68)
    for name, word, expected in TESTS:
        n = max(word) + 2 if word else 1
        computed = float(tr_M_word(word, n, z_num, h_num))
        match = "✓" if abs(computed - expected) < 1e-9 else "✗"
        print(f"  {name:>24} {computed:>+14.6f} {expected:>+14.6f} "
              f"{match:>6}")

    # Additional: figure-8 (σ₀σ₁⁻¹)². σ₁⁻¹ = σ₁ - h in our convention.
    print("\nFigure-8 (σ₀σ₁⁻¹)² via tr_M_element (symbolic q, eval at q₀):")
    from hecke_symbolic import (SymbolicHeckeElement, SymbolicHeckeDivision,
                                  HA as H_SYMB_full, q as q_sym)
    div = SymbolicHeckeDivision()
    s0 = SymbolicHeckeElement({(0,): sp.Integer(1)})
    s1_inv = SymbolicHeckeElement({(1,): sp.Integer(1),
                                     (): -H_SYMB_full})
    figure_8 = s0 * s1_inv * s0 * s1_inv
    figure_8, _ = div.reduce(figure_8, engine='laurent')
    # Symbolic trace
    tr_sym = tr_M_element(figure_8, 3)
    tr_num = complex(tr_sym.subs(q_sym, q0_num))
    tr_num_re = tr_num.real if abs(tr_num.imag) < 1e-9 else tr_num
    print(f"  tr_M (symbolic) = {sp.simplify(tr_sym)}")
    print(f"  tr_M at q₀      = {tr_num_re}   (prop says ≈ 0.182)")
