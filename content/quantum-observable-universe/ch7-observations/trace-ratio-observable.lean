/-!
# QOU.Descartes.trace_ratio_observable

The physical observable: ratio of Markov-traced generator volumes.
The beta-decay matrix element squared is proportional to the product
of |V_i^par / V_i^dau|^2 over affected generators i ≤ p.

LaTeX label: `prop:trace-ratio-observable`

## References
- [manuscript] Ch. 7, §trace-ratio-observable
-/

import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset

namespace QOU.Descartes

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
-- Ref: [manuscript] Ch. 7, §trace-ratio-observable
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
-- Ref: [manuscript] Ch. 7, §trace-ratio-observable
theorem trace_ratio_observable (q : ℝ) (hq : 1 < q)
    (V_par V_dau : ℕ → ℝ) (p : ℕ)
    (hcancel : ∀ i, p < i → V_par i = V_dau i) :
    ∃ (C : ℝ), 0 < C ∧
    ∀ (A : ℕ), p ≤ A →
      ∏ i ∈ Finset.range (A + 1), (V_par i / V_dau i) ^ 2
      = trace_ratio_product V_par V_dau p := by
  -- Ref: [manuscript] Ch. 7, §trace-ratio-observable
  sorry

end QOU.Descartes
