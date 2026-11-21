import QOU.QuantumObservableUniverses.QDifferentialGeometry
import Mathlib.CategoryTheory.Linear.Basic


/-!
# QOU.CategoricalDirac.unique — uniqueness of the categorical Dirac operator

`𝒟_∇` is uniquely determined by its defining formula once the connection
`∇`, the substrate parameter `q` (with inverse `qinv`), and the Reeb data
(`nablaEndo`, `reeb`) are fixed: the `dirac_formula` field forces the Dirac
morphism, so two operators sharing those data coincide.

LaTeX: `\label{prop:categorical-dirac-operator-unique}`

## References

- [leitner2026] §2-quantum-observable-universes/categorical-dirac-operator-unique
- [connes1994] Noncommutative Geometry
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Uniqueness of the categorical Dirac operator.**

    Given fixed connection, substrate parameter `q` / inverse `qinv`, and
    Reeb data `nablaEndo` (`∇`) and `reeb` (`ι_ξ∇`), the operator
    `𝒟_∇ = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ∇` is uniquely determined: the `dirac`
    morphism is forced by [`def:categorical-dirac-operator`]'s
    `dirac_formula`, so two such operators are equal.

    This replaces the earlier `axiom … : Subsingleton (CategoricalDiracOperator …)`,
    which was **false** (the structure has free fields, so distinct data give
    distinct operators).  Uniqueness holds only conditionally on shared data —
    exactly the narrative claim. -/
-- Ref: [connes1994]
theorem CategoricalDirac.unique
    {R : Type*} [CommRing R]
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear R C]
    (fh : FrobeniusHopfData C)
    (D₁ D₂ : CategoricalDiracOperator R C fh)
    (hconn : D₁.connection = D₂.connection)
    (hq : D₁.q = D₂.q) (hqinv : D₁.qinv = D₂.qinv)
    (hnabla : D₁.nablaEndo = D₂.nablaEndo) (hreeb : D₁.reeb = D₂.reeb) :
    D₁ = D₂ := by
  obtain ⟨c₁, q₁, qi₁, _, n₁, r₁, d₁, hf₁⟩ := D₁
  obtain ⟨c₂, q₂, qi₂, _, n₂, r₂, d₂, hf₂⟩ := D₂
  simp only at hconn hq hqinv hnabla hreeb
  subst hconn hq hqinv hnabla hreeb
  -- `dirac` is forced by the formula from the (now shared) data; the two
  -- remaining fields (`q_unit`, `dirac_formula`) are proof-irrelevant.
  have hd : d₁ = d₂ := hf₁.trans hf₂.symm
  subst hd
  rfl

end QOU
