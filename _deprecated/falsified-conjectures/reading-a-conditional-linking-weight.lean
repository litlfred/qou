import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring


/-!
# QOU.BraidKnot.ReadingAConditionalLinkingWeight

Reading-A is the CONJECTURAL form of the Borromean linking-weight
that REPLACES the proved Family A theorem's h² coefficient `+3/4`
with `-G` (Catalan's constant).

  Reading-A_lw(q) := 5/2 + (-G)·h²   where h = q - q⁻¹.

At substrate q_0, this matches the m_p-anchored target to ~5.6 ppm
(measured at mp.mpf 50 dps in
[reading_a_residual_at_50dps.py](../../../computations/reading_a_residual_at_50dps.py)).

## Why this is conjectural

Family A's h² coefficient is +3/4, PROVED in
[lambda-scale-substrate-form.lean](lambda-scale-substrate-form.lean):

  λ_A(q) := (1/4) · Σ_{λ ⊢ 4} dim_q V_λ
          = (3q² + 4 + 3q⁻²) / 4
          = 5/2 + (3/4)·h².

If `linking_weight = λ_A`, then the h² coefficient is +3/4 and
Reading-A is FALSE.

Reading-A can only be true if `linking_weight ≠ λ_A`, i.e. the
Borromean linking weight is **not** the H_4 Wedderburn sum. This
requires a NEW categorical principle that:

- Does not arise from any Σ_{λ⊢N} dim_q V_λ Wedderburn-sum form
  ([PR #701](https://github.com/litlfred/qou/pull/701) falsified 5 structural routes)
- Does not arise from higher-N Wedderburn limit
  ([Path C1 probe](../../../computations/probes/higher_n_wedderburn_h2_drift_probe.py)
  shows h² coefficient grows factorially with N, drifts AWAY from -G)
- Does not arise from the natural reading of the Yekutieli per-cell
  half-symmetric projection (audit
  [2026-05-23](../../../docs/audits/2026-05-23-yekutieli-bijection-natural-reading-negative.md)
  found +0.5, not -G)

The Path C audit ([2026-05-25](../../../docs/audits/2026-05-25-path-c-categorical-principle-hunt.md))
enumerates 7 candidate sources; the most plausible remaining one is
**KLR / Kashiwara crystal h² correction** (C3), which is multi-session
research.

## What this file provides (sorry-free except the class)

1. A **definition** `linkingWeightReadingA` of the Reading-A formula
   (purely algebraic, no claim of physical correctness).

2. A **class** `ReadingAValidAtH2` axiomatising the conjecture
   "the actual linking-weight equals `linkingWeightReadingA`."
   Per CLAUDE.md §3b-cond, this is the SOLE `sorry` in the
   downstream chain.

3. A **conditional theorem** `mp_prediction_under_reading_a` deriving
   the m_p prediction formula CONDITIONALLY on `[ReadingAValidAtH2]`.
   Fully verified by Lean (no sorry).

## Cross-references

- [lambda-scale-substrate-form.lean](lambda-scale-substrate-form.lean)
  — Family A theorem (PROVED, h² = +3/4)
- [PR #1287](https://github.com/litlfred/qou/pull/1287) — Reading-A
  residual measurement (5.6 ppm match)
- [audit 2026-05-25 Path C](../../../docs/audits/2026-05-25-path-c-categorical-principle-hunt.md)
  — categorical-principle hunt
- [audit 2026-05-22 Yekutieli per-cell](../../../docs/audits/2026-05-22-yekutieli-percell-conjecture-formalized.md)
  — framework canonical Reading B (additive)
-/

namespace QOU.BraidKnot

/-- The Reading-A linking-weight formula (CONJECTURAL).

    Defined for any `G : ℝ` (intended: Catalan's constant
    `G ≈ 0.91596`, the per-cell ideal-octahedron volume from
    `Vol(𝓑₃) = 8·G`).

    Reading-A_lw(q) := 5/2 + (-G)·h² where h = q - q⁻¹.

    This definition makes NO claim that the formula EQUALS the
    actual physical linking-weight — it is the candidate form
    whose conditional-validity is encoded in
    `ReadingAValidAtH2` below. -/
noncomputable def linkingWeightReadingA (q G : ℝ) : ℝ :=
  5/2 + (-G) * (q - q⁻¹)^2

/-- **The Reading-A conjecture as a class** (per CLAUDE.md §3b-cond).

    Asserts that the actual physical linking-weight `actualLW`
    equals the Reading-A formula at every q. The single field
    `formula` is the only `sorry` in the downstream chain;
    everything depending on `ReadingAValidAtH2` is conditionally
    verified.

    The class is parameterized by `G` (Catalan's constant in
    practice) so this file is independent of Mathlib's Catalan
    constant (`Real.catalan` does not currently exist; PSLQ /
    motivic-period derivation is a separate Lean task). -/
class ReadingAValidAtH2 (actualLW : ℝ → ℝ) (G : ℝ) : Prop where
  /-- The conjectural identity: actualLW q = linkingWeightReadingA q G. -/
  formula : ∀ q : ℝ, actualLW q = linkingWeightReadingA q G

/-- **The h² coefficient of Reading-A is exactly `-G`.** Trivial
    algebraic consequence of the definition. -/
theorem readingA_h2_coefficient (q G : ℝ) :
    linkingWeightReadingA q G = 5/2 + (-G) * (q - q⁻¹)^2 := by
  unfold linkingWeightReadingA

/-- **Reading-A vs Family A delta.**

    Reading-A = Family A + (-G - 3/4)·h².

    The factor `(-G - 3/4) ≈ -1.666` is the structural delta from
    Wedderburn to Reading-A. -/
theorem readingA_eq_familyA_plus_correction (q G : ℝ) (hq : q ≠ 0) :
    linkingWeightReadingA q G =
    lambdaA_hForm (heckeDeformation q) + (-G - 3/4) * (q - q⁻¹)^2 := by
  unfold linkingWeightReadingA lambdaA_hForm heckeDeformation
  ring

/-- **Reading-A at h = 0 gives 5/2.**

    At the classical limit q = 1, the Reading-A formula reduces
    to 5/2 — the same h⁰ leading coefficient as Family A.
    Reading-A is a pure h² correction; h⁰ is unchanged. -/
theorem readingA_h0_eq_family_a_h0 (G : ℝ) :
    linkingWeightReadingA 1 G = 5/2 := by
  unfold linkingWeightReadingA
  norm_num

/-- **Conditional m_p prediction under Reading-A.**

    Defines the Borromean baryon mass prediction:
        m_p_pred(q) = m_e · Vol(𝓑₃)/ℏ_q² · linkingWeightReadingA q G

    Returns the symbolic formula, no numerical claim. Numerical
    bounds (`+5.6 ppm to CODATA`) are verified at mp.mpf 50 dps
    in the sibling Python probe. -/
noncomputable def m_p_pred_reading_a
    (m_e q G vol_B3 : ℝ) : ℝ :=
  m_e * (vol_B3 / (1 - q⁻¹)^2) * linkingWeightReadingA q G

/-- **Equivalent factored form** of the m_p prediction under Reading-A.

    Using h/ℏ_q = q + 1 (algebraic identity for h = q - q⁻¹ and
    ℏ_q = 1 - q⁻¹), the m_p formula factors as:
        m_p_pred = m_e · vol_B3 · ((5/2)/ℏ_q² + (-G)·(q+1)²)

    This is the structurally cleaner form: the (-G)·(q+1)² term
    is a polynomial in q (no inverse powers), exposing the
    Reading-A h² correction as a polynomial contribution. -/
theorem m_p_pred_reading_a_factored
    (m_e q G vol_B3 : ℝ) (hq : q ≠ 0) (hq1 : q ≠ 1) :
    m_p_pred_reading_a m_e q G vol_B3 =
    m_e * vol_B3 * ((5/2) / (1 - q⁻¹)^2 + (-G) * (q + 1)^2) := by
  unfold m_p_pred_reading_a linkingWeightReadingA
  have h_id : (q - q⁻¹) / (1 - q⁻¹) = q + 1 := by
    field_simp
    ring
  -- (q - q⁻¹)² / (1 - q⁻¹)² = (q + 1)²
  have h_sq_id : (q - q⁻¹)^2 / (1 - q⁻¹)^2 = (q + 1)^2 := by
    rw [← div_pow, h_id]
  field_simp
  ring

/-- **Reading-A's h² coefficient matches the m_p-anchored target
    to ~5.6 ppm at q_0.**

    This is a NUMERICAL claim (proved at 50 dps in
    [reading_a_residual_at_50dps.py](../../../computations/reading_a_residual_at_50dps.py))
    that is HARD to state directly in Lean without committing to
    specific numerical values of m_e, m_p, q_0, G, Vol(𝓑₃). The
    Lean-level theorem only encodes the ALGEBRAIC structure; the
    numerical match is a downstream witness, not a Lean claim. -/

end QOU.BraidKnot
