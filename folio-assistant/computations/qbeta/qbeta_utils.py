"""qbeta_utils — shared numeric helpers for the Q_β c_k / Δτ_M probes.

Single source of truth for the small mathematical utilities reused across
the `qbeta_*` computation scripts, so the same closed form is not
re-typed (and silently diverged) in multiple probes.

Canonical provenance of each helper is cited inline. The Lean
formalisation is authoritative; these are the numeric (mpmath) mirrors.
"""
from __future__ import annotations

from mpmath import mpf, sqrt as mpsqrt


# ── Per-Wedderburn-block characters χ_λ(Δ_T_β)(q) over H_3(q) ──
# Closed forms from `qbeta-per-block-paper-closed-forms.witness.json`,
# formalised as `chi_block_{3,21,111}` in
# `QOU/BraidKnot/QBetaPerBlockChiClosedForms.lean`.

def chi_block_3(q: mpf) -> mpf:
    """χ_(3)(q) = -(q²-1)(q²+1)² / (4q)."""
    return -(q ** 2 - 1) * (q ** 2 + 1) ** 2 / (4 * q)


def chi_block_21(q: mpf) -> mpf:
    """χ_(2,1)(q) = (q²-1)(-q⁴-1) / (4q³)."""
    return (q ** 2 - 1) * (-(q ** 4) - 1) / (4 * q ** 3)


def chi_block_111(q: mpf) -> mpf:
    """χ_(1,1,1)(q) = -(q²-1)(q²+1)² / (4q⁵)."""
    return -(q ** 2 - 1) * (q ** 2 + 1) ** 2 / (4 * q ** 5)


def markov_parameter(q: mpf) -> mpf:
    """The canonical Markov parameter z(q) = √q / (1 + q).

    Mirrors `markov_parameter` in
    `QOU/BraidKnot/QBetaPerBlockChiClosedForms.lean`.
    """
    return mpsqrt(q) / (1 + q)


def delta_tau_M_surrogate(q: mpf) -> mpf:
    """Rational Δτ_M surrogate (NON-canonical y_λ weights).

    Closed form (canonical source: Lean `delta_tau_M_surrogate` in
    `QOU/BraidKnot/QBetaPerBlockChiClosedForms.lean`, Extension #1;
    originally from `qbeta_c3_multiblock_recursion_attack.py`):

        Δτ_M_sur(q) =
          (-q¹¹ + q¹⁰ - 2q⁹ + q⁸ + q⁶ - q⁵ - q³ + 2q² - q + 1)
          / (4 q⁵ (q² + q + 1))

    This uses the rational dimension-shape surrogate for the Wenzl
    y_λ weights (y_λ = q^ℓ(λ) / ((1+q)(1+q+q²))), NOT the canonical
    √q-bearing weights. Retained for the cross-anchor NEAR-MATCH
    diagnostic only.
    """
    num = (
        -(q ** 11)
        + q ** 10
        - 2 * q ** 9
        + q ** 8
        + q ** 6
        - q ** 5
        - q ** 3
        + 2 * q ** 2
        - q
        + 1
    )
    den = 4 * q ** 5 * (q ** 2 + q + 1)
    return num / den


def delta_tau_M_canonical_explicit(q: mpf) -> mpf:
    """Canonical Δτ_M evaluated at the EXPLICIT √q-bearing instance of
    `CanonicalMarkovWeightsH3` (Lean `CanonicalMarkovWeightsH3.explicitInstance`):

        y_(3) = z,  y_(2,1) = 1/2 - z,  y_(1,1,1) = z,   z = √q/(1+q)

    so Δτ_M_can(q) = z·χ_(3) + (1/2 - z)·χ_(2,1) + z·χ_(1,1,1).

    NOTE: the explicit instance is one valid inhabitant of the class,
    NOT THE canonical Wenzl–Markov instance (which is open math). See
    `QBetaCanonicalMarkovWeightsInstance.lean`.
    """
    z = markov_parameter(q)
    return (
        z * chi_block_3(q)
        + (mpf("0.5") - z) * chi_block_21(q)
        + z * chi_block_111(q)
    )
