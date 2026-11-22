/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLIsotopy
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
* `PLIsotopyToId E` — every orientation-preserving homeomorphism of `E` that is PL in both
  directions is PL isotopic to the identity. **A `Prop`, stated, not proved here.**

## What is a THEOREM here

* `PLIsotopy.refl`, `PLIsotopy.trans` — the identity is PL isotopic to itself; PL isotopies to
  `g` and to `h` give one to `h ∘ g`.
* `PLAmbientIsotopic.of_plIsotopy` — a PL isotopy from the identity to a homeomorphism carrying
  each component of `L` onto its partner in `L'` (orientation preserved) is a PL ambient isotopy.
* `PLAmbientIsotopic.of_plHomeo` — conditional on `PLIsotopyToId E`: an orientation-preserving
  PL homeomorphism carrying `L` onto `L'` gives a PL ambient isotopy.
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

variable (E) in
/-- **PL isotopy to the identity (stated, not proved).** Every orientation-preserving
homeomorphism of `E` that is PL in both directions is PL isotopic to the identity.

For `finrank ℝ E = 3` this is classical: the scaling isotopy `t • h (t⁻¹ • x)` joins `h` to its
cone at infinity, and the cone of an orientation-preserving PL homeomorphism of the 2-sphere is
PL isotopic to the identity (Alexander's trick together with the PL Schoenflies theorem in the
plane). See J. W. Alexander, *On the deformation of an n-cell*, Proc. Nat. Acad. Sci. 9 (1923)
406–407, and E. E. Moise, *Geometric Topology in Dimensions 2 and 3*, Springer GTM 47 (1977). -/
def PLIsotopyToId : Prop :=
  ∀ h : E ≃ₜ E, IsPL.OrientationPreserving h → IsPL h.symm → PLIsotopicToId h

/-- **An orientation-preserving PL homeomorphism carrying `L` onto `L'` gives a PL ambient
isotopy**, conditional on `PLIsotopyToId E`. -/
theorem PLAmbientIsotopic.of_plHomeo (hiso : PLIsotopyToId E) {L L' : PolygonalLink E}
    (h : E ≃ₜ E) (hor : IsPL.OrientationPreserving h) (hinv : IsPL h.symm)
    (e : Fin L.k ≃ Fin L'.k)
    (hfin : ∀ i, ∃ φ : ℝ → ℝ, OrientedReparam φ ∧
      ∀ t, h ((L.comp i).param t) = (L'.comp (e i)).param (φ t)) :
    PLAmbientIsotopic L L' :=
  PLAmbientIsotopic.of_plIsotopy (hiso h hor hinv).some e hfin

end QOU.MathlibExt.PL
