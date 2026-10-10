import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.LinearAlgebra.FiniteDimensional.Defs
import Mathlib.Tactic

/-!
# The Faddeev quasi-period lattice `⟨ib, i/b⟩` is non-degenerate iff `b² ∉ ℝ`

Discharges the `hspan` input of `QOU.QBeta.FaddeevRigidityReduction`: the two
quasi-periods of the `Φ_b` ratio, `I·b` (compact) and `I/b` (modular-dual), form
a genuine `ℝ`-basis of `ℂ` exactly when `b² ∉ ℝ` — i.e. `(b^2).im ≠ 0`. This is the
substrate non-degeneracy condition: it holds on the physical branch `arg b = π/4`
(where `b²` is purely imaginary) and **fails for real `b`** (the `|q| = 1` regime),
where both periods lie on the imaginary axis and the lattice collapses — so
Faddeev–Volkov rigidity genuinely requires the substrate branch, not just any `b`.

Verified `lean`-direct against pinned Mathlib (exit 0).
-/

open Complex Module

namespace QOU.QBeta.PeriodLatticeBasis

/-- `v = I·b` and `w = I/b` are ℝ-linearly independent in ℂ exactly when
`b² ∉ ℝ` (`(b^2).im ≠ 0`). -/
theorem periods_linearIndependent {b : ℂ} (hb2 : (b ^ 2).im ≠ 0) :
    LinearIndependent ℝ ![I * b, I / b] := by
  have hb : b ≠ 0 := by
    rintro rfl; simp at hb2
  rw [LinearIndependent.pair_iff]
  intro s t hst
  rw [Complex.real_smul, Complex.real_smul] at hst
  have key : (s : ℂ) * b ^ 2 + t = 0 := by
    have hmul := congrArg (fun z => z * b) hst
    simp only [zero_mul] at hmul
    field_simp [hb] at hmul
    have hI : (I : ℂ) ≠ 0 := Complex.I_ne_zero
    apply mul_left_cancel₀ hI
    ring_nf
    ring_nf at hmul
    linear_combination hmul
  have hsim : s * (b ^ 2).im = 0 := by
    have := congrArg Complex.im key
    simpa [Complex.add_im, Complex.mul_im, Complex.ofReal_re, Complex.ofReal_im] using this
  have hs : s = 0 := by
    rcases mul_eq_zero.mp hsim with h | h
    · exact h
    · exact absurd h hb2
  refine ⟨hs, ?_⟩
  rw [hs] at key
  simp only [Complex.ofReal_zero, zero_mul, zero_add] at key
  exact_mod_cast key

/-- The two quasi-periods `⟨I·b, I/b⟩` form an ℝ-basis of ℂ when `b² ∉ ℝ`. -/
theorem exists_period_basis {b : ℂ} (hb2 : (b ^ 2).im ≠ 0) :
    ∃ bas : Basis (Fin 2) ℝ ℂ, bas 0 = I * b ∧ bas 1 = I / b := by
  have hli := periods_linearIndependent hb2
  have hcard : Fintype.card (Fin 2) = Module.finrank ℝ ℂ := by
    simp [Complex.finrank_real_complex]
  refine ⟨basisOfLinearIndependentOfCardEqFinrank hli hcard, ?_, ?_⟩
  · simp [coe_basisOfLinearIndependentOfCardEqFinrank]
  · simp [coe_basisOfLinearIndependentOfCardEqFinrank]

end QOU.QBeta.PeriodLatticeBasis
