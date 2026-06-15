"""Canonical V2 mirror-chirality factor a_K for use across compute infra.

Single source of truth for Term 5 chirality in the 6-term mass
formula.  Replaces the production heuristic `term5_chirality(Z, N,
chirality_signs)` which computed Π (1 + sign · h) over a hand-coded
sign pattern from `chirality_signs_for_isotope(iso)`.

## Why V2

The Gram-matrix conjecture (`conj:knot-factor-frobenius-pairing`):
`a_K = G_{β, β*} / G_{1, 1} = τ(β · β*⁻¹)`. Under V2 (β* = β_mirror,
geometric mirror knot: each crossing flipped), this is

  a_K = τ(β · β_mirror⁻¹).

The legacy slow audit's V1 = β⁻¹ (multiplicative inverse) gives
`τ(β · β⁻¹) = τ(1_n)` which depends only on strand count, NOT the
braid — informationless. V2 is the canonical chirality measure.

## Compute path

Per-irrep numeric Hoefsmit at q_0 via
`global_wedderburn_sum_q_hecke_seminormal` infrastructure:
  - `atom_braid_word_3A` → braid word
  - reverse-word ++ original = V2 composite word (β · β_mirror⁻¹)
  - per λ ⊢ 3A: `build_seminormal_matrices` + `chi_lambda_of_word`
  - sum `Σ_λ y_λ(q_0) · χ^λ_q`

Cached via `@lru_cache` on (Z, N, q_val) — sub-second per atom on
cache miss, instant on hit.

## API

  `aK_v2(Z, N, q_val=Q_0)` → mpmath-compatible value of a_K
  `aK_v2_full(Z, N, q_val=Q_0)` → dict with per-partition breakdown

Both callable from any compute script.  No state, no I/O.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from functools import lru_cache
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from q_parameter import Q as Q_0_FLOAT  # noqa: E402
from mass_at_3A_proper import (  # noqa: E402
    atom_braid_word_3A,
    chi_lambda_of_word,
)
from hecke_characters import build_seminormal_matrices  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402


def v2_composite_word(beta_word):
    """Word representing β · β_mirror⁻¹ under V2.

    For pure-crossing atom braids ((1, 0) = σ_i and (1, -h) = σ_i⁻¹),
    β_mirror⁻¹ = reverse-word(β) — derived in
    `probe_term5_aK_v2_mirror_chirality.py` docstring.
    """
    return list(beta_word) + list(reversed(beta_word))


@lru_cache(maxsize=128)
def _aK_v2_cached(Z: int, N: int, q_val_float: float) -> tuple:
    """Internal cache key on (Z, N, q_val rounded to float64).

    Returns (aK_float, n_partitions, elapsed_s, rows_tuple).
    """
    A = Z + N
    n = 3 * A
    beta_word = atom_braid_word_3A(Z, N, include_inter=True)
    composite = v2_composite_word(beta_word)
    n_gens = n - 1

    bad = [g for *_, g in composite if not (0 <= g < n_gens)]
    if bad:
        raise ValueError(
            f"V2 composite word out-of-range generators {sorted(set(bad))} "
            f"for n_gens = {n_gens} (Z={Z}, N={N})"
        )

    y_vals = y_lambda_at(n, q_val=q_val_float)
    t0 = time.perf_counter()
    total = 0.0
    rows = []
    for shape, y in y_vals.items():
        sigmas, dim, _syts = build_seminormal_matrices(shape, q=q_val_float)
        if dim == 0:
            continue
        chi = chi_lambda_of_word(sigmas, dim, composite, n_gens)
        contrib = float(y) * float(chi)
        total += contrib
        rows.append({
            "partition": list(shape),
            "dim": int(dim),
            "y_at_q0": float(y),
            "chi_v2_at_q0": float(chi),
            "contribution": float(contrib),
        })
    elapsed_s = time.perf_counter() - t0
    return (float(total), len(rows), elapsed_s, tuple(rows))


def aK_v2(Z: int, N: int, q_val=None):
    """Canonical V2 chirality factor a_K(Z, N) at substrate q.

    Returns mpmath `mp.mpf` for use in 50-dps mass-formula paths.
    Caches per (Z, N) keyed on float64-rounded q.
    """
    qf = float(q_val) if q_val is not None else float(Q_0_FLOAT)
    aK_f, _, _, _ = _aK_v2_cached(Z, N, qf)
    return mp.mpf(aK_f)


def aK_v2_full(Z: int, N: int, q_val=None) -> dict:
    """Full V2 a_K record: value + per-partition breakdown + timing.

    Useful for witness emission and inspection.
    """
    qf = float(q_val) if q_val is not None else float(Q_0_FLOAT)
    aK_f, n_part, elapsed, rows = _aK_v2_cached(Z, N, qf)
    return {
        "aK_value": aK_f,
        "n_partitions": n_part,
        "elapsed_s": elapsed,
        "rows": list(rows),
    }


def term5_v2_factor(Z: int, N: int, q_val=None):
    """Drop-in replacement for `paper_six_term_isotope_sweep.term5_chirality`.

    Returns the V2 a_K as an `mp.mpf`. Same return shape as the
    legacy closed form; callers consume the value directly.
    """
    return aK_v2(Z, N, q_val=q_val)


__all__ = [
    "v2_composite_word",
    "aK_v2",
    "aK_v2_full",
    "term5_v2_factor",
]
