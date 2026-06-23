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

import functools
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from hecke_symbolic import (  # noqa: E402
    SymbolicHeckeElement,
    SymbolicHeckeDivision,
    HA,           # h = q − q⁻¹
    q as q_sym,   # the symbolic substrate parameter
)
from markov_trace_canonical import tr_M_element  # noqa: E402

# Numerical h from `hecke_core` (used by `atom_braid_word_3A` to build
# the (c, d) triples).  Imported lazily inside the builders.
_H_NUM_TOL = 1e-9

# Color-weighted p-n averaged crossing support (owner default
# pn_convention="bring_color_weighted", per mass_at_3A_proper.atom_braid_word_3A):
# the inter-nucleon crossing is σ − h·(½ − δ/4)·𝟙 with
# δ = flavor_split_subleading(q₀), NOT the color-blind σ − h/2.
# Lazily initialised (q_parameter is imported lazily elsewhere here to
# avoid import cycles). Returns (δ_numeric_at_q0, δ_symbolic_in_q).
_COLOR_DELTA: "tuple[float, object] | None" = None


def _color_delta():
    global _COLOR_DELTA
    if _COLOR_DELTA is None:
        from _li_2_q_util import flavor_split_subleading
        from q_parameter import Q as _Q0
        d_num = float(flavor_split_subleading(mp.mpf(str(_Q0))))
        # symbolic mirror of flavor_split_subleading(q):
        #   leading = (q−1)²·(1−q⁻⁴)/3 ;  subleading = leading·(1+((q−1)/q)³)
        leading = (q_sym - 1) ** 2 * (1 - q_sym ** (-4)) / 3
        d_sym = leading * (1 + ((q_sym - 1) / q_sym) ** 3)
        _COLOR_DELTA = (d_num, d_sym)
    return _COLOR_DELTA


