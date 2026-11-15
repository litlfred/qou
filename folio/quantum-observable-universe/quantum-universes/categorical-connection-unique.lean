import QOU.Basic
import QOU.QuantumObservableUniverse.GaugeTheory


/-!
# QOU.CategoricalConnection.unique_up_to_gauge — uniqueness up to gauge

Connections form an affine space over Ω¹(A) ⊗ Ad(A).

LaTeX: `\label{prop:categorical-connection-unique}`

## Honest statement (2026-06-09 axiom audit)

The previous version asserted
`axiom : Subsingleton (CategoricalConnection C fh)`, which is **false**:
the structure has free data fields (`Omega1 : C` itself, plus
`leibniz_rhs` constrained only through `leibniz`), so distinct
instances exist in any category with two objects.

What *is* provable — with no axiom — is the determination the Leibniz
rule genuinely provides: fixing the gauge data (the 1-form object
`Omega1` and the Leibniz right-hand side), the connection morphism is
unique whenever the multiplication `μ` is an epimorphism, since
`leibniz` pins `μ ≫ ∇`.  The full affine-torsor statement (difference
of two connections is an `Ad(A)`-valued 1-form) requires a preadditive
monoidal category to even *state* the difference; recording that
torsor structure is the open refactor.  `CategoricalConnection` is
imported here from the `QOU` library.

## References

- [leitner2026] §1-quantum-universes/categorical-connection-unique
- [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
-/

namespace QOU

open CategoryTheory
open MonoidalCategory

universe u v

/-- **Uniqueness of categorical connections up to gauge (proved,
    conditional on `Epi fh.mul`).**

    Two `CategoricalConnection C fh` instances with the same 1-form
    object and the same Leibniz right-hand side (after `eqToHom`
    transport) have the same connection morphism, provided the
    multiplication is an epimorphism: the Leibniz rule `μ ≫ ∇ = rhs`
    then cancels.  This replaces a false
    `Subsingleton (CategoricalConnection C fh)` axiom (free fields
    admit distinct instances) with the determination the Leibniz rule
    genuinely provides. -/
-- Ref: [kock2004] Frobenius Algebras and 2D TQFT, Ch 2
theorem CategoricalConnection.unique_up_to_gauge
    {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
    (fh : FrobeniusHopfData C) [Epi fh.mul]
    (D₁ D₂ : CategoricalConnection C fh)
    (hΩ : D₁.Omega1 = D₂.Omega1)
    (hrhs : D₁.leibniz_rhs ≫ (fh.obj ◁ eqToHom hΩ) = D₂.leibniz_rhs) :
    D₁.nabla ≫ (fh.obj ◁ eqToHom hΩ) = D₂.nabla := by
  rw [← cancel_epi fh.mul, ← Category.assoc, D₁.leibniz, hrhs, D₂.leibniz]

end QOU
