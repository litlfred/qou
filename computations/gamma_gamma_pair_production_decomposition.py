#!/usr/bin/env python3
"""
CLASS-A acknowledged-anchor (Workplan-0b): M_P_MEV_VALIDATION here is the
inverse TARGET — `linking_weight_exact_via_anchor` solves backward for the
linking weight that would make m_p hit CODATA ("what to hit"); no CODATA
value flows into a prediction. Verified 2026-06-17 (I11 adjudication).

gamma_gamma_pair_production_decomposition.py — γγ̄ pair-production
decomposition of the Borromean braid β_Bor at each Gröbner-Shirshov
filtration order, localising where the 2.89% VolDensity residual enters.

## The γγ̄ pair-production reading of β_Bor

The Borromean braid in H₃(q) is

    β_Bor = (σ₀ σ₁⁻¹)³

Each factor (σ₀ σ₁⁻¹) is a γγ̄ pair-production element:

  σ₀  = positive crossing on strands (0,1)  →  photon γ
  σ₁⁻¹ = negative crossing on strands (1,2) →  anti-photon γ̄

The product σ₀·σ₁⁻¹ creates a γγ̄ pair on overlapping strand pairs,
exactly the categorical analogue of a γγ → e⁺e⁻ QED vertex (with the
σ₀σ₁σ₀ = trefoil = e⁻ identification of the existing
`knot-operator-table.py`).  β_Bor is therefore THREE sequential γγ̄
pair-production events whose linking pattern is the Borromean
3-component link.

Scope note (2026-11-20). Owner ruling (bean qou-99qc, 2026-11-18, confirmed 2026-11-20):
def:photon is gamma(phi) = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^-1, so V = s0 s1^-1 is ONE
photon's fourth term, not a photon / anti-photon pair. beta_Bor = V^3 = gamma(0,0,qh) gamma(0,0,-q^-1 h),
TWO four-term photons (mass-theory/borromean-two-photon-factorisation; checked exactly in
probes/photon_chiral/photon_chiral_ports_probe.py section C). Every Markov-trace number below is a
property of the braid and does not move; only the event count reading (3 gamma-gammabar) is superseded.

## The GS filtration

Via the Hecke skein  σᵢ⁻¹ = σᵢ − h  (h = q − q⁻¹), the Borromean
word expands into a polynomial in {σ₀, σ₁} with coefficients in
ℤ[h].  The polynomial is naturally **graded by h-power**, which is
the Gröbner-Shirshov filtration order:

  h⁰ order: classical limit (q=1) — pure word count
  h² order: first Hecke-relation correction
  h⁴ order: second correction
  h⁶ order: third, …

Family A's PROVED categorical linking weight terminates exactly at h²:

  linking_weight_A(q) = 5/2 + (3/4) h²       (PROVED, Lean-formalised)

But the Markov-trace-via-Jones-polynomial route does NOT a priori
terminate at h².  Its higher-order h-coefficients are computable
directly from the Jones polynomial of 𝓑₃,

  V(𝓑₃, t) = −t⁻³ + 3t⁻² − 2t⁻¹ + 4 − 2t + 3t² − t³,  t = q²,

which converts to a Markov-trace expansion of all orders in h.

## Localising the 2.89% residual — CORRECTED FRAMING (2026-05-25)

The framework's open question (per [the canonical doc]
(../../docs/lambda-scale-absorbed-into-vol-density.md)) is **where
inside VolDensity the gap enters**.

**First-version (BUGGY) framing**: with the WRONG Markov-trace
normalisation `(q^{1/2} + q^{-1/2})² = q + 2 + q⁻¹` inherited from
`borromean_markov_trace_h2` in `_li_2_q_util.py`, the probe claimed
"92% at h² coefficient, 8% at h⁴+ truncation" and pointed at Reading-A
as the dominant fix.  This was wrong.

**Corrected framing** (with the Lean-proved standard normalisation
`[2]_q² = (q + q⁻¹)² = q² + 2 + q⁻²` from `BorromeanMarkovTrace.lean`):
the h² coefficient of `tr_M(β_Bor)` is EXACTLY ZERO (Lean-proved), and
the closed form is `(4 + h² − 3h⁴ − h⁶) / (h² + 4)`.

The interesting axis is now **Family A vs Jones**:

  • Family A (Wedderburn dim sum on H_4): `5/2 + (3/4) h²`
  • Jones (Lean-proved H_3 Markov trace via bridge):
    `5/2 + 0·h² − 3·h⁴ − (1/4)·h⁶ + (1/16)·h⁸ + …`
  • These are DIFFERENT theorems about DIFFERENT mathematical
    objects — both Lean-proved, both correct.

At q₀, Jones (Lean-correct) lands ~47% closer to the CODATA-anchor
target than Family A.  Which is the categorically-correct
`linking_weight` is the OPEN question — neither is fully right, and
the simple bridge `linking_weight = 5/2 + 4·(tr_M − 1)` is itself a
hack (it forces tr_M(q=1) = 1 to equal Family A's 5/2 by adding a
constant — not derived).

## Audit-only — does NOT consume CODATA literals as predictions

The CODATA m_p anchor is used here ONLY to back-out the
"categorically-exact" linking_weight target via mass-formula inversion
(`linking_weight_exact_via_anchor`).  That value is the reference;
the framework predictions (`linking_weight_family_a`,
`linking_weight_via_jones`) are derived independently and compared
to it.  No CODATA literal flows into a prediction.

## See also

- [`docs/lambda-scale-absorbed-into-vol-density.md`](../../docs/lambda-scale-absorbed-into-vol-density.md)
- [`computations/_li_2_q_util.py`](_li_2_q_util.py)
  (`per_knot_density_borromean`, `linking_weight_family_a`, `borromean_markov_trace_h2`)
- [`computations/knot-operator-table.py`](knot-operator-table.py)
  (γγ pair-production identification in NF basis)
- [`docs/audits/2026-05-23-yekutieli-bijection-natural-reading-negative.md`](../../docs/audits/2026-05-23-yekutieli-bijection-natural-reading-negative.md)
  (Reading-A vs Reading-B framing)

Ref: [adams1985] Vol(𝓑₃) = 8·G — Adams, "The Noncompact Hyperbolic
3-Manifold of Minimal Volume" (1987).
Ref: [kassel2008] Kassel & Turaev, "Braid Groups" §4.5 (Markov trace
via Jones polynomial).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as q0  # noqa: E402
from _li_2_q_util import linking_weight_family_a  # noqa: E402
from codata_constants import M_E_MEV, M_P_MEV_VALIDATION  # noqa: E402


# ── Borromean braid word in H₃(q) ──────────────────────────────
#
#   β_Bor = (σ₀ σ₁⁻¹)³
#
# Expansion via σᵢ⁻¹ = σᵢ − h gives a polynomial in {σ₀, σ₁}
# with coefficients in ℤ[h].  We work directly with the Jones
# polynomial of its closure, which is equivalent and cleaner.

BORROMEAN_BRAID_WORD = "(σ₀·σ₁⁻¹)³"
BORROMEAN_GAMMA_GAMMA_BAR_FACTORS = 3  # three V = σ₀σ₁⁻¹ letters (record reading: γγ̄ events)
BORROMEAN_FOUR_TERM_PHOTONS = 2  # V³ = γ(0,0,qh)·γ(0,0,−q⁻¹h) under def:photon (ruling 2026-11-18/20)


def jones_borromean(q):
    """Jones polynomial of the Borromean rings 𝓑₃ at t = q².

        V(𝓑₃, t) = −t⁻³ + 3t⁻² − 2t⁻¹ + 4 − 2t + 3t² − t³

    Ref: KnotInfo entry L6a4; Adams "The Knot Book" §6.1.
    """
    t = q ** 2
    t_inv = mpf(1) / t
    return (
        -t_inv ** 3
        + 3 * t_inv ** 2
        - 2 * t_inv
        + 4
        - 2 * t
        + 3 * t ** 2
        - t ** 3
    )


def markov_trace_borromean_via_jones(q):
    """Markov trace of β_Bor via its Jones polynomial.

    Convention matches the Lean-proved
    [`QOU.BraidsAndKnots.trM_borromean`](../../folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/BorromeanMarkovTrace.lean):
    normalize by `[2]_q² = (q + q⁻¹)² = q² + 2 + q⁻²`, which is the
    Kauffman–Jones standard `(t^{1/2} + t^{-1/2})^(n-1)` for n=3
    strands at t = q².

    CORRECTION (2026-05-25): an earlier version of this function (and
    the sibling `borromean_markov_trace_h2` in `_li_2_q_util.py`) used
    `(q^{1/2} + q^{-1/2})² = q + 2 + q⁻¹` — a NON-standard
    normalization that treats the substrate parameter `q` as the Jones
    variable `t` (not as q with t = q²).  This gave the WRONG h²
    coefficient (3/16 instead of the proved 0), inflating the apparent
    gap between Markov trace and Family A and leading to the bogus
    "92% at h²" gap localisation in the first version of this probe.

    With the correct Lean-aligned normalisation, the h² coefficient of
    tr_M(β_Bor) is EXACTLY ZERO (proved in
    `BorromeanMarkovTrace.lean §h2_coefficient_cancellation`), and the
    closed form is `(4 + h² − 3h⁴ − h⁶) / (h² + 4)`.

    Ref: [kassel2008] Kassel & Turaev, "Braid Groups" §4.5;
         Lean-proved `trM_borromean` closed form.
    """
    # convention D — verified by EVALUATION at q0, not by reading: computations/audits/borromean_convention_by_evaluation.py
    V_q = jones_borromean(q)
    norm = (q + mpf(1) / q) ** 2  # = [2]_q² (Kauffman-Jones standard)
    return V_q / norm


def linking_weight_via_jones(q):
    """linking_weight inferred from the Markov trace of β_Bor.

    Per [`borromean_markov_trace_h2`](_li_2_q_util.py) docstring,
    the canonical rescaling between tr_M(β_Bor, q) and the Family-A
    linking weight is

        linking_weight_jones(q) := 5/2 + 4 · (tr_M(β_Bor, q) − 1)

    This gives 5/2 + (3/4) h² at h² order, matching Family A
    exactly.  Higher h-orders are NOT a priori zero — they are
    what this probe extracts.
    """
    tr = markov_trace_borromean_via_jones(q)
    return mpf(5) / 2 + 4 * (tr - 1)


def linking_weight_exact_via_anchor(q):
    """The 'categorically-exact' linking weight that would make
    m_p match CODATA exactly.

        m_p = m_e · (Vol(𝓑₃)/ℏ_q²) · linking_weight_exact
      ⇒ linking_weight_exact = m_p_CODATA / (m_e · Vol(𝓑₃)/ℏ_q²)

    Used as the reference for "what we need to hit" — no CODATA value
    flows into a prediction, only into the target.
    """
    hbar_q = 1 - mpf(1) / q
    vol_b3 = 8 * mp.catalan
    geom_leading = vol_b3 / hbar_q ** 2
    return mpf(M_P_MEV_VALIDATION) / (mpf(M_E_MEV) * geom_leading)


def extract_h_polynomial_coefficients(func, max_order=10):
    """Extract the coefficients of func expanded in powers of h.

    Uses mpmath's `mp.taylor`, which is numerically stable and avoids
    the ill-conditioned Vandermonde system the earlier finite-difference
    sampling approach used (cond ≈ 10⁴⁸ for max_order=8 at eps=1e-6).

    h = q − q⁻¹  ⇒  q = (h + √(h² + 4)) / 2

    By bar-symmetry of the linking_weight under q ↔ q⁻¹ (i.e. h ↔ −h),
    only even-order coefficients are non-zero; we return just those.

    Returns [c_0, c_2, c_4, …, c_max_order].

    Ref: Gemini PR #1272 review (2026-05-25) — Vandermonde extraction
    was numerically ill-conditioned; switched to `mp.taylor`.
    """
    def g(h):
        # h can be complex (mpc) when mp.taylor evaluates off-axis.
        q_from_h = (h + mp.sqrt(h ** 2 + 4)) / 2
        return func(q_from_h)

    coeffs = mp.taylor(g, 0, max_order)
    return [coeffs[2 * k] for k in range(max_order // 2 + 1)]


def compare_at_h_order(coeffs_family_a, coeffs_jones, coeffs_exact):
    """Per even h-order, report Family-A vs Jones vs exact-anchor
    coefficients and the deltas.
    """
    rows = []
    for k in range(len(coeffs_family_a)):
        order = 2 * k
        c_fa = coeffs_family_a[k]
        c_jn = coeffs_jones[k]
        c_ex = coeffs_exact[k]
        rows.append(
            {
                "h_order": order,
                "family_a": mp.nstr(c_fa, 12),
                "jones": mp.nstr(c_jn, 12),
                "exact_anchor": mp.nstr(c_ex, 12),
                "delta_jones_vs_fa": mp.nstr(c_jn - c_fa, 12),
                "delta_exact_vs_fa": mp.nstr(c_ex - c_fa, 12),
                "delta_exact_vs_jones": mp.nstr(c_ex - c_jn, 12),
            }
        )
    return rows


def main():
    set_compute_dps()

    # Construct the witness builder early so `durationMs` covers the
    # full compute, not just the JSON-build step (copilot PR #1272 review).
    w = WitnessBuilder(
        "gamma-gamma-pair-production-decomposition",
        engine="mpmath",
    )
    w.set_audit_only("docs/audits/2026-05-25-non-abelian-stokes-reading-a-exploration.md")

    # ─── Step 1: point evaluation at q₀ ───────────────────────────
    q = q0
    fa_at_q0 = linking_weight_family_a(q)
    jn_at_q0 = linking_weight_via_jones(q)
    ex_at_q0 = linking_weight_exact_via_anchor(q)

    h0 = q - mpf(1) / q

    print("=" * 72)
    print("  γγ̄ pair-production decomposition of β_Bor")
    print(f"  q₀ = {mp.nstr(q, 12)}  h₀ = {mp.nstr(h0, 12)}")
    print("=" * 72)
    print()
    print(f"  V letters in β_Bor:     {BORROMEAN_GAMMA_GAMMA_BAR_FACTORS}")
    print(f"  four-term photons:      {BORROMEAN_FOUR_TERM_PHOTONS}  (V³ = γ₊γ₋, def:photon)")
    print(f"  Borromean braid word:   {BORROMEAN_BRAID_WORD}")
    print()
    print("  Point evaluations at q₀:")
    print(f"    linking_weight_family_a       = {mp.nstr(fa_at_q0, 14)}")
    print(f"    linking_weight_via_jones      = {mp.nstr(jn_at_q0, 14)}")
    print(f"    linking_weight_exact (anchor) = {mp.nstr(ex_at_q0, 14)}")
    print(f"    Δ (exact − family_a)         = {mp.nstr(ex_at_q0 - fa_at_q0, 14)}")
    print(f"    Δ (jones  − family_a)        = {mp.nstr(jn_at_q0 - fa_at_q0, 14)}")
    print(f"    Δ (exact  − jones)           = {mp.nstr(ex_at_q0 - jn_at_q0, 14)}")
    print()

    # ─── Step 2: per-h-order decomposition ─────────────────────────
    print("  Per-h-order coefficient extraction (Taylor in h around h=0):")
    print()
    max_order = 8  # extract through h⁸
    coeffs_fa = extract_h_polynomial_coefficients(linking_weight_family_a, max_order)
    coeffs_jn = extract_h_polynomial_coefficients(linking_weight_via_jones, max_order)
    # NOTE: exact_anchor diverges at h=0 (ℏ_q² → 0), so it has no
    # h-Taylor expansion.  Report it only as a POINT value at q₀.
    coeffs_ex = [mpf("nan")] * len(coeffs_fa)

    rows = compare_at_h_order(coeffs_fa, coeffs_jn, coeffs_ex)
    print(
        f"    {'h^k':>5s} | {'family_a':>16s} | {'jones':>16s} | "
        f"{'exact_anchor':>16s} | {'Δ(jn−fa)':>16s} | {'Δ(ex−fa)':>16s}"
    )
    print("    " + "-" * 110)
    for r in rows:
        print(
            f"    {('h^' + str(r['h_order'])):>5s} | "
            f"{r['family_a']:>16s} | {r['jones']:>16s} | "
            f"{r['exact_anchor']:>16s} | {r['delta_jones_vs_fa']:>16s} | "
            f"{r['delta_exact_vs_fa']:>16s}"
        )
    print()

    # ─── Step 3: write witness ─────────────────────────────────────
    w.set_description(
        "γγ̄ pair-production decomposition of β_Bor = (σ₀σ₁⁻¹)³ at "
        "each Gröbner-Shirshov filtration order (h-power).  Compares "
        "PROVED Family A linking_weight (which terminates at h²) "
        "against the Markov-trace-via-Jones-polynomial route (all "
        "orders in h) and against the CODATA-anchor target.  Localises "
        "whether the 2.89% VolDensity(𝓑₃) gap enters at h² (Reading-A "
        "hypothesis: +3/4 h² should be −G h²) or at h⁴⁺ (q-dilog tower "
        "hypothesis: Family A truncates higher-order corrections). "
        "Audit-only — no CODATA value flows into a prediction; the "
        "anchor inversion is for target reconstruction only."
    )
    w.add_parameter("q0", mp.nstr(q, 20))
    w.add_parameter("h0", mp.nstr(h0, 20))
    w.add_parameter("borromean_braid_word", BORROMEAN_BRAID_WORD)
    w.add_parameter("gamma_gamma_bar_factors", BORROMEAN_GAMMA_GAMMA_BAR_FACTORS)
    w.add_parameter("four_term_photons_in_beta_Bor", BORROMEAN_FOUR_TERM_PHOTONS)
    w.add_parameter("max_h_order", max_order)

    w.add_data("point_eval_at_q0", {
        "family_a": mp.nstr(fa_at_q0, 20),
        "via_jones": mp.nstr(jn_at_q0, 20),
        "exact_anchor": mp.nstr(ex_at_q0, 20),
        "delta_exact_minus_family_a": mp.nstr(ex_at_q0 - fa_at_q0, 20),
        "delta_jones_minus_family_a": mp.nstr(jn_at_q0 - fa_at_q0, 20),
        "delta_exact_minus_jones": mp.nstr(ex_at_q0 - jn_at_q0, 20),
    })
    w.add_data("h_order_decomposition", rows)

    # ─── Step 4: structural assertions ─────────────────────────────
    # A1: Family A and Jones DISAGREE at h² order — they are different
    # theorems about different objects (H_4 Wedderburn dim sum vs
    # H_3 Markov trace).  This is the CORRECTED finding (the earlier
    # version of this probe used a buggy Markov-trace normalisation
    # that made them appear to agree at h² — see Edit comment in
    # `markov_trace_borromean_via_jones`).
    delta_h2_jones_vs_fa = coeffs_jn[1] - coeffs_fa[1]
    w.add_assertion(
        name="family_a_disagrees_jones_at_h2_corrected",
        computed=mp.nstr(delta_h2_jones_vs_fa, 20),
        expected="-0.75",  # Family A: +3/4; Jones: 0  →  delta = -3/4
        tolerance=1e-12,
        source="With the CORRECT Kauffman-Jones normalisation [2]_q² = q² + 2 + q⁻² "
               "(matching `BorromeanMarkovTrace.lean § h2_coefficient_cancellation`), the "
               "h² coefficient of tr_M(β_Bor) is exactly ZERO.  Family A's +3/4 h² "
               "coefficient is a SEPARATE Wedderburn sum on H_4, not derivable from the "
               "H_3 Markov trace via the simple bridge linking_weight = 5/2 + 4·(tr_M − 1). "
               "The two are different mathematical objects.",
    )

    # A2: Family A is zero at h⁴⁺ (terminates at h²).
    fa_max_higher = max(abs(coeffs_fa[k]) for k in range(2, len(coeffs_fa)))
    w.add_assertion(
        name="family_a_terminates_at_h2",
        computed=mp.nstr(fa_max_higher, 20),
        expected="0",
        tolerance=1e-12,
        source="Family A linking_weight = (1/4)·Σ_{λ⊢4} dim_q V_λ = 5/2 + (3/4) h² "
               "terminates exactly at h² (Lean-proved in lambda-scale-substrate-form.lean).",
    )

    # A3: Jones polynomial has non-zero h⁴⁺ corrections.
    jn_max_higher = max(abs(coeffs_jn[k]) for k in range(2, len(coeffs_jn)))
    # Compare the magnitude of Jones h⁴-coefficient to a structural
    # threshold (1.0); we expect it ≈ 3.03 which exceeds 1 → "Jones has
    # real higher-order correction".
    jones_h4_minus_threshold = jn_max_higher - mpf(1)
    w.add_assertion(
        name="jones_has_h4_or_higher_correction_above_unit_threshold",
        computed=float(jones_h4_minus_threshold > 0),
        expected=1.0,
        tolerance=1e-12,
        source="Jones polynomial V(𝓑₃, q²) is degree-3 in q²; its expansion in h "
               "necessarily has terms beyond h².  Max |c_{2k>2}| ≈ 3.03 (the h⁴ "
               "coefficient).  Pass iff |c_{h⁴}| > 1.",
    )

    # A4: CORRECTED gap localisation — Family A vs Lean-correct Jones
    # vs CODATA target.  With the right normalisation, the picture is
    # FUNDAMENTALLY DIFFERENT than the buggy first version: Jones (Lean-
    # correct) already lands closer to the target than Family A, so the
    # interesting axis is "which route should be canonical", not "where
    # in h does the gap concentrate".
    point_gap_exact_minus_fa = ex_at_q0 - fa_at_q0       # signed
    point_gap_exact_minus_jones = ex_at_q0 - jn_at_q0    # signed
    fa_residual_abs = abs(point_gap_exact_minus_fa)
    jones_residual_abs = abs(point_gap_exact_minus_jones)
    fraction_of_fa_gap_closed_by_jones = (
        (fa_residual_abs - jones_residual_abs) / fa_residual_abs
        if fa_residual_abs > 0
        else mpf(0)
    )

    w.add_data("gap_localisation", {
        "family_a_at_q0": mp.nstr(fa_at_q0, 20),
        "jones_at_q0_lean_correct": mp.nstr(jn_at_q0, 20),
        "codata_anchor_target": mp.nstr(ex_at_q0, 20),
        "family_a_residual_signed": mp.nstr(point_gap_exact_minus_fa, 20),
        "jones_residual_signed": mp.nstr(point_gap_exact_minus_jones, 20),
        "family_a_residual_abs": mp.nstr(fa_residual_abs, 20),
        "jones_residual_abs": mp.nstr(jones_residual_abs, 20),
        "fraction_of_fa_gap_closed_by_jones": mp.nstr(fraction_of_fa_gap_closed_by_jones * 100, 8),
        "interpretation": (
            "Family A (Wedderburn dim sum on H_4) and Jones (H_3 Markov trace of "
            "β_Bor, Lean-proved closed form via [2]_q² normalisation) DISAGREE at h² "
            "coefficient: Family A's +3/4 vs Jones's 0.  Both are independently Lean-"
            "proved theorems about DIFFERENT mathematical objects.  Numerically, the "
            "Lean-correct Jones value lands ~47% closer to the CODATA-anchor target "
            "than Family A — suggesting the actual `linking_weight` may be the H_3 "
            "Markov trace, not the H_4 Wedderburn dim sum.  Open question: which is "
            "the categorically-correct `linking_weight`?  The simple bridge "
            "`linking_weight = 5/2 + 4·(tr_M − 1)` is itself a hack (forces tr_M(q=1)"
            "=1 to equal Family A's 5/2 by adding a constant)."
        ),
    })

    # Flag-style assertion: confirm Jones lands closer to target than Family A.
    jones_beats_family_a = float(jones_residual_abs < fa_residual_abs)
    w.add_assertion(
        name="jones_closer_to_target_than_family_a",
        computed=jones_beats_family_a,
        expected=1.0,
        tolerance=1e-12,
        source=(
            f"Lean-correct Jones gives |residual| = {mp.nstr(jones_residual_abs, 6)}, "
            f"Family A gives |residual| = {mp.nstr(fa_residual_abs, 6)}.  Jones closes "
            f"{mp.nstr(fraction_of_fa_gap_closed_by_jones * 100, 4)}% of Family A's "
            f"residual at q₀.  This re-opens the question of which "
            f"linking_weight is categorically correct."
        ),
    )

    out_path = w.save()
    print(f"  Witness: {out_path}")


if __name__ == "__main__":
    main()
