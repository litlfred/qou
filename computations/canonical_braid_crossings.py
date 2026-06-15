#!/usr/bin/env python3
"""
canonical_braid_crossings.py — bridge `atom_braid_word_3A` →
`(gen_idx, ctype)` format for `chi_lambda_symbolic` consumers.

Generalises the `deuteron_canonical_crossings` helper from PR #564's
`rho_k_h3a_refinement.py` to arbitrary `(Z, N)`.  Replaces all
calls to the **legacy** `hecke_character_symbolic.atomic_braid_to_crossings`
(which uses a non-canonical disjoint-product convention; per the
P3' canonical word fix on PR #564 commit c068550c, the canonical
convention is `mass_at_3A_proper.atom_braid_word_3A` with the
operator-valued interface `I = σ_{n_1} − h/2 · 1`).

The conversion classifies each `(c, d, gen_idx)` triple by `d`:

    d = 0        →  ctype = "sigma"     (positive crossing σ_g)
    d = −h       →  ctype = "sigma_inv" (negative crossing σ_g⁻¹;
                                         from σ² = h·σ + 1 ⇒ σ⁻¹ = σ − h)
    d = −h/2     →  ctype = "averaged"  (interface σ_g − h/2 · 1)

All three are the canonical Hecke-algebra building blocks consumed
by `hoefsmit_symbolic.chi_lambda_symbolic` and
`hecke_character_symbolic.q_character_on_braid_word`.

References:
- PR #546 (`hoefsmit_symbolic.py`) — closed-form symbolic χ^λ
- PR #564 commit c068550c — canonical-word fix on rho_k_h3a_refinement.py
- prop:hecke-branching-trace-decomposition (operator-valued interface)
- prop:q-hecke-seminormal-character-closure (this PR's closure)

@module folio-assistant/computations/canonical_braid_crossings
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


_AVG_COLOR_DELTA = None  # cached δ = flavor_split_subleading(q₀)


def _avg_color_delta():
    """Substrate flavor split δ = (m_n − m_p)/M_N at q₀ as an **mp.mpf**
    (full precision), for the color-weighted averaged p-n crossing
    `−h·(1/2 − δ/4)`. Lazy + cached; the **single source of δ** for the whole
    braid pipeline (mass_at_3A_proper, chi_lambda_numerical, marshalling).
    Float-context callers wrap with `float()`; mpmath callers use it directly
    so the high-dps paths keep full precision."""
    global _AVG_COLOR_DELTA
    if _AVG_COLOR_DELTA is None:
        import mpmath as _mp
        from _li_2_q_util import flavor_split_subleading
        from q_parameter import Q as _Q0
        _AVG_COLOR_DELTA = flavor_split_subleading(_mp.mpf(str(_Q0)))  # mp.mpf
    return _AVG_COLOR_DELTA


def classify_crossing(
    c: float, d: float, h_val: float, *, context: str | None = None,
) -> str:
    """Classify a `(c, d)` Hecke-algebra crossing pair into a ctype
    `{sigma, sigma_inv, averaged}` against the substrate `h = q - q⁻¹`.

    Shared utility for downstream consumers (canonical braid crossings,
    Wenzl LR convention adapter, Rust binary wrappers). Centralises
    the tolerance constants so any future refinement is reflected
    everywhere.

    `context` is an optional string appended to error messages so
    call-site debugging (e.g. "atom (Z, N) = (2, 2) gen 5") survives
    the wrapping. The helper itself does no parsing of the context.
    """
    suffix = f" [{context}]" if context else ""
    if abs(c - 1.0) > 1e-12:
        raise ValueError(
            f"Unexpected coefficient c={c} (expected 1){suffix}"
        )
    if abs(d) < 1e-12:
        return "sigma"
    if abs(d - (-h_val)) < 1e-9:
        return "sigma_inv"
    # "averaged" p-n interface: color-blind −h/2, OR color-weighted
    # −h·(1/2 − δ/4) (bring_color_weighted default, mass_at_3A_proper).
    delta = float(_avg_color_delta())                # float-context comparison
    if (abs(d - (-h_val / 2.0)) < 1e-9
            or abs(d - (-h_val * (0.5 - delta / 4.0))) < 1e-9):
        return "averaged"
    raise ValueError(
        f"Unrecognised crossing (c, d)=({c}, {d}); expected d ∈ "
        f"{{0, -h, -h/2, -h·(1/2-δ/4)}} with h≈{h_val:.6f}, "
        f"δ≈{delta:.6e}{suffix}"
    )


def atom_canonical_crossings(
    Z: int, N: int,
    *,
    include_inter: bool = True,
    m_pp: int = 1, m_pn: int = 1, m_nn: int = 1,
) -> list[tuple[int, str]]:
    """Canonical (gen_idx, ctype) crossings for atomic braid β(Z, N).

    Source of truth: `mass_at_3A_proper.atom_braid_word_3A(Z, N)`.

    Returns a list of `(gen_idx, ctype)` pairs consumable by
    `hoefsmit_symbolic.chi_lambda_symbolic` and
    `hecke_character_symbolic.q_character_on_braid_word`.

    Replaces the legacy `hecke_character_symbolic.atomic_braid_to_crossings`,
    which used a disjoint-product convention not matching the
    canonical Markov-axiom reducer.
    """
    from mass_at_3A_proper import atom_braid_word_3A
    from hecke_core import h as h_val  # numeric h = q_0 − q_0⁻¹

    triples = atom_braid_word_3A(
        Z, N,
        m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
        include_inter=include_inter,
    )
    out: list[tuple[int, str]] = []
    for run_idx, (c, d, g) in enumerate(triples):
        ctx = f"atom_canonical_crossings(Z={Z}, N={N}) gen={int(g)} run={run_idx}"
        out.append((int(g), classify_crossing(
            float(c), float(d), h_val, context=ctx,
        )))
    return out


__all__ = ["atom_canonical_crossings", "classify_crossing"]
