/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLTriangulation
import Mathlib.Analysis.Convex.Join
import Mathlib.Tactic.Module

set_option autoImplicit false

/-!
# The cone on a complex (issue #8902, Moise build part A, for part B's Schoenflies)

The cone `p * K` on a simplicial complex `K` with apex `p`: the faces of `K`, the apex `{p}`, and
`insert p σ` for every face `σ` of `K`. It is a simplicial complex as soon as `p ∉ K.space` and each
ray from `p` meets `K.space` at most once.

## What is a DEFINITION here

* `RaysMeetOnce p S` — each ray from `p` meets `S` at most once:
  `x - p = t • (y - p)` with `t > 0` and `x, y ∈ S` forces `x = y`.
* `coneComplex K p hp hray` — the cone.

## What is a THEOREM here

* `notMem_affineSpan_of_rays` — if `p ∉ S`, rays from `p` meet `S` at most once and
  `convexHull σ ⊆ S`, then `p ∉ affineSpan σ`. (Push the centroid of `σ` away from `p`: it stays in
  `convexHull σ` and on the same ray.)
* `affineIndependent_insert` — adding a point outside the affine span keeps independence.
* `mem_convexHull_insert_iff` — `x ∈ convexHull (insert p σ)` iff `x = p` or
  `x = p + b • (y - p)` with `y ∈ convexHull σ`, `b ∈ [0, 1]`.
* `coneComplex_space` — `(p * K).space = insert p (convexJoin ℝ {p} K.space)`.
* `coneComplex_faces_finite`, `isSubcomplex_coneComplex`, `mem_coneComplex_faces`.
-/

namespace QOU.MathlibExt.PL

open Set Geometry

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- Each ray from `p` meets `S` at most once. -/
def RaysMeetOnce (p : E) (S : Set E) : Prop :=
  ∀ x ∈ S, ∀ y ∈ S, ∀ t : ℝ, 0 < t → x - p = t • (y - p) → x = y

