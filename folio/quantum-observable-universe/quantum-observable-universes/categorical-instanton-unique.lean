import QOU.Basic
import QOU.QuantumObservableUniverse.Instanton


/-!
# QOU.CategoricalInstanton.unique_up_to_gauge — uniqueness of instantons modulo gauge

Two categorical instantons of the same c₂ are related by a
categorical gauge transformation.

LaTeX: `\label{prop:categorical-instanton-unique}`

## Honest statement (2026-06-09 axiom audit)

The previous version asserted
`axiom : Subsingleton (@CategoricalInstanton C _ _ fh)`, which is
**false**: the structure has free data fields (`connection`,
`curvature`, `hodge`), so distinct instantons exist in any category
where `fh.obj` has two distinct endomorphisms.

What *is* provable — with no axiom — is extensionality: instantons
with the same connection, curvature, and Hodge structure are equal
(self-duality is propositional).  The narrative's moduli statement
(instantons of equal second Chern class agree up to a categorical
gauge transformation) needs a gauge-transformation action on
`CategoricalInstanton` (imported here from the `QOU` library), which
the structure does not yet carry; defining that action and stating the
quotient-level classification is the open structure refactor.

## References

- [leitner2026] §2-quantum-observable-universes/categorical-instanton-unique
- [atiyah1978] https://doi.org/10.1098/rspa.1978.0143
-/

namespace QOU

universe u v

/-- **Uniqueness of categorical instantons (proved extensionality).**

    Two `CategoricalInstanton C fh` instances with the same connection,
    curvature, and Hodge involution are equal: the `self_dual` field is
    propositional.  This replaces a false
    `Subsingleton (CategoricalInstanton C fh)` axiom (free fields admit
    distinct instances) with the extensionality the structure genuinely
    supports; the gauge-quotient moduli statement is the open refactor
    (see the file docstring). -/
-- Ref: [atiyah1978] https://doi.org/10.1098/rspa.1978.0143
theorem CategoricalInstanton.unique_up_to_gauge
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (fh : @FrobeniusHopfData C _ _ _)
    (I₁ I₂ : @CategoricalInstanton C _ _ _ fh)
    (hconn : I₁.connection = I₂.connection)
    (hcurv : I₁.curvature = I₂.curvature)
    (hhodge : I₁.hodge = I₂.hodge) : I₁ = I₂ := by
  cases I₁
  cases I₂
  subst hconn
  subst hcurv
  subst hhodge
  rfl

end QOU
