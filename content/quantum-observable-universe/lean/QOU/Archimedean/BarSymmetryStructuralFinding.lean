import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import QOU.Archimedean.LinkingWeightSubstrateBounds
import QOU.Archimedean.BringColorTubeQForm

/-!
# Bar-symmetry structural finding (PROVED)

Formalises the structural finding from
[`folio-assistant/computations/bar_symmetry_three_candidates.py`](../../../../../folio-assistant/computations/bar_symmetry_three_candidates.py):

**The Bring color-tube candidate breaks bar-symmetry** under
q ↔ q⁻¹, while Family A and via-Jones (Markov trace) are
bar-symmetric.

## The bar-involution principle

For categorical objects in the Hecke / quantum-group setting, the
bar involution `q ↔ q⁻¹` is a natural symmetry. Per the cheat sheet
§4 "Φ_q (Faddeev) vs Li_2^q (Rogers) — context sorting":

- Φ_q (Faddeev): bar-ASYMMETRIC (mass-anchor side)
- Li_2^q (Rogers): bar-SYMMETRIC (binding context side)

For linking_weight in the mass chain, both bar-symmetric (Family A,
via-Jones) and bar-asymmetric (Bring color-tube) forms are
candidates. The bar-symmetry property is an additional structural
axis of distinctness.

## Status

PROVED sorry-free at the substrate q₀ rational literal: Bring
color-tube takes different values at q₀ and at q₀⁻¹, confirming
bar-asymmetry numerically.

## References

- [`bar_symmetry_three_candidates.py`](../../../../../folio-assistant/computations/bar_symmetry_three_candidates.py) — numerical probe
- [`docs/canonical-derivation-cheat-sheet.md`](../../../../../docs/canonical-derivation-cheat-sheet.md) §4 — Φ_q vs Li_2^q
- `lambda-scale-substrate-form.lean § lambdaA_q_inv_symmetric` —
  Family A's bar-symmetry is already PROVED in the Lean tree
-/

namespace QOU.Archimedean

open Real

/-! ## §1  Family A is bar-symmetric (restatement)

The theorem `lambdaA_q_inv_symmetric` in
`lambda-scale-substrate-form.lean` proves `lambdaA(q) = lambdaA(q⁻¹)`
for nonzero q. We restate the substrate-specific corollary here. -/

/-- Family A evaluated at q₀ equals Family A evaluated at q₀⁻¹.
    Provable via the q ↔ q⁻¹ symmetry of `(3q² + 4 + 3q⁻²)/4`. -/
theorem familyA_at_q_0_eq_at_q_0_inv :
    (3 * q_0_substrate ^ 2 + 4 + 3 * q_0_substrate ^ (-2 : ℤ)) / 4
      = (3 * (1 / q_0_substrate) ^ 2 + 4 + 3 * (1 / q_0_substrate) ^ (-2 : ℤ)) / 4 := by
  have hq : q_0_substrate ≠ 0 := q_0_substrate_ne_zero
  have h_inv_ne : (1 / q_0_substrate) ≠ 0 := one_div_ne_zero hq
  rw [show ((1 / q_0_substrate) ^ (-2 : ℤ) : ℝ) = q_0_substrate ^ 2 by
    rw [zpow_neg, zpow_two]
    field_simp]
  rw [show ((1 / q_0_substrate) ^ 2 : ℝ) = q_0_substrate ^ (-2 : ℤ) by
    rw [zpow_neg, zpow_two]
    field_simp]
  ring

/-! ## §2  Bring color-tube is bar-asymmetric (PROVED) -/

/-- **Bring color-tube breaks bar-symmetry at q₀** (PROVED).

    `bringColorTube q_0` and `bringColorTube (1/q_0)` take materially
    different values:
      - bringColorTube(q_0) ≈ 2.460
      - bringColorTube(1/q_0) ≈ 0.931
      - |difference| ≈ 1.529 ≫ 0

    The q^{10} factor in `1/(1 − (q − q⁻¹) · q^{10})` is the
    asymmetry source. Under q ↔ q⁻¹:
      - h_q = q − q⁻¹ → −h_q
      - q^{10} → q^{−10}
      - product h·q^{10} → −h·q^{−10} (NOT just sign-flipped)

    Hence the denominator changes shape, and the function value
    differs.

    Proof: numerical bound separation. We show
      bringColorTube q_0 > 2.45  AND  bringColorTube (1/q_0) < 1.0
    so they cannot be equal. The bounds are proved via `norm_num`
    on the rational q₀ literal. -/
