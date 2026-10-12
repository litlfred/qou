/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.Model.GLnDatum
import QOU.OrientedSkein.OS.Universal

/-!
# `QOU.OrientedSkein.Model.GLnLift` — the vector-representation functor out of `OS(z, t)`

Dispatch B of PR #7705 (bean `qou-slck`).  The universal property of the oriented skein category
(`QOU.OrientedSkein.OS.lift`) applied to the `GL_n` datum (`QOU.OrientedSkein.Model.GLnDatum`)
gives an `R`-linear monoidal functor

`glnFunctor : OS(q, qi, q^n, [n]_q) ⥤ ModuleCat R`,  `E ↦ R^n`,  `S ↦ Ř`.

**Nondegeneracy of `OS`** (`OS_cross_ne_smul`): for `n ≥ 2`, over a nontrivial ring, the crossing
generator of `OS(q, qi, q^n, [n]_q)` is not a scalar multiple of the identity of `E ⊗ E`.  The
proof pushes a putative relation `S = c · 1` through `glnFunctor` and contradicts
`GLnRMatrix.S_ne_smul_id`.  This is strictly more than `OSCat.id_unit_ne_zero` (the one-dimensional
unit model): that model sends `S` to a scalar, so it cannot separate `S` from `q · 1`.

Sorry-free; no axioms beyond Lean/Mathlib's.
-/

namespace QOU.OrientedSkein.GLn

open CategoryTheory MonoidalCategory QOU.OrientedSkein.OS

universe u

variable {R : Type u} [CommRing R] {n : ℕ} (q qi : R)

/-- The vector-representation functor `OS(q, qi, q^n, [n]_q) ⥤ ModuleCat R`, `E ↦ R^n`. -/
noncomputable abbrev glnFunctor (h : q * qi = 1) :
    OSCat q qi (q ^ n) (∑ i, wt n q qi i) ⥤ ModuleCat.{u} R :=
  lift (datum (n := n) q qi h)

/-- The functor sends the crossing of `OS` to the `GL_n` R-matrix (up to the unitors coming from
`E ↦ E ⊗ 𝟙`). -/
theorem glnFunctor_S (h : q * qi = 1) :
    (glnFunctor (n := n) q qi h).map (OSCat.cross q qi (q ^ n) (∑ i, wt n q qi i)).S =
      (X R n ◁ (ρ_ (X R n)).hom) ≫ S q qi ≫ (X R n ◁ (ρ_ (X R n)).inv) :=
  lift_S _

/-- **Nondegeneracy of `OS(q, qi, q^n, [n]_q)`.**  For `n ≥ 2` the crossing generator is not a
scalar multiple of the identity. -/
theorem OS_cross_ne_smul [Nontrivial R] (hn : 2 ≤ n) (h : q * qi = 1) (c : R) :
    (OSCat.cross q qi (q ^ n) (∑ i, wt n q qi i)).S ≠ c • 𝟙 _ := by
  intro hS
  have h1 := congrArg (glnFunctor (n := n) q qi h).map hS
  rw [glnFunctor_S, CategoryTheory.Functor.map_smul, CategoryTheory.Functor.map_id] at h1
  apply S_ne_smul_id q qi hn c
  have h2 := congrArg (fun f => (X R n ◁ (ρ_ (X R n)).inv) ≫ f ≫ (X R n ◁ (ρ_ (X R n)).hom)) h1
  simp only [← whiskerLeft_comp_assoc, Iso.inv_hom_id, whiskerLeft_id, Category.id_comp,
    Category.assoc, ← whiskerLeft_comp, Iso.inv_hom_id, Category.comp_id, Linear.smul_comp,
    Linear.comp_smul] at h2
  rw [h2]
  congr 1
  erw [Category.id_comp]
  rw [← whiskerLeft_comp, Iso.inv_hom_id, whiskerLeft_id]

end QOU.OrientedSkein.GLn
