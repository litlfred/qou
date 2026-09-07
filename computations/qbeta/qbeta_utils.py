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
# Closed forms formalised as `chi_block_{3,21,111}` in
# `QOU/BraidKnot/QBetaPerBlockChiClosedForms.lean`, which is authoritative.
# (3) and (1,1,1) are from `qbeta-per-block-paper-closed-forms.witness.json`;
# (2,1) is from `qbeta_per_block_chi_borromean_closed_forms_probe.py`.
#
# INTRA-NUCLEON ORDERING (beans qou-hu1f / qou-eddc, 2026-09-05..07)
# ------------------------------------------------------------------
# Exactly one of the three blocks depends on the order in which the two nucleon
# strands are braided, and it is the only 2-dimensional one. (3) and (1,1,1)
# are 1-dimensional, so their generators act by scalars and commute; sympy
# confirms their two frames differ by exactly 0, not merely by something small.
# (2,1) is where σ₀ and σ₁ genuinely do not commute, and it moves.
#
# The canonical word is borromean, `(σ₀σ₁⁻¹)³`. The superseded grouped word
# (all σ₀, then all σ₁) is reachable via `intra_order="grouped"` so historical
# comparisons stay reproducible — do not delete it, and do not flip a caller
# that is deliberately pinned to it.

_VALID_ORDERS = ("borromean", "grouped")


def _check_order(intra_order: str) -> str:
    if intra_order not in _VALID_ORDERS:
        raise ValueError(
            f"intra_order must be one of {_VALID_ORDERS}, got {intra_order!r}")
    return intra_order


def chi_block_3(q: mpf) -> mpf:
    """χ_(3)(q) = -(q²-1)(q²+1)² / (4q).  Ordering-independent (dim 1)."""
    return -(q ** 2 - 1) * (q ** 2 + 1) ** 2 / (4 * q)


def chi_block_21(q: mpf, *, intra_order: str = "borromean") -> mpf:
    """χ_(2,1)(q), the one ordering-dependent block (dim 2).

    borromean (canonical):
        (q²-1)(q⁴+1)·P(q) / (4q⁹),
        P = 2q¹²-5q¹⁰+5q⁸-5q⁶+5q⁴-5q²+2
    grouped (superseded):
        (q²-1)(-q⁴-1) / (4q³)

    The two agree at q = 1 (`P(1) = -1`, both vanish), both carry the (q²-1)
    factor, and both are odd in h = q - 1/q with the same -h/2 leading term.
    They differ from the h³ term on.
    """
    if _check_order(intra_order) == "grouped":
        return (q ** 2 - 1) * (-(q ** 4) - 1) / (4 * q ** 3)
    P = (2 * q ** 12 - 5 * q ** 10 + 5 * q ** 8 - 5 * q ** 6
         + 5 * q ** 4 - 5 * q ** 2 + 2)
    return (q ** 2 - 1) * (q ** 4 + 1) * P / (4 * q ** 9)


def chi_block_111(q: mpf) -> mpf:
    """χ_(1,1,1)(q) = -(q²-1)(q²+1)² / (4q⁵).  Ordering-independent (dim 1)."""
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