theorem bringColorTube_breaks_bar_symmetry_at_q_0 :
    bringColorTube q_0_substrate ≠ bringColorTube (1 / q_0_substrate) := by
  -- Strategy: bringColorTube(q_0) > 2 and bringColorTube(1/q_0) < 1.5,
  -- so they cannot be equal.
  intro heq
  -- Show bringColorTube q_0 > 2.45 (existing theorem reused from §4 bring_term_at_q_0_bound)
  have hq : q_0_substrate ≠ 0 := q_0_substrate_ne_zero
  have hb_q_0 : bringColorTube q_0_substrate
              = 1 / bringColorTubeDen q_0_substrate := by
    exact bringColorTube_q_form q_0_substrate hq bringColorTubeDen_at_q_0_ne_zero
  -- At q_0_substrate^-1, bringColorTubeDen = 1 + (1/q_0)^9 - (1/q_0)^11
  -- Numerically: 1 + (0.901)^9 - (0.901)^11 = 1 + 0.387 - 0.314 = 1.073
  -- So bringColorTube(1/q_0) = 1/1.073 ≈ 0.932
  have hbi_pos : bringColorTubeDen (1 / q_0_substrate) > 0 := by
    unfold bringColorTubeDen q_0_substrate
    norm_num
  have hbi_ne : bringColorTubeDen (1 / q_0_substrate) ≠ 0 := ne_of_gt hbi_pos
  have h_inv_ne : (1 / q_0_substrate) ≠ 0 :=
    one_div_ne_zero hq
  have hb_q_inv : bringColorTube (1 / q_0_substrate)
                = 1 / bringColorTubeDen (1 / q_0_substrate) := by
    exact bringColorTube_q_form (1 / q_0_substrate) h_inv_ne hbi_ne
  -- bringColorTube q_0 > 2.45 (from §4)
  have ⟨h_b_lo, _⟩ := bring_term_at_q_0_bound
  rw [← hb_q_0] at h_b_lo  -- now: bringColorTube q_0 > 245/100
  -- bringColorTube (1/q_0) < 1.5
  have h_bi_hi : bringColorTube (1 / q_0_substrate) < 15 / 10 := by
    rw [hb_q_inv]
    rw [div_lt_iff hbi_pos]
    unfold bringColorTubeDen q_0_substrate
    norm_num
  -- Apply heq to derive contradiction
  rw [heq] at h_b_lo
  linarith

/-! ## §3  Combined Bring + Faddeev h⁴ is bar-asymmetric (corollary)

Since Faddeev h⁴ is bar-symmetric (h⁴ is even) but Bring is not,
the combined `Bring + Faddeev h⁴ − 1` inherits Bring's asymmetry. -/

/-- Faddeev h⁴ is bar-symmetric (it depends on h only through h⁴,
    and h → −h flips sign but h⁴ is even). -/
theorem faddeevH4_bar_symmetric (q : ℝ) (hq : q ≠ 0) :
    faddeevH4 q = faddeevH4 (1 / q) := by
  unfold faddeevH4 heckeH
  -- (q - q⁻¹)⁴ = (q⁻¹ - q)⁴  (4th power is sign-insensitive)
  have h_inv_q_ne : (1 / q) ≠ 0 := one_div_ne_zero hq
  congr 1
  congr 1
  ring

/-- The combined `linkingWeightBringFaddeevH4 = bring + faddeev − 1`
    inherits Bring's bar-asymmetry: it breaks bar-symmetry at q₀. -/
theorem linkingWeightBringFaddeevH4_breaks_bar_symmetry_at_q_0 :
    linkingWeightBringFaddeevH4 q_0_substrate
      ≠ linkingWeightBringFaddeevH4 (1 / q_0_substrate) := by
  intro heq
  -- Unfold: bring + faddeev - 1 = bring' + faddeev' - 1
  -- ⇒ bring + faddeev = bring' + faddeev'
  -- Since faddeev = faddeev' (bar-symmetric), ⇒ bring = bring'
  -- But that contradicts bringColorTube_breaks_bar_symmetry_at_q_0.
  have hq : q_0_substrate ≠ 0 := q_0_substrate_ne_zero
  have h_faddeev_eq : faddeevH4 q_0_substrate = faddeevH4 (1 / q_0_substrate) :=
    faddeevH4_bar_symmetric q_0_substrate hq
  -- Manipulate to extract bring = bring' contradiction
  unfold linkingWeightBringFaddeevH4 at heq
  have h_bring_eq :
      bringColorTube q_0_substrate = bringColorTube (1 / q_0_substrate) := by
    linarith
  exact bringColorTube_breaks_bar_symmetry_at_q_0 h_bring_eq

/-! ## §4  Honest-accounting summary

PROVED (sorry-free) in this file:
  ✓ familyA_at_q_0_eq_at_q_0_inv (Family A bar-symmetric)
  ✓ bringColorTube_breaks_bar_symmetry_at_q_0 (Bring breaks)
  ✓ faddeevH4_bar_symmetric (Faddeev preserves)
  ✓ linkingWeightBringFaddeevH4_breaks_bar_symmetry_at_q_0 (combined breaks)

Structural implication: the Bring + Faddeev h⁴ candidate occupies a
DIFFERENT bar-symmetry class than Family A and via-Jones. Per the
cheat sheet §4 framing, mass-anchor compute (Φ_q side) is allowed
to be bar-asymmetric, but the established linking_weight candidates
(Family A, via-Jones) are bar-symmetric. So the Bring + Faddeev h⁴
candidate introduces NEW bar-asymmetry that neither established
candidate carries.

This does NOT directly disqualify Bring + Faddeev h⁴, but it
weakens the case for canonicity: the +108 ppm m_p match relies on
the q^{10} asymmetry, and a bar-symmetric variant
(`(bring(q) + bring(q⁻¹))/2`) loses the match by ~30%.

Per Rule 14: the categorical proof of additive composition would
need to either:
  (a) explain WHY bar-asymmetric forms are canonical for the
      linking_weight in the mass chain, OR
  (b) replace Bring color-tube with a bar-symmetric variant
      (e.g. (1/(1-h·q^10) + 1/(1+h·q^-10))/2 — but this loses
      the numerical match at q_0).

The bar-symmetric variant would lose the 108 ppm match but be
structurally cleaner. The asymmetric variant has the numerical
match but is structurally weaker.
-/

end QOU.Archimedean
