/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLCone

set_option autoImplicit false

/-!
# Derived subdivisions: independence of chain centres (issue #8902, Moise build part A)

A derived subdivision (`IsDerived` in `PLTriangulation.lean`) puts a point `a σ` in the open
simplex of each face `σ` and takes as faces the images of the strict chains of faces. This file
proves the first fact behind it: the centres of a chain of faces of an affinely independent set are
affinely independent, and distinct faces of the chain have distinct centres.

## What is a THEOREM here

* `sum_smul_notMem_affineSpan` — a combination of the points of an affinely independent `T` that
  puts nonzero weight on a point outside `τ ⊆ T` is not in `affineSpan τ`.
* `affineIndependent_chain_image` — for a chain `C` of nonempty faces contained in an affinely
  independent `T`, and centres `a σ` with all weights positive, `C.image a` is affinely independent
  and `a` is injective on `C`. (Induct on the largest face `M`: its centre has positive weight on a
  vertex outside the next face, which spans every other centre.)

## What is NOT proved here

That the derived subdivision is a simplicial complex with the same space as `K` (the
intersection property and the covering). For the barycentric choice `a = bary` these are proved in
`PLBarycentric.lean` (`baryComplex`, `baryComplex_space`, `exists_derived`).
-/

namespace QOU.MathlibExt.PL

