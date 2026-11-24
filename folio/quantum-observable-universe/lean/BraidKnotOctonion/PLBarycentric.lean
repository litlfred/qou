/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLDerived
import Mathlib.Algebra.BigOperators.Field

set_option autoImplicit false

/-!
# The barycentric subdivision (issue #8902, Moise build part A)

## What is a DEFINITION here

* `bary σ` — the barycentre `(#σ)⁻¹ • ∑ v ∈ σ, v`.
* `lam C μ u` — the vertex weight `∑ σ ∈ C with u ∈ σ, μ σ / #σ` of the combination
  `∑ σ ∈ C, μ σ • bary σ`.

## What is a THEOREM here

* `sum_smul_bary` — `∑ σ ∈ C, μ σ • bary σ = ∑ u ∈ T, lam C μ u • u` when every `σ ⊆ T`.
* `coords_unique` — affine coordinates on an affinely independent `T` are unique.
* `lam_gap` — on a chain, a face `σ` with weight `μ σ` separates: `lam u + μ σ / #σ ≤ lam w` for
  `w ∈ σ`, `u ∉ σ`.
* `exists_level_face` — a vertex of positive weight lies in a face of positive weight on which its
  weight is the least.
* `mem_of_pos_of_eq` — two chain representations of one point use the same faces of positive
  weight.
* `eq_zero_of_not_subset` — a face of positive weight lies in any face whose hull contains the
  point.
* `baryComplex K` — the barycentric subdivision is a simplicial complex: its faces are the images
  under `bary` of the chains of faces of `K`.
* `exists_chain_of_weights`, `baryComplex_space` — it has the same space as `K`.
* `baryComplex_faces_finite`, `subdivides_baryComplex`, `isDerived_baryComplex`.
* `exists_derived` — **every triangulation of `P` has a derived subdivision triangulating `P`.**
-/

namespace QOU.MathlibExt.PL

open Set Geometry Finset

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- The **barycentre** of a finite set. -/
noncomputable def bary (σ : Finset E) : E := ((σ.card : ℝ))⁻¹ • ∑ v ∈ σ, v

