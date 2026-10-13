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

Per-irrep mpf Hoefsmit at q_0, at `max(mp.dps, COMPUTE_DPS)`; no float64 on the path:
  - `atom_braid_word_3A(..., q=q)` → braid word, at the same mpf q
  - reverse-word ++ original = V2 composite word (β · β_mirror⁻¹)
  - per λ ⊢ 3A with y_λ ≠ 0: `build_seminormal_matrices_mp` +
    `_chi_of_word_structured_mp`
  - `mp.fsum` of `y_λ(q_0) · χ^λ_q`

Cached via `@lru_cache` on (Z, N, exact mpf q, dps).

## API

  `aK_v2(Z, N, q_val=Q_0)` → `mp.mpf` value of a_K
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

from q_parameter import Q_MP as Q_0_MP  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from hecke_characters import build_seminormal_matrices_mp  # noqa: E402
from _precision import COMPUTE_DPS  # noqa: E402
# Imported HERE, not inside the cached kernel: `y_lambda_su_n` calls
# `set_compute_dps(50)` at import, which REASSIGNS the global `mp.dps`. Done
# inside the kernel's `mp.workdps(dps)` block, that silently dropped the rest of
# the block to 50 digits (measured: a_K moved at the 51st digit). At module
# scope the side effect lands exactly where the old lazy import inside
# `y_lambda_at` put it — on the first a_K call — so callers see no change in
# global state; the kernel itself is protected by its own workdps and by the
# dps assertion before the final sum.
from y_lambda_su_n import y_lambda_su_n  # noqa: E402


def v2_composite_word(beta_word):
    """Word representing β · β_mirror⁻¹ under V2.

    For pure-crossing atom braids ((1, 0) = σ_i and (1, -h) = σ_i⁻¹),
    β_mirror⁻¹ = reverse-word(β) — derived in
    `probe_term5_aK_v2_mirror_chirality.py` docstring.
    """
    return list(beta_word) + list(reversed(beta_word))


@lru_cache(maxsize=128)
def _aK_v2_cached(Z: int, N: int, q_key: tuple, dps: int) -> tuple:
    """Internal cache, keyed on (Z, N, q as its exact mpf tuple, dps).

    NO FLOAT64 (bean-less precision fix, 2026-10-13). This kernel used to key
    on `float(q)`, build the seminormal matrices at that float, run the
    character through the float64 `chi_lambda_of_word`, and accumulate
    `float(y) * float(chi)` — so every a_K reaching the 50-dps mass formula
    carried ~16 good digits and the six-term sweep witness padded them out to
    60 (the float64-padding ratchet's ~45 rows). It now carries `mpf` end to
    end:

      * q is the caller's mpf (default `q_parameter.Q_MP`, the same pin the
        sweep evaluates its other terms at) — never rounded to a double;
      * the word is built at that SAME q (it was built at the 50-digit
        default while the matrices were built at the float, a precision
        straddle inside one quantity);
      * y_λ comes from `y_lambda_su_n(n, q, 2)` (convention D, the function
        `y_lambda_at`'s numeric branch calls) without the 50-digit
        `sp.Float` rendering `y_lambda_at` applies on the way out;
      * the matrices are the exact `build_seminormal_matrices_mp` twin, and
        χ is formed by `_chi_of_word_structured_mp` below.

    Shapes with y_λ == 0 contribute exactly 0. Under convention D that is
    every λ with more than two rows (`schur_principal` picks up `[0]_q = 0`
    exactly), so χ is not evaluated there: the sum is unchanged, and it is
    what keeps n = 12 (⁴He) affordable in mpf — 7 nonzero blocks, largest
    dim 297, instead of 77 blocks up to dim 7700. Their rows record
    `chi_v2_at_q0 = None`.

    The whole body runs in `mp.workdps(dps)` so a cached mpf never inherits
    whatever ambient precision the first caller happened to be at.
    """
    with mp.workdps(dps):
        q = mp.make_mpf(q_key)
        A = Z + N
        n = 3 * A
        beta_word = atom_braid_word_3A(Z, N, include_inter=True, q=q)
        composite = v2_composite_word(beta_word)
        n_gens = n - 1

        bad = [g for *_, g in composite if not (0 <= g < n_gens)]
        if bad:
            raise ValueError(
                f"V2 composite word out-of-range generators {sorted(set(bad))} "
                f"for n_gens = {n_gens} (Z={Z}, N={N})"
            )

        y_vals = y_lambda_su_n(n, q, 2)
        t0 = time.perf_counter()
        terms = []
        rows = []
        for shape, y in y_vals.items():
            if y == 0:
                rows.append({
                    "partition": list(shape),
                    "dim": None,
                    "y_at_q0": mp.mpf(0),
                    "chi_v2_at_q0": None,
                    "contribution": mp.mpf(0),
                })
                continue
            sigmas, dim, _syts = build_seminormal_matrices_mp(shape, q)
            if dim == 0:
                continue
            chi = _chi_of_word_structured_mp(sigmas, dim, composite)
            contrib = y * chi
            terms.append(contrib)
            rows.append({
                "partition": list(shape),
                "dim": int(dim),
                "y_at_q0": y,
                "chi_v2_at_q0": chi,
                "contribution": contrib,
            })
        if mp.mp.dps != dps:
            raise RuntimeError(
                f"aK_v2: working precision changed under the kernel "
                f"({dps} -> {mp.mp.dps}); a callee reassigned the global mp.dps"
            )
        total = mp.fsum(terms)
        elapsed_s = time.perf_counter() - t0
    return (total, len(rows), elapsed_s, tuple(rows))


