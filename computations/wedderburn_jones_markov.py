#!/usr/bin/env python3
"""
wedderburn_jones_markov.py — canonical Jones-Markov Wedderburn sum.

Replacement for `schur_weyl_symbolic.global_wedderburn_sum_symbolic` and
`per_stratum_sum_symbolic` that uses the **correct Jones-Markov weights
y_λ(q)** via Wenzl's Schur principal specialization, NOT the
2-variable Schur formula `s_λ(q, q⁻¹) / H_q(λ)` (which vanishes for
≥ 3-row partitions, dropping the `(1^p)` sign-rep entirely).

Per
[`docs/audits/2026-05-08-p3-h-3a-divergence.md`](../../docs/audits/2026-05-08-p3-h-3a-divergence.md),
the legacy `schur_weyl_weight(partition, q)` is NOT the Markov-trace
weight at q ≠ 1.  The QOU paper requires `y_λ(q)` per
`markov_weights_symbolic.solve_y_lambda(n)`.

This module exposes the canonical sum with **numerical-q-from-start**
performance: substitutes `q = q_0` BEFORE the symbolic `sp.cancel`
that was the bottleneck in naive `solve_y_lambda(n)` for n ≥ 6.

References:
- markov_weights_symbolic.solve_y_lambda — canonical y_λ(q)
- prop:atomic-mass-gb-nf
- 1ppb workplan §P3 (`docs/coordination/1ppb.md`)
- docs/audits/2026-05-08-p3-h-3a-divergence.md

@module computations/wedderburn_jones_markov
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import os
import sys
from math import factorial
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import sympy as sp  # noqa: E402

import markov_weights_symbolic as m  # noqa: E402

Q_SYM = sp.symbols("q", positive=True)


def _f_lambda(shape: tuple) -> int:
    """SYT count via the hook-length formula: f^λ = n! / Π h_x."""
    hs, _ = m.hooks_and_contents(list(shape))
    prod = 1
    for h in hs:
        prod *= h
    n = sum(shape)
    return factorial(n) // prod


def _schur_principal_at_q(args):
    """Top-level worker for multiprocessing.Pool.imap_unordered."""
    sh, q_str = args
    return sh, m.schur_principal_symbolic(list(sh)).subs(
        Q_SYM, sp.sympify(q_str)
    ).evalf(30)


_Y_LAMBDA_AT_Q0_WITNESS_CACHE: dict[int, dict[tuple, sp.Expr]] | None = None
_Y_LAMBDA_AT_Q0_WITNESS_Q0: float | None = None


def _load_y_lambda_at_q0_witness() -> dict[int, dict[tuple, sp.Expr]]:
    """Load precomputed 50-dps y_λ(q_0) values from witness.

    `y-lambda-at-q0.witness.json` carries numeric y_λ at q_0 for
    n = 2..12 — built once by `y_lambda_at_q0_cache.py`.  Loading
    is O(KB) and replaces the per-call 150-300s recompute path
    that bottlenecked V2 chirality and ⁴He compositional probes.

    Returns `{n: {partition: mpf-or-sympy y_lambda}}` keyed by n,
    or empty dict if witness file missing (caller falls back to
    the slow recompute path).

    Also records, in `_Y_LAMBDA_AT_Q0_WITNESS_Q0`, the q_0 the witness was
    actually BUILT at.  Callers must gate on that value, not on the package
    constant — see `y_lambda_at`.
    """
    global _Y_LAMBDA_AT_Q0_WITNESS_CACHE, _Y_LAMBDA_AT_Q0_WITNESS_Q0
    if _Y_LAMBDA_AT_Q0_WITNESS_CACHE is not None:
        return _Y_LAMBDA_AT_Q0_WITNESS_CACHE
    import json
    from pathlib import Path
    path = Path(__file__).parent / "y-lambda-at-q0.witness.json"
    if not path.exists():
        _Y_LAMBDA_AT_Q0_WITNESS_CACHE = {}
        return {}
    w = json.loads(path.read_text())
    by_n: dict[int, dict[tuple, sp.Expr]] = {}
    for n_str, rows in w.get("data", {}).get("by_n", {}).items():
        n_key = int(n_str)
        d: dict[tuple, sp.Expr] = {}
        for r in rows:
            shape = tuple(r["partition"])
            d[shape] = sp.Float(r["y_at_q0_50dps"], 50)
        by_n[n_key] = d
    # Record the q_0 this witness was built at, so the fast path can refuse to
    # serve it to a caller asking for a DIFFERENT anchor.
    _q0 = (w.get("parameters", {}) or {}).get("q_0") or w.get("q0Value")
    try:
        _Y_LAMBDA_AT_Q0_WITNESS_Q0 = float(_q0) if _q0 is not None else None
    except (TypeError, ValueError):
        _Y_LAMBDA_AT_Q0_WITNESS_Q0 = None
    _Y_LAMBDA_AT_Q0_WITNESS_CACHE = by_n
    return by_n


def y_lambda_at(
    n: int,
    q_val: sp.Expr | float | None = None,
    workers: int | None = None,
) -> dict[tuple, sp.Expr]:
    """Jones-Markov y_λ(q) at H_n — registry convention **D** since 2026-08-09.

    OWNER RULING: convention C excised. Every path below returned C
    (`y_λ(3,q₀) = (0.4153958, 0.2809296, 0.0227449)`, `z = 1/(√q+1/√q)`); this
    function now returns D (`(0.5054042, 0.2472979, 0)`, `z = q³/(q²+1)`).

    D's weights are the SU(2) quantum dimensions, computed by the hook-content
    principal specialisation in `y_lambda_su_n` and normalised `Σ y_λ f^λ = 1`.
    The defining difference is the row cap: `y_λ = 0` for `ℓ(λ) > 2`, which under
    C was nonzero — and that zero is exactly what
    `markovWeights_eq_jones_of_threeRow_eq_zero` needs to force D uniquely.

    THE THREE C FAST PATHS BELOW ARE NOW DEAD and are retained only as the
    historical record of what C was; the D result returns before any of them is
    reached. In particular `y-lambda-at-q0.witness.json` holds C weights and must
    NOT be served — that cache is why the switch has to happen here rather than
    only at `markov_z`.

    Scale note, because it governs the migration: this function has ~155
    consumers, more than twice the other three C implementations combined, and
    it was *unregistered* as a C implementation until 2026-08-09.

    The mass channel is unaffected — `m_p_substrate_identity_50dps.trM_borromean`
    uses the Lean closed form `(4+h²−3h⁴−h⁶)/(h²+4)` directly and never calls
    this. Verified: m_p unchanged.
    """
    from y_lambda_su_n import y_lambda_su_n as _y_su_n
    import mpmath as _mp
    # A SYMBOLIC q_val must reach the exact solver below, not the numeric branch.
    # It used to fall through to `_mp.mpf(str(q_val))` and die inside mpmath with
    # `invalid literal for int() with base 10: 'q'` — a symbolic-q caller had no
    # way in even though the exact convention-D solver was already wired for
    # `q_val=None`. Now `y_lambda_at(n, <symbol>)` returns y_λ exact in THAT
    # symbol. (bean `qou-j320`; needed by the symbolic trace in
    # `computations/substrate/bar_involution_is_isospin_probe.py`.)
    _symbolic = bool(getattr(q_val, "free_symbols", None))
    if q_val is not None and not _symbolic:
        _y = _y_su_n(n, _mp.mpf(str(q_val)), 2)
        return {sh: sp.Float(_mp.nstr(v, 30), 30) for sh, v in _y.items()}
    # Symbolic q: route to the EXACT convention-D solver (wired 2026-08-09).
    # This path previously RAISED — the excision left it with no D
    # implementation, and returning the C solver below would have silently
    # reintroduced C. `y_lambda_su_n_symbolic` is the same hook-content formula
    # as the numeric branch, over sympy, so the two agree to round-off
    # (measured 5.35e-51 at 50 dps) and `z` comes out as `q³/(q²+1)` exactly.
    #
    # It is also far cheaper than the C path it replaces: C needed an ~18 min
    # linear solve at n=4, this is a product formula and returns instantly.
    from y_lambda_su_n import y_lambda_su_n_symbolic as _y_su_n_sym
    return _y_su_n_sym(n, Q_SYM if q_val is None else q_val, 2)


def _y_lambda_at_convention_C_HISTORICAL(
    n: int,
    q_val: sp.Expr | float | None = None,
    workers: int | None = None,
) -> dict[tuple, sp.Expr]:
    """DEAD — convention C, excised 2026-08-09. Kept as the historical record.

    Original docstring follows.

    Jones-Markov y_λ(q) at H_n.

    If `q_val` is None (default): returns symbolic y_λ via
    `markov_weights_symbolic.solve_y_lambda(n)` — fast for n ≤ 3,
    slow for n ≥ 6 (sp.cancel on rational expressions).

    If `q_val` is a number AND matches q_0 (the substrate parameter,
    within 1e-12 tolerance): loads precomputed 50-dps values from
    `y-lambda-at-q0.witness.json` (sub-millisecond hot path,
    ~10 ms cold path including JSON parse).  This is the primary
    accelerator for V2 chirality, ⁴He compositional probes, and
    every other consumer that pins q to the substrate value.

    Else (numeric q_val that's not q_0): falls back to the
    **numerical-q-from-start** path by substituting in the Schur
    principal specialization BEFORE the Wenzl normalization,
    avoiding sp.cancel.

        n=3:  ~0.05s    (any path)
        n=6:  ~3.8s     (numerical-q-from-start)  vs  >60s (symbolic)
        n=9:  ~63s      (numerical)              vs  infeasible (symbolic)
        n=12: ~150-300s sequential, parallelisable across the 77
              partitions via `workers > 1` (multiprocessing).

    The `workers` parameter (default: None = sequential) enables
    process-pool parallelism for n ≥ 9 where partition count grows
    rapidly.  Set to `os.cpu_count()` (or a smaller value to leave
    cores free) for maximum throughput on the numerical-q path.

    SIDE EFFECT — the FIRST call raises global `mp.dps` to 50
    ---------------------------------------------------------
    Measured: a caller holding `mp.dps = 40` gets 50 back after its first
    `y_lambda_at(...)`.  Subsequent calls leave it alone, so this is a
    once-per-process effect, not a per-call one.

    The cause is a LAZY IMPORT, not this function's arithmetic: the first
    call pulls `y_lambda_su_n`, whose module scope runs `set_compute_dps(50)`
    (`y_lambda_su_n.py:269`).  That call is DELIBERATE AND CORRECT — it must
    precede the `mpf()` registry literals below it or `REG_ZC` / `REG_ZD` are
    parsed at mpmath's default 15 dps, rounded to 53 bits, and are already
    wrong when built; `module_const_precision_audit --strict` flags exactly
    those two.  Do not "fix" it by removing it.

    It is documented here because the consequence is invisible at the call
    site: a producer that sets `mp.dps = 40`, calls this, and then records
    `"compute_dps": mp.dps` writes a witness saying 50 while the file says 40.
    The values are not wrong — the later arithmetic really does run at 50 —
    but the declared precision is not the computed precision.  If you need a
    guaranteed working precision, set it AFTER your first call, or wrap the
    region in `mp.workdps(...)`.
    """
    shapes = [tuple(s) for s in m.partitions_of(n)]
    if q_val is None:
        return m.solve_y_lambda(n)

    # Fast path 1: serve the cached witness ONLY if the caller is asking for the
    # very q_0 the witness was BUILT at.
    #
    # This gate used to compare against `q_parameter.Q` (the PROTON / experimental
    # pin) while the witness itself is built at the MUON / ideal-3-CAL pin — 11.54 ppb
    # apart.  Passing `q_parameter.Q` therefore satisfied the gate TRIVIALLY and the
    # ideal-layer cache was served to an experimental-layer caller with no signal that
    # a calibration-layer boundary had been crossed.  See AGENTS.md §"q₀ anchor
    # convention" (owner directive 2026-08-07: default to the experimental anchor) and
    # `computations/deltalambda/mu3_anchor_consistency_probe.py`.
    #
    # Gating on the witness's own recorded q_0 means a proton-anchored caller now falls
    # through to fast path 2 (live closed form at the requested q) and gets values at
    # the anchor it actually asked for.  A caller that genuinely wants the muon cache
    # still hits it by passing the muon q_0.
    try:
        witness_by_n = _load_y_lambda_at_q0_witness()
        if _Y_LAMBDA_AT_Q0_WITNESS_Q0 is not None and \
                abs(float(q_val) - _Y_LAMBDA_AT_Q0_WITNESS_Q0) < 1e-12:
            cached = witness_by_n.get(n)
            if cached is not None and len(cached) == len(shapes):
                return dict(cached)
    except (ImportError, TypeError, ValueError):
        pass

    # Fast path 2: mpmath-direct hook-length closed form.
    # O(|λ|) mpf ops per partition; ~10⁵× faster than the sympy
    # path below at n ≥ 12. Verified to ~10⁻⁵⁰ vs the cached
    # witness for n ∈ {2..12}. See `schur_principal_mpmath.py`
    # for the closed-form derivation.
    try:
        import mpmath as _mp_inner
        from schur_principal_mpmath import y_lambda_at_q0_mpmath
        q_mp = _mp_inner.mpf(str(q_val))
        y_mp = y_lambda_at_q0_mpmath(n, q_mp)
        # Convert mpmath → sympy for consumer compatibility.
        return {sh: sp.Float(_mp_inner.nstr(y, 30), 30)
                for sh, y in y_mp.items()}
    except (ImportError, Exception):
        # Fall through to the legacy sympy path on any failure.
        pass

    # Legacy fallback: numerical-q-from-start (sympy)
    q_eval = sp.sympify(q_val)
    s_vals: dict[tuple, sp.Expr] = {}
    if workers and workers > 1 and len(shapes) > 1:
        q_str = str(q_eval)
        with Pool(processes=workers) as pool:
            for sh, val in pool.imap_unordered(
                _schur_principal_at_q,
                [(sh, q_str) for sh in shapes],
            ):
                s_vals[sh] = val
    else:
        for sh in shapes:
            s_vals[sh] = (
                m.schur_principal_symbolic(list(sh)).subs(Q_SYM, q_eval).evalf(30)
            )
    Z = sp.Integer(0)
    for sh in shapes:
        Z = Z + s_vals[sh] * _f_lambda(sh)
    return {sh: s_vals[sh] / Z for sh in shapes}


def global_wedderburn_sum_jones_markov(
    A: int,
    q_val: sp.Expr | float | None = None,
    char_kind: str = "trivial",
    Z: int | None = None,
    N: int | None = None,
    include_inter: bool = True,
    m_pp: int = 1,
    m_pn: int = 1,
    m_nn: int = 1,
) -> tuple[sp.Expr, list[dict]]:
    """Σ_{λ ⊢ 3A} y_λ(q) · χ^λ(𝒜) — canonical Jones-Markov form.

    Drop-in replacement for
    `schur_weyl_symbolic.global_wedderburn_sum_symbolic` that uses the
    correct Wenzl/Jones-Markov weight y_λ rather than the 2-variable
    Schur s_λ(q, q⁻¹) / H_q(λ).  The 2-variable form vanishes for
    partitions with > 2 rows, dropping the `(1^p)` sign-rep
    contribution that `prop:alpha-shift-torus-knot` identifies as the
    pole-order maximizer.

    Parameters mirror the legacy function; the only addition is
    `q_val` — pass q_0 to enable numerical-q-from-start (recommended
    for A ≥ 2 to avoid the sp.cancel bottleneck).

    Returns (sympy_expr, partitions_with_weights_list).
    """
    from schur_weyl_symbolic import (  # noqa: E402
        specht_character_atomic,
        specht_character_placeholder,
    )

    if char_kind == "mn-atom":
        if Z is None or N is None:
            raise ValueError("char_kind='mn-atom' requires Z and N.")
        if Z + N != A:
            raise ValueError(f"Z + N = {Z + N} != A = {A}")

    n = 3 * A
    y_vals = y_lambda_at(n, q_val)
    shapes = list(y_vals.keys())

    terms = []
    total = sp.Integer(0)
    for lam in shapes:
        y = y_vals[lam]
        # TL_n restriction: under convention D the Ocneanu weight y_λ is
        # EXACTLY zero for every λ with ≥ 3 rows — proved sorry-free for all
        # n by QOU.QBeta.WenzlWeight.conventionD_weight_eq_zero_iff (see
        # docs/audits/2026-08-16-tl-all-n-weight-vanishing.md). Those blocks
        # span ker(H_n ↠ TL_n), of dimension n! − Catalan(n) (1, 10, 78, 588,
        # 4611, 38890 at n = 3..8). Their contribution y·χ is identically 0,
        # so skipping them BEFORE the expensive character build changes no
        # value — it only avoids computing χ_λ in the radical. This is a
        # speed change, not a correctness fix.
        if sp.sympify(y).is_zero:
            continue  # zero Ocneanu weight ⇒ y·χ = 0 (TL_n radical)
        if char_kind == "mn-atom":
            chi = specht_character_atomic(
                lam, Z, N, include_inter, m_pp, m_pn, m_nn
            )
        else:
            chi = specht_character_placeholder(lam)
        # Use sp.sympify(...).is_zero — robust against unsimplified
        # sympy expressions where structural `== 0` would miss
        # mathematical zeros (gemini review on PR #572).
        if sp.sympify(chi).is_zero:
            continue  # skip zero-character partitions
        contrib = y * chi
        total += contrib
        terms.append({
            "partition": lam,
            "weight": y,
            "character": chi,
            "contribution": contrib,
        })
    return total, terms


def per_stratum_sum_jones_markov(
    A: int,
    S,
    q_val: sp.Expr | float | None = None,
) -> tuple[sp.Expr, list[dict]]:
    """Σ_{λ ⊢ 3A} y_λ(q) · χ^λ(π_S) — canonical Jones-Markov form.

    Drop-in replacement for
    `schur_weyl_symbolic.per_stratum_sum_symbolic` using y_λ rather
    than 2-variable Schur.

    Parameters
    ----------
    A : int
        Number of nucleons (3A strands).
    S : iterable
        Subset of generator indices.
    q_val : optional numeric q (e.g. q_0).  None = symbolic.
    """
    from murnaghan_nakayama import (  # noqa: E402
        cycle_type_of_permutation,
        mn_character,
    )
    from schur_weyl_symbolic import stratum_permutation  # noqa: E402

    perm = stratum_permutation(A, S)
    cyc = cycle_type_of_permutation(perm)
    n = 3 * A
    y_vals = y_lambda_at(n, q_val)
    shapes = list(y_vals.keys())

    terms = []
    total = sp.Integer(0)
    for lam in shapes:
        y = y_vals[lam]
        chi = mn_character(lam, cyc)
        if chi == 0:
            continue
        contrib = y * chi
        total += contrib
        terms.append({
            "partition": lam,
            "weight": y,
            "character": chi,
            "contribution": contrib,
        })
    return total, terms


def global_wedderburn_sum_q_hecke_seminormal(
    Z: int,
    N: int,
    q_val: float,
    *,
    include_inter: bool = True,
    m_pp: int = 1,
    m_pn: int = 1,
    m_nn: int = 1,
) -> tuple[float, list[dict]]:
    """tr_M(β_atomic(Z, N)) = Σ_{λ ⊢ 3A} y_λ(q_0) · χ^λ_q(β) — exact form.

    **Closes the character gap** flagged in
    docs/audits/2026-05-08-q-hecke-character-gap-closure.md.

    Composes:
      - y_λ via Wenzl Schur principal specialization (numerical-q-from-start)
      - χ^λ_q via Hoefsmit seminormal matrices at q_val (numerical, float64)

    Drop-in replacement for the q=1-character-limited
    `global_wedderburn_sum_jones_markov` when consumers need the
    canonical Hecke character at q ≠ 1.  Numerically agrees with
    `markov_trace_recursive` (canonical Markov-axiom reducer) to
    1e-13 (proton/neutron, A=1) — 1e-10 (deuteron, A=2) relative;
    full-precision mpmath path lives on PR #564 as
    `rho_k_h3a_refinement.py` with 50-dps agreement at 1.4e-16.

    Returns (tr_M_value, per_partition_breakdown).
    """
    import numpy as np

    from hecke_characters import build_seminormal_matrices  # noqa: E402
    from mass_at_3A_proper import (  # noqa: E402
        atom_braid_word_3A,
        chi_lambda_of_word,
    )

    A = Z + N
    n = 3 * A
    word = atom_braid_word_3A(
        Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
        include_inter=include_inter,
    )
    y_vals = y_lambda_at(n, q_val=q_val)
    n_gens_required = n - 1

    # Validate that every braid-word generator is in range BEFORE the
    # per-partition loop.  Catching IndexError per-partition (and
    # silently skipping) would mask wiring bugs and give a wrong
    # `total` without any signal (copilot-pull-request-reviewer on PR
    # #572).  word entries are (c, d, gen_idx) tuples;
    # gen_idx must satisfy 0 ≤ gen_idx < n_gens_required to act on
    # the seminormal of any λ ⊢ n with full dimension.
    bad_gens = [g for *_, g in word
                if not (0 <= g < n_gens_required)]
    if bad_gens:
        raise ValueError(
            f"Braid word contains out-of-range generator indices "
            f"{sorted(set(bad_gens))} for n_gens_required = "
            f"{n_gens_required} (n = {n}).  This indicates a wiring "
            f"bug in atom_braid_word_3A or the caller; refusing to "
            f"silently drop partitions and return a wrong total."
        )

    rows = []
    total = 0.0
    for shape, y in y_vals.items():
        sigmas, dim, _syts = build_seminormal_matrices(shape, q=q_val)
        if dim == 0:
            continue
        # IndexError now propagates with context (no silent skip).
        chi = chi_lambda_of_word(sigmas, dim, word, n_gens_required)
        contrib = float(y) * float(chi)
        total += contrib
        rows.append({
            "partition": list(shape),
            "dim": int(dim),
            "y_at_q0": float(y),
            "chi_q_at_q0": float(chi),
            "contribution": float(contrib),
        })
    return total, rows


__all__ = [
    "y_lambda_at",
    "global_wedderburn_sum_jones_markov",
    "per_stratum_sum_jones_markov",
    "global_wedderburn_sum_q_hecke_seminormal",
]
