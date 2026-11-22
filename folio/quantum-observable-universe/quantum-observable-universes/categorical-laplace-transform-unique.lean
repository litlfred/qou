import QOU.Basic
import QOU.QuantumObservableUniverses.QIntegralTransforms


/-!
# QOU.CategoricalLaplace.unique — uniqueness of the categorical Laplace transform

`𝓛` is characterised as the monoidal mate of the q-coproduct `Δ_q` under the
Frobenius pairing.  That characterisation fixes the underlying `transform`
map, so two categorical Laplace transforms with the same `transform`
coincide.

LaTeX: `\label{prop:categorical-laplace-unique}`

## Honest statement (2026-06-09 axiom audit)

The previous version recorded an external axiom (a bare `Subsingleton`
was noted as too strong) on an auto-bound `CategoricalLaplace` — never
imported, hence unchecked.

This file imports the relocated `CategoricalLaplace` structure
(`QOU.QuantumObservableUniverses.QIntegralTransforms`) and **proves** —
with no axiom — the conditional determination: two Laplace data with the
same `transform` map are equal (the monoidal-law fields are
proof-irrelevant).  This is the content of the narrative "unique mate of
`Δ_q`" claim once the characterising map is fixed.  (A bare `Subsingleton`
would be false in general — distinct `transform` maps give distinct data.
The current `monoidal_unit` law does happen to force `transform f s = f`,
which would collapse the type, but relying on that leans on an over-strong
law; pinning the genuine convolution unit as a field is the open structure
refactor.)

## References

- [leitner2026] §2-quantum-observable-universes/categorical-laplace-transform-unique
- [kassel1995] Quantum Groups, §IV
-/

namespace QOU

/-- **Uniqueness of the categorical Laplace transform (proved,
    conditional on the shared `transform`).**

    The categorical Laplace transform is the monoidal mate of `Δ_q`
    under the Frobenius pairing; that property fixes the `transform`
    map.  Two `CategoricalLaplace A` data with the same `transform` are
    therefore equal (the monoidal-law fields are proof-irrelevant).
    Replaces a false / unchecked `Subsingleton (CategoricalLaplace A)`
    axiom. -/
-- Ref: [kassel1995] Quantum Groups, §IV
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
