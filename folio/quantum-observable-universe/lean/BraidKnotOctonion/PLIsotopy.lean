/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLMaps
import BraidKnotOctonion.PLAmbientIsotopy

set_option autoImplicit false

/-!
# PL ambient isotopy of polygonal links (issue #8902, stage 2, part 8)

Owner ruling 2026-11-21 ("Both"): after the topological version, PL isotopy and the proof that
the two agree. This file defines the PL version.

## What is a DEFINITION here

* `AmbientIsotopy.track I : ℝ × E → E`, `(t, x) ↦ H (clamp t) x`, with `clamp` the projection
  of `ℝ` onto `[0, 1]`. `trackInv` is the same with `(H _)⁻¹`.
* `PLAmbientIsotopic L L'` — some ambient isotopy from `L` to `L'` has a **PL track**.

## What is a THEOREM here

* `IsPL.prodMk`, `IsPL.fst`, `IsPL.snd`, `IsPL.const`, `IsPL.add` — closure of PL maps.
* `AmbientIsotopy.isPL_trackInv` — in finite dimension, if the track is PL, so is the inverse
  track. It is the second coordinate of the inverse of the level-preserving PL bijection
  `(t, x) ↦ (t, track (t, x))` of `ℝ × E`, and inverses of PL bijections are PL (`IsPL.of_leftInverse`).
* `PLAmbientIsotopic.refl`, `.symm`, `.trans` — PL ambient isotopy is an equivalence relation
  (in finite dimension; `refl` and `trans` need none).
* `PLAmbientIsotopic.ambientIsotopic` — a PL ambient isotopy is an ambient isotopy.

## What is NOT proved here

* That a Δ-move is a PL ambient isotopy (next part), nor the converse.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E F G : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [NormedAddCommGroup G] [NormedSpace ℝ G]

namespace IsPL

lemma const (c : F) : IsPL (fun _ : E => c) := by
  have := affine (ContinuousAffineMap.const ℝ E c)
  simpa using this

lemma fst : IsPL (Prod.fst : E × F → E) := by
  have := affine (ContinuousLinearMap.fst ℝ E F).toContinuousAffineMap
  simpa using this

lemma snd : IsPL (Prod.snd : E × F → F) := by
  have := affine (ContinuousLinearMap.snd ℝ E F).toContinuousAffineMap
  simpa using this

/-- The product of two affine maps, as an affine map. -/
noncomputable def affineProd (A : E →ᴬ[ℝ] F) (B : E →ᴬ[ℝ] G) : E →ᴬ[ℝ] F × G :=
  (A.contLinear.prod B.contLinear).toContinuousAffineMap +
    ContinuousAffineMap.const ℝ E (A 0, B 0)

lemma affineProd_apply (A : E →ᴬ[ℝ] F) (B : E →ᴬ[ℝ] G) (x : E) :
    affineProd A B x = (A x, B x) := by
  simp [affineProd, affine_apply_eq A x, affine_apply_eq B x]

lemma prodMk {f : E → F} {g : E → G} (hf : IsPL f) (hg : IsPL g) :
    IsPL (fun x => (f x, g x)) := by
  obtain ⟨ι, _, K, A, hK, hKu, hfA⟩ := hf
  obtain ⟨κ, _, L, B, hL, hLu, hgB⟩ := hg
  refine ⟨ι × κ, inferInstance, fun p => K p.1 ∩ L p.2, fun p => affineProd (A p.1) (B p.2),
    fun p => (hK p.1).inter (hL p.2), ?_, ?_⟩
  · refine eq_univ_of_forall fun x => ?_
    obtain ⟨i, hi⟩ := mem_iUnion.mp (hKu ▸ mem_univ x)
    obtain ⟨j, hj⟩ := mem_iUnion.mp (hLu ▸ mem_univ x)
    exact mem_iUnion.mpr ⟨(i, j), hi, hj⟩
  · rintro ⟨i, j⟩ x ⟨hi, hj⟩
    show (f x, g x) = _
    rw [affineProd_apply, hfA i hi, hgB j hj]

lemma add {f g : E → F} (hf : IsPL f) (hg : IsPL g) : IsPL (fun x => f x + g x) := by
  have h := (affine ((ContinuousLinearMap.fst ℝ F F) +
    (ContinuousLinearMap.snd ℝ F F)).toContinuousAffineMap).comp (hf.prodMk hg)
  simpa [Function.comp_def] using h

lemma neg {f : E → F} (hf : IsPL f) : IsPL (fun x => -f x) := by
  have h := (affine (-(ContinuousLinearMap.id ℝ F)).toContinuousAffineMap).comp hf
  simpa [Function.comp_def] using h

end IsPL

/-- The clamp of `ℝ` onto the unit interval. -/
noncomputable abbrev clamp01 (t : ℝ) : unitInterval := projIcc 0 1 zero_le_one t

