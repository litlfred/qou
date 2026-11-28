/-
  THE DISCRETE GAUSSIAN SUM IS `O(1/√a)` — the `√N` in Laplace's method.

      ∑_{d < m} e^{−a d²}  ≤  1 + ½√(π/a)        for every `a > 0`, every `m`

  uniformly in `m`.  This is the step that turns a trivial "N terms, each at
  most the largest" bound into `√N` terms' worth, and it is where the `N^{3/2}`
  in `⟨4₁⟩_N ≈ c_σ N^{3/2} e^{N·Vol/2π}` comes from: the exponent `1/2` is
  exactly this lemma's `1/√a` at `a ∝ 1/N`.

  Mathlib has both halves and not the combination:
  `AntitoneOn.sum_le_integral` compares a decreasing sum to its integral, and
  `integral_gaussian_Ioi b : ∫_{(0,∞)} e^{−bx²} = ½√(π/b)` evaluates the
  integral.  The lemma below is the two of them joined, with the `d = 0` term
  (which no integral comparison can see) peeled off by hand.

  The second form, with `d(d−1)` in the exponent, is what a per-step tail bound
  actually produces: summing a linear penalty over `d` steps gives
  `1 + 2 + … + (d−1) = d(d−1)/2`, not `d²`.  It costs one extra unit in the
  constant because `d(d−1) ≥ (d−1)²` fails at `d = 0`.

  -- Ref: [leitner2026] QOU/Knot/KashaevTailBound.lean
-/
import Mathlib.Analysis.SumIntegralComparisons
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.Tactic

namespace QOU.MathlibExt

open Real MeasureTheory

/-- `x ↦ e^{−a x²}` is antitone on `[0, M]`. -/
theorem antitoneOn_exp_neg_mul_sq {a M : ℝ} (ha : 0 < a) :
    AntitoneOn (fun x : ℝ => Real.exp (-a * x ^ 2)) (Set.Icc 0 M) := by
  intro x hx y hy hxy
  rw [Set.mem_Icc] at hx hy
  refine Real.exp_le_exp.mpr ?_
  nlinarith [mul_nonneg ha.le (mul_nonneg (sub_nonneg.mpr hxy)
    (by linarith [hx.1, hy.1] : (0 : ℝ) ≤ y + x))]

/-- `∫_0^M e^{−a x²} ≤ ½√(π/a)` — the half-line Gaussian dominates any
initial segment of it. -/
theorem integral_exp_neg_mul_sq_le {a M : ℝ} (ha : 0 < a) (hM : 0 ≤ M) :
    ∫ x in (0:ℝ)..M, Real.exp (-a * x ^ 2) ≤ Real.sqrt (π / a) / 2 := by
  have h1 : ∫ x in (0:ℝ)..M, Real.exp (-a * x ^ 2)
      ≤ ∫ x in Set.Ioi (0:ℝ), Real.exp (-a * x ^ 2) := by
    rw [intervalIntegral.integral_of_le hM]
    apply MeasureTheory.setIntegral_mono_set
    · exact (integrable_exp_neg_mul_sq ha).integrableOn
    · filter_upwards with x using (Real.exp_pos _).le
    · exact Filter.Eventually.of_forall (fun x hx => Set.mem_Ioi.mpr hx.1)
  rwa [integral_gaussian_Ioi] at h1

/-- **The discrete Gaussian sum, bounded uniformly in the number of terms.**
`∑_{d < m} e^{−a d²} ≤ 1 + ½√(π/a)`.  The `1` is the `d = 0` term, which the
integral comparison cannot see. -/
theorem sum_exp_neg_mul_sq_le {a : ℝ} (ha : 0 < a) (m : ℕ) :
    ∑ d ∈ Finset.range m, Real.exp (-a * (d : ℝ) ^ 2)
      ≤ 1 + Real.sqrt (π / a) / 2 := by
  have hsq : (0 : ℝ) ≤ Real.sqrt (π / a) / 2 := by positivity
  cases m with
  | zero => simpa using by linarith
  | succ n =>
      rw [Finset.sum_range_succ']
      have h0 : Real.exp (-a * ((0 : ℕ) : ℝ) ^ 2) = 1 := by norm_num
      rw [h0]
      have hsum : ∑ i ∈ Finset.range n, Real.exp (-a * ((i + 1 : ℕ) : ℝ) ^ 2)
          ≤ ∫ x in (0:ℝ)..(n : ℝ), Real.exp (-a * x ^ 2) := by
        have h := (antitoneOn_exp_neg_mul_sq (a := a) (M := (0 : ℝ) + (n : ℝ))
          ha).sum_le_integral
        simpa using h
      have hint := integral_exp_neg_mul_sq_le (a := a) (M := (n : ℝ)) ha
        (Nat.cast_nonneg n)
      linarith

/-- The form a per-step tail bound produces: the penalty accumulated over `d`
steps is `1 + 2 + … + (d−1) = d(d−1)/2`, so the exponent carries `d(d−1)`, not
`d²`.  Costs one extra unit because `d(d−1) ≥ (d−1)²` fails at `d = 0`. -/
theorem sum_exp_neg_mul_mul_pred_le {a : ℝ} (ha : 0 < a) (m : ℕ) :
    ∑ d ∈ Finset.range m, Real.exp (-(a * (d : ℝ) * ((d : ℝ) - 1)))
      ≤ 2 + Real.sqrt (π / a) / 2 := by
  have hsq : (0 : ℝ) ≤ Real.sqrt (π / a) / 2 := by positivity
  cases m with
  | zero => simpa using by linarith
  | succ n =>
      rw [Finset.sum_range_succ']
      have h0 : Real.exp (-(a * ((0 : ℕ) : ℝ) * (((0 : ℕ) : ℝ) - 1))) = 1 := by
        norm_num
      rw [h0]
      have hstep : ∀ i ∈ Finset.range n,
          Real.exp (-(a * ((i + 1 : ℕ) : ℝ) * (((i + 1 : ℕ) : ℝ) - 1)))
            ≤ Real.exp (-a * (i : ℝ) ^ 2) := by
        intro i _
        refine Real.exp_le_exp.mpr ?_
        push_cast
        nlinarith [Nat.cast_nonneg (α := ℝ) i]
      have hle := Finset.sum_le_sum hstep
      have hbound := sum_exp_neg_mul_sq_le (a := a) ha n
      linarith

end QOU.MathlibExt
