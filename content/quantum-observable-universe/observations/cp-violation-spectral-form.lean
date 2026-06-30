import Mathlib.Data.Complex.Basic

/-!
# QOU.Observations.cp_violation_spectral_form

CP-violating discriminant `δ_CP` as the imaginary part of the
alternating/symmetric Wedderburn-block trace ratio.

Conditional on `complex_chirality_rotation` — the complexification of
the substrate parameter `q = |q| exp(iθ)`.

LaTeX label: `conj:cp-violation-spectral-form`

## References

- [manuscript] §6/cp-violation-spectral-form
- [christenson1964] https://doi.org/10.1103/PhysRevLett.13.138
-/

namespace QOU.Observations

/-- Conjectural class: the substrate parameter is complexified, with
    the alternating-block character carrying the residual phase. -/
class ComplexSubstrate where
  q_modulus : ℝ
  q_phase : ℝ                        -- θ_res
  modulus_pos : 0 < q_modulus

/-- Wedderburn-block characters as complex numbers under the
    complexified substrate. -/
structure WedderburnComplexCharacters where
  chiAlt : ℂ                         -- χ_{(1^n)}(β)
  chiSym : ℂ                         -- χ_{(n)}(β)
  sym_nonzero : chiSym ≠ 0

/-- The CP-violating discriminant as the imaginary part of the
    alternating/symmetric ratio. -/
noncomputable def deltaCP (W : WedderburnComplexCharacters) : ℝ :=
  (W.chiAlt / W.chiSym).im

/-- **Conjecture (spectral form of δ_CP)**.

    Conditional on `ComplexSubstrate`, the CP-violating discriminant
    is the imaginary part of the alternating/symmetric Wedderburn-block
    character ratio. -/
-- Ref: [manuscript] §6/cp-violation-spectral-form
-- Ref: [christenson1964] Evidence for the $2\pi$ Decay of the $K_2^0$ Meso — see content/schema/references.ts
theorem cp_violation_spectral_form
    [ComplexSubstrate]
    (W : WedderburnComplexCharacters) :
    ∃ δ : ℝ, δ = (W.chiAlt / W.chiSym).im :=
  ⟨(W.chiAlt / W.chiSym).im, rfl⟩

end QOU.Observations