lemma clamp01_one_sub (t : ℝ) : clamp01 (1 - t) = unitInterval.symm (clamp01 t) := by
  apply Subtype.ext
  simp only [clamp01, unitInterval.coe_symm_eq, coe_projIcc]
  rcases le_total t 0 with h | h
  · rw [min_eq_right (by linarith : t ≤ 1), max_eq_left h,
      min_eq_left (by linarith : (1:ℝ) ≤ 1 - t), max_eq_right zero_le_one]
    ring
  rcases le_total t 1 with h' | h'
  · rw [min_eq_right h', max_eq_right h, min_eq_right (by linarith : 1 - t ≤ 1),
      max_eq_right (by linarith : (0:ℝ) ≤ 1 - t)]
  · rw [min_eq_left h', max_eq_right zero_le_one, min_eq_right (by linarith : 1 - t ≤ 1),
      max_eq_left (by linarith : 1 - t ≤ 0)]
    ring

variable {L L' L'' : PolygonalLink E}

namespace AmbientIsotopy

/-- The track `(t, x) ↦ H (clamp t) x` on `ℝ × E`. -/
noncomputable def track (I : AmbientIsotopy L L') (p : ℝ × E) : E := I.H (clamp01 p.1) p.2

/-- The inverse track `(t, y) ↦ (H (clamp t))⁻¹ y`. -/
noncomputable def trackInv (I : AmbientIsotopy L L') (p : ℝ × E) : E :=
  (I.H (clamp01 p.1)).symm p.2

/-- **The inverse track of a PL isotopy is PL** (finite dimension). -/
theorem isPL_trackInv [FiniteDimensional ℝ E] (I : AmbientIsotopy L L') (h : IsPL I.track) :
    IsPL I.trackInv := by
  have hΦ : IsPL (fun p : ℝ × E => (p.1, I.track p)) := IsPL.fst.prodMk h
  have hΨ : IsPL (fun p : ℝ × E => (p.1, I.trackInv p)) := by
    refine IsPL.of_leftInverse hΦ (fun p => ?_) (fun p => ?_)
    · simp [track, trackInv]
    · simp [track, trackInv]
  have := IsPL.snd.comp hΨ
  simpa [Function.comp_def] using this

lemma track_refl (L : PolygonalLink E) (p : ℝ × E) : (AmbientIsotopy.refl L).track p = p.2 :=
  rfl

lemma track_trans (I : AmbientIsotopy L L') (J : AmbientIsotopy L' L'') (p : ℝ × E) :
    (I.trans J).track p = J.track (p.1, I.track p) :=
  rfl

lemma track_symm (I : AmbientIsotopy L L') (p : ℝ × E) :
    I.symm.track p = I.track (1 - p.1, I.trackInv (1, p.2)) := by
  simp only [track, trackInv, AmbientIsotopy.symm, Homeomorph.trans_apply, clamp01_one_sub]
  have : clamp01 1 = 1 := Subtype.ext (by simp [clamp01])
  rw [this]

end AmbientIsotopy

/-- Two oriented polygonal links are **PL ambient isotopic**: some ambient isotopy between them
has a PL track. -/
def PLAmbientIsotopic (L L' : PolygonalLink E) : Prop :=
  ∃ I : AmbientIsotopy L L', IsPL I.track

namespace PLAmbientIsotopic

/-- **A PL ambient isotopy is an ambient isotopy.** -/
theorem ambientIsotopic (h : PLAmbientIsotopic L L') : AmbientIsotopic L L' :=
  let ⟨I, _⟩ := h; ⟨I⟩

theorem refl (L : PolygonalLink E) : PLAmbientIsotopic L L :=
  ⟨AmbientIsotopy.refl L, by
    have : (AmbientIsotopy.refl L).track = Prod.snd := funext (AmbientIsotopy.track_refl L)
    rw [this]
    exact IsPL.snd⟩

theorem trans (h : PLAmbientIsotopic L L') (h' : PLAmbientIsotopic L' L'') :
    PLAmbientIsotopic L L'' := by
  obtain ⟨I, hI⟩ := h
  obtain ⟨J, hJ⟩ := h'
  refine ⟨I.trans J, ?_⟩
  have : (I.trans J).track = J.track ∘ (fun p => (p.1, I.track p)) :=
    funext (AmbientIsotopy.track_trans I J)
  rw [this]
  exact hJ.comp (IsPL.fst.prodMk hI)

theorem symm [FiniteDimensional ℝ E] (h : PLAmbientIsotopic L L') : PLAmbientIsotopic L' L := by
  obtain ⟨I, hI⟩ := h
  refine ⟨I.symm, ?_⟩
  have : I.symm.track =
      I.track ∘ (fun p : ℝ × E => (1 + -p.1, I.trackInv (1, p.2))) := by
    funext p
    rw [AmbientIsotopy.track_symm, Function.comp_apply, ← sub_eq_add_neg]
  rw [this]
  refine hI.comp ((IsPL.const 1).add IsPL.fst.neg |>.prodMk ?_)
  exact (I.isPL_trackInv hI).comp ((IsPL.const 1).prodMk IsPL.snd)

end PLAmbientIsotopic

end QOU.MathlibExt.PL
