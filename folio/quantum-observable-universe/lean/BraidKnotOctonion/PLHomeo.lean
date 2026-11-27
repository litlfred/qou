/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLIsotopy
import Mathlib.LinearAlgebra.Determinant

set_option autoImplicit false

/-!
# PL isotopies of homeomorphisms (issue #8902, Moise build part A)

The interface between a PL homeomorphism `h` of `E` and PL ambient isotopy of links: if `h` is
joined to the identity by a PL isotopy and carries `L` onto `L'`, then `L` and `L'` are PL ambient
isotopic. The Moise build (part B) produces such an `h`; part A shows it is PL isotopic to the
identity.

## What is a DEFINITION here

* `PLIsotopy h` — a family `H t` (`t ∈ [0, 1]`) of homeomorphisms of `E`, jointly continuous
  with jointly continuous inverses, from `H 0 = id` to `H 1 = h`, whose track
  `(t, x) ↦ H (clamp t) x` on `ℝ × E` is PL (`IsPL`, finitely many polyhedral pieces).
* `PLIsotopicToId h` — such an isotopy exists.
* `IsPL.OrientationPreserving f` — `f` has a PL presentation whose linear part has positive
  determinant on every piece with nonempty interior.

## What is a THEOREM here

* `PLIsotopy.refl`, `PLIsotopy.trans` — the identity is PL isotopic to itself; PL isotopies to
  `g` and to `h` give one to `h ∘ g`.
* `PLAmbientIsotopic.of_plIsotopy` — a PL isotopy from the identity to a homeomorphism carrying
  each component of `L` onto its partner in `L'` (orientation preserved) is a PL ambient isotopy.

Which homeomorphisms are PL isotopic to the identity is settled in `PLScaling.lean`: in finite
dimension, exactly the PL ones at bounded distance from the identity
(`plIsotopicToId_iff_bounded`). In particular `x ↦ 2 • x` is not, although it is linear and
orientation preserving.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- **A PL isotopy from the identity to `h`.** -/
structure PLIsotopy (h : E ≃ₜ E) where
  /-- The homeomorphism at time `t`. -/
  H : unitInterval → E ≃ₜ E
  /-- Joint continuity in time and space. -/
  continuous : Continuous fun p : unitInterval × E => H p.1 p.2
  /-- Joint continuity of the inverses. -/
  continuous_symm : Continuous fun p : unitInterval × E => (H p.1).symm p.2
  /-- It starts at the identity. -/
  start : ∀ x, H 0 x = x
  /-- It ends at `h`. -/
  finish : ∀ x, H 1 x = h x
  /-- The track on `ℝ × E` is PL. -/
  isPL : IsPL fun p : ℝ × E => H (clamp01 p.1) p.2

/-- `h` is **PL isotopic to the identity**. -/
def PLIsotopicToId (h : E ≃ₜ E) : Prop := Nonempty (PLIsotopy h)

namespace PLIsotopy

/-- The constant isotopy. -/
def refl : PLIsotopy (Homeomorph.refl E) where
  H := fun _ => Homeomorph.refl E
  continuous := continuous_snd
  continuous_symm := continuous_snd
  start := fun _ => rfl
  finish := fun _ => rfl
  isPL := IsPL.snd

/-- Run two isotopies at once: `t ↦ H t ∘ G t`, from the identity to `h ∘ g`. -/
def trans {g h : E ≃ₜ E} (G : PLIsotopy g) (I : PLIsotopy h) : PLIsotopy (g.trans h) where
  H := fun t => (G.H t).trans (I.H t)
  continuous := I.continuous.comp (continuous_fst.prodMk G.continuous)
  continuous_symm := G.continuous_symm.comp (continuous_fst.prodMk I.continuous_symm)
  start := fun x => by simp [G.start, I.start]
  finish := fun x => by simp [G.finish, I.finish]
  isPL := by
    have := I.isPL.comp (IsPL.fst.prodMk G.isPL)
    simpa [Function.comp_def] using this

end PLIsotopy

theorem PLIsotopicToId.refl : PLIsotopicToId (Homeomorph.refl E) := ⟨PLIsotopy.refl⟩

theorem PLIsotopicToId.trans {g h : E ≃ₜ E} (hg : PLIsotopicToId g) (hh : PLIsotopicToId h) :
    PLIsotopicToId (g.trans h) :=
  ⟨hg.some.trans hh.some⟩

/-- **A PL isotopy from the identity to a homeomorphism carrying `L` onto `L'` is a PL ambient
isotopy.** -/
theorem PLAmbientIsotopic.of_plIsotopy {L L' : PolygonalLink E} {h : E ≃ₜ E} (I : PLIsotopy h)
    (e : Fin L.k ≃ Fin L'.k)
    (hfin : ∀ i, ∃ φ : ℝ → ℝ, OrientedReparam φ ∧
      ∀ t, h ((L.comp i).param t) = (L'.comp (e i)).param (φ t)) :
    PLAmbientIsotopic L L' :=
  ⟨{ H := I.H
     continuous := I.continuous
     continuous_symm := I.continuous_symm
     start := I.start
     e := e
     finish := fun i => by
       obtain ⟨φ, hφ, h'⟩ := hfin i
       exact ⟨φ, hφ, fun t => by rw [I.finish]; exact h' t⟩ }, I.isPL⟩

/-- **Orientation-preserving PL map**: some PL presentation has linear parts of positive
determinant on every piece with nonempty interior. -/
def IsPL.OrientationPreserving (f : E → E) : Prop :=
  ∃ (ι : Type) (_ : Fintype ι) (K : ι → Set E) (A : ι → E →ᴬ[ℝ] E),
    (∀ i, IsPolyhedron (K i)) ∧ (⋃ i, K i) = Set.univ ∧ (∀ i, EqOn f (A i) (K i)) ∧
      ∀ i, (interior (K i)).Nonempty → 0 < LinearMap.det ((A i).contLinear : E →ₗ[ℝ] E)

lemma IsPL.OrientationPreserving.isPL {f : E → E} (h : IsPL.OrientationPreserving f) : IsPL f :=
  let ⟨ι, hι, K, A, hK, hKu, hfA, _⟩ := h; ⟨ι, hι, K, A, hK, hKu, hfA⟩

end QOU.MathlibExt.PL
