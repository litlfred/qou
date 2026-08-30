/-
# Step 2 over `𝓞 K`, assembled: the two embedding bounds meet the vanishing criterion

`RothAlgebraicInteger` left step 2's `𝓞 K` entry point, `le_index_of_norm_lt`, taking its
per-embedding smallness as a hypothesis, and supplied the two estimates that discharge it — the
Taylor bound at `φ₀` and the plain height budget at the other `d−1` conjugates.  This file puts
them together, so step 2 over `𝓞 K` runs from step 1's output to an index lower bound with only a
numeric inequality left over.

## The asymmetry is the content

`eq_zero_of_norm_mul_pow_lt_one` needs `‖φ₀ x‖ · M^{d−1} < 1`, so the two estimates enter the
final inequality *differently*: the `φ₀` bound linearly, the conjugate bound raised to the
`d−1`.  That is why `conjBound` is worth naming — it is multiplied by itself `d−1` times, so a
factor wasted there costs `d−1` times as much as one wasted at `φ₀`, and the two should not be
tuned as if they were interchangeable.

Over `ℤ` there is no such asymmetry, because `d = 1` and the whole `M^{d−1}` factor is `1`.  The
`ℤ` statement is the degenerate case of this one, which is a fact about the shape and not a route
to deriving one from the other — the vanishing criteria are genuinely different theorems.

## What is still a hypothesis, and where it goes

`hfinal`.  Exactly as in the `ℤ` chain, and for the same reason: it is a comparison of explicit
constants, and discharging it belongs with the parameter record that `RothNormalisation` handles
for the `ℤ` side.  Nothing else remains between step 1's auxiliary polynomial and a lower bound on
the index at the rational point.
-/
import QOU.Mathlib.RothAlgebraicInteger
import QOU.Mathlib.RothContradiction

open NumberField Finset

namespace MvPolynomial

variable {K : Type*} [Field K] [NumberField K] {m : ℕ}

/-- **The bound each of the `d−1` other conjugates contributes**, already scaled by the
denominator `∏ q_h^{r_h}`.  Named because `eq_zero_of_norm_mul_pow_lt_one` raises it to the
`d−1`, so slack here is `d−1` times as expensive as slack at `φ₀`. -/
noncomputable def conjBound (r qd : Fin m → ℕ) (H B' : ℝ) : ℝ :=
  ((∏ h, (qd h) ^ (r h) : ℕ) : ℝ)
    * (((∏ h, (r h + 1) : ℕ) : ℝ) * (H * (2 * B') ^ (∑ h, r h)))

/-- **Step 2 over `𝓞 K`, assembled.**  Step 1's index at `α` (`hidx`) plus the approximation
quality (`hγ`, `hS`) give a lower bound on the index at the rational point, with only the numeric
comparison `hfinal` left over.

`hidx` is load-bearing: it is what restricts the sum in the `φ₀` estimate.  An earlier draft of
this arc considered taking the smallness directly as a hypothesis, which would have made this
argument independent of step 1 — true, and missing the auxiliary polynomial's entire purpose. -/
theorem le_index_of_taylor_house (r : Fin m → ℕ)
    (pn : Fin m → ℤ) (qd : Fin m → ℕ) (hq : ∀ h, qd h ≠ 0)
    (P : MvPolynomial (Fin m) (𝓞 K)) (hdeg : ∀ h, degreeOf h P ≤ r h)
    (α : Fin m → 𝓞 K) (φ₀ : K →+* ℂ)
    {H B B' : ℝ} (hB1 : 1 ≤ B) (hB1' : 1 ≤ B')
    (hH : ∀ k, house ((algebraMap (𝓞 K) K) (coeff k P)) ≤ H)
    (hα : ∀ h, house ((algebraMap (𝓞 K) K) (α h)) ≤ B)
    (hβ : ∀ h, ‖((((pn h : ℚ) / (qd h : ℚ)) : ℚ) : ℂ)‖ ≤ B')
    {G : Fin m → ℝ} (hG0 : ∀ h, 0 ≤ G h) (hG1 : ∀ h, G h ≤ 1)
    (hγ : ∀ h, ‖((((pn h : ℚ) / (qd h : ℚ)) : ℚ) : ℂ)
        - φ₀ ((algebraMap (𝓞 K) K) (α h))‖ ≤ G h)
    {μ ν : ℚ} (hidx : ((μ : ℚ) : WithTop ℚ)
      ≤ index r (fun h => (algebraMap (𝓞 K) K) (α h)) (map (algebraMap (𝓞 K) K) P))
    {S : ℝ} (hS0 : 0 ≤ S)
    (hS : ∀ i n : Fin m →₀ ℕ, idxWeight r i < ν → (∀ h, n h ≤ r h) → μ ≤ idxWeight r n →
      (∏ h, (G h) ^ (n h - i h)) ≤ S)
    (hfinal : ((∏ h, (qd h) ^ (r h) : ℕ) : ℝ)
        * (((∏ h, (r h + 1) : ℕ) : ℝ)
            * ((((∏ h, (r h + 1) : ℕ) : ℝ) * (H * (2 * B) ^ (∑ h, r h)))
                * ((2 : ℝ) ^ (∑ h, r h) * S)))
        * (conjBound r qd H B') ^ (Fintype.card (K →+* ℂ) - 1) < 1) :
    ((ν : ℚ) : WithTop ℚ)
      ≤ index r (fun h => algebraMap ℚ K ((pn h : ℚ) / (qd h : ℚ)))
          (map (algebraMap (𝓞 K) K) P) := by
  classical
  have hD0 : (0 : ℝ) ≤ ((∏ h, (qd h) ^ (r h) : ℕ) : ℝ) := Nat.cast_nonneg _
  have hH0 : (0 : ℝ) ≤ H := le_trans (house_nonneg _) (hH 0)
  have hB'0 : (0 : ℝ) ≤ 2 * B' := by linarith
  have hM0 : (0 : ℝ) ≤ conjBound r qd H B' := by
    rw [conjBound]
    positivity
  refine le_index_of_norm_lt pn qd hq r P hdeg φ₀ (M := conjBound r qd H B') (ν := ν)
    (fun i hi => ⟨fun φ _ => ?_, ?_⟩)
  · rw [conjBound]
    exact mul_le_mul_of_nonneg_left
      (norm_embedding_coeff_translate_le φ pn qd r hdeg hB1' hH hβ i) hD0
  · have hφ₀ := norm_embedding_coeff_translate_le_index φ₀ pn qd r hdeg α hB1 hH hα
      hG0 hG1 hγ hidx i hS0 (fun n hnr hμn => hS i n hi hnr hμn)
    have hstep : ((∏ h, (qd h) ^ (r h) : ℕ) : ℝ)
        * ‖φ₀ (coeff i (translate (fun h => algebraMap ℚ K ((pn h : ℚ) / (qd h : ℚ)))
            (map (algebraMap (𝓞 K) K) P)))‖
        ≤ ((∏ h, (qd h) ^ (r h) : ℕ) : ℝ)
          * (((∏ h, (r h + 1) : ℕ) : ℝ)
              * ((((∏ h, (r h + 1) : ℕ) : ℝ) * (H * (2 * B) ^ (∑ h, r h)))
                  * ((2 : ℝ) ^ (∑ h, r h) * S))) :=
      mul_le_mul_of_nonneg_left hφ₀ hD0
    refine lt_of_le_of_lt ?_ hfinal
    exact mul_le_mul_of_nonneg_right hstep (pow_nonneg hM0 _)

end MvPolynomial