open Set Geometry

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- A combination with nonzero weight off `τ` is off `affineSpan τ`. -/
theorem sum_smul_notMem_affineSpan {T τ : Finset E} (hT : AffineIndependent ℝ ((↑) : T → E))
    (hτ : τ ⊆ T) {w : E → ℝ} (hw : ∑ v ∈ T, w v = 1) {v : E} (hvT : v ∈ T) (hvτ : v ∉ τ)
    (hv : w v ≠ 0) : ∑ u ∈ T, w u • u ∉ affineSpan ℝ (τ : Set E) := by
  intro h
  have hw' : ∑ i ∈ (Finset.univ : Finset T), w i = 1 := by
    rw [Finset.sum_coe_sort T w]
    exact hw
  have himg : ((↑) : T → E) '' {i | (i : E) ∈ τ} = τ := by
    ext x
    constructor
    · rintro ⟨i, hi, rfl⟩
      exact hi
    · intro hx
      exact ⟨⟨x, hτ hx⟩, hx, rfl⟩
  have hm : (Finset.univ : Finset T).affineCombination ℝ ((↑) : T → E) (fun i => w i) ∈
      affineSpan ℝ (((↑) : T → E) '' {i | (i : E) ∈ τ}) := by
    rw [himg, Finset.affineCombination_eq_linear_combination _ _ _ hw',
      Finset.sum_coe_sort T (fun u => w u • u)]
    exact h
  exact hv (hT.eq_zero_of_affineCombination_mem_affineSpan hw' hm (Finset.mem_univ ⟨v, hvT⟩) hvτ)

omit [NormedAddCommGroup E] [NormedSpace ℝ E] in
/-- The largest face of a chain contains all the others. -/
theorem exists_max_of_chain {C : Finset (Finset E)} (hne : C.Nonempty)
    (hch : ∀ σ ∈ C, ∀ τ ∈ C, σ ⊆ τ ∨ τ ⊆ σ) : ∃ M ∈ C, ∀ σ ∈ C, σ ⊆ M := by
  obtain ⟨M, hMC, hMmax⟩ := C.exists_max_image Finset.card hne
  refine ⟨M, hMC, fun σ hσ => (hch σ hσ M hMC).elim id fun h => ?_⟩
  exact (Finset.eq_of_subset_of_card_le h (hMmax σ hσ)).ge

/-- **The centres of a chain of faces are affinely independent.** -/
theorem affineIndependent_chain_image [DecidableEq E] {T : Finset E}
    (hT : AffineIndependent ℝ ((↑) : T → E)) (a : Finset E → E)
    (ha : ∀ σ ⊆ T, σ.Nonempty → ∃ w : E → ℝ, (∀ v ∈ σ, 0 < w v) ∧ ∑ v ∈ σ, w v = 1 ∧
      a σ = σ.centerMass w id) (C : Finset (Finset E)) (hC : ∀ σ ∈ C, σ ⊆ T ∧ σ.Nonempty)
    (hch : ∀ σ ∈ C, ∀ τ ∈ C, σ ⊆ τ ∨ τ ⊆ σ) :
    AffineIndependent ℝ ((↑) : (C.image a) → E) ∧ Set.InjOn a C := by
  induction C using Finset.strongInduction with
  | H C ih =>
  rcases C.eq_empty_or_nonempty with rfl | hne
  · haveI : Subsingleton (↥((∅ : Finset (Finset E)).image a)) :=
      ⟨fun x _ => by
        obtain ⟨y, hy⟩ := x
        simp at hy⟩
    exact ⟨affineIndependent_of_subsingleton ℝ _, by simp⟩
  obtain ⟨M, hMC, hsubM⟩ := exists_max_of_chain hne hch
  have hmem : ∀ {σ}, σ ∈ C.erase M → σ ∈ C := fun h => Finset.mem_of_mem_erase h
  obtain ⟨hind, hinj⟩ := ih (C.erase M) (Finset.erase_ssubset hMC) (fun σ hσ => hC σ (hmem hσ))
    (fun σ hσ τ hτ => hch σ (hmem hσ) τ (hmem hτ))
  -- the centre of `M` is off the span of the other centres
  have hnot : a M ∉ affineSpan ℝ (((C.erase M).image a : Finset E) : Set E) := by
    rcases (C.erase M).eq_empty_or_nonempty with hemp | hne'
    · simp only [hemp, Finset.image_empty, Finset.coe_empty, AffineSubspace.span_empty]
      exact AffineSubspace.notMem_bot ℝ E _
    obtain ⟨N, hNC, hsubN⟩ := exists_max_of_chain hne'
      (fun σ hσ τ hτ => hch σ (hmem hσ) τ (hmem hτ))
    have hNM : N ⊂ M :=
      Finset.ssubset_iff_subset_ne.mpr ⟨hsubM N (hmem hNC), Finset.ne_of_mem_erase hNC⟩
    obtain ⟨v, hvM, hvN⟩ := Finset.exists_of_ssubset hNM
    obtain ⟨w, hw0, hw1, haM⟩ := ha M (hC M hMC).1 (hC M hMC).2
    have hle : affineSpan ℝ (((C.erase M).image a : Finset E) : Set E) ≤
        affineSpan ℝ (N : Set E) := by
      refine affineSpan_le.mpr ?_
      intro x hx
      rw [Finset.coe_image] at hx
      obtain ⟨σ, hσ, rfl⟩ := hx
      obtain ⟨u, hu0, hu1, haσ⟩ := ha σ (hC σ (hmem hσ)).1 (hC σ (hmem hσ)).2
      have hin : a σ ∈ convexHull ℝ (σ : Set E) := by
        rw [haσ]
        exact σ.centerMass_mem_convexHull (fun v hv => (hu0 v hv).le) (by rw [hu1]; exact one_pos)
          fun v hv => hv
      exact convexHull_subset_affineSpan _
        (convexHull_mono (Finset.coe_subset.mpr (hsubN σ hσ)) hin)
    have hTM : AffineIndependent ℝ ((↑) : M → E) :=
      hT.mono (Finset.coe_subset.mpr (hC M hMC).1)
    have haM' : a M = ∑ u ∈ M, w u • u := by
      rw [haM, Finset.centerMass_eq_of_sum_1 _ _ hw1]
      rfl
    intro h
    exact sum_smul_notMem_affineSpan hTM hNM.subset hw1 hvM hvN (hw0 v hvM).ne'
      (haM' ▸ hle h)
  rw [← Finset.insert_erase hMC, Finset.image_insert, Finset.coe_insert]
  refine ⟨affineIndependent_insert hind hnot, ?_⟩
  refine (Set.injOn_insert (by simp)).mpr ⟨hinj, ?_⟩
  rintro ⟨σ, hσ, hσM⟩
  exact hnot (subset_affineSpan ℝ _ (by rw [Finset.coe_image]; exact ⟨σ, hσ, hσM⟩))

end QOU.MathlibExt.PL
