import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.Algebra.Category.ModuleCat.Monoidal.Symmetric
import Mathlib.Tactic.CategoryTheory.Coherence
import Mathlib.Tactic.Ring
import Mathlib.Algebra.Category.ModuleCat.Kernels

/-!
# The trivial quantum universe — `R`-Mod with `A = 𝟙`

`quantum-universe-exists.lean` asserts `Nonempty (QuantumUniverse R)` as an
**axiom**, with the note *"Trivial witness: R-Mod with A = R."*  This file
builds that witness, so the claim becomes a theorem.

`C := ModuleCat R`, `A := 𝟙`, one block.  Every obligation is discharged; there
is no `sorry` and no new axiom.

## What this does and does not settle

It settles that `QuantumUniverse` is **inhabited**, hence that its axioms are
mutually consistent, and it exercises the fields added under bean `qou-w1g8`
(`Preadditive`, `Linear R`, `IsUnit`, `centralIdem_complete`, `unitEndEquiv`) —
which until now nothing constructed, so nothing could falsify.

It does **not** produce a `QuantumObservableUniverse`.  At `A = 𝟙` the
augmentation ideal is zero, so `adjoint_nontrivial` (bean `qou-fav8`) cannot be
satisfied.  That is the intended behaviour: before that field existed, this same
trivial witness would have satisfied the observability axiom via
`adjointObj := 0`.  QOU existence still requires a non-trivial `A`, which is what
its `[kassel1995]` §IX citation was always about.

-- Ref: [leitner2026] §1-quantum-universes/quantum-universe-exists
-/

open CategoryTheory MonoidalCategory

namespace QOU.TrivialWitness

universe w

variable (R : Type w) [CommRing R]

/-- **`End(𝟙)` is the ground ring**, for `ModuleCat R`.

    `r ↦ r • 𝟙` with inverse `f ↦ f(1)`.  This is the `unitEndEquiv` obligation,
    and it holds over any commutative ring — no field needed. -/
noncomputable def unitEndEquivModuleCat : R ≃+* End (𝟙_ (ModuleCat R)) where
  toFun r := r • (𝟙 (𝟙_ (ModuleCat R)))
  invFun f := f.hom (1 : R)
  left_inv := by intro r; simp
  right_inv := by
    intro f; apply ModuleCat.hom_ext; apply LinearMap.ext; intro x
    simp only [ModuleCat.hom_smul, ModuleCat.hom_id, LinearMap.smul_apply,
      LinearMap.id_apply, smul_eq_mul]
    conv_rhs => rw [show x = x • (1 : R) by rw [smul_eq_mul, mul_one]]
    rw [map_smul, smul_eq_mul, mul_comm]
  map_mul' := by
    intro a b; apply ModuleCat.hom_ext; apply LinearMap.ext; intro x
    simp only [ModuleCat.hom_smul, ModuleCat.hom_id, LinearMap.smul_apply,
      LinearMap.id_apply, smul_eq_mul, End.mul_def, ModuleCat.hom_comp,
      LinearMap.comp_apply]
    ring
  map_add' := by intro a b; rw [← add_smul]

/-- **The Frobenius–Hopf object at the tensor unit.**

    `μ = λ_`, `Δ = λ_⁻¹`, everything else the identity, `coev = λ_⁻¹`.  Every
    equation is pure coherence and holds in *any* monoidal category — including
    the eight algebra / coalgebra / antipode laws added 2026-09-14 under bean
    `qou-c64q`, which is the point of keeping this witness: it is the only
    record-literal construction of `FrobeniusHopfData` in the corpus, so it is
    the only thing that can falsify a newly-added field. -/
noncomputable def unitFrobHopf (C : Type*) [Category C] [MonoidalCategory C]
    [BraidedCategory C] : FrobeniusHopfData C where
  obj := 𝟙_ C
  mul := (λ_ (𝟙_ C)).hom
  unit := 𝟙 _
  comul := (λ_ (𝟙_ C)).inv
  counit := 𝟙 _
  antipode := 𝟙 _
  frobeniusForm := 𝟙 _
  coevaluation := (λ_ (𝟙_ C)).inv
  pairing_snake_left := by coherence
  pairing_snake_right := by coherence
  frobenius_relation := by coherence
  one_mul := by coherence
  mul_one := by coherence
  mul_assoc := by coherence
  counit_comul := by coherence
  comul_counit := by coherence
  comul_assoc := by coherence
  antipode_anti_mul := by simp [MonoidalCategory.unitors_inv_equal]
  antipode_anti_comul := by simp [MonoidalCategory.unitors_inv_equal]
  antipode_unit := by simp
  antipode_counit := by simp
  antipode_involutive := by simp
  antipode_frobeniusForm := by simp

/-- **The trivial quantum universe.**  `C = ModuleCat R`, `A = 𝟙`, one block.

    Discharges every field, including the five added under `qou-w1g8`. -/
noncomputable def trivialQU : QOU.QuantumUniverse.{w + 1, w, w, w} R where
  C := ModuleCat R
  frobHopf := unitFrobHopf (ModuleCat R)
  fibreFunctor := (forget (ModuleCat R))
  frobenius_symmetric := by
    intro f
    simp only [FrobeniusHopfData.leftTrace, FrobeniusHopfData.rightTrace,
      FrobeniusHopfData.ev, unitFrobHopf]
    rw [MonoidalCategory.whiskerRight_id, MonoidalCategory.id_whiskerLeft,
      MonoidalCategory.unitors_equal]
    simp
    rw [← MonoidalCategory.unitors_equal]
    simp
  unitEndEquiv := unitEndEquivModuleCat R
  blocks := PUnit
  centralIdem _ := 𝟙 _
  centralIdem_idem _ := by simp
  centralIdem_orthogonal := by rintro ⟨⟩ ⟨⟩ h; exact absurd rfl h
  centralIdem_complete := by simp
  frobWeight _ := 1
  frobWeight_isUnit _ := isUnit_one
  dimQ _ := 1
  dimQ_isUnit _ := isUnit_one
  differentialForms := ModuleCat.kernelCone (unitFrobHopf (ModuleCat R)).mul
  differentialForms_isLimit := ModuleCat.kernelIsLimit _

/-- **`QuantumUniverse` is inhabited** — the claim `quantum-universe-exists.lean`
    carries as an `axiom`, now a theorem. -/
-- Ref: [leitner2026] §1-quantum-universes/quantum-universe-exists
theorem nonempty_quantumUniverse :
    Nonempty (QOU.QuantumUniverse.{w + 1, w, w, w} R) :=
  ⟨trivialQU R⟩

end QOU.TrivialWitness

/-!
## Axiom audit

`#print axioms QOU.TrivialWitness.nonempty_quantumUniverse` reports

    depends on axioms: [propext, Classical.choice, Quot.sound]

— Lean's own three and nothing else.  No `sorryAx`, and none of this
repository's axioms.
-/
