import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.CategoricalLaplace.unique — uniqueness of the categorical Laplace transform

`𝓛` is characterised as the monoidal mate of the q-coproduct `Δ_q` under the
Frobenius pairing.  That characterisation fixes the underlying `transform`
map, so two categorical Laplace transforms with the same `transform`
coincide.

LaTeX: `\label{prop:categorical-laplace-unique}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-laplace-transform-unique
- [kassel1995] Quantum Groups, §IV
-/

namespace QOU

noncomputable section
abbrev R_q := LaurentPolynomial ℤ

/-- **Uniqueness of the categorical Laplace transform.**

    The categorical Laplace transform is the monoidal mate of `Δ_q` under the
    Frobenius pairing; that property fixes the `transform` map.  Two
    `CategoricalLaplace A` data with the same `transform` are therefore equal
    (the monoidal-law fields are proof-irrelevant).

    This replaces the earlier `axiom … : Subsingleton (CategoricalLaplace A)`,
    which was **false / too strong** (distinct `transform` maps give distinct
    Laplace data, so they are not all equal).  Uniqueness holds only
    conditionally on the shared `transform` — the content of the narrative
    "unique mate of `Δ_q`" claim once the characterising map is fixed. -/
-- Ref: [kassel1995]
theorem CategoricalLaplace.unique
    {A : Type*} (L₁ L₂ : CategoricalLaplace A)
    (h : L₁.transform = L₂.transform) :
    L₁ = L₂ := by
  obtain ⟨t₁, _, _⟩ := L₁
  obtain ⟨t₂, _, _⟩ := L₂
  simp only at h
  subst h
  rfl

end QOU
