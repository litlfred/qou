"""qbeta_utils — shared numeric helpers for the Q_β c_k / Δτ_M probes.

Single source of truth for the small mathematical utilities reused across
the `qbeta_*` computation scripts, so the same closed form is not
re-typed (and silently diverged) in multiple probes.

Canonical provenance of each helper is cited inline. The Lean
formalisation is authoritative; these are the numeric (mpmath) mirrors.
"""
from __future__ import annotations

from mpmath import mpf, sqrt as mpsqrt, cos as mpcos, fabs as mpfabs


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


#: The variable the Q_β `c_k` rungs are currently expanded in.
#:
#: `"u"` — the committed frame, `u = b·ℏ_q²`.
#: `"h"` — the migration target, `h = q − 1/q` (bean `qou-cwin`).
#:
#: The two are NOT interchangeable labels for one ladder: `u ∼ h²`, so the
#: same function has different rungs in each, and `u → h` reversion needs
#: `√u`. A `c_k` value is meaningless without knowing which frame it is in —
#: which is the whole reason this constant exists rather than being implied.
LADDER_FRAME = "u"


def markov_parameter(q: mpf) -> mpf:
    """The Q_β channel's **convention-C** Markov parameter z(q) = √q/(1 + q).

    **NOT canonical.** This docstring read "the canonical Markov parameter"
    until 2026-08-16; convention C was excised by owner ruling 2026-08-09 and
    re-affirmed 2026-08-15, and the canonical parameter is D's q³/(q²+1).

    The value is deliberately still C and this function is deliberately not
    migrated: the registry records `channels.qbeta-decay` as
    `agreed-migration-pending` — convention settled to D, code not yet moved —
    and `evaluators.z` registers this symbol as C so that **R9 calls it and
    asserts z_C numerically on every validator run**. Flipping it before the
    ladder is re-derived would put the registry in contradiction with its own
    evaluator, and the re-derivation is bean `qou-cds1`, not a z-swap:
    `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` (sorry-free) proves the C-frame
    ladder and the two-row forcing are mutually exclusive.

    So "C" here is a recorded, gated state — not drift. What was wrong was
    calling it canonical, which is the label defect the C→D campaign kept
    finding: a description that outlived the ruling it predates.

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


# ── Q_β precision-ladder substrate quantities + empirical c_3 target ──
# These let any probe compute the CAL-anchored c_3 target at an ARBITRARY
# substrate q (not just the cached proton anchor), which is what the
# cross-anchor discrimination test needs.
#
# Canonical source of the inversion: `qbeta_ck_cache.py` (steps 1–3):
#   c_3(q) = (Q_codata / Q_N2(q) − 1) / u(q)^3
# with Q_codata the experimental (anchor-INDEPENDENT) neutron β-decay
# Q-value treated as the exact CAL-3 anchor, and
#   Q_N2(q) = m_e · Q_A(q) · cos(α(q) − b(q)·ℏ_q(q)²/2) · (1 + c_2·u(q)²),
#   c_2 = −1 (Lean-proved Taylor-exact).

def substrate_ladder_quantities(q: mpf) -> dict:
    """Return the Q_β-ladder substrate quantities at substrate value `q`.

    Keys: `h`, `hbar_q`, `b`, `u`, `z`, `alpha`, `Q_A_over_me`, `ladder_frame`.
    Mirrors the opening block of `qbeta_ck_cache.py::main`.

    `ladder_frame` names the variable the `c_k` rungs are expanded in. It is
    currently `"u"`, and it is emitted so that every witness built from these
    quantities can DECLARE its frame rather than leave a reader to infer it.

    Why the field exists (bean `qou-cwin`, T0). The owner authorised
    re-expressing the ladder in `h = q − 1/q` instead of `u = b·ℏ_q²`, which
    changes every `c_k` number. The convention C→D campaign taught what
    happens when artifacts do not declare their frame: PR #5210's own
    impact tool could only report *"0 of 12 declare `markov_convention`, so
    the count is a lower bound"* — a migration whose artifacts are silent
    about their frame cannot be measured, only guessed at. Measured here
    before any number moved: of 278 `c_k`-bearing witnesses under
    `computations/qbeta/`, **0** declared a frame.

    Adding this key is safe for the 102 in-repo consumers: none iterates the
    returned dict (checked by resolving each `x = substrate_ladder_quantities(...)`
    binding and searching for `x.items()` / `x.values()`), so a non-numeric
    value cannot reach arithmetic or a numeric serializer.

    Precondition: `q > 0` and `q ≠ 1`. At `q = 1` the substrate degenerates
    (`hbar_q = 0` ⇒ `u = 0`), which makes downstream consumers like
    `c3_target_at` divide by zero. Callers operating in the classical
    limit must guard `q = 1` themselves before calling.
    """
    sq = mpsqrt(q)
    h = q - 1 / q
    hbar_q = (q - 1) / q
    b = mpsqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar_q ** 2
    z = 1 / (sq + 1 / sq)
    alpha = (z - 1) * h / 2
    Q_A_over_me = mpfabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    return {
        "h": h, "hbar_q": hbar_q, "b": b, "u": u,
        "z": z, "alpha": alpha, "Q_A_over_me": Q_A_over_me,
        "ladder_frame": LADDER_FRAME,
    }


def c3_target_at(q: mpf, q_codata: mpf, m_e: mpf) -> mpf:
    """Empirical (CAL-anchored) c_3 target at substrate `q`.

    **Precondition: `q > 0` and `q ≠ 1`.** At the classical point `q = 1`
    the substrate quantity `u(q) = b(q)·ℏ_q(q)²` vanishes, and the ladder
    inversion divides by `u³`; calling with `q = 1` raises `ValueError`
    rather than the opaque `ZeroDivisionError` mpmath would otherwise
    surface. Substrate anchors (`q_proton`, `q_muon`) satisfy this by
    construction.

    Ladder inversion through the N=2 rung (c_2 = −1 Lean-proved):

        Q_A   = m_e · |q²−2q−1| · (q+1) / (2q³)
        Q_N1  = Q_A · cos(α − b·ℏ_q²/2)
        Q_N2  = Q_N1 · (1 + c_2·u²),   c_2 = −1
        c_3   = (Q_codata / Q_N2 − 1) / u³

    `q_codata` (the experimental neutron β-decay Q-value) is the SAME at
    every substrate anchor — it is a physical constant, not a function of
    q. Only the substrate quantities (Q_A, u, α, …) move with `q`, so the
    c_3 target genuinely differs between the proton and muon anchors. The
    cross-anchor swing of this target is the discriminator the f-map
    search uses to separate a true closure from a single-anchor near-match.
    """
    sub = substrate_ladder_quantities(q)
    if sub["u"] == 0:
        raise ValueError(
            f"c3_target_at: substrate u(q) = b·ℏ_q² is zero at q={q!s} "
            f"(classical limit). The inversion divides by u³; pass a "
            f"substrate anchor with q ≠ 1."
        )
    Q_A = m_e * sub["Q_A_over_me"]
    Q_N1 = Q_A * mpcos(sub["alpha"] - sub["b"] * sub["hbar_q"] ** 2 / 2)
    Q_N2 = Q_N1 * (1 + (-1) * sub["u"] ** 2)
    return (q_codata / Q_N2 - 1) / sub["u"] ** 3