def markov_parameter_convention_C(q: mpf) -> mpf:
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

    SYMBOLIC q IS SUPPORTED (added 2026-08-30, qou-t9r1). Until then this was
    mpmath-only -- `mpsqrt` raises `TypeError: cannot create mpf from q` on a
    sympy Symbol -- so every SYMBOLIC consumer needing the C arm had to inline
    `sqrt(q)/(1+q)`, which is precisely the invisibility the guard above exists
    to prevent. The guard had a type hole exactly the size of its own purpose.
    Measured instance: `probes/qbeta_fmap_power_class_prune.py` inlined it to
    build the Lean-defined `CanonicalMarkovWeightsH3.explicitInstance`, whose
    definition legitimately fixes z = sqrt(q)/(1+q); the site was correct and
    ungreppable. Taxonomy row 21.
    """
    # NOTE the NON-EMPTY test. `hasattr(q, "free_symbols")` is also True for
    # sympy NUMERICS -- Rational(1,2) and Float(1.11) both carry the attribute
    # with an EMPTY set -- so the bare hasattr routed numeric callers into the
    # symbolic branch and handed them a sympy expression where they asked for a
    # number. Measured; and mpmath accepts both (mpsqrt(Rational(1,2)) ->
    # 0.471404520791032), so the numeric arm is the correct destination for
    # them. Caught by Copilot on PR #6058.
    if getattr(q, "free_symbols", None):   # genuinely symbolic sympy Expr
        import sympy as _sp
        return _sp.sqrt(q) / (1 + q)
    return mpsqrt(q) / (1 + q)


def delta_tau_M_surrogate(q: mpf, *, intra_order: str = "borromean") -> mpf:
    """Rational Δτ_M surrogate (NON-canonical y_λ weights).

    Closed form (canonical source: Lean `delta_tau_M_surrogate` in
    `QOU/BraidKnot/QBetaPerBlockChiClosedForms.lean`, Extension #1;
    originally from `qbeta_c3_multiblock_recursion_attack.py`):

    borromean (canonical, matches Lean since 2026-09-07):

        Δτ_M_sur(q) =
          (2q¹⁷ - 2q¹⁶ - 5q¹⁵ + 4q¹⁴ + 8q¹³ - 9q¹² - 8q¹¹ + 9q¹⁰ + 11q⁹
           - 11q⁸ - 9q⁷ + 8q⁶ + 9q⁵ - 8q⁴ - 4q³ + 5q² + 2q - 2)
          / (4 q⁸ (q² + q + 1))

    grouped (superseded, what this returned before 2026-09-07):

        Δτ_M_sur(q) =
          (-q¹¹ + q¹⁰ - 2q⁹ + q⁸ + q⁶ - q⁵ - q³ + 2q² - q + 1)
          / (4 q⁵ (q² + q + 1))

    Both are the y_λ-weighted sum of the three blocks, differing only through
    χ_(2,1); Taylor coefficients at q = 1 agree at orders 0-2 and diverge at 3.

    This uses the rational dimension-shape surrogate for the Wenzl
    y_λ weights (y_λ = q^ℓ(λ) / ((1+q)(1+q+q²))), NOT the canonical
    √q-bearing weights. Retained for the cross-anchor NEAR-MATCH
    diagnostic only.
    """
    if _check_order(intra_order) == "grouped":
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
        return num / (4 * q ** 5 * (q ** 2 + q + 1))
    num = (
        2 * q ** 17 - 2 * q ** 16 - 5 * q ** 15 + 4 * q ** 14 + 8 * q ** 13
        - 9 * q ** 12 - 8 * q ** 11 + 9 * q ** 10 + 11 * q ** 9 - 11 * q ** 8
        - 9 * q ** 7 + 8 * q ** 6 + 9 * q ** 5 - 8 * q ** 4 - 4 * q ** 3
        + 5 * q ** 2 + 2 * q - 2
    )
    return num / (4 * q ** 8 * (q ** 2 + q + 1))


def delta_tau_M_canonical_explicit(
        q: mpf, *, intra_order: str = "borromean") -> mpf:
    """Canonical Δτ_M evaluated at the EXPLICIT √q-bearing instance of
    `CanonicalMarkovWeightsH3` (Lean `CanonicalMarkovWeightsH3.explicitInstance`):

        y_(3) = z,  y_(2,1) = 1/2 - z,  y_(1,1,1) = z,   z = √q/(1+q)

    so Δτ_M_can(q) = z·χ_(3) + (1/2 - z)·χ_(2,1) + z·χ_(1,1,1).

    NOTE: the explicit instance is one valid inhabitant of the class,
    NOT THE canonical Wenzl–Markov instance (which is open math). See
    `QBetaCanonicalMarkovWeightsInstance.lean`.
    """
    z = markov_parameter_convention_C(q)
    return (
        z * chi_block_3(q)
        + (mpf("0.5") - z) * chi_block_21(q, intra_order=intra_order)
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


class _ConventionGuardedQuantities(dict):
    """Ladder quantities whose CONVENTION-CARRYING keys must be asked for.

    `h`, `hbar_q`, `b`, `u`, `Q_A_over_me` are convention-free and are always
    present -- measured 2026-08-26: 35 of the 48 in-repo consumers use only
    those, and they are untouched by this guard.

    `z` and `alpha` are the ONLY places a Markov convention enters the entire
    Q_beta ladder, so they are withheld unless the caller names a convention.
    Convention C was excised by owner ruling (2026-08-09, re-affirmed
    2026-08-15 and 2026-08-26); the point of this guard is that nobody can
    pick up a C `z` from this helper WITHOUT SAYING SO. A consumer that needs
    the C arm for a deliberate comparison passes `convention="C"` and is then
    visible to `grep`, which an inline `sqrt(q)/(1+q)` never was.

    Raises on the withheld keys rather than returning None, because a silent
    `None` reaching mpmath arithmetic is exactly the failure mode this exists
    to prevent.
    """

    _WITHHELD = ("z", "alpha")

    def __missing__(self, key):
        if key in self._WITHHELD:
            raise KeyError(
                f"{key!r} withheld: it carries the Markov convention, and this "
                "helper will not hand one out unnamed. Call "
                "substrate_ladder_quantities(q, convention='D') for the "
                "canonical parameter, or convention='C' for the EXCISED "
                "convention -- permitted only as a deliberate comparison arm, "
                "and registered as such in "
                "docs/coordination/trace-convention-registry.json. "
                "Under D the c_k ladder is NOT derived (bean qou-cds1): "
                "substituting z_D into alpha = (z-1)h/2 is proved invalid by "
                "QOU.QBeta.decayLadder_zC_threeRow_ne_zero and "
                "QOU.QBeta.eigenphase_bar_defect_of_fullBar."
            )
        raise KeyError(key)

    def get(self, key, default=None):
        # Override so a withheld key cannot be swallowed into a silent None.
        if key in self._WITHHELD and key not in self:
            return self[key]          # -> __missing__, raises
        return super().get(key, default)


def substrate_ladder_quantities(q: mpf, *, convention: str | None = None) -> dict:
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
    # DELIBERATELY convention C, exactly as `markov_parameter` above — see its
    # docstring for the full reason. Restated HERE because this is a SECOND,
    # independent inline spelling of the same value: a reader who arrives at
    # this function alone sees a bare C `z` with no note, and the standing
    # instruction is to migrate C to D. Doing that here would be WRONG.
    # `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` makes the C-frame ladder and
    # the mass channel's three-row forcing mutually exclusive, so substituting
    # z_D into this ladder is not a valid move — the ladder must be RE-DERIVED
    # (bean `qou-cds1`), which is research, not cleanup.
    #
    # Not replaced by a call to `markov_parameter(q)` either, tempting as that
    # is for keeping one documented site: the two spellings are algebraically
    # equal but NOT bit-equal — `1/(√q + 1/√q)` against `√q/(1+q)` differ by
    # 1.6e-61 relative at 60 dps — and this is the one ladder that must not be
    # perturbed by a substitution, however small.
    Q_A_over_me = mpfabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    out = _ConventionGuardedQuantities(
        h=h, hbar_q=hbar_q, b=b, u=u,
        Q_A_over_me=Q_A_over_me, ladder_frame=LADDER_FRAME,
    )
    if convention is None:
        return out                      # z / alpha withheld; see the guard
    if convention == "C":
        # EXCISED convention, reachable only by asking for it BY NAME. The two
        # spellings are algebraically equal but NOT bit-equal -- `1/(√q + 1/√q)`
        # against `√q/(1+q)` differ by 1.6e-61 relative at 60 dps -- and this is
        # the one ladder that must not be perturbed by a substitution, however
        # small, so the original spelling is kept verbatim.
        z = 1 / (sq + 1 / sq)
    elif convention == "D":
        z = q ** 3 / (q ** 2 + 1)
    else:
        raise ValueError(
            f"unknown Markov convention {convention!r}; expected 'C' or 'D'")
    out["z"] = z
    out["alpha"] = (z - 1) * h / 2
    out["markov_convention"] = convention
    return out


def c3_target_at(q: mpf, q_codata: mpf, m_e: mpf, *,
                 convention: str = "C") -> mpf:
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
    # Defaults to the EXCISED convention C so every committed c_3 target this
    # helper has produced stays reproducible to the digit. It is NOT a
    # recommendation: under D no ladder is derived (qou-cds1), so there is no
    # D-frame c_3 target to default to. Named explicitly rather than inherited
    # silently, which is the whole point of the guard above.
    sub = substrate_ladder_quantities(q, convention=convention)
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
