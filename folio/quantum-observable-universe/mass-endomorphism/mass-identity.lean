import Mathlib.Algebra.Module.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.CategoryTheory.Monoidal.Category
import QOU.QuantumObservableUniverse.CategoricalFoundations
import QOU.Torsion.MassTraceIdentity


/-!
# QOU.MassIdentity — Mass of a cycle via the Frobenius mass integrand and non-abelian holonomy

The inertial mass of a closed cycle `ϱ = hol w : 𝟙 → A` (the non-abelian ordered convolution
product of a word `w` of segment transports in `Hom(𝟙, A)`) is the norm of the composite
`𝟙 xrightarrow{ϱ} A xrightarrow{Ψ} A xrightarrow{∫_A} 𝟙`, where `Ψ = (∫_A ⊗ id) ∘ Δ` is the
mass integrand (`QOU.Torsion.MassTraceIdentity.massIntegrand`). The categorical trace of the
associated left-multiplication endomorphism `L_{hol w} ≫ Ψ` is `∫_A(u · hol w · c)`.

This file uses the canonical `FrobeniusHopfData` from `QOU.Basic`
(the quantum-universe definition) and `QOU.Torsion.MassTraceIdentity`
to ensure type consistency across the critical path.

**Pre-Archimedean stub.** The previous version coupled this stub
to `[NormedCommRing R]` and returned `ℝ` via `‖·‖`, which is the
Archimedean norm — not the Frobenius norm.  Step 4 of the
forward-derivation ([`docs/audits/2026-05-02-forward-derivation-pre-archimedean.md`](../../../docs/audits/2026-05-02-forward-derivation-pre-archimedean.md))
is explicit: the Frobenius norm `‖x‖_F² := ⟨x, x⟩_F` is valued in
the ground ring `R`, *not* in `ℝ`.  We split the file into two
declarations:

  1. `frobeniusMass` — valued in `R`, abstract `[CommRing R]`
     carrying a Frobenius pairing.  Pre-Archimedean.
  2. `scalarMass`    — valued in `ℝ`, requires `[NormedCommRing R]`,
     the post-τ Archimedean realisation.  Lives downstream of
     `QOU.ArchimedeanMassFormula` per `QOU.GroundRingAnnotations`.

## References

- [leitner2026] §3 Lifting and Descent
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-! ## The inertial mass of a closed cycle

    The inertial mass of a closed cycle `γ : 𝟙 → A` in a Frobenius–Hopf
    object is

    `m(γ) = ‖tr((λ ⊗ id) ∘ Δ ∘ γ)‖_F`

    where `Δ` is the comultiplication (encoding the connection), `λ` is the
    Frobenius form, and `tr` is the categorical trace from the rigid structure.

    This definition connects directly to the canonical `FrobeniusHopfData`
    structure (quantum-universe.lean), using its `comul`, `frobeniusForm`,
    and the rigidity evaluation morphism.

    LaTeX: `\label{def:mass-identity}`

    At the categorical level, the mass is computed from morphisms in `C`.
    For categorical evaluation, we pass to the scalar ring `R` via the
    fibre functor. -/

/-- **Frobenius mass** — the mass formula evaluated in the ground ring
    `R` via the Frobenius pairing.

    Given the image `x : R` of the categorical trace under the fibre
    functor, the Frobenius norm `‖x‖_F` is `⟨x, x⟩_F`-derived (a
    quantity in `R`, not in `ℝ`).  The caller supplies the Frobenius
    pairing through the `frobenius_form` argument.

    For the Archimedean evaluation of `‖·‖_F` at `q = q₀`, see
    `scalarMass` below. -/
-- Ref: [leitner2026] §3, Definition: Mass (categorical trace)
def frobeniusMass {R : Type*} [CommRing R]
    (frobenius_form : R → R → R)
    (trace_of_frobenius_of_comult : R) : R :=
  frobenius_form trace_of_frobenius_of_comult trace_of_frobenius_of_comult

/-- **Scalar mass** — the post-τ Archimedean realisation of
    `frobeniusMass`.  Requires the Archimedean norm structure
    `[NormedCommRing R]`; lives downstream of the formal chain.

    Given the image `x : R` of the categorical trace under the fibre
    functor, `scalarMass x = ‖x‖`.  This corresponds to evaluating
    the categorical Frobenius norm at the substrate parameter
    `q = q₀ ∈ ℝ`.

    Per `QOU.GroundRingAnnotations`, this declaration is **not**
    part of the formal pre-Arch chain — it is the Archimedean
    bridge. -/
-- Ref: [leitner2026] §3, Archimedean specialisation
noncomputable def scalarMass {R : Type*} [NormedCommRing R]
    (trace_of_frobenius_of_comult : R) : ℝ :=
  ‖trace_of_frobenius_of_comult‖

/-- Scalar mass is non-negative (immediate from norm). -/
theorem scalarMass_nonneg {R : Type*} [NormedCommRing R]
    (val : R) : 0 ≤ scalarMass val :=
  norm_nonneg _

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
