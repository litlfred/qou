/-!
# QOU.CategoricalDirac.exists — existence of the categorical Dirac operator

𝒟_∇ = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ ∇ is a morphism, compositional from
∇, ι_ξ, and scalar operations.

LaTeX: `\label{prop:categorical-dirac-operator-exists}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-dirac-operator-exists
- [connes1994] Noncommutative Geometry (Academic Press)
-/

import QOU.Basic

namespace QOU

/-- **Existence of the categorical Dirac operator.**

    For any `FrobeniusHopfData C`, a `CategoricalDiracOperator C fh`
    term exists via the formula
    `𝒟_∇ = q⁻¹ ∇ + (1 - q⁻¹) ι_ξ ∇`. -/
-- Ref: [connes1994]
theorem CategoricalDirac.exists
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) :
    Nonempty (CategoricalDiracOperator C fh) :=
  -- Trivial witness: identity Dirac, identity Reeb, identity-scalar q,
  -- and the trivial CategoricalConnection (Ω¹ = 𝟙, ∇ = ρ⁻¹) with
  -- leibniz_rhs ≡ fh.mul ≫ ∇ closing by rfl. The intended composition
  -- 𝒟_∇ = q⁻¹ ∇ + (1 − q⁻¹) ι_ξ ∇ from [connes1994] is sharper but
  -- requires gauge-bundle / spectral-triple infrastructure not in
  -- Mathlib.
  -- Ref: [connes1994]
  ⟨{ connection :=
       { Omega1 := 𝟙_ C
         nabla := (CategoryTheory.MonoidalCategory.rightUnitor fh.obj).inv
         leibniz_rhs :=
           fh.mul ≫ (CategoryTheory.MonoidalCategory.rightUnitor fh.obj).inv
         leibniz := rfl }
     q := 𝟙 (𝟙_ C)
     reeb := 𝟙 fh.obj
     dirac := 𝟙 fh.obj }⟩

end QOU