lemma bary_eq_centerMass {σ : Finset E} (hσ : σ.Nonempty) :
    ∃ w : E → ℝ, (∀ v ∈ σ, 0 < w v) ∧ ∑ v ∈ σ, w v = 1 ∧ bary σ = σ.centerMass w id := by
  have hc : (σ.card : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr hσ.card_pos.ne'
  refine ⟨fun _ => ((σ.card : ℝ))⁻¹, fun _ _ => inv_pos.mpr (by positivity), ?_, ?_⟩
  · rw [sum_const, nsmul_eq_mul, mul_inv_cancel₀ hc]
  · rw [centerMass, sum_const, nsmul_eq_mul, mul_inv_cancel₀ hc, inv_one, one_smul, bary,
      smul_sum]
    rfl

lemma bary_mem_convexHull {σ : Finset E} (hσ : σ.Nonempty) :
    bary σ ∈ convexHull ℝ (σ : Set E) := by
  obtain ⟨w, hw0, hw1, he⟩ := bary_eq_centerMass hσ
  rw [he]
  exact σ.centerMass_mem_convexHull (fun v hv => (hw0 v hv).le) (by rw [hw1]; exact one_pos)
    fun v hv => hv

/-- **Affine coordinates are unique.** -/
theorem coords_unique {T : Finset E} (hT : AffineIndependent ℝ ((↑) : T → E)) {α β : E → ℝ}
    (hα : ∑ u ∈ T, α u = 1) (hβ : ∑ u ∈ T, β u = 1)
    (h : ∑ u ∈ T, α u • u = ∑ u ∈ T, β u • u) : ∀ u ∈ T, α u = β u := by
  have hα' : ∑ i : T, α i = 1 := by rw [sum_coe_sort T α]; exact hα
  have hβ' : ∑ i : T, β i = 1 := by rw [sum_coe_sort T β]; exact hβ
  have key := (affineIndependent_iff_eq_of_fintype_affineCombination_eq ℝ _).mp hT
    (fun i => α i) (fun i => β i) hα' hβ' (by
      rw [Finset.affineCombination_eq_linear_combination _ _ _ hα',
        Finset.affineCombination_eq_linear_combination _ _ _ hβ',
        sum_coe_sort T (fun u => α u • u), sum_coe_sort T (fun u => β u • u)]
      exact h)
  exact fun u hu => congrFun key ⟨u, hu⟩

variable [DecidableEq E]

/-- The **vertex weight** of `u` in `∑ σ ∈ C, μ σ • bary σ`. -/
noncomputable def lam (C : Finset (Finset E)) (μ : Finset E → ℝ) (u : E) : ℝ :=
  ∑ σ ∈ C, if u ∈ σ then μ σ / σ.card else 0

lemma sum_smul_bary {T : Finset E} {C : Finset (Finset E)} (hC : ∀ σ ∈ C, σ ⊆ T)
    (μ : Finset E → ℝ) : ∑ σ ∈ C, μ σ • bary σ = ∑ u ∈ T, lam C μ u • u := by
  simp only [lam, sum_smul]
  rw [sum_comm]
  refine sum_congr rfl fun σ hσ => ?_
  simp only [ite_smul, zero_smul]
  rw [sum_ite_mem, Finset.inter_eq_right.mpr (hC σ hσ), bary, smul_sum, smul_sum]
  refine sum_congr rfl fun u _ => ?_
  rw [smul_smul, div_eq_mul_inv]

omit [NormedAddCommGroup E] [NormedSpace ℝ E] in
lemma sum_lam {T : Finset E} {C : Finset (Finset E)} (hC : ∀ σ ∈ C, σ ⊆ T ∧ σ.Nonempty)
    (μ : Finset E → ℝ) : ∑ u ∈ T, lam C μ u = ∑ σ ∈ C, μ σ := by
  simp only [lam]
  rw [sum_comm]
  refine sum_congr rfl fun σ hσ => ?_
  rw [sum_ite_mem, Finset.inter_eq_right.mpr (hC σ hσ).1, sum_const, nsmul_eq_mul]
  have hc : (σ.card : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (hC σ hσ).2.card_pos.ne'
  field_simp

omit [NormedAddCommGroup E] [NormedSpace ℝ E] in
lemma lam_nonneg {C : Finset (Finset E)} {μ : Finset E → ℝ} (hμ : ∀ σ ∈ C, 0 ≤ μ σ) (u : E) :
    0 ≤ lam C μ u :=
  sum_nonneg fun σ hσ => by split_ifs <;> [exact div_nonneg (hμ σ hσ) (Nat.cast_nonneg _); rfl]

omit [NormedAddCommGroup E] [NormedSpace ℝ E] in
lemma le_lam {C : Finset (Finset E)} {μ : Finset E → ℝ} (hμ : ∀ σ ∈ C, 0 ≤ μ σ) {σ : Finset E}
    (hσ : σ ∈ C) {u : E} (hu : u ∈ σ) : μ σ / σ.card ≤ lam C μ u := by
  have := single_le_sum (f := fun τ => if u ∈ τ then μ τ / τ.card else 0)
    (fun τ hτ => by
      dsimp only
      split_ifs <;> [exact div_nonneg (hμ τ hτ) (Nat.cast_nonneg _); rfl]) hσ
  simpa [hu] using this

omit [NormedAddCommGroup E] [NormedSpace ℝ E] in
lemma lam_term_nonneg {C : Finset (Finset E)} {μ : Finset E → ℝ} (hμ : ∀ σ ∈ C, 0 ≤ μ σ)
    {τ : Finset E} (hτ : τ ∈ C) (u : E) : 0 ≤ if u ∈ τ then μ τ / τ.card else 0 := by
  split_ifs <;> [exact div_nonneg (hμ τ hτ) (Nat.cast_nonneg _); rfl]

omit [NormedAddCommGroup E] [NormedSpace ℝ E] in
/-- **The gap at a face of a chain.** -/
theorem lam_gap {C : Finset (Finset E)} {μ : Finset E → ℝ} (hμ : ∀ σ ∈ C, 0 ≤ μ σ)
    (hch : ∀ σ ∈ C, ∀ τ ∈ C, σ ⊆ τ ∨ τ ⊆ σ) {σ : Finset E} (hσ : σ ∈ C) {w u : E}
    (hw : w ∈ σ) (hu : u ∉ σ) : lam C μ u + μ σ / σ.card ≤ lam C μ w := by
  have e : lam C μ u + μ σ / σ.card = ∑ τ ∈ C, ((if u ∈ τ then μ τ / τ.card else 0) +
      if τ = σ then μ σ / σ.card else 0) := by
    rw [sum_add_distrib, sum_ite_eq' C σ, if_pos hσ]
    rfl
  rw [e, lam]
  refine sum_le_sum fun τ hτ => ?_
  by_cases hτσ : τ = σ
  · subst hτσ
    simp [hu, hw]
  · rw [if_neg hτσ, add_zero]
    by_cases huτ : u ∈ τ
    · have hwτ : w ∈ τ := by
        rcases hch σ hσ τ hτ with h | h
        · exact h hw
        · exact absurd (h huτ) hu
      simp [huτ, hwτ]
    · rw [if_neg huτ]
      exact lam_term_nonneg hμ hτ w

omit [NormedAddCommGroup E] [NormedSpace ℝ E] in
/-- **The level face of a vertex**: a vertex of positive weight lies in a face of positive weight
on which its weight is least. -/
theorem exists_level_face {C : Finset (Finset E)} {μ : Finset E → ℝ} (hμ : ∀ σ ∈ C, 0 ≤ μ σ)
    (hch : ∀ σ ∈ C, ∀ τ ∈ C, σ ⊆ τ ∨ τ ⊆ σ) {v : E} (hv : 0 < lam C μ v) :
    ∃ τ ∈ C, 0 < μ τ ∧ v ∈ τ ∧ ∀ w ∈ τ, lam C μ v ≤ lam C μ w := by
  set P := C.filter (fun τ => v ∈ τ ∧ 0 < μ τ) with hPdef
  have hP : P.Nonempty := by
    by_contra hP
    rw [Finset.not_nonempty_iff_eq_empty] at hP
    apply hv.ne'
    refine sum_eq_zero fun τ hτ => ?_
    split_ifs with hvτ
    · have hn : ¬ (0 < μ τ) := fun h => by
        have hm : τ ∈ P := mem_filter.mpr ⟨hτ, hvτ, h⟩
        rw [hP] at hm
        simp at hm
      rw [le_antisymm (not_lt.mp hn) (hμ τ hτ), zero_div]
    · rfl
  obtain ⟨τ0, hτ0P, hmin⟩ := P.exists_min_image card hP
  obtain ⟨hτ0, hvτ0, hμτ0⟩ := mem_filter.mp hτ0P
  refine ⟨τ0, hτ0, hμτ0, hvτ0, fun w hw => sum_le_sum fun τ hτ => ?_⟩
  by_cases hvτ : v ∈ τ
  · rcases (hμ τ hτ).lt_or_eq with hpos | hzero
    · have hsub : τ0 ⊆ τ := by
        rcases hch τ hτ τ0 hτ0 with h | h
        · rw [eq_of_subset_of_card_le h (hmin τ (mem_filter.mpr ⟨hτ, hvτ, hpos⟩))]
        · exact h
      simp [hvτ, hsub hw]
    · rw [if_pos hvτ, ← hzero, zero_div]
      split_ifs <;> rfl
  · rw [if_neg hvτ]
    exact lam_term_nonneg hμ hτ w

/-- **Two chain representations of a point use the same faces of positive weight.** -/
theorem mem_of_pos_of_eq {T : Finset E} (hT : AffineIndependent ℝ ((↑) : T → E))
    {C D : Finset (Finset E)} {μ ν : Finset E → ℝ}
    (hC : ∀ σ ∈ C, σ ⊆ T ∧ σ.Nonempty) (hD : ∀ σ ∈ D, σ ⊆ T ∧ σ.Nonempty)
    (hchC : ∀ σ ∈ C, ∀ τ ∈ C, σ ⊆ τ ∨ τ ⊆ σ) (hchD : ∀ σ ∈ D, ∀ τ ∈ D, σ ⊆ τ ∨ τ ⊆ σ)
    (hμ : ∀ σ ∈ C, 0 ≤ μ σ) (hν : ∀ σ ∈ D, 0 ≤ ν σ) (hμ1 : ∑ σ ∈ C, μ σ = 1)
    (hν1 : ∑ σ ∈ D, ν σ = 1) (h : ∑ σ ∈ C, μ σ • bary σ = ∑ σ ∈ D, ν σ • bary σ)
    {σ : Finset E} (hσ : σ ∈ C) (hpos : 0 < μ σ) : σ ∈ D := by
  have hlam : ∀ u ∈ T, lam C μ u = lam D ν u :=
    coords_unique hT (by rw [sum_lam hC, hμ1]) (by rw [sum_lam hD, hν1])
      (by rw [← sum_smul_bary (fun σ h => (hC σ h).1), ← sum_smul_bary (fun σ h => (hD σ h).1),
        h])
  obtain ⟨hσT, hσne⟩ := hC σ hσ
  obtain ⟨v, hvσ, hvmin⟩ := σ.exists_min_image (lam C μ) hσne
  have hcard : (0 : ℝ) < σ.card := Nat.cast_pos.mpr hσne.card_pos
  have hv0 : 0 < lam D ν v := by
    rw [← hlam v (hσT hvσ)]
    exact (div_pos hpos hcard).trans_le (le_lam hμ hσ hvσ)
  obtain ⟨τ, hτD, hντ, hvτ, hτmin⟩ := exists_level_face hν hchD hv0
  have hτT := (hD τ hτD).1
  suffices e : σ = τ by rw [e]; exact hτD
  ext u
  constructor
  · intro hu
    by_contra huτ
    have h1 := lam_gap hν hchD hτD hvτ huτ
    have h2 := hvmin u hu
    rw [hlam u (hσT hu), hlam v (hσT hvσ)] at h2
    have : 0 < ν τ / τ.card := div_pos hντ (Nat.cast_pos.mpr (hD τ hτD).2.card_pos)
    linarith
  · intro hu
    by_contra huσ
    have h1 := lam_gap hμ hchC hσ hvσ huσ
    have h2 := hτmin u hu
    rw [← hlam u (hτT hu), ← hlam v (hσT hvσ)] at h2
    have : 0 < μ σ / σ.card := div_pos hpos hcard
    linarith

/-- **A face of positive weight lies in any face whose hull contains the point.** -/
theorem eq_zero_of_not_subset {T F : Finset E} (hT : AffineIndependent ℝ ((↑) : T → E))
    (hFT : F ⊆ T) {C : Finset (Finset E)} {μ : Finset E → ℝ}
    (hC : ∀ σ ∈ C, σ ⊆ T ∧ σ.Nonempty) (hμ : ∀ σ ∈ C, 0 ≤ μ σ) (hμ1 : ∑ σ ∈ C, μ σ = 1)
    (hx : ∑ σ ∈ C, μ σ • bary σ ∈ convexHull ℝ (F : Set E)) {σ : Finset E} (hσ : σ ∈ C)
    (hσF : ¬ σ ⊆ F) : μ σ = 0 := by
  obtain ⟨β, -, hβ1, hβx⟩ := Finset.mem_convexHull'.mp hx
  set β' : E → ℝ := fun u => if u ∈ F then β u else 0 with hβ'def
  have hβ'1 : ∑ u ∈ T, β' u = 1 := by
    rw [hβ'def, sum_ite_mem, Finset.inter_eq_right.mpr hFT, hβ1]
  have hβ'x : ∑ u ∈ T, β' u • u = ∑ σ ∈ C, μ σ • bary σ := by
    simp only [hβ'def, ite_smul, zero_smul]
    rw [sum_ite_mem, Finset.inter_eq_right.mpr hFT, hβx]
  have hlam := coords_unique hT (by rw [sum_lam hC, hμ1]) hβ'1
    (by rw [← sum_smul_bary (fun σ h => (hC σ h).1), hβ'x])
  obtain ⟨u, huσ, huF⟩ := Finset.not_subset.mp hσF
  have h1 := le_lam hμ hσ huσ
  rw [hlam u ((hC σ hσ).1 huσ)] at h1
  simp only [hβ'def, if_neg huF] at h1
  have hcard : (0 : ℝ) < σ.card := Nat.cast_pos.mpr (hC σ hσ).2.card_pos
  rw [div_le_iff₀ hcard, zero_mul] at h1
  exact le_antisymm h1 (hμ σ hσ)

/-- Points of the hull of a chain's barycentres are chain combinations. -/
theorem mem_convexHull_image_bary_iff {T : Finset E} (hT : AffineIndependent ℝ ((↑) : T → E))
    {C : Finset (Finset E)} (hC : ∀ σ ∈ C, σ ⊆ T ∧ σ.Nonempty)
    (hch : ∀ σ ∈ C, ∀ τ ∈ C, σ ⊆ τ ∨ τ ⊆ σ) {x : E} :
    x ∈ convexHull ℝ ((C.image bary : Finset E) : Set E) ↔
      ∃ μ : Finset E → ℝ, (∀ σ ∈ C, 0 ≤ μ σ) ∧ ∑ σ ∈ C, μ σ = 1 ∧
        x = ∑ σ ∈ C, μ σ • bary σ := by
  constructor
  · intro hx
    obtain ⟨w, hw0, hw1, hwx⟩ := Finset.mem_convexHull'.mp hx
    have hinj := (affineIndependent_chain_image hT bary
      (fun σ _ hne => bary_eq_centerMass hne) C hC hch).2
    refine ⟨fun σ => w (bary σ), fun σ hσ => hw0 _ (mem_image_of_mem _ hσ), ?_, ?_⟩
    · rw [← hw1, sum_image fun a ha b hb h => hinj ha hb h]
    · rw [← hwx, sum_image fun a ha b hb h => hinj ha hb h]
  · rintro ⟨μ, hμ, hμ1, rfl⟩
    exact (convex_convexHull ℝ _).sum_mem hμ hμ1 fun σ hσ =>
      subset_convexHull ℝ _ (mem_coe.mpr (mem_image_of_mem _ hσ))

lemma convexHull_image_bary_subset {C : Finset (Finset E)} {M : Finset E}
    (hC : ∀ σ ∈ C, σ ⊆ M ∧ σ.Nonempty) :
    convexHull ℝ ((C.image bary : Finset E) : Set E) ⊆ convexHull ℝ (M : Set E) :=
  convexHull_min (fun y hy => by
    obtain ⟨σ, hσ, rfl⟩ := mem_image.mp (mem_coe.mp hy)
    exact convexHull_mono (coe_subset.mpr (hC σ hσ).1) (bary_mem_convexHull (hC σ hσ).2))
    (convex_convexHull ℝ _)

/-- A **chain of faces** of `K`: nonempty, totally ordered by inclusion. -/
def IsFaceChain (K : SimplicialComplex ℝ E) (C : Finset (Finset E)) : Prop :=
  C.Nonempty ∧ (∀ σ ∈ C, σ ∈ K.faces) ∧ ∀ σ ∈ C, ∀ τ ∈ C, σ ⊆ τ ∨ τ ⊆ σ

/-- **The barycentric subdivision** of `K`. -/
noncomputable def baryComplex (K : SimplicialComplex ℝ E) : SimplicialComplex ℝ E where
  faces := {s | ∃ C, IsFaceChain K C ∧ s = C.image bary}
  empty_notMem := by
    rintro ⟨C, ⟨hne, -, -⟩, h⟩
    exact (hne.image bary).ne_empty h.symm
  indep := by
    rintro s ⟨C, ⟨hne, hK, hch⟩, rfl⟩
    obtain ⟨M, hMC, hM⟩ := exists_max_of_chain hne hch
    exact (affineIndependent_chain_image (K.indep (hK M hMC)) bary
      (fun σ _ h => bary_eq_centerMass h) C
      (fun σ hσ => ⟨hM σ hσ, K.nonempty_of_mem_faces (hK σ hσ)⟩) hch).1
  down_closed := by
    rintro s t ⟨C, ⟨hne, hK, hch⟩, rfl⟩ hts ht
    refine ⟨C.filter (fun σ => bary σ ∈ t), ⟨?_, fun σ hσ => hK σ (mem_filter.mp hσ).1,
      fun σ hσ τ hτ => hch σ (mem_filter.mp hσ).1 τ (mem_filter.mp hτ).1⟩, ?_⟩
    · obtain ⟨y, hy⟩ := nonempty_iff_ne_empty.mpr ht
      obtain ⟨σ, hσ, rfl⟩ := mem_image.mp (hts hy)
      exact ⟨σ, mem_filter.mpr ⟨hσ, hy⟩⟩
    · ext y
      constructor
      · intro hy
        obtain ⟨σ, hσ, rfl⟩ := mem_image.mp (hts hy)
        exact mem_image.mpr ⟨σ, mem_filter.mpr ⟨hσ, hy⟩, rfl⟩
      · intro hy
        obtain ⟨σ, hσ, rfl⟩ := mem_image.mp hy
        exact (mem_filter.mp hσ).2
  inter_subset_convexHull := by
    rintro s t ⟨C, ⟨hneC, hKC, hchC⟩, rfl⟩ ⟨D, ⟨hneD, hKD, hchD⟩, rfl⟩ x ⟨hxC, hxD⟩
    obtain ⟨M1, hM1C, hM1⟩ := exists_max_of_chain hneC hchC
    obtain ⟨M2, hM2D, hM2⟩ := exists_max_of_chain hneD hchD
    have hCT : ∀ σ ∈ C, σ ⊆ M1 ∧ σ.Nonempty :=
      fun σ hσ => ⟨hM1 σ hσ, K.nonempty_of_mem_faces (hKC σ hσ)⟩
    have hDT : ∀ σ ∈ D, σ ⊆ M2 ∧ σ.Nonempty :=
      fun σ hσ => ⟨hM2 σ hσ, K.nonempty_of_mem_faces (hKD σ hσ)⟩
    have hT1 := K.indep (hKC M1 hM1C)
    have hT2 := K.indep (hKD M2 hM2D)
    have hxF := K.inter_subset_convexHull (hKC M1 hM1C) (hKD M2 hM2D)
      ⟨convexHull_image_bary_subset hCT hxC, convexHull_image_bary_subset hDT hxD⟩
    rw [← coe_inter] at hxF
    obtain ⟨μ, hμ, hμ1, rfl⟩ := (mem_convexHull_image_bary_iff hT1 hCT hchC).mp hxC
    obtain ⟨ν, hν, hν1, hxeq⟩ := (mem_convexHull_image_bary_iff hT2 hDT hchD).mp hxD
    have hFne : M1 ∩ M2 ≠ ∅ := by
      rintro h
      rw [h, coe_empty, convexHull_empty] at hxF
      exact hxF
    have hFK : M1 ∩ M2 ∈ K.faces := K.down_closed (hKC M1 hM1C) inter_subset_left hFne
    have hTF := K.indep hFK
    set C' := C.filter (fun σ => μ σ ≠ 0) with hC'def
    set D' := D.filter (fun σ => ν σ ≠ 0) with hD'def
    have hC'F : ∀ σ ∈ C', σ ⊆ M1 ∩ M2 ∧ σ.Nonempty := fun σ hσ => by
      obtain ⟨hσC, hσ0⟩ := mem_filter.mp hσ
      refine ⟨?_, (hCT σ hσC).2⟩
      by_contra h
      exact hσ0 (eq_zero_of_not_subset hT1 inter_subset_left hCT hμ hμ1 hxF hσC h)
    have hD'F : ∀ σ ∈ D', σ ⊆ M1 ∩ M2 ∧ σ.Nonempty := fun σ hσ => by
      obtain ⟨hσD, hσ0⟩ := mem_filter.mp hσ
      refine ⟨?_, (hDT σ hσD).2⟩
      by_contra h
      exact hσ0 (eq_zero_of_not_subset hT2 inter_subset_right hDT hν hν1 (hxeq ▸ hxF) hσD h)
    have hsC : ∑ σ ∈ C', μ σ • bary σ = ∑ σ ∈ C, μ σ • bary σ :=
      sum_filter_of_ne fun σ _ h hμ0 => h (by rw [hμ0, zero_smul])
    have hsD : ∑ σ ∈ D', ν σ • bary σ = ∑ σ ∈ D, ν σ • bary σ :=
      sum_filter_of_ne fun σ _ h hν0 => h (by rw [hν0, zero_smul])
    have hμ1' : ∑ σ ∈ C', μ σ = 1 := by rw [hC'def, sum_filter_ne_zero, hμ1]
    have hν1' : ∑ σ ∈ D', ν σ = 1 := by rw [hD'def, sum_filter_ne_zero, hν1]
    have key : ∀ σ ∈ C', σ ∈ D := fun σ hσ => by
      obtain ⟨hσC, hσ0⟩ := mem_filter.mp hσ
      exact (mem_filter.mp (mem_of_pos_of_eq hTF hC'F hD'F
        (fun a ha b hb => hchC a (mem_filter.mp ha).1 b (mem_filter.mp hb).1)
        (fun a ha b hb => hchD a (mem_filter.mp ha).1 b (mem_filter.mp hb).1)
        (fun a ha => hμ a (mem_filter.mp ha).1) (fun a ha => hν a (mem_filter.mp ha).1)
        hμ1' hν1' (by rw [hsC, hsD, hxeq]) hσ (lt_of_le_of_ne (hμ σ hσC) (Ne.symm hσ0)))).1
    rw [← hsC]
    exact (convex_convexHull ℝ _).sum_mem (fun σ hσ => hμ σ (mem_filter.mp hσ).1) hμ1'
      fun σ hσ => subset_convexHull ℝ _ ⟨mem_coe.mpr (mem_image_of_mem _ (mem_filter.mp hσ).1),
        mem_coe.mpr (mem_image_of_mem _ (key σ hσ))⟩

/-- **Positive weights are a chain combination of barycentres** (peel off the least weight). -/
theorem exists_chain_of_weights : ∀ (n : ℕ) (S : Finset E), S.card ≤ n → ∀ β : E → ℝ,
    (∀ u ∈ S, 0 < β u) → ∑ u ∈ S, β u = 1 →
    ∃ C : Finset (Finset E), C.Nonempty ∧ (∀ τ ∈ C, τ ⊆ S ∧ τ.Nonempty) ∧
      (∀ σ ∈ C, ∀ τ ∈ C, σ ⊆ τ ∨ τ ⊆ σ) ∧ ∃ μ : Finset E → ℝ, (∀ τ ∈ C, 0 ≤ μ τ) ∧
        ∑ τ ∈ C, μ τ = 1 ∧ ∑ u ∈ S, β u • u = ∑ τ ∈ C, μ τ • bary τ := by
  intro n
  induction n with
  | zero =>
    intro S hS β _ h1
    rw [card_eq_zero.mp (Nat.le_zero.mp hS), sum_empty] at h1
    exact absurd h1 zero_ne_one
  | succ n ih =>
  intro S hS β hβ h1
  have hSne : S.Nonempty := by
    rw [Finset.nonempty_iff_ne_empty]
    rintro rfl
    rw [sum_empty] at h1
    exact zero_ne_one h1
  obtain ⟨v0, hv0, hmin⟩ := S.exists_min_image β hSne
  set m := β v0 with hm
  set k : ℝ := (S.card : ℝ) with hk
  have hk0 : 0 < k := Nat.cast_pos.mpr hSne.card_pos
  set S' := S.filter (fun u => m < β u) with hS'def
  have hS'S : S' ⊆ S := filter_subset _ _
  have hv0S' : v0 ∉ S' := fun h => lt_irrefl _ (mem_filter.mp h).2
  have hoff : ∀ u ∈ S, u ∉ S' → β u = m := fun u hu hu' =>
    le_antisymm (not_lt.mp fun h => hu' (mem_filter.mpr ⟨hu, h⟩)) (hmin u hu)
  have hsplit : ∑ u ∈ S, β u • u = m • ∑ u ∈ S, u + ∑ u ∈ S', (β u - m) • u := by
    have e : ∑ u ∈ S', (β u - m) • u = ∑ u ∈ S, (β u - m) • u :=
      sum_filter_of_ne fun u hu h => by
        by_contra hlt
        exact h (by rw [hoff u hu fun h' => hlt (mem_filter.mp h').2, sub_self, zero_smul])
    rw [e, smul_sum, ← sum_add_distrib]
    exact sum_congr rfl fun u _ => by rw [sub_smul]; abel
  have hsplit1 : 1 = m * k + ∑ u ∈ S', (β u - m) := by
    have e : ∑ u ∈ S', (β u - m) = ∑ u ∈ S, (β u - m) :=
      sum_filter_of_ne fun u hu h => by
        by_contra hlt
        exact h (by rw [hoff u hu fun h' => hlt (mem_filter.mp h').2, sub_self])
    rw [e, sum_sub_distrib, sum_const, nsmul_eq_mul, h1, hk]
    ring
  have hbary : m • ∑ u ∈ S, u = (m * k) • bary S := by
    rw [bary, smul_smul, mul_assoc, mul_inv_cancel₀ hk0.ne', mul_one]
  rcases S'.eq_empty_or_nonempty with hS'e | hS'ne
  · refine ⟨{S}, singleton_nonempty _, fun τ hτ => by
      rw [mem_singleton.mp hτ]; exact ⟨subset_refl _, hSne⟩, fun σ hσ τ hτ => by
      rw [mem_singleton.mp hσ, mem_singleton.mp hτ]; exact Or.inl (subset_refl _),
      fun _ => 1, fun _ _ => zero_le_one, by simp, ?_⟩
    have hmk : m * k = 1 := by
      rw [hS'e, sum_empty, add_zero] at hsplit1
      exact hsplit1.symm
    rw [hsplit, hS'e, sum_empty, add_zero, hbary, hmk, sum_singleton]
  · set r := ∑ u ∈ S', (β u - m) with hr
    have hr0 : 0 < r := sum_pos (fun u hu => sub_pos.mpr (mem_filter.mp hu).2) hS'ne
    have hcard : S'.card ≤ n := by
      have := card_lt_card (ssubset_of_subset_of_ne hS'S fun h => hv0S' (h ▸ hv0))
      omega
    obtain ⟨C', hC'ne, hC', hch', μ', hμ', hμ'1, he'⟩ := ih S' hcard (fun u => (β u - m) / r)
      (fun u hu => div_pos (sub_pos.mpr (mem_filter.mp hu).2) hr0)
      (by
        show ∑ u ∈ S', (β u - m) / r = 1
        rw [← Finset.sum_div, ← hr, div_self hr0.ne'])
    have hSC' : S ∉ C' := fun h => hv0S' ((hC' S h).1 hv0)
    refine ⟨insert S C', insert_nonempty _ _, ?_, ?_,
      fun τ => if τ = S then m * k else r * μ' τ, ?_, ?_, ?_⟩
    · intro τ hτ
      rcases mem_insert.mp hτ with rfl | hτ
      · exact ⟨subset_refl _, hSne⟩
      · exact ⟨(hC' τ hτ).1.trans hS'S, (hC' τ hτ).2⟩
    · intro σ hσ τ hτ
      rcases mem_insert.mp hσ with h1 | h1 <;> rcases mem_insert.mp hτ with h2 | h2
      · rw [h1, h2]
        exact Or.inl (subset_refl _)
      · rw [h1]
        exact Or.inr ((hC' τ h2).1.trans hS'S)
      · rw [h2]
        exact Or.inl ((hC' σ h1).1.trans hS'S)
      · exact hch' σ h1 τ h2
    · intro τ hτ
      show 0 ≤ if τ = S then m * k else r * μ' τ
      split_ifs with h
      · exact mul_nonneg (hβ v0 hv0).le hk0.le
      · exact mul_nonneg hr0.le (hμ' τ ((mem_insert.mp hτ).resolve_left h))
    · have hne : ∀ τ ∈ C', τ ≠ S := fun τ hτ h => hSC' (h ▸ hτ)
      show (∑ τ ∈ insert S C', if τ = S then m * k else r * μ' τ) = 1
      rw [sum_insert hSC', if_pos rfl, sum_congr rfl fun τ hτ => if_neg (hne τ hτ), ← mul_sum,
        hμ'1, mul_one, ← hsplit1]
    · have hne : ∀ τ ∈ C', τ ≠ S := fun τ hτ h => hSC' (h ▸ hτ)
      show ∑ u ∈ S, β u • u = ∑ τ ∈ insert S C', (if τ = S then m * k else r * μ' τ) • bary τ
      rw [sum_insert hSC', if_pos rfl]
      have e2 : ∑ τ ∈ C', (if τ = S then m * k else r * μ' τ) • bary τ =
          r • ∑ τ ∈ C', μ' τ • bary τ := by
        rw [smul_sum]
        exact sum_congr rfl fun τ hτ => by rw [if_neg (hne τ hτ), mul_smul]
      rw [e2, ← he', hsplit, hbary, smul_sum]
      congr 1
      refine sum_congr rfl fun u _ => ?_
      rw [smul_smul]
      congr 1
      field_simp

/-- **The barycentric subdivision has the same space.** -/
theorem baryComplex_space (K : SimplicialComplex ℝ E) : (baryComplex K).space = K.space := by
  ext x
  simp only [SimplicialComplex.space, mem_iUnion, exists_prop]
  constructor
  · rintro ⟨s, ⟨C, ⟨hne, hK, hch⟩, rfl⟩, hx⟩
    obtain ⟨M, hMC, hM⟩ := exists_max_of_chain hne hch
    exact ⟨M, hK M hMC, convexHull_image_bary_subset
      (fun σ hσ => ⟨hM σ hσ, K.nonempty_of_mem_faces (hK σ hσ)⟩) hx⟩
  · rintro ⟨σ, hσ, hx⟩
    obtain ⟨β, hβ0, hβ1, hβx⟩ := Finset.mem_convexHull'.mp hx
    set S := σ.filter (fun u => β u ≠ 0) with hSdef
    have hS1 : ∑ u ∈ S, β u = 1 := by rw [hSdef, sum_filter_ne_zero, hβ1]
    have hSx : ∑ u ∈ S, β u • u = x := by
      have e := sum_filter_of_ne (s := σ) (f := fun u => β u • u) (p := fun u => β u ≠ 0)
        fun u _ h hb => h (by dsimp only; rw [hb, zero_smul])
      rw [hSdef, e, hβx]
    obtain ⟨C, hne, hC, hch, μ, hμ, hμ1, he⟩ := exists_chain_of_weights S.card S le_rfl β
      (fun u hu => lt_of_le_of_ne (hβ0 u (mem_filter.mp hu).1) (Ne.symm (mem_filter.mp hu).2))
      hS1
    have hSσ : S ⊆ σ := filter_subset _ _
    refine ⟨C.image bary, ⟨C, ⟨hne, fun τ hτ => K.down_closed hσ ((hC τ hτ).1.trans hSσ)
      (hC τ hτ).2.ne_empty, hch⟩, rfl⟩, ?_⟩
    rw [← hSx, he]
    exact (convex_convexHull ℝ _).sum_mem hμ hμ1 fun τ hτ =>
      subset_convexHull ℝ _ (mem_coe.mpr (mem_image_of_mem _ hτ))

theorem baryComplex_faces_finite {K : SimplicialComplex ℝ E} (hK : K.faces.Finite) :
    (baryComplex K).faces.Finite := by
  refine ((hK.toFinset.powerset : Finset (Finset (Finset E))).finite_toSet.image
    (fun C => C.image bary)).subset ?_
  rintro s ⟨C, ⟨-, hKC, -⟩, rfl⟩
  exact ⟨C, mem_coe.mpr (mem_powerset.mpr fun σ hσ => hK.mem_toFinset.mpr (hKC σ hσ)), rfl⟩

theorem subdivides_baryComplex (K : SimplicialComplex ℝ E) : Subdivides (baryComplex K) K := by
  refine ⟨baryComplex_space K, ?_⟩
  rintro s ⟨C, ⟨hne, hK, hch⟩, rfl⟩
  obtain ⟨M, hMC, hM⟩ := exists_max_of_chain hne hch
  exact ⟨M, hK M hMC, convexHull_image_bary_subset
    (fun σ hσ => ⟨hM σ hσ, K.nonempty_of_mem_faces (hK σ hσ)⟩)⟩

theorem isDerived_baryComplex (K : SimplicialComplex ℝ E) : IsDerived (baryComplex K) K := by
  refine ⟨bary, fun σ hσ => bary_eq_centerMass (K.nonempty_of_mem_faces hσ), ?_⟩
  ext s
  constructor
  · rintro ⟨C, ⟨hne, hK, hch⟩, rfl⟩
    exact ⟨C, hne, hK, hch, coe_image⟩
  · rintro ⟨C, hne, hK, hch, h⟩
    exact ⟨C, ⟨hne, hK, hch⟩, coe_injective (by rw [h, coe_image])⟩

/-- **Derived subdivisions exist**: a triangulation of `P` has a derived subdivision that also
triangulates `P`. -/
theorem exists_derived {K : SimplicialComplex ℝ E} {P : Set E} (hK : Triangulates K P) :
    ∃ K' : SimplicialComplex ℝ E, IsDerived K' K ∧ Subdivides K' K ∧ Triangulates K' P :=
  ⟨baryComplex K, isDerived_baryComplex K, subdivides_baryComplex K,
    baryComplex_faces_finite hK.1, (baryComplex_space K).trans hK.2⟩

end QOU.MathlibExt.PL