# Cache for crossing_from_cd: per (gen_idx, c-rounded, d-rounded)
# the resulting SymbolicHeckeElement is uniquely determined. Keying
# on rounded floats avoids identity-comparison issues.
_CROSSING_CACHE: dict = {}


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

    Cached on (gen_idx, c-rounded, d-rounded, h_num-rounded). For
    atomic-braid words at A=4 the same crossing template gets
    instantiated O(2A) times per atom; caching the conversion shaves
    sympy-construction overhead in the hot path.
    """
    cf, df = float(c), float(d)
    cache_key = (gen_idx, round(cf, 12), round(df, 12), round(h_num, 12))
    cached = _CROSSING_CACHE.get(cache_key)
    if cached is not None:
        return cached
    if abs(cf - 1.0) < _H_NUM_TOL and abs(df) < _H_NUM_TOL:
        # σ
        result = SymbolicHeckeElement({(gen_idx,): sp.Integer(1)})
    elif abs(cf - 1.0) < _H_NUM_TOL and abs(df + h_num) < _H_NUM_TOL:
        # σ − h·𝟏
        result = SymbolicHeckeElement({
            (gen_idx,): sp.Integer(1),
            (): -HA,
        })
    elif abs(cf - 1.0) < _H_NUM_TOL and abs(df + h_num / 2) < _H_NUM_TOL:
        # σ − (h/2)·𝟏
        result = SymbolicHeckeElement({
            (gen_idx,): sp.Integer(1),
            (): -HA / 2,
        })
    elif abs(cf) < _H_NUM_TOL and abs(df - 1.0) < _H_NUM_TOL:
        # identity (no crossing)
        result = SymbolicHeckeElement.identity()
    elif abs(cf - 1.0) < _H_NUM_TOL and \
            abs(df + h_num * (0.5 - _color_delta()[0] / 4.0)) < _H_NUM_TOL:
        # σ − h·(½ − δ/4)·𝟙  (color-weighted p-n averaged crossing)
        _, d_sym = _color_delta()
        result = SymbolicHeckeElement({
            (gen_idx,): sp.Integer(1),
            (): -HA * (sp.Rational(1, 2) - d_sym / 4),
        })
    else:
        raise ValueError(
            f"unknown (c, d) crossing: c={cf!r}, d={df!r} at gen={gen_idx} "
            f"(h={h_num!r})"
        )
    _CROSSING_CACHE[cache_key] = result
    return result


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

@functools.lru_cache(maxsize=4)
def _nucleon_nf_and_trace(
    Z: int, N: int, max_iterations: int
) -> tuple[SymbolicHeckeElement, sp.Expr]:
    """Pre-compute the reduced NF and Markov trace of a single nucleon
    (proton (1,0) or neutron (0,1)) in H_3(q). Cached for the session.

    Returns (nf_element, tr_M_value). The NF is in H_3(q) so the only
    generators present are σ_1, σ_2 (i.e. word indices 1, 2).
    """
    from mass_at_3A_proper import atom_braid_word_3A
    from markov_trace_canonical import tr_M_element

    word = atom_braid_word_3A(Z, N, include_inter=True)
    div = SymbolicHeckeDivision()
    nf = incremental_reduced_element(
        word, div=div, max_iterations_per_step=max_iterations
    )
    tr = tr_M_element(nf, 3, simplify=False)
    return nf, tr


def _shift_nf(nf: SymbolicHeckeElement, δ: int) -> SymbolicHeckeElement:
    """Return `nf` with every generator index in every word shifted by δ.

    Hoisted out of `tr_M_atomic` so it can be combined with
    `_shifted_nucleon_nf` caching (Strategy #3 from
    `docs/audits/2026-05-20-markov-peel-bottleneck-profile.md`).
    """
    shifted_terms: dict = {}
    for w, c in nf.terms.items():
        w_shifted = tuple(g + δ for g in w)
        shifted_terms[w_shifted] = c
    return SymbolicHeckeElement(shifted_terms)


@functools.lru_cache(maxsize=32)
def _shifted_nucleon_nf(
    Z: int, N: int, δ: int, max_iterations: int
) -> tuple[SymbolicHeckeElement, sp.Expr]:
    """`_nucleon_nf_and_trace(Z, N)` with generator indices shifted by δ.

    Cached across calls: the same (species=p|n, δ) returns the
    same shifted NF without re-running the shift loop. For A ≥ 4
    atoms the same δ ∈ {0, 3, 6, 9, ...} recurs across each call
    to `tr_M_atomic`; pre-caching saves ~1.5-2× per call vs the
    inline `_shift_nf(nf, δ)` recompute.

    Returns the shifted NF and the (unshifted) tr_M value — the
    Markov trace is invariant under generator-index shift on the
    nucleon's local 3-strand block (since `tr_M_element` traces
    over the local Hecke sub-algebra).
    """
    nf, tr = _nucleon_nf_and_trace(Z, N, max_iterations)
    if δ == 0:
        return nf, tr
    return _shift_nf(nf, δ), tr


def tr_M_atomic(
    Z: int,
    N: int,
    *,
    include_inter: bool = True,
    reduce_first: bool = True,
    max_iterations: int = 10000,
    pre_register_nucleons: bool = True,
    use_fast: bool = True,
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

    # Fast path: route through the LaurentQ-coefficient pipeline in
    # `hecke_laurent_fast.tr_M_atomic_fast`.  Numerical equivalence at
    # q = q₀ verified on all atoms in [proton, neutron, deuteron,
    # tritium, helium-3, helium-4, lithium-5]; speedup 3-25× over the
    # sympy path below.  Opt out with `use_fast=False` to recover the
    # sympy path verbatim (e.g. for callers that depend on the exact
    # symbolic form rather than the numerical value at q₀).
    if use_fast and reduce_first:
        from hecke_laurent_fast import tr_M_atomic_fast
        try:
            return tr_M_atomic_fast(
                Z, N, include_inter=include_inter,
                max_iterations=max_iterations,
            )
        except ValueError as e:
            # The color-weighted inter-nucleon crossing (A ≥ 2 under the
            # bring_color_weighted convention) carries a non-Laurent δ(q)
            # coefficient (flavor_split_subleading), which the LaurentQ
            # fast path cannot represent. Fall back to the exact
            # sympy/Ocneanu slow path below, which handles arbitrary
            # rational-in-q coefficients. A=1 (proton/neutron) has no
            # inter-nucleon crossing and stays on the fast path.
            if "non-Laurent" not in str(e):
                raise

    word = atom_braid_word_3A(Z, N, include_inter=include_inter)

    # Pre-registration of proton/neutron NFs (default ON; opt-out
    # by passing `pre_register_nucleons=False`).
    # For each nucleon position k ∈ [0, A), register the proton (or
    # neutron) NF pre-shifted by δ=3k as a distinct atom_id. The
    # reduce() Rule 4 multi-term matcher then folds occurrences at
    # offset 0 (against each pre-shifted NF), keeping intermediate
    # term counts bounded during incremental reduction. Before
    # tracing, `unfold` distributes the formal tokens back into
    # generator words; the surrounding inter-nucleon crossings are
    # preserved as a literal suffix, so the unfolded element is the
    # algebraically-equivalent reduced form.
    #
    # atom_id encoding: `-(100 * (k + 1) + species)`, species
    # ∈ {1: proton, 2: neutron}. So nucleon-0 proton = -101,
    # nucleon-1 proton = -201, nucleon-2 neutron = -302, etc.
    div: SymbolicHeckeDivision | None = None
    if pre_register_nucleons and A >= 2:
        div = SymbolicHeckeDivision()

        # Order: build the per-nucleon registration in the same
        # left-to-right order as atom_braid_word_3A — protons first
        # (positions 0..Z-1), then neutrons (positions Z..A-1).
        # Uses `_shifted_nucleon_nf` (module-level + lru_cached)
        # so repeated calls with the same (species, δ) skip the
        # shift loop (Strategy #3 from
        # docs/audits/2026-05-20-markov-peel-bottleneck-profile.md).
        for k in range(Z):
            δ = 3 * k
            p_nf_shifted, p_tr = _shifted_nucleon_nf(
                1, 0, δ, max_iterations
            )
            div.register_quotient(
                -(100 * (k + 1) + 1),
                p_nf_shifted,
                name=f"proton@{δ}",
                n_strands=3,
                tr_M_value=p_tr,
            )
        for k in range(N):
            δ = 3 * (Z + k)
            n_nf_shifted, n_tr = _shifted_nucleon_nf(
                0, 1, δ, max_iterations
            )
            div.register_quotient(
                -(100 * (Z + k + 1) + 2),
                n_nf_shifted,
                name=f"neutron@{δ}",
                n_strands=3,
                tr_M_value=n_tr,
            )

    if reduce_first:
        # Interleave reduction with multiplication.  Building the full
        # unreduced product first explodes to ~9000 terms at A=3 and
        # the fixpoint reducer chokes on the cross-term interactions
        # (timing out > 9 minutes on tritium).  The incremental path
        # keeps the intermediate term count bounded.
        elem = incremental_reduced_element(
            word, div=div,
            max_iterations_per_step=max_iterations,
        )
    else:
        elem = word_to_element(word)

    # If folding was active, unfold formal tokens into the
    # full reduced word before tracing. tr_M_element only
    # understands non-negative generator indices; unfold restores
    # the algebraically-equivalent generator-only representation.
    if div is not None and any(
        any(g < 0 for g in w) for w in elem.terms
    ):
        elem = div.unfold(elem)

    # `simplify=False`: skip the `sp.simplify` aggregation step.  At
    # A=3 the aggregated total has ~5000-12000 sympy ops; calling
    # `simplify` on it exceeds 30 minutes (³He) while the recursion
    # itself runs in under a second.  Numerical evaluation at q=q₀
    # is unaffected by simplification.  Callers that want a tidied
    # symbolic form can `sp.cancel` or `sp.together` the result
    # themselves (still much faster than `simplify`).
    return tr_M_element(elem, n_strands, simplify=False)


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
            # Stay in mpmath the whole way — `float()` would silently
            # truncate the 50-dps value to float64 (~17 digits), breaking
            # the L1 1-ppQ goal for any downstream consumer. Per the
            # author 2026-06-09 ("float64 is EVIL") + the new
            # `compute_no_mpf_to_float_cast` critical-severity QA
            # criterion that flags exactly this pattern.
            tr_q0 = mp.mpf(str(tr_sym.subs(q_sym, Q0).evalf(50)))
            print(f"  {label:9s}  Z={Z} N={N}  tr_M(q₀) = {mp.nstr(tr_q0, 16)}")
        except Exception as exc:
            print(f"  {label:9s}  Z={Z} N={N}  FAILED: {exc!r}")
