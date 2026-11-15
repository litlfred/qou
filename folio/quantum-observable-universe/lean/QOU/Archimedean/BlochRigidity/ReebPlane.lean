import QOU.BringCone
import QOU.StandardModel.PolarizationRealStructure
import Mathlib.Analysis.Complex.Basic

/-!
# The complex plane as the Reeb `i`-plane of the Bring cone

The complex structure and the real structure used in Bloch–Suslin rigidity are not new data:
both are restrictions of structures the corpus already carries on the Bring cone
`BringCone ℝ = ℍ`.

* `cplx a b = a + b i` embeds `ℂ` as the plane `span(1, i)`.
* **Complex structure.** The Reeb operator `reebM_i` (right multiplication by `i`, one of the
  three complex structures of the Reeb triad) preserves that plane and acts on it as
  multiplication by `I` (`reebM_i_cplx`).
* **Real structure.** Every member `p ↦ u p ū`, `u = c j + d k` with `c² + d² = 1`, of the
  circle of real structures `realStr` preserves the plane and acts on it as complex conjugation
  (`realStr_cplx`). So on this plane the `λ`-ambiguity of `PolarizationRealStructure.lean`
  disappears: the whole circle restricts to one conjugation.
-/

open Complex

namespace QOU.Tetraplectic

/-- `ℂ` as the Reeb `i`-plane `span(1, i) ⊂ ℍ`. -/
def ofComplex (z : ℂ) : BringCone ℝ := cplx z.re z.im

theorem ofComplex_injective : Function.Injective ofComplex := by
  intro z w h
  have h1 := congrArg (fun p : BringCone ℝ => p.re) h
  have h2 := congrArg (fun p : BringCone ℝ => p.imI) h
  simp [ofComplex, cplx] at h1 h2
  exact Complex.ext h1 h2

/-- The Reeb complex structure restricts to multiplication by `I`. -/
theorem reebM_i_ofComplex (z : ℂ) : reebM_i (ofComplex z) = ofComplex (I * z) := by
  ext <;> simp [reebM_i, ofComplex, cplx]

/-- Every real structure of the circle restricts to complex conjugation. -/
theorem realStr_ofComplex {c d : ℝ} (h : c * c + d * d = 1) (z : ℂ) :
    realStr (orthW c d) (ofComplex z) = ofComplex ((starRingEnd ℂ) z) := by
  ext <;> simp [realStr, orthW, ofComplex, cplx] <;>
    first
    | ring1
    | linear_combination (z.re + z.im) * h
    | linear_combination (-(z.re + z.im)) * h
    | linear_combination z.re * h
    | linear_combination (-z.re) * h
    | linear_combination z.im * h
    | linear_combination (-z.im) * h

end QOU.Tetraplectic
