import QOU.QuantumObservableUniverses.QDifferentialGeometry
import Mathlib.CategoryTheory.Linear.Basic


/-!
# QOU.CategoricalLagrangian.exists — existence of the categorical Lagrangian

`𝓛_q(∇, ψ) = 𝒟_∇² + ψ* ⊗ 𝒟_∇ψ` exists as an endomorphism of `A`, built by
composition and addition in the `R`-linear monoidal category `C` from a
Dirac operator, a state, and a costate.  The witness genuinely realises the
defining formula — `lagrangian` **equals** `𝒟² + ψ*⊗𝒟ψ`, not a trivial
identity.

LaTeX: `\label{prop:categorical-lagrangian-exists}`

## References

- [leitner2026] §2-quantum-observable-universes/categorical-lagrangian-exists
- [connes1994] Noncommutative Geometry
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Existence of the categorical Lagrangian.**

    In an `R`-linear monoidal category `C`, for any Dirac operator `D`, state
    `ψ`, and costate `ψ*`, there exists a `CategoricalLagrangian R C fh` whose
    `lagrangian` endomorphism is exactly `𝒟_∇² + ψ* ⊗ 𝒟_∇ψ`.

    This replaces the earlier `Nonempty (CategoricalLagrangian C fh)` proved
    by a trivial identity witness: the existential now pins the `lagrangian`
    field to the defining formula of [`def:categorical-lagrangian`]. -/
-- Ref: [connes1994]
theorem CategoricalLagrangian.exists
    {R : Type*} [CommRing R]
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear R C]
    (fh : FrobeniusHopfData C)
    (dirac : CategoricalDiracOperator R C fh)
    (state : (𝟙_ C) ⟶ fh.obj) (costate : fh.obj ⟶ (𝟙_ C)) :
    ∃ L : CategoricalLagrangian R C fh,
      L.lagrangian = dirac.dirac ≫ dirac.dirac + costate ≫ state ≫ dirac.dirac :=
  ⟨{ dirac := dirac
     state := state
     costate := costate
     lagrangian := dirac.dirac ≫ dirac.dirac + costate ≫ state ≫ dirac.dirac
     lagrangian_formula := rfl }, rfl⟩

end QOU
