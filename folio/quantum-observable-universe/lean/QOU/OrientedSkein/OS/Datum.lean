/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.OS.Monoidal
import QOU.OrientedSkein.SkeinDatum

/-!
# `QOU.OrientedSkein.OS.Datum` — the universal oriented skein datum

Stage 3c of the formalisation of the oriented skein category `OS(z, t)` (issue #7703).

The oriented skein category carries an oriented skein datum on its generating objects
`E = [true]` and `F = [false]`: the cup and cap form an exact pairing `F ⊣ E` (the zigzag
relations), the generator `S` is a Hecke crossing (the quadratic and braid relations), the
generator `T` is inverse to the sideways crossing, and the dimension relation holds.  Every
axiom is one of the defining relations of `OS`, read through the dictionary between layers and
whiskered generators.  This is the datum through which every interpretation of `OS` factors (the
universal property, `QOU.OrientedSkein.OS.Universal`).

## Main definitions

* `OSCat.E`, `OSCat.F` — the generating objects.
* `OSCat.gen g` — the generating morphism `g`.
* `OSCat.exactPairing` — `F ⊣ E`, with coevaluation `C` and evaluation `D`.
* `OSCat.datum` — the universal `OrientedSkeinDatum q qi t δ E F`.

Sorry-free.

## References

* [brundan2017] J. Brundan, *Representations of the oriented skein category*, arXiv 1712.08953,
  Theorem 1.1.
-/

namespace QOU.OrientedSkein.OS

open CategoryTheory MonoidalCategory

noncomputable section

variable {R : Type*} [CommRing R] {q qi t δ : R}

namespace OSCat

variable (q qi t δ) in
/-- The generating object `E = ↑`. -/
def E : OSCat q qi t δ := ⟨[true]⟩

variable (q qi t δ) in
/-- The generating object `F = ↓`. -/
def F : OSCat q qi t δ := ⟨[false]⟩

/-- The layer of a lone generator. -/
def lone (g : Gen) : Step := ⟨[], g, []⟩

theorem valid_lone (g : Gen) : Valid g.src [lone g] g.tgt :=
  ⟨by simp [lone, Step.src], by simp [lone, Step.tgt]⟩

/-- A defining relation holds in `OS` between `ρ.src` and `ρ.tgt`. -/
theorem rel_holds (ρ : Rel) {X Y : OSCat q qi t δ} (hX : X.w = ρ.src) (hY : Y.w = ρ.tgt) :
    (homMk (ρ.lhs t) (by rw [hX, hY]; exact ρ.lhs_mem t) : X ⟶ Y) =
      homMk (ρ.rhs q qi δ) (by rw [hX, hY]; exact ρ.rhs_mem q qi δ) := by
  refine homMk_eq_homMk _ _ ?_
  have := whiskA_rel_mem_rels (q := q) (qi := qi) (t := t) (δ := δ) ρ [] [] (x := X.w) (y := Y.w)
    (by simp [hX]) (by simp [hY])
  rwa [whiskA_nil] at this

/-- Unfold every morphism of `OS` built from the monoidal structure to a representative. -/
macro "os_unfold" : tactic =>
  `(tactic| simp only [monoidalComp, MonoidalCoherence.assoc_iso, MonoidalCoherence.assoc'_iso,
      MonoidalCoherence.refl_iso, MonoidalCoherence.whiskerLeft_iso,
      MonoidalCoherence.whiskerRight_iso, MonoidalCoherence.tensor_right_iso,
      MonoidalCoherence.tensor_right'_iso, MonoidalCoherence.left_iso, MonoidalCoherence.left'_iso,
      MonoidalCoherence.right_iso, MonoidalCoherence.right'_iso, Iso.trans_hom, Iso.refl_hom,
      Iso.symm_hom, whiskerLeftIso_hom, whiskerRightIso_hom, associator_hom, associator_inv,
      leftUnitor_hom, leftUnitor_inv, rightUnitor_hom, rightUnitor_inv, id_eq_homMk,
      whiskerLeft_homMk, homMk_whiskerRight, homMk_comp, Category.assoc])


/-- A defining relation, in the form used after unfolding: representatives computing to its two
sides are identified. -/
theorem rel_eq (ρ : Rel) {X Y : OSCat q qi t δ} (hX : X.w = ρ.src) (hY : Y.w = ρ.tgt)
    {f g : PA R} (hf : f ∈ supp R X.w Y.w) (hg : g ∈ supp R X.w Y.w) (hfl : f = ρ.lhs t)
    (hgr : g = ρ.rhs q qi δ) : (homMk f hf : X ⟶ Y) = homMk g hg := by
  subst hfl hgr
  exact rel_holds ρ hX hY

/-- Compute a representative built from whiskered paths down to a single path. -/
macro "path_simp" : tactic =>
  `(tactic| simp only [whiskA_pth, whiskA_one, whiskA_nil, ← pth_nil, pth_mul, List.map_cons,
      List.map_nil, List.cons_append, List.nil_append, List.append_nil, Step.whisk, lone, E, F, Rel.lhs,
      Rel.rhs, sidewaysPath, Gen.src, Gen.tgt, List.singleton_append, one_mul, mul_one])

/-- The generating morphism `g : g.src ⟶ g.tgt`. -/
def gen (g : Gen) : (⟨g.src⟩ : OSCat q qi t δ) ⟶ ⟨g.tgt⟩ :=
  homMk (pth [lone g]) (pth_mem_supp (valid_lone g))

/-- The cup `C` and cap `D` form an exact pairing `F ⊣ E` (the zigzag relations). -/
instance exactPairing : ExactPairing (F q qi t δ) (E q qi t δ) where
  coevaluation' := gen .C
  evaluation' := gen .D
  coevaluation_evaluation' := by
    simp only [gen]
    os_unfold
    exact rel_eq .zigE rfl rfl _ _ (by path_simp) (by path_simp)
  evaluation_coevaluation' := by
    simp only [gen]
    os_unfold
    exact rel_eq .zigF rfl rfl _ _ (by path_simp) (by path_simp)

theorem coevaluation_eq : η_ (F q qi t δ) (E q qi t δ) = gen .C := rfl
theorem evaluation_eq : ε_ (F q qi t δ) (E q qi t δ) = gen .D := rfl

variable (q qi t δ) in
/-- The generator `S` is a Hecke crossing on `E` (the quadratic and braid relations). -/
def cross : HeckeCrossing q qi (E q qi t δ) where
  S := gen .S
  quad := by
    simp only [IsHeckeQuad, gen]
    os_unfold
    simp only [← homMk_smul, ← homMk_add]
    exact rel_eq .quad rfl rfl _ _ (by path_simp) (by path_simp)
  braid := by
    simp only [leftCross, gen]
    os_unfold
    exact rel_eq .braid rfl rfl _ _ (by path_simp) (by path_simp)

variable (q qi t δ) in
/-- The **universal oriented skein datum** in `OS(z, t)`. -/
def datum : OrientedSkeinDatum q qi t δ (E q qi t δ) (F q qi t δ) where
  cross := cross q qi t δ
  T := gen .T
  T_sideways := by
    simp only [sideways, cross, coevaluation_eq, evaluation_eq, gen]
    os_unfold
    exact rel_eq .TS rfl rfl _ _ (by path_simp) (by path_simp)
  sideways_T := by
    simp only [sideways, cross, coevaluation_eq, evaluation_eq, gen]
    os_unfold
    exact rel_eq .ST rfl rfl _ _ (by path_simp) (by path_simp)
  dim := by
    simp only [coevaluation_eq, evaluation_eq, gen]
    os_unfold
    simp only [← homMk_smul]
    exact rel_eq .dim rfl rfl _ _ (by path_simp) (by path_simp)

end OSCat

end

end QOU.OrientedSkein.OS