/-- **A point seeing `S` along rays is outside the affine span of each simplex in `S`.** -/
theorem notMem_affineSpan_of_rays {p : E} {S : Set E} (hray : RaysMeetOnce p S) (hp : p ∉ S)
    {σ : Finset E} (hσ : convexHull ℝ (σ : Set E) ⊆ S) : p ∉ affineSpan ℝ (σ : Set E) := by
  intro hpσ
  rcases σ.eq_empty_or_nonempty with rfl | hne
  · simp only [Finset.coe_empty, AffineSubspace.span_empty] at hpσ
    exact AffineSubspace.notMem_bot ℝ E p hpσ
  have hrange : (σ : Set E) = Set.range ((↑) : σ → E) := by ext x; simp
  rw [hrange] at hpσ
  obtain ⟨w, hw1, hpw⟩ := eq_affineCombination_of_mem_affineSpan_of_fintype hpσ
  rw [Finset.affineCombination_eq_linear_combination _ _ _ hw1] at hpw
  haveI : Nonempty σ := ⟨⟨_, hne.choose_spec⟩⟩
  obtain ⟨n, hndef⟩ : ∃ n : ℝ, n = Fintype.card σ := ⟨_, rfl⟩
  have hn : 0 < n := by rw [hndef]; exact_mod_cast Fintype.card_pos
  obtain ⟨M, hMdef⟩ : ∃ M : ℝ, M = ∑ i, |w i| := ⟨_, rfl⟩
  have hM : 0 ≤ M := hMdef ▸ Finset.sum_nonneg fun i _ => abs_nonneg _
  obtain ⟨ε, hεdef⟩ : ∃ ε : ℝ, ε = (n * (1 + M))⁻¹ := ⟨_, rfl⟩
  have hε : 0 < ε := hεdef ▸ inv_pos.mpr (mul_pos hn (by linarith))
  have hεn : ε * (1 + M) = n⁻¹ := by
    rw [hεdef, mul_inv, mul_assoc, inv_mul_cancel₀ (by linarith : (1 + M) ≠ 0), mul_one]
  have hmem : ∀ v : σ → ℝ, (∀ i, 0 ≤ v i) → ∑ i, v i = 1 →
      ∑ i : σ, v i • (i : E) ∈ S := fun v h0 h1 =>
    hσ ((convex_convexHull ℝ _).sum_mem (fun i _ => h0 i) h1 fun i _ => subset_convexHull ℝ _ i.2)
  have hsumn : ∑ _i : σ, n⁻¹ = 1 := by
    rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, ← hndef]
    exact mul_inv_cancel₀ hn.ne'
  obtain ⟨x0, hx0def⟩ : ∃ x0 : E, x0 = ∑ i : σ, n⁻¹ • (i : E) := ⟨_, rfl⟩
  obtain ⟨z, hzdef⟩ : ∃ z : E, z = ∑ i : σ, ((1 + ε) * n⁻¹ - ε * w i) • (i : E) :=
    ⟨_, rfl⟩
  have hx0 : x0 ∈ S := hx0def ▸ hmem _ (fun _ => inv_nonneg.mpr hn.le) hsumn
  have hz : z ∈ S := by
    refine hzdef ▸ hmem _ (fun i => ?_) ?_
    · have h1 : |w i| ≤ M := hMdef ▸
        Finset.single_le_sum (f := fun i => |w i|) (fun i _ => abs_nonneg _) (Finset.mem_univ i)
      have h2 : ε * w i ≤ ε * M := mul_le_mul_of_nonneg_left ((le_abs_self _).trans h1) hε.le
      have h3 : ε * M ≤ ε * (1 + M) := mul_le_mul_of_nonneg_left (by linarith) hε.le
      have h4 : n⁻¹ ≤ (1 + ε) * n⁻¹ :=
        le_mul_of_one_le_left (inv_nonneg.mpr hn.le) (by linarith)
      linarith
    · rw [Finset.sum_sub_distrib, ← Finset.mul_sum, ← Finset.mul_sum, hsumn, hw1]
      ring
  have hzx : z = (1 + ε) • x0 - ε • p := by
    rw [hzdef, hx0def, hpw]
    simp only [sub_smul, Finset.sum_sub_distrib, mul_smul, ← Finset.smul_sum]
  have hray' : z - p = (1 + ε) • (x0 - p) := by rw [hzx]; module
  have hzx0 := hray z hz x0 hx0 (1 + ε) (by linarith) hray'
  rw [hzx0] at hray'
  have h5 : ε • (x0 - p) = 0 := by
    calc ε • (x0 - p) = (1 + ε) • (x0 - p) - (x0 - p) := by module
      _ = 0 := by rw [← hray', sub_self]
  rcases smul_eq_zero.mp h5 with h | h
  · exact hε.ne' h
  · exact hp (sub_eq_zero.mp h ▸ hx0)

/-- **Adding a point outside the affine span keeps affine independence.** -/
theorem affineIndependent_insert [DecidableEq E] {p : E} {σ : Finset E}
    (hσ : AffineIndependent ℝ ((↑) : σ → E)) (hp : p ∉ affineSpan ℝ (σ : Set E)) :
    AffineIndependent ℝ ((↑) : ↥(insert p σ) → E) := by
  let i : ↥(insert p σ) := ⟨p, Finset.mem_insert_self p σ⟩
  have hmemσ : ∀ y : ↥(insert p σ), y ≠ i → (y : E) ∈ σ := fun y hy =>
    (Finset.mem_insert.mp y.2).resolve_left fun h => hy (Subtype.ext h)
  refine AffineIndependent.affineIndependent_of_notMem_span (i := i) ?_ ?_
  · let e : {y : ↥(insert p σ) // y ≠ i} ↪ σ :=
      ⟨fun y => ⟨y.1.1, hmemσ y.1 y.2⟩, fun a b h => by
        have h' := congrArg Subtype.val h
        exact Subtype.ext (Subtype.ext h')⟩
    exact hσ.comp_embedding e
  · refine fun h => hp (affineSpan_mono ℝ ?_ h)
    rintro _ ⟨y, hy, rfl⟩
    exact hmemσ y hy

/-- Points of the hull of `insert p σ`. -/
theorem mem_convexHull_insert_iff {p x : E} {σ : Set E} :
    x ∈ convexHull ℝ (insert p σ) ↔
      x = p ∨ ∃ y ∈ convexHull ℝ σ, ∃ b ∈ Icc (0 : ℝ) 1, x = p + b • (y - p) := by
  rcases σ.eq_empty_or_nonempty with rfl | hσ
  · simp [convexHull_singleton]
  rw [convexHull_insert hσ, mem_convexJoin]
  constructor
  · rintro ⟨a, ha, y, hy, hx⟩
    rw [mem_singleton_iff] at ha
    subst ha
    rw [segment_eq_image'] at hx
    obtain ⟨b, hb, rfl⟩ := hx
    exact Or.inr ⟨y, hy, b, hb, rfl⟩
  · rintro (rfl | ⟨y, hy, b, hb, rfl⟩)
    · obtain ⟨y, hy⟩ := hσ
      exact ⟨x, rfl, y, subset_convexHull ℝ _ hy, left_mem_segment ℝ _ _⟩
    · exact ⟨p, rfl, y, hy, by rw [segment_eq_image']; exact ⟨b, hb, rfl⟩⟩

/-- Two cone coordinates of the same point other than the apex have the same base point. -/
theorem eq_of_cone_coords {p : E} {S : Set E} (hray : RaysMeetOnce p S) {y y' : E} (hy : y ∈ S)
    (hy' : y' ∈ S) {b b' : ℝ} (hb : 0 ≤ b) (hb' : 0 ≤ b')
    (h : p + b • (y - p) = p + b' • (y' - p)) (hne : p + b • (y - p) ≠ p) : y = y' := by
  have hb0 : b ≠ 0 := by rintro rfl; simp at hne
  have hb0' : b' ≠ 0 := by rintro rfl; rw [h] at hne; simp at hne
  have h' : b • (y - p) = b' • (y' - p) := add_left_cancel h
  refine hray y hy y' hy' (b' / b) (div_pos (lt_of_le_of_ne hb' (Ne.symm hb0'))
    (lt_of_le_of_ne hb (Ne.symm hb0))) ?_
  rw [div_eq_inv_mul, mul_smul, ← h', inv_smul_smul₀ hb0]

section Cone

variable [DecidableEq E]

/-- **The cone `p * K`.** -/
noncomputable def coneComplex (K : SimplicialComplex ℝ E) (p : E) (hp : p ∉ K.space)
    (hray : RaysMeetOnce p K.space) : SimplicialComplex ℝ E where
  faces := K.faces ∪ {s | ∃ σ, (σ ∈ K.faces ∨ σ = ∅) ∧ s = insert p σ}
  indep := by
    rintro s (hs | ⟨σ, hσ, rfl⟩)
    · exact K.indep hs
    · have hhull : convexHull ℝ (σ : Set E) ⊆ K.space := by
        rcases hσ with hσ | rfl
        · exact K.convexHull_subset_space hσ
        · simp
      have hσi : AffineIndependent ℝ ((↑) : σ → E) := by
        rcases hσ with hσ | rfl
        · exact K.indep hσ
        · exact affineIndependent_of_subsingleton ℝ _
      exact affineIndependent_insert hσi (notMem_affineSpan_of_rays hray hp hhull)
  isRelLowerSet_faces := by
    have hne : (∅ : Finset E) ∉
        (K.faces ∪ {s | ∃ σ, (σ ∈ K.faces ∨ σ = ∅) ∧ s = insert p σ}) := by
      rintro (h | ⟨σ, -, h⟩)
      · exact K.empty_notMem h
      · exact Finset.insert_ne_empty p σ h.symm
    have hdc : ∀ {s t : Finset E}, s ∈ (K.faces ∪ {s | ∃ σ, (σ ∈ K.faces ∨ σ = ∅) ∧ s = insert p σ}) →
        t ⊆ s → t ≠ ∅ → t ∈ (K.faces ∪ {s | ∃ σ, (σ ∈ K.faces ∨ σ = ∅) ∧ s = insert p σ}) := by
      rintro s t (hs | ⟨σ, hσ, rfl⟩) hts ht
      · exact Or.inl (K.down_closed hs hts (Finset.nonempty_iff_ne_empty.mpr ht))
      have hsub : ∀ x ∈ t, x ≠ p → x ∈ σ := fun x hx hne =>
        (Finset.mem_insert.mp (hts hx)).resolve_left hne
      by_cases hpt : p ∈ t
      · refine Or.inr ⟨t.erase p, ?_, (Finset.insert_erase hpt).symm⟩
        by_cases he : t.erase p = ∅
        · exact Or.inr he
        obtain ⟨x, hx⟩ := Finset.nonempty_iff_ne_empty.mpr he
        rw [Finset.mem_erase] at hx
        rcases hσ with hσ | rfl
        · refine Or.inl (K.down_closed hσ (fun y hy => ?_)
            (Finset.nonempty_iff_ne_empty.mpr he))
          rw [Finset.mem_erase] at hy
          exact hsub y hy.2 hy.1
        · exact absurd (hsub x hx.2 hx.1) (Finset.notMem_empty x)
      · obtain ⟨x, hx⟩ := Finset.nonempty_iff_ne_empty.mpr ht
        have hxp : x ≠ p := fun h => hpt (h ▸ hx)
        rcases hσ with hσ | rfl
        · exact Or.inl (K.down_closed hσ (fun y hy => hsub y hy fun (h : y = p) => hpt (h ▸ hy))
            (Finset.nonempty_iff_ne_empty.mpr ht))
        · exact absurd (hsub x hx hxp) (Finset.notMem_empty x)
    intro s hs
    exact ⟨Finset.nonempty_iff_ne_empty.mpr (fun h => hne (h ▸ hs)),
      fun t hts ht => hdc hs hts (Finset.nonempty_iff_ne_empty.mp ht)⟩
  inter_subset_convexHull := by
    -- a point of a face of `K` and of an apex face lies in the base of the apex face
    have hKA : ∀ {s τ : Finset E}, s ∈ K.faces → (τ ∈ K.faces ∨ τ = ∅) →
        convexHull ℝ ↑s ∩ convexHull ℝ ↑(insert p τ) ⊆
          convexHull ℝ (↑s ∩ ↑(insert p τ) : Set E) := by
      rintro s τ hs hτ x ⟨hxs, hxτ⟩
      have hxS : x ∈ K.space := K.convexHull_subset_space hs hxs
      rw [Finset.coe_insert, mem_convexHull_insert_iff] at hxτ
      rcases hxτ with rfl | ⟨y, hy, b, hb, rfl⟩
      · exact absurd hxS hp
      rcases hτ with hτ | rfl
      swap
      · simp at hy
      have hyS : y ∈ K.space := K.convexHull_subset_space hτ hy
      have hb0 : 0 < b := by
        rcases hb.1.lt_or_eq with h | h
        · exact h
        · subst h
          exact absurd (by simpa using hxS) hp
      have hxy := hray _ hxS y hyS b hb0 (by rw [add_sub_cancel_left])
      have hmem := K.inter_subset_convexHull hs hτ ⟨hxs, by rw [hxy]; exact hy⟩
      refine convexHull_mono (inter_subset_inter_right _ ?_) hmem
      rw [Finset.coe_insert]
      exact subset_insert _ _
    rintro s t (hs | ⟨σ, hσ, rfl⟩) (ht | ⟨τ, hτ, rfl⟩)
    · exact K.inter_subset_convexHull hs ht
    · exact hKA hs hτ
    · rw [inter_comm, inter_comm (↑(insert p σ) : Set E)]
      exact hKA ht hσ
    · rintro x ⟨hx1, hx2⟩
      have hpmem : p ∈ convexHull ℝ (↑(insert p σ) ∩ ↑(insert p τ) : Set E) :=
        subset_convexHull ℝ _ ⟨Finset.mem_coe.mpr (Finset.mem_insert_self _ _),
          Finset.mem_coe.mpr (Finset.mem_insert_self _ _)⟩
      rw [Finset.coe_insert, mem_convexHull_insert_iff] at hx1 hx2
      rcases hx1 with rfl | ⟨y, hy, b, hb, rfl⟩
      · exact hpmem
      by_cases hxp : p + b • (y - p) = p
      · rw [hxp]
        exact hpmem
      rcases hx2 with h | ⟨y', hy', b', hb', h⟩
      · exact absurd h hxp
      rcases hσ with hσ | rfl
      swap
      · simp at hy
      rcases hτ with hτ | rfl
      swap
      · simp at hy'
      have hyy := eq_of_cone_coords hray (K.convexHull_subset_space hσ hy)
        (K.convexHull_subset_space hτ hy') hb.1 hb'.1 h hxp
      subst hyy
      have hyst := K.inter_subset_convexHull hσ hτ ⟨hy, hy'⟩
      have hsub : (↑σ ∩ ↑τ : Set E) ⊆ ↑(insert p σ) ∩ ↑(insert p τ) := by
        rw [Finset.coe_insert, Finset.coe_insert]
        exact inter_subset_inter (subset_insert _ _) (subset_insert _ _)
      refine (convex_convexHull ℝ _).segment_subset hpmem (convexHull_mono hsub hyst) ?_
      rw [segment_eq_image']
      exact ⟨b, hb, rfl⟩

variable {K : SimplicialComplex ℝ E} {p : E} {hp : p ∉ K.space} {hray : RaysMeetOnce p K.space}

lemma mem_coneComplex_faces {s : Finset E} :
    s ∈ (coneComplex K p hp hray).faces ↔
      s ∈ K.faces ∨ ∃ σ, (σ ∈ K.faces ∨ σ = ∅) ∧ s = insert p σ :=
  Iff.rfl

lemma isSubcomplex_coneComplex : IsSubcomplex K (coneComplex K p hp hray) :=
  fun _ h => Or.inl h

lemma coneComplex_faces_finite (hK : K.faces.Finite) :
    (coneComplex K p hp hray).faces.Finite := by
  refine (hK.union ((hK.union (finite_singleton ∅)).image (insert p))).subset ?_
  rintro s (h | ⟨σ, hσ, rfl⟩)
  · exact Or.inl h
  · exact Or.inr ⟨σ, hσ, rfl⟩

/-- **The space of the cone** is the union of the segments from `p` to `K.space`, and `p`. -/
theorem coneComplex_space :
    (coneComplex K p hp hray).space = insert p (convexJoin ℝ {p} K.space) := by
  ext x
  rw [SimplicialComplex.mem_space_iff, mem_insert_iff, mem_convexJoin]
  constructor
  · rintro ⟨s, hs | ⟨σ, hσ, rfl⟩, hx⟩
    · exact Or.inr ⟨p, rfl, x, K.convexHull_subset_space hs hx, right_mem_segment ℝ _ _⟩
    · rw [Finset.coe_insert, mem_convexHull_insert_iff] at hx
      rcases hx with rfl | ⟨y, hy, b, hb, rfl⟩
      · exact Or.inl rfl
      rcases hσ with hσ | rfl
      swap
      · simp at hy
      exact Or.inr ⟨p, rfl, y, K.convexHull_subset_space hσ hy, by
        rw [segment_eq_image']
        exact ⟨b, hb, rfl⟩⟩
  · rintro (rfl | ⟨a, ha, y, hy, hx⟩)
    · exact ⟨insert x ∅, Or.inr ⟨∅, Or.inr rfl, rfl⟩, subset_convexHull ℝ _ (by simp)⟩
    · rw [mem_singleton_iff] at ha
      subst ha
      obtain ⟨τ, hτ, hyτ⟩ := SimplicialComplex.mem_space_iff.mp hy
      refine ⟨insert a τ, Or.inr ⟨τ, Or.inl hτ, rfl⟩, ?_⟩
      rw [Finset.coe_insert, mem_convexHull_insert_iff]
      rw [segment_eq_image'] at hx
      obtain ⟨b, hb, rfl⟩ := hx
      exact Or.inr ⟨y, hyτ, b, hb, rfl⟩

end Cone

end QOU.MathlibExt.PL
