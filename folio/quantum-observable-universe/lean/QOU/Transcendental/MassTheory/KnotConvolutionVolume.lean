/-
# The volume of a knot convolution operator is additive under composition

Analytic half of `QOU.Observations.KnotConvolutionOperator`. The volume read off a convolution
operator is the growth rate of its block scalars at the roots of unity:
`Vol(z) = lim_N (2π/N) log |c_N(ζ_N)|` (Kashaev; for `4₁` this is the volume conjecture, a theorem
of Andersen–Hansen, cited and not proved here). This file proves:

* `growth_comp`: if `(2π/N) log aₙ → V` and `(2π/N) log bₙ → W` with `aₙ, bₙ > 0`, then
  `(2π/N) log (aₙ bₙ) → V + W`. So the volume of a composite (a connected sum) is the sum of the
  volumes, as hyperbolic volume is additive under connected sum.
* `growth_of_bounded`: if `|log aₙ|` stays bounded, the growth rate is `0`. Scalars that do not
  grow exponentially, such as those of torus-type closures, carry no volume.
-/
import QOU.Observations.KnotConvolutionOperator
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Tactic

namespace QOU.Transcendental.MassTheory.KnotConvolutionVolume

open Filter Topology Real

/-- The growth rate sequence `(2π/N) log aₙ`. -/
noncomputable def growth (a : ℕ → ℝ) (N : ℕ) : ℝ := 2 * π / N * Real.log (a N)

/-- **Volume is additive under composition.** -/
theorem growth_comp (a b : ℕ → ℝ) (ha : ∀ N, 0 < a N) (hb : ∀ N, 0 < b N) (V W : ℝ)
    (hV : Tendsto (growth a) atTop (𝓝 V)) (hW : Tendsto (growth b) atTop (𝓝 W)) :
    Tendsto (growth fun N => a N * b N) atTop (𝓝 (V + W)) := by
  have : (growth fun N => a N * b N) = fun N => growth a N + growth b N := by
    funext N
    simp only [growth]
    rw [Real.log_mul (ha N).ne' (hb N).ne']
    ring
  rw [this]
  exact hV.add hW

/-- **Bounded log means zero volume.** -/
theorem growth_of_bounded (a : ℕ → ℝ) (C : ℝ) (hC : ∀ N, |Real.log (a N)| ≤ C) :
    Tendsto (growth a) atTop (𝓝 0) := by
  have h1 : Tendsto (fun N : ℕ => 2 * π * C / N) atTop (𝓝 0) := by
    simpa using (tendsto_const_div_atTop_nhds_zero_nat (2 * π * C))
  rw [tendsto_zero_iff_abs_tendsto_zero]
  refine squeeze_zero (fun N => abs_nonneg _) (fun N => ?_) h1
  show |growth a N| ≤ 2 * π * C / N
  simp only [growth, abs_mul]
  rcases Nat.eq_zero_or_pos N with h | h
  · subst h; simp
  · have hN : (0 : ℝ) < N := by exact_mod_cast h
    rw [abs_of_pos (by positivity : 0 < 2 * π / (N : ℝ))]
    calc 2 * π / N * |Real.log (a N)| ≤ 2 * π / N * C :=
          mul_le_mul_of_nonneg_left (hC N) (by positivity)
      _ = 2 * π * C / N := by ring

end QOU.Transcendental.MassTheory.KnotConvolutionVolume
