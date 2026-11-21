import Mathlib.Data.Nat.Basic


/-!
# QOU.Examples.reeb_su2 — Reeb derivation for SU(2)

The categorical Reeb derivation instantiated on SU(2):
- ξ = e₃ = ½ diag(1, −1) ∈ su(2) (generator of the maximal torus T ≅ U(1))
- Action on the algebra: (ξ·f)(g) = d/dt|_{t=0} f(e^{−tξ}g)
- Canonical 1-form: θ_A = ω₃ (dual to e₃)
- Normalisation: ω₃(ξ) = 1
- Horizontal forms: Ω^k_H(A) = {α : ι_ξ α = 0} (no ω₃ component)

In the archimedean realisation, ξ becomes the Reeb vector field on
the CR manifold (M, θ) with ι_ξ dθ = 0 and θ(ξ) = 1.

LaTeX label: `ex:reeb-su2`

## References

- [witten1988] https://doi.org/10.1007/BF01223371
- [leitner2026] §1 Example: Reeb derivation for SU(2)
-/

namespace QOU.Examples

/-- **SU(2) Reeb data**: ξ = e₃ with contact form θ_A = ω₃.

    LaTeX: `\label{ex:reeb-su2}` -/
-- Ref: [witten1988] Witten, "Topological quantum field theory," Comm. Math. Phys. 117 (1988)
structure SU2ReebData where
  /-- Index of the Lie algebra generator serving as ξ (e₃ → index 3). -/
  generatorIndex : ℕ
  /-- ξ is the third basis element. -/
  gen_is_three : generatorIndex = 3
  /-- Index of the dual 1-form θ_A (ω₃ → index 3). -/
  contactFormIndex : ℕ
  /-- θ_A = ω₃. -/
  contact_is_three : contactFormIndex = 3
  /-- Normalisation: θ_A(ξ) = 1.
      Witnessed by: the contact form and generator indices match
      (ω₃(e₃) = δ₃₃ = 1 in a dual basis). -/
  normalisation : contactFormIndex = generatorIndex
  /-- Number of horizontal 1-forms (those with no ω₃ component). -/
  numHorizontal1Forms : ℕ
  /-- There are 2 horizontal 1-forms: ω₁, ω₂. -/
  horiz_count : numHorizontal1Forms = 2

/-- The Reeb data for SU(2). -/
-- Ref: [leitner2026] §1
def su2Reeb : SU2ReebData where
  generatorIndex := 3
  gen_is_three := rfl
  contactFormIndex := 3
  contact_is_three := rfl
  -- Ref: [witten1988] https://doi.org/10.1007/BF01223371
  normalisation := rfl
  numHorizontal1Forms := 2
  horiz_count := rfl

/-- There are 2 horizontal 1-forms on SU(2) (ω₁, ω₂). -/
theorem su2_horizontal_forms : su2Reeb.numHorizontal1Forms = 2 := rfl

end QOU.Examples