def _chi_of_word_structured_mp(sigmas, dim, word):
    """`tr(Π_k (c_k·σ_{g_k} + d_k·I))` in mpf, O(|word|·dim²).

    mpf twin of `mass_at_3A_proper._chi_of_word_structured` (which is float64
    by contract). A Hoefsmit seminormal generator is diagonal plus at most one
    off-diagonal entry per column, so each column of the running product is
    rescaled and picks up exactly one other column per letter. The structure
    is CHECKED per generator, not assumed; a violation raises rather than
    silently dropping a term.
    """
    split = []
    for S in sigmas:
        diag = [S[i, i] for i in range(dim)]
        off = []
        seen_cols = set()
        for i in range(dim):
            for j in range(dim):
                if i != j and S[i, j] != 0:
                    if j in seen_cols:
                        raise ValueError(
                            "seminormal generator has two off-diagonal "
                            "entries in one column; structured mpf character "
                            "path does not apply"
                        )
                    seen_cols.add(j)
                    off.append((i, j, S[i, j]))
        split.append((diag, off))

    # PT[j] is column j of the running product (start: identity).
    PT = [[mp.mpf(1) if r == c else mp.mpf(0) for c in range(dim)]
          for r in range(dim)]
    for (c, d, g) in word:
        c = mp.mpf(c)
        d = mp.mpf(d)
        diag, off = split[g]
        tmp = [(j, [x * (c * v) for x in PT[i]]) for (i, j, v) in off]
        for j in range(dim):
            s = d + c * diag[j]
            PT[j] = [x * s for x in PT[j]]
        for j, row in tmp:
            PT[j] = [a + b for a, b in zip(PT[j], row)]
    return mp.fsum(PT[j][j] for j in range(dim))


def _resolve_q(q_val) -> "mp.mpf":
    """The caller's q as an mpf; a Python float is refused (NO FLOAT64)."""
    if q_val is None:
        return Q_0_MP
    if isinstance(q_val, float):
        raise TypeError(
            f"aK_v2: q is a Python float ({q_val!r}), which caps a_K at ~16 "
            f"digits. Pass an mpf or a decimal string (default: "
            f"q_parameter.Q_MP)."
        )
    return q_val if isinstance(q_val, mp.mpf) else mp.mpf(str(q_val))


def _cache_args(Z: int, N: int, q_val) -> tuple:
    dps = max(mp.mp.dps, COMPUTE_DPS)
    q = _resolve_q(q_val)
    # Key on the mpf's exact binary representation, so the cache can never
    # conflate two q's that agree to 16 digits (it used to key on float(q)).
    return (Z, N, q._mpf_, dps)


def aK_v2(Z: int, N: int, q_val=None):
    """Canonical V2 chirality factor a_K(Z, N) at substrate q.

    Returns an `mp.mpf` computed in mpf end to end at
    `max(mp.dps, COMPUTE_DPS)`, and returned AT that precision: it is not
    re-rounded to the caller's ambient dps (which is 50 in any process that
    has imported `y_lambda_su_n`). Serialize it with `_precision.fmt`.
    """
    total, _, _, _ = _aK_v2_cached(*_cache_args(Z, N, q_val))
    return total


def aK_v2_full(Z: int, N: int, q_val=None) -> dict:
    """Full V2 a_K record: value + per-partition breakdown + timing.

    Every numeric field is an `mp.mpf` (or `None` for a χ not evaluated
    because its weight is exactly zero); serialize with `_precision.fmt`.
    """
    total, n_part, elapsed, rows = _aK_v2_cached(*_cache_args(Z, N, q_val))
    return {
        "aK_value": total,
        "n_partitions": n_part,
        "elapsed_s": elapsed,
        "rows": [dict(r) for r in rows],
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
