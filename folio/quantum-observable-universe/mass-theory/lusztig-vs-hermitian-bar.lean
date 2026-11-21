import Mathlib.Data.Complex.Basic
import Mathlib.Analysis.Normed.Field.Basic

/-!
# QOU.BraidKnot.LusztigVsHermitianBar

The Lusztig bar (`q ↦ q⁻¹`) and the Hermitian `∗` (`q ↦ conj q⁻¹`)
on the complex Hecke algebra `H_n(ℂ, q)` are distinct anti-involutions
on the parameter in general; they coincide on the parameter iff
`q ∈ ℝ` (equivalently `q.im = 0`).

This file states the parameter-level claim only — the action on the
braid generators `σ_i` is identical (`σ_i ↦ σ_i⁻¹`) under both
involutions, so the algebra-level claim reduces to the
parameter-level claim proved here.
-/

-- Ref: [leitner2026] prop:lusztig-vs-hermitian-bar
-- Ref: [leitner2026] def:bar-involution
-- Ref: [leitner2026] prop:q-zero-complex-extension
-- Ref: [wenzl1988] doi:10.1007/BF01404457

namespace QOU.BraidKnot.LusztigVsHermitianBar

open Complex ComplexConjugate

/-- For nonzero `q : ℂ`, the Lusztig involution `q ↦ q⁻¹` and the
    Hermitian involution `q ↦ (conj q)⁻¹` agree on the parameter
    iff `q ∈ ℝ` (i.e. `q.im = 0`). -/
theorem lusztig_eq_hermitian_iff_real (q : ℂ) (hq : q ≠ 0) :
    q⁻¹ = (conj q)⁻¹ ↔ q.im = 0 := by
  rw [inv_inj]
  exact ⟨fun h => by
    have hre : (conj q).im = q.im := by rw [← h]
    rw [Complex.conj_im] at hre
    linarith,
   fun h => Complex.ext (by simp [Complex.conj_re]) (by simp [Complex.conj_im, h])⟩

/-- Specialization: on `q ∈ ℝ` (viewed in `ℂ`), Lusztig and
    Hermitian agree on the parameter. -/
theorem lusztig_eq_hermitian_on_real (r : ℝ) (hr : (r : ℂ) ≠ 0) :
    ((r : ℂ))⁻¹ = (conj (r : ℂ))⁻¹ := by
  rw [(lusztig_eq_hermitian_iff_real (r : ℂ) hr).mpr]
  simp

end QOU.BraidKnot.LusztigVsHermitianBar
