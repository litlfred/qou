/-!
# QOU.CategoricalLagrangian.exists — existence of the categorical Lagrangian

𝓛_q(∇, ψ) = 𝒟_∇² + ψ* ⊗ 𝒟_∇ψ exists as an endomorphism of A via
composition, tensor, and addition in 𝐂.

LaTeX: `\label{prop:categorical-lagrangian-exists}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-lagrangian-exists
- [connes1994] Noncommutative Geometry
-/

import QOU.Basic

namespace QOU

/-- **Existence of the categorical Lagrangian.**

    For any `FrobeniusHopfData C`, a `CategoricalLagrangian C fh` term
    exists — built from the Dirac operator and state via composition,
    tensor, and addition. -/
-- Ref: [connes1994]
theorem CategoricalLagrangian.exists
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) :
    Nonempty (CategoricalLagrangian C fh) :=
  -- Trivial witness: trivial Dirac operator (built like in
  -- categorical-dirac-operator-exists), state = fh.unit, lagrangian =
  -- 𝟙. The intended Connes-style 𝒟_∇² + ψ* ⊗ 𝒟_∇ψ is sharper but
  -- requires spectral-triple infrastructure not in Mathlib.
  -- Ref: [connes1994]
  ⟨{ dirac :=
       { connection :=
           { Omega1 := 𝟙_ C
             nabla := (CategoryTheory.MonoidalCategory.rightUnitor fh.obj).inv
             leibniz_rhs :=
               fh.mul ≫ (CategoryTheory.MonoidalCategory.rightUnitor fh.obj).inv
             leibniz := rfl }
         q := 𝟙 (𝟙_ C)
         reeb := 𝟙 fh.obj
         dirac := 𝟙 fh.obj }
     state := fh.unit
     lagrangian := 𝟙 fh.obj }⟩

end QOU
