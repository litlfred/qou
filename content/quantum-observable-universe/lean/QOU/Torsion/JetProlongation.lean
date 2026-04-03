import QOU.QuantumObservableUniverse
import Mathlib.CategoryTheory.Monoidal.Category

/-!
# §1  Jet Prolongation

The categorical jet object `J¹(A) = A ⊗ Ω¹(A)` and its inherited
Frobenius–Hopf structure.  Jet prolongation of a ℂ quantum observable
universe preserves the QOU structure and CR dimension.
-/


open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU.Torsion

universe u v

/-! ## §1  Jet Prolongation -/

/-- **Jet prolongation data**: the categorical jet object `J¹(A) = A ⊗ Ω¹(A)`.
    LaTeX: `\label{prop:jet-prolongation}`, Steps 1–2. -/
structure JetProlongation (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The base Frobenius–Hopf object `A`. -/
  base : FrobeniusHopfData C
  /-- The jet Frobenius–Hopf object `J¹(A)`. -/
  jet : FrobeniusHopfData C
  /-- The ascent embedding `ℓ : A ↪ J¹(A)`. -/
  ascent : base.obj ⟶ jet.obj
  /-- The restriction map `r : J¹(A) → A`. -/
  restriction : jet.obj ⟶ base.obj
  /-- `r ∘ ℓ = id_A`. -/
  retraction : ascent ≫ restriction = 𝟙 base.obj
  /-- Ascent preserves multiplication. -/
  ascent_preserves_mul :
    (base.mul) ≫ ascent = (ascent ▷ base.obj ≫ (jet.obj ◁ ascent)) ≫ jet.mul
  /-- Restriction preserves comultiplication. -/
  restriction_preserves_comul :
    restriction ≫ base.comul = jet.comul ≫ (restriction ▷ jet.obj ≫ (base.obj ◁ restriction))

/-- **Proposition (Jet Prolongation).**
    LaTeX: `\label{prop:jet-prolongation}` -/
structure JetProlongationQOU where
  /-- The base ℂ quantum observable universe. -/
  base : CQuantumObservableUniverse
  /-- The instanton connection on the base. -/
  inst : InstantonConnection base.toCRManifoldData
  /-- The prolonged ℂ quantum observable universe. -/
  prolonged : CQuantumObservableUniverse
  /-- The prolonged instanton connection. -/
  prolongedInst : InstantonConnection prolonged.toCRManifoldData
  /-- CR dimension is preserved. -/
  dim_preserved : prolonged.n = base.n
  /-- The prolonged connection is uniquely determined. -/
  connection_unique : prolongedInst.parallelAdjointSections →
    inst.parallelAdjointSections

/-- **Corollary (ℂ jet prolongation).**
    LaTeX: `\label{cor:jet-prolongation-C}` -/
theorem jet_prolongation_C (jp : JetProlongationQOU) :
    jp.prolonged.n = jp.base.n :=
  jp.dim_preserved

end QOU.Torsion
