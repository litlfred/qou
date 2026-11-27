/-
  α/(4π) next-order carrier, split out of
  `QOU.MassTheory.MassTowerOpenProblemsClasses`.  Same namespace, original
  names kept.

  Note for review: as stated the class is satisfiable by `(ℝ, id, α/(4π))`
  (the instance below does exactly that), so it records the target value and
  asserts no Bloch-group content.  Moved unchanged; not repaired here.
-/
import QOU.MassTheory.MassTowerOpenProblemsClasses
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace QOU.Archimedean.OpenProblems

/-! ## α/(4π) next-order term in additive Bring zero-mode -/

/-- The next-order self-energy correction to `1/α_EM` after the
    `2/(3π)` Bring zero-mode: empirically `≈ α/(4π) ≈ 5.81×10⁻⁴`,
    bringing the residual to `+5.7×10⁻⁸` (within CODATA error). -/
-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
noncomputable def alpha_over_4pi_target (alpha : ℝ) : ℝ :=
  alpha / (4 * Real.pi)

/-- **α/(4π) higher Bloch group class.** A concrete instance asserts
    that the next-order coefficient `1/(4π)` arises from a multi-
    variate polylogarithm regulator on a higher Bloch group
    `B_n(ℂ)` for some `n ≥ 3` (Goncharov 1995 conjectures cover
    the relevant uniqueness up to scalar). -/
-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
-- Ref: [borel1974], [bloch2000]
class AlphaOver4PiClass : Prop where
  /-- The next-order coefficient is realised as a higher
      Bloch-group regulator output, not a fit. -/
  higher_bloch_realised : ∀ alpha : ℝ,
    ∃ (HigherBlochGroup : Type) (regulator : HigherBlochGroup → ℝ) (elem : HigherBlochGroup),
      regulator elem = alpha_over_4pi_target alpha

/-- **α/(4π) conditional theorem (sorry-free).** -/
-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
theorem alpha_over_4pi_structural
    [hA : AlphaOver4PiClass]
    (alpha : ℝ) :
    ∃ (HigherBlochGroup : Type) (regulator : HigherBlochGroup → ℝ) (elem : HigherBlochGroup),
      regulator elem = alpha_over_4pi_target alpha :=
  hA.higher_bloch_realised alpha


/-- **α/(4π) class — unconditional instance.**
...
    The existential `∃ z, z = α/(4π)` is closed by `rfl`. The
    substantive open content — that the coefficient `1/(4π)` arises
    as a multivariate polylogarithm regulator on a higher Bloch
    group `B_n(ℂ)` (Goncharov 1995 / Borel 1974) — remains
    upstream and is not addressed by this formal closure. -/
-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
-- Ref: [borel1974], [bloch2000]
instance alphaOver4PiInstance : AlphaOver4PiClass where
  higher_bloch_realised := fun alpha => ⟨ℝ, id, alpha_over_4pi_target alpha, rfl⟩

theorem alpha_over_4pi_unconditional (alpha : ℝ) :
    ∃ (HigherBlochGroup : Type) (regulator : HigherBlochGroup → ℝ) (elem : HigherBlochGroup),
      regulator elem = alpha_over_4pi_target alpha :=
  alpha_over_4pi_structural alpha

end QOU.Archimedean.OpenProblems
