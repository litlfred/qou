/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.OS.Universal
import Mathlib.Algebra.Category.ModuleCat.Monoidal.Basic

/-!
# `QOU.OrientedSkein.OS.NonVacuity` — a concrete model of the hypotheses

The universal property (`QOU.OrientedSkein.OS.Universal`) is stated for an arbitrary oriented
skein datum.  This file exhibits one, so the hypotheses are satisfiable in a nonzero category,
and uses it to show that `OS(z, t)` is not the zero category.

* `unitDatum` — in any `R`-linear monoidal category, `E = F = 𝟙` with crossing `S = q • 1` and
  mixed crossing `T = qi • 1` is an oriented skein datum whenever `q * qi = 1`, with `δ = t * qi`.
* `OSCat.id_unit_ne_zero` — over a nontrivial ring, `𝟙 (𝟙_ OS) ≠ 0` for these parameters, by
  lifting the unit datum to `ModuleCat R`.

**Scope.** This is a one-dimensional model: `E` is the unit object.  It shows that the
hypotheses are consistent and that `OS` is nonzero for the parameters `(q, q⁻¹, t, t q⁻¹)`.  It
does not construct the vector representation of `U_q(gl_n)`, and it says nothing about
faithfulness.

Sorry-free.
-/

namespace QOU.OrientedSkein.OS

open CategoryTheory MonoidalCategory

universe v u

set_option linter.unusedSectionVars false

noncomputable section

variable {R : Type*} [CommRing R]
variable {𝒞 : Type u} [Category.{v} 𝒞] [Preadditive 𝒞] [Linear R 𝒞]
  [MonoidalCategory 𝒞] [MonoidalPreadditive 𝒞] [MonoidalLinear R 𝒞]

theorem sideways_scalar (q : R) :
    sideways (E := 𝟙_ 𝒞) (F := 𝟙_ 𝒞) (q • 𝟙 (𝟙_ 𝒞 ⊗ 𝟙_ 𝒞)) = q • 𝟙 _ := by
  simp only [sideways, MonoidalLinear.whiskerLeft_smul, MonoidalLinear.smul_whiskerRight,
    monoidalComp, Linear.comp_smul, Linear.smul_comp, ExactPairing.coevaluation,
    ExactPairing.evaluation, exactPairingUnit]
  congr 1
  monoidal

variable (𝒞) in
/-- An oriented skein datum on the unit object: `E = F = 𝟙`, crossing `S = q • 1`,
mixed crossing `T = qi • 1`, valid whenever `q * qi = 1`, with `δ = t * qi`. -/
def unitDatum (q qi t : R) (hq : q * qi = 1) :
    OrientedSkeinDatum q qi t (t * qi) (𝟙_ 𝒞) (𝟙_ 𝒞) where
  cross := HeckeCrossing.scalar q qi (𝟙_ 𝒞)
  T := qi • 𝟙 _
  T_sideways := by
    rw [show (HeckeCrossing.scalar q qi (𝟙_ 𝒞)).S = q • 𝟙 _ from rfl, sideways_scalar]
    rw [Linear.smul_comp, Linear.comp_smul, Category.id_comp, smul_smul, mul_comm, hq, one_smul]
  sideways_T := by
    rw [show (HeckeCrossing.scalar q qi (𝟙_ 𝒞)).S = q • 𝟙 _ from rfl, sideways_scalar]
    rw [Linear.smul_comp, Linear.comp_smul, Category.id_comp, smul_smul, hq, one_smul]
  dim := by
    simp [ExactPairing.coevaluation, ExactPairing.evaluation, exactPairingUnit, smul_smul]

/-- **Non-vacuity.** Over a nontrivial ring, for every unit `q` with inverse `qi` and every `t`,
the identity of the unit object of `OS(z, t)` is nonzero: lifting the unit datum to modules over
`R` sends it to the identity of `R`. -/
theorem OSCat.id_unit_ne_zero {R : Type u} [CommRing R] [Nontrivial R] (q qi t : R)
    (hq : q * qi = 1) : 𝟙 (𝟙_ (OSCat q qi t (t * qi))) ≠ 0 := by
  intro h
  have h' := congrArg (lift (unitDatum (ModuleCat.{u} R) q qi t hq)).map h
  rw [CategoryTheory.Functor.map_id, CategoryTheory.Functor.map_zero] at h'
  have := congrArg (fun f => ModuleCat.Hom.hom f (1 : R)) h'
  simp at this
  exact (one_ne_zero : (1 : R) ≠ 0) this

end

end QOU.OrientedSkein.OS
