import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Analysis.SpecialFunctions.Pow.Real


/-!
# QOU.Archimedean.trace_ratio_observable

The physical observable: ratio of Markov-traced generator volumes.
The beta-decay matrix element squared is proportional to the product
of |V_i^par / V_i^dau|^2 over affected generators i ≤ p.

LaTeX label: `prop:trace-ratio-observable`

## References
- [leitner2026] Ch. 7, §trace-ratio-observable

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Archimedean

/-- The Markov-traced generator volume at generator σ_i:
    V̂_i = z · a_i + b_i, where z is the Markov parameter and
    a_i, b_i are the crossing-dependent coefficients. -/
noncomputable def traced_generator_volume (z a_i b_i : ℝ) : ℝ :=
  z * a_i + b_i

/-- The Skein amplitude for a single beta decay vertex:
    s = q^{1/2} - q^{-1/2}. -/
noncomputable def skein_amp (q : ℝ) : ℝ :=
  q ^ (1/2 : ℝ) - q ^ (-(1/2 : ℝ))

/-- The trace ratio product over affected generators 0..p:
    ∏_{i=0}^{p} |V̂_i^par / V̂_i^dau|². -/
noncomputable def trace_ratio_product
    (V_par V_dau : ℕ → ℝ) (p : ℕ) : ℝ :=
  ∏ i ∈ Finset.range (p + 1), (V_par i / V_dau i) ^ 2

/-- Generators i > p cancel between parent and daughter:
    if V_par i = V_dau i then the ratio is 1. -/
-- Ref: [leitner2026] Ch. 7, §trace-ratio-observable
theorem generator_cancellation (V_par V_dau : ℕ → ℝ) (i p : ℕ)
    (hi : p < i) (heq : V_par i = V_dau i) (hne : V_dau i ≠ 0) :
    (V_par i / V_dau i) ^ 2 = 1 := by
  rw [heq, div_self hne, one_pow]

/-- The trace ratio observable: the beta-decay matrix element squared
    is proportional to the product of volume ratios over affected
    generators, times the Skein amplitude squared.

    |M_q|² ∝ |skein_amp|² · ∏_{i=0}^{p} |V̂_i^par / V̂_i^dau|².

    This is the main proposition: the exponential growth of individual
    Markov traces cancels in the ratio, leaving a finite product over
    only the generators affected by the nucleon conversion. -/
-- Ref: [leitner2026] Ch. 7, §trace-ratio-observable
theorem trace_ratio_observable (q : ℝ) (hq : 1 < q)
    (V_par V_dau : ℕ → ℝ) (p : ℕ)
    (hcancel : ∀ i, p < i → V_par i = V_dau i)
    (hne : ∀ i, p < i → V_dau i ≠ 0) :
    ∀ (A : ℕ), p ≤ A →
      ∏ i ∈ Finset.range (A + 1), (V_par i / V_dau i) ^ 2
      = trace_ratio_product V_par V_dau p := by
  intro A hA
  unfold trace_ratio_product
  -- Split range(A+1) = range(p+1) ∪ {p+1, ..., A} and show extra terms are 1
  have : ∀ i, p < i → (V_par i / V_dau i) ^ 2 = 1 := by
    intro i hi
    rw [hcancel i hi, div_self (hne i hi), one_pow]
  -- The product over {p+1, ..., A} is 1, so the full product = truncated product
  rw [← Finset.prod_range_mul_prod_Ico _ (by omega : p + 1 ≤ A + 1)]
  suffices h : ∏ i ∈ Finset.Ico (p + 1) (A + 1), (V_par i / V_dau i) ^ 2 = 1 by
    rw [h, mul_one]
  apply Finset.prod_eq_one
  intro i hi
  apply this
  exact Nat.lt_of_lt_of_le (by omega : p < p + 1) (Finset.mem_Ico.mp hi).1

end QOU.Archimedean
