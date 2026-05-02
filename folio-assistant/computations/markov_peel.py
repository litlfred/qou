#!/usr/bin/env python3
"""
Markov-axiom recursive ascent for atomic braid words.

Production path for `tr_M(β)` on atomic braids that bypasses the
Hoefsmit per-Wedderburn-block sum.  Instead of building dim-up-to-462
matrices `ρ_λ(σ_i)` for every partition `λ ⊢ 3A` and summing
`Σ_λ y_λ · χ_λ(β)`, this module reduces a braid word in `H_n(q)`
to canonical form and then **peels the top generator** via the
Markov axiom

    tr_M^{(n)}(x · σ_{n−1}) = z · tr_M^{(n−1)}(x)    ∀ x ∈ H_{n−1}(q)

recursing down the chain `H_n ⊃ H_{n−1} ⊃ … ⊃ H_1` until reaching
the base case `tr_M^{(1)}(1) = 1`.

The Hecke quadratic `σ_i² = (q − q⁻¹)σ_i + 1` produces a binary
branching at each squared generator; the resulting tree is bounded
by braid length and reduction depth, never materialising a matrix
representation of the algebra.

This is **Phase 1** — a thin wrapper around the existing recursive
trace primitives:
  - `hecke_symbolic.SymbolicHeckeDivision` for Gröbner–Shirshov
    reduction and crossing constructors
  - `markov_trace_canonical.tr_M_element` for the recursive ascent

It exposes a single production API `tr_M_atomic(Z, N)` that returns
the symbolic Markov trace of the atomic braid for atom (Z, N) as a
sympy expression in `q`.

Phase 2+ work (extend Gröbner–Shirshov for `n > 3`, eliminate the
Ocneanu fallback) is tracked in #508.

Reference: prop:markov-pair-z2 (QOU narrative).
Witness: `markov-peel.witness.json` (cross-check against
`atomic-tr-m-mpfr-50dps.witness.json`).
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Tuple, List

import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from hecke_symbolic import (  # noqa: E402
    SymbolicHeckeElement,
    SymbolicHeckeDivision,
    HA,           # h = q − q⁻¹
    q as q_sym,   # the symbolic substrate parameter
    z_markov,
)
from markov_trace_canonical import tr_M_element  # noqa: E402

# Numerical h from `hecke_core` (used by `atom_braid_word_3A` to build
# the (c, d) triples).  Imported lazily inside the builders.
_H_NUM_TOL = 1e-9


# ── Crossing → Hecke element ────────────────────────────────────────

def crossing_from_cd(
    gen_idx: int,
    c,
    d,
    *,
    h_num: float,
) -> SymbolicHeckeElement:
    """Translate one `(c, d, gen_idx)` triple into a SymbolicHeckeElement.

    The crossing operator is `c·σ_i + d·𝟏`.  Numerical `(c, d)` from
    `atom_braid_word_3A` are recognised as one of the canonical
    symbolic forms (so the resulting element stays exact in `q`):

      (1, 0)    → σ_i               (positive crossing)
      (1, −h)   → σ_i − h·𝟏 = σ_i⁻¹
      (1, −h/2) → σ_i − (h/2)·𝟏 = ½(σ_i + σ_i⁻¹)
      (0, 1)    → 𝟏                  (no-interaction)

    Any unrecognised `(c, d)` raises — Phase-1 deliberately keeps the
    domain narrow so we get loud failures on convention drift.
    """
    cf, df = float(c), float(d)
    if abs(cf - 1.0) < _H_NUM_TOL and abs(df) < _H_NUM_TOL:
        # σ
        return SymbolicHeckeElement({(gen_idx,): sp.Integer(1)})
    if abs(cf - 1.0) < _H_NUM_TOL and abs(df + h_num) < _H_NUM_TOL:
        # σ − h·𝟏
        return SymbolicHeckeElement({
            (gen_idx,): sp.Integer(1),
            (): -HA,
        })
    if abs(cf - 1.0) < _H_NUM_TOL and abs(df + h_num / 2) < _H_NUM_TOL:
        # σ − (h/2)·𝟏
        return SymbolicHeckeElement({
            (gen_idx,): sp.Integer(1),
            (): -HA / 2,
        })
    if abs(cf) < _H_NUM_TOL and abs(df - 1.0) < _H_NUM_TOL:
        # identity (no crossing)
        return SymbolicHeckeElement.identity()
    raise ValueError(
        f"unknown (c, d) crossing: c={cf!r}, d={df!r} at gen={gen_idx} "
        f"(h={h_num!r})"
    )


def crossing_element(gen_idx: int, cross_type: str) -> SymbolicHeckeElement:
    """Legacy convenience wrapper used by the unit tests.

    Matches the string convention in `atomic_braid_to_crossings`:
      "sigma"     → σ_i
      "sigma_inv" → σ_i − h·𝟏
      "averaged"  → σ_i − (h/2)·𝟏
    """
    sigma = SymbolicHeckeElement({(gen_idx,): sp.Integer(1)})
    if cross_type == "sigma":
        return sigma
    if cross_type == "sigma_inv":
        return sigma + SymbolicHeckeElement({(): -HA})
    if cross_type == "averaged":
        return sigma + SymbolicHeckeElement({(): -HA / 2})
    raise ValueError(f"unknown cross_type: {cross_type!r}")


def word_to_element(word) -> SymbolicHeckeElement:
    """Turn a `[(c, d, gen_idx), …]` list (the production
    `atom_braid_word_3A` shape) into a single `SymbolicHeckeElement`
    by left-to-right multiplication.

    Builds the **unreduced** product `Π (c·σ + d·𝟏)`; the term count
    grows like `2^k` for a length-`k` word.  For atomic braids of
    length ≥ 30, prefer `incremental_reduced_element` which interleaves
    reduction with multiplication and keeps the term count bounded.
    """
    from hecke_core import h as _h_num  # numerical q − q⁻¹
    elem = SymbolicHeckeElement.identity()
    for c, d, gen in word:
        elem = elem * crossing_from_cd(gen, c, d, h_num=float(_h_num))
    return elem


def incremental_reduced_element(
    word,
    *,
    div: "SymbolicHeckeDivision | None" = None,
    max_iterations_per_step: int = 5000,
) -> SymbolicHeckeElement:
    """Multiply factors of `word` one at a time, reducing after each.

    The naive `word_to_element` builds the full unreduced product
    before any reduction, producing `2^k` terms for a length-`k` word.
    For atomic braids with `A ≥ 3` (word length ≥ 30), this explodes
    to thousands of terms before reduction can collapse them, and the
    subsequent fixpoint reduction loop chokes on the cross-term
    interactions.

    Interleaving reduction with multiplication keeps the intermediate
    term count bounded by the rank of `H_n(q)` (small).  The same
    pattern is used by the `__main__` demo in `hecke_symbolic.py` —
    promoting it here makes it the production path for atomic
    `tr_M(β)` evaluation.

    `word` matches the `atom_braid_word_3A` shape: list of
    `(c, d, gen_idx)` triples with numeric `(c, d)`.
    """
    from hecke_core import h as _h_num
    if div is None:
        div = SymbolicHeckeDivision()
    elem = SymbolicHeckeElement.identity()
    h_num = float(_h_num)
    for c, d, gen in word:
        factor = crossing_from_cd(gen, c, d, h_num=h_num)
        elem = elem * factor
        elem, _stats = div.reduce(
            elem, max_iterations=max_iterations_per_step
        )
    return elem


# ── Top-level production API ────────────────────────────────────────

def tr_M_atomic(
    Z: int,
    N: int,
    *,
    include_inter: bool = True,
    reduce_first: bool = True,
    max_iterations: int = 10000,
):
    """Symbolic Markov trace `tr_M(β)` of the atomic braid for (Z, N).

    Builds the atomic braid word via `atomic_braid_to_crossings`,
    optionally reduces in `H_n(q)` via Gröbner–Shirshov, then takes
    the canonical Markov trace via Markov-axiom recursive ascent.

    Returns a sympy expression in the symbolic substrate parameter
    `q` (and the derived `h = q − q⁻¹`, `z = 1/(q^½ + q^{-½})`).

    Parameters
    ----------
    Z, N : int
        Proton and neutron counts; A = Z + N, n_strands = 3·A.
    include_inter : bool
        Whether to include inter-nucleon crossings (default True;
        matches the production atomic-braid convention).
    reduce_first : bool
        Apply Gröbner–Shirshov reduction before tracing.  Strongly
        recommended: an unreduced word may exceed the recursion
        depth in `tr_M_element` for n > 3.
    max_iterations : int
        Cap for `SymbolicHeckeDivision.reduce`.

    Notes
    -----
    For `A ≥ 3`, the existing Gröbner–Shirshov reduction in
    `hecke_symbolic` is **incomplete**, and `tr_M_element` may fall
    back to the Ocneanu-weight path.  This is correct but slower
    and somewhat defeats the point.  Phase 2 of #508 completes the
    rewrite system so the recursion terminates without fallback.
    """
    # Local import — the production-path word builder lives in
    # `mass_at_3A_proper` (the Hoefsmit witness in
    # `atomic-tr-m-mpfr-50dps.witness.json` consumes the same word).
    from mass_at_3A_proper import atom_braid_word_3A

    A = Z + N
    n_strands = 3 * A

    word = atom_braid_word_3A(Z, N, include_inter=include_inter)

    if reduce_first:
        # Interleave reduction with multiplication.  Building the full
        # unreduced product first explodes to ~9000 terms at A=3 and
        # the fixpoint reducer chokes on the cross-term interactions
        # (timing out > 9 minutes on tritium).  The incremental path
        # keeps the intermediate term count bounded.
        elem = incremental_reduced_element(
            word, max_iterations_per_step=max_iterations
        )
    else:
        elem = word_to_element(word)

    return tr_M_element(elem, n_strands)


# ── Quick smoke test (deuteron cross-check) ─────────────────────────

if __name__ == "__main__":
    from q_parameter import Q as Q0

    print("Markov-axiom recursive ascent — smoke test")
    print("=" * 60)
    for label, (Z, N) in [
        ("proton",   (1, 0)),
        ("neutron",  (0, 1)),
        ("deuteron", (1, 1)),
    ]:
        try:
            tr_sym = tr_M_atomic(Z, N)
            tr_q0 = float(tr_sym.subs(q_sym, Q0).evalf(30))
            print(f"  {label:9s}  Z={Z} N={N}  tr_M(q₀) = {tr_q0:+.16e}")
        except Exception as exc:
            print(f"  {label:9s}  Z={Z} N={N}  FAILED: {exc!r}")
