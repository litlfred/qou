import Mathlib.Algebra.Module.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.CategoryTheory.Monoidal.Category
import QOU.Core.CategoricalFoundations
import QOU.LiftingDescent.MassTraceIdentity


/-!
# QOU.MassIdentity — Mass of a cycle via the Frobenius mass integrand and non-abelian holonomy

The inertial mass of a closed cycle `ϱ = hol w : 𝟙 → A` (the non-abelian ordered convolution
product of a word `w` of segment transports in `Hom(𝟙, A)`) is the composite
`𝟙 xrightarrow{ϱ} A xrightarrow{Ψ} A xrightarrow{∫_A} 𝟙`, an element of `End(𝟙) = R`, where
`Ψ = (∫_A ⊗ id) ∘ Δ` is the mass integrand (`QOU.Torsion.MassTraceIdentity.massIntegrand`).
That composite is `cycleFrobeniusEval` below. The categorical trace of the associated
left-multiplication endomorphism `L_{hol w} ≫ Ψ` is `∫_A(u · hol w · c)`.

**Mass is valued in the ring (owner ruling 2026-11-27, bean `qou-5o1v`).** No norm is applied.
The earlier `frobeniusMass` (the quadratic `⟨x, x⟩_F`) and `scalarMass` (`‖x‖ : ℝ`) are removed.
On braid classes the mass is `massClass` (`BraidKnotOctonion/MassTraceMarkovClass.lean`), and
`BraidKnotOctonion/MassClassRingHom.lean` proves it commutes with every ring homomorphism. The
absolute value and the logarithm used to compare with measurement are in
`QOU/Transcendental/MassTheory/MassComparison.lean`.

This file uses the canonical `FrobeniusHopfData` from `QOU.Basic`
(the quantum-universe definition) and `QOU.Torsion.MassTraceIdentity`
to ensure type consistency across the critical path.

## References

- [leitner2026] §3 Lifting and Descent
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-! ## The inertial mass of a closed cycle

    The inertial mass of a closed cycle `ϱ : 𝟙 → A` in a Frobenius–Hopf object is the scalar

    `m(ϱ) = ∫_A ∘ (∫_A ⊗ id) ∘ Δ ∘ ϱ  ∈ End(𝟙) = R`,

    with no norm (`cycleFrobeniusEval`). LaTeX: `\label{def:mass-identity}` -/

/-- **Categorical mass morphism**: the composite `(λ ⊗ id) ∘ Δ`
    in the monoidal category `C`, whose composition with a cycle `ϱ : 𝟙 → A`
    and the Frobenius form `∫_A` gives the pre-norm mass scalar.

    This uses the canonical `FrobeniusHopfData` from quantum-universe.lean
    to maintain type consistency with the foundational definitions. -/
-- Ref: [leitner2026] §3, Definition: Mass (categorical trace)
def massComposite {C : Type u} [Category.{v} C] [MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (fh : FrobeniusHopfData C) : fh.obj ⟶ (𝟙_ C) ⊗ fh.obj :=
  fh.comul ≫ (fh.frobeniusForm ▷ fh.obj)

/-- **Frobenius evaluation of the non-abelian holonomy of a transport word (Option 1).**
    Forms the ordered convolution product `hol fh w : 𝟙_ C ⟶ fh.obj` first, then applies
    the mass integrand `Ψ` and the Frobenius form `∫_A`. -/
def cycleFrobeniusEval {C : Type u} [Category.{v} C] [MonoidalCategory C]
    [CategoryTheory.BraidedCategory C] (fh : FrobeniusHopfData C)
    (w : List (𝟙_ C ⟶ fh.obj)) : 𝟙_ C ⟶ 𝟙_ C :=
  Torsion.MassTraceIdentity.hol fh w ≫
    Torsion.MassTraceIdentity.massIntegrand fh ≫ fh.frobeniusForm

/-- `cycleFrobeniusEval` equals `∫_A(u · hol w)` where `u = Ψ ∘ η` is the density. -/
theorem cycleFrobeniusEval_eq {C : Type u} [Category.{v} C] [MonoidalCategory C]
    [CategoryTheory.BraidedCategory C] (fh : FrobeniusHopfData C)
    (w : List (𝟙_ C ⟶ fh.obj)) :
    cycleFrobeniusEval fh w =
      Torsion.MassTraceIdentity.conv fh
        (Torsion.MassTraceIdentity.density fh)
        (Torsion.MassTraceIdentity.hol fh w) ≫ fh.frobeniusForm :=
  Torsion.MassTraceIdentity.frobeniusForm_massIntegrand_hol fh w

/-- **Categorical trace of the left-multiplication mass endomorphism of `hol w`.** -/
def cycleMassTrace {C : Type u} [Category.{v} C] [MonoidalCategory C]
    [CategoryTheory.BraidedCategory C] (fh : FrobeniusHopfData C)
    (w : List (𝟙_ C ⟶ fh.obj)) : 𝟙_ C ⟶ 𝟙_ C :=
  fh.leftTrace
    (Torsion.MassTraceIdentity.leftMul fh (Torsion.MassTraceIdentity.hol fh w) ≫
      Torsion.MassTraceIdentity.massIntegrand fh)

/-- `cycleMassTrace` equals `∫_A(u · hol w · c)` where `c = μ ∘ coev` is the Casimir element. -/
theorem cycleMassTrace_eq {C : Type u} [Category.{v} C] [MonoidalCategory C]
    [CategoryTheory.BraidedCategory C] (fh : FrobeniusHopfData C)
    (w : List (𝟙_ C ⟶ fh.obj)) :
    cycleMassTrace fh w =
      Torsion.MassTraceIdentity.casimir fh ≫
        Torsion.MassTraceIdentity.leftMul fh
          (Torsion.MassTraceIdentity.conv fh
            (Torsion.MassTraceIdentity.density fh)
            (Torsion.MassTraceIdentity.hol fh w)) ≫
        fh.frobeniusForm :=
  Torsion.MassTraceIdentity.massTrace_eq_functional_hol fh w

end QOU
