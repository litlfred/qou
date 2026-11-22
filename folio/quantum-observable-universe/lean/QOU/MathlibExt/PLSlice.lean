/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLTriangulation
import Mathlib.Analysis.Convex.Combination
import Mathlib.Tactic.Module

set_option autoImplicit false

/-!
# Slicing by a hyperplane (issue #8902, Moise build part A, for part B's Schoenflies)

A hyperplane `{ψ = c}` that misses the vertices of a simplex cuts it in the convex hull of the
points where it crosses the edges.

## What is a DEFINITION here

* `crossPt ψ c u v` — the point of the line `u v` where `ψ = c`:
  `(ψ v - ψ u)⁻¹ • ((ψ v - c) • u - (ψ u - c) • v)`.
* `crossSet ψ c s` — the crossing points `crossPt ψ c u v` over `u, v ∈ s` with
  `ψ u < c < ψ v`.

## What is a THEOREM here

* `map_crossPt`, `crossPt_mem_segment` — `crossPt` lies on the hyperplane and on the segment.
* `convexHull_inter_hyperplane` — **the slice of a simplex**: if `ψ ≠ c` at every point of `s`,
  `convexHull s ∩ {ψ = c} = convexHull (crossSet ψ c s)`. No affine independence is needed. For
  `x = ∑ w v • v` on the hyperplane put `A = ∑_{ψ v > c} w v (ψ v - c) = ∑_{ψ u < c} w u (c - ψ u)`;
  then `x = ∑_{u, v} (w u w v (ψ v - ψ u) / A) • crossPt u v`, with weights summing to `1`.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] (ψ : E →L[ℝ] ℝ) (c : ℝ)

/-- The point of the line through `u` and `v` where `ψ = c`. -/
noncomputable def crossPt (u v : E) : E :=
  (ψ v - ψ u)⁻¹ • ((ψ v - c) • u - (ψ u - c) • v)

/-- The crossing points of the edges of `s` with the hyperplane `{ψ = c}`. -/
noncomputable def crossSet [DecidableEq E] (s : Finset E) : Finset E :=
  ((s.filter fun u => ψ u < c) ×ˢ (s.filter fun v => c < ψ v)).image fun p => crossPt ψ c p.1 p.2

variable {ψ c}

lemma map_crossPt {u v : E} (h : ψ u ≠ ψ v) : ψ (crossPt ψ c u v) = c := by
  have h' : ψ v - ψ u ≠ 0 := sub_ne_zero.mpr (Ne.symm h)
  simp only [crossPt, map_smul, map_sub, smul_eq_mul]
  field_simp
  ring

lemma crossPt_mem_segment {u v : E} (hu : ψ u < c) (hv : c < ψ v) :
    crossPt ψ c u v ∈ segment ℝ u v := by
  have hd : 0 < ψ v - ψ u := by linarith
  refine ⟨(ψ v - c) / (ψ v - ψ u), (c - ψ u) / (ψ v - ψ u), div_nonneg (by linarith) hd.le,
    div_nonneg (by linarith) hd.le, by field_simp; ring, ?_⟩
  simp only [crossPt, div_eq_inv_mul, mul_smul]
  module

lemma crossSet_subset [DecidableEq E] (s : Finset E) :
    (crossSet ψ c s : Set E) ⊆ convexHull ℝ ↑s ∩ {x | ψ x = c} := by
  intro x hx
  simp only [crossSet, Finset.coe_image, mem_image, Finset.mem_coe, Finset.mem_product,
    Finset.mem_filter] at hx
  obtain ⟨⟨u, v⟩, ⟨⟨hus, hu⟩, hvs, hv⟩, rfl⟩ := hx
  refine ⟨segment_subset_convexHull hus hvs (crossPt_mem_segment hu hv), ?_⟩
  exact map_crossPt (by linarith)

/-- **The slice of a simplex** by a hyperplane missing its vertices. -/
theorem convexHull_inter_hyperplane [DecidableEq E] (s : Finset E) (hgen : ∀ v ∈ s, ψ v ≠ c) :
    convexHull ℝ ↑s ∩ {x | ψ x = c} = convexHull ℝ ↑(crossSet ψ c s) := by
  apply Subset.antisymm
  · rintro x ⟨hx, hψ⟩
    obtain ⟨w, hw0, hw1, rfl⟩ := Finset.mem_convexHull'.mp hx
    simp only [mem_setOf_eq, map_sum, map_smul, smul_eq_mul] at hψ
    set N := s.filter fun u => ψ u < c
    set P := s.filter fun v => c < ψ v
    have hP : s.filter (fun v => ¬ ψ v < c) = P := by
      refine Finset.filter_congr fun v hv => ?_
      constructor
      · intro h; exact lt_of_le_of_ne (not_lt.mp h) (hgen v hv).symm
      · intro h; exact not_lt.mpr h.le
    have hsplit : ∀ f : E → ℝ, ∑ v ∈ s, f v = ∑ u ∈ N, f u + ∑ v ∈ P, f v := fun f => by
      rw [← Finset.sum_filter_add_sum_filter_not s (fun v => ψ v < c), hP]
    have hsplitE : ∀ f : E → E, ∑ v ∈ s, f v = ∑ u ∈ N, f u + ∑ v ∈ P, f v := fun f => by
      rw [← Finset.sum_filter_add_sum_filter_not s (fun v => ψ v < c), hP]
    set A := ∑ v ∈ P, w v * (ψ v - c) with hAdef
    have hbal : ∑ u ∈ N, w u * (c - ψ u) = A := by
      have h0 : ∑ v ∈ s, w v * (ψ v - c) = 0 := by
        simp only [mul_sub, Finset.sum_sub_distrib, ← Finset.sum_mul, hw1, hψ]
        ring
      rw [hsplit] at h0
      have : ∑ u ∈ N, w u * (c - ψ u) = -∑ u ∈ N, w u * (ψ u - c) := by
        rw [← Finset.sum_neg_distrib]
        exact Finset.sum_congr rfl fun u _ => by ring
      rw [this]
      linarith
    have hPnn : ∀ v ∈ P, 0 ≤ w v * (ψ v - c) := fun v hv =>
      mul_nonneg (hw0 v (Finset.mem_filter.mp hv).1)
        (by linarith [(Finset.mem_filter.mp hv).2])
    have hNnn : ∀ u ∈ N, 0 ≤ w u * (c - ψ u) := fun u hu =>
      mul_nonneg (hw0 u (Finset.mem_filter.mp hu).1)
        (by linarith [(Finset.mem_filter.mp hu).2])
    have hApos : 0 < A := by
      rcases (Finset.sum_nonneg hPnn).lt_or_eq with h | h
      · exact h
      exfalso
      have hP0 : ∀ v ∈ P, w v = 0 := fun v hv => by
        have := (Finset.sum_eq_zero_iff_of_nonneg hPnn).mp h.symm v hv
        rcases mul_eq_zero.mp this with h' | h'
        · exact h'
        · linarith [(Finset.mem_filter.mp hv).2]
      have hN0 : ∀ u ∈ N, w u = 0 := fun u hu => by
        have := (Finset.sum_eq_zero_iff_of_nonneg hNnn).mp (by rw [hbal, hAdef]; exact h.symm) u hu
        rcases mul_eq_zero.mp this with h' | h'
        · exact h'
        · linarith [(Finset.mem_filter.mp hu).2]
      rw [hsplit, Finset.sum_eq_zero hN0, Finset.sum_eq_zero hP0] at hw1
      norm_num at hw1
    -- weights on pairs
    let μ : E × E → ℝ := fun p => w p.1 * w p.2 * (ψ p.2 - ψ p.1) / A
    have hμ0 : ∀ p ∈ N ×ˢ P, 0 ≤ μ p := by
      rintro ⟨u, v⟩ hp
      obtain ⟨hu, hv⟩ := Finset.mem_product.mp hp
      have := (Finset.mem_filter.mp hu).2
      have := (Finset.mem_filter.mp hv).2
      exact div_nonneg (mul_nonneg (mul_nonneg (hw0 u (Finset.mem_filter.mp hu).1)
        (hw0 v (Finset.mem_filter.mp hv).1)) (by linarith)) hApos.le
    have hμ1 : ∑ p ∈ N ×ˢ P, μ p = 1 := by
      rw [Finset.sum_product]
      have : ∀ u ∈ N, ∑ v ∈ P, μ (u, v) = w u + w u * (c - ψ u) * (∑ v ∈ P, w v) / A := by
        intro u _
        simp only [μ]
        rw [show (fun v => w u * w v * (ψ v - ψ u) / A) =
          fun v => w u / A * (w v * (ψ v - c)) + w u * (c - ψ u) / A * w v by
            funext v; ring]
        rw [Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum, ← hAdef]
        field_simp
      rw [Finset.sum_congr rfl this, Finset.sum_add_distrib]
      rw [show (fun u => w u * (c - ψ u) * (∑ v ∈ P, w v) / A) =
        fun u => (w u * (c - ψ u)) * ((∑ v ∈ P, w v) / A) by funext u; ring]
      rw [← Finset.sum_mul, hbal, mul_div_cancel₀ _ hApos.ne', ← hsplit, hw1]
    have hcomb : ∑ p ∈ N ×ˢ P, μ p • crossPt ψ c p.1 p.2 = ∑ v ∈ s, w v • v := by
      have hterm : ∀ u ∈ N, ∀ v ∈ P, μ (u, v) • crossPt ψ c u v =
          (w u / A * (w v * (ψ v - c))) • u + (w v / A * (w u * (c - ψ u))) • v := by
        intro u hu v hv
        have hd : ψ v - ψ u ≠ 0 := by
          have := (Finset.mem_filter.mp hu).2
          have := (Finset.mem_filter.mp hv).2
          intro h; linarith
        simp only [μ, crossPt, smul_smul]
        rw [show w u * w v * (ψ v - ψ u) / A * (ψ v - ψ u)⁻¹ = w u * w v / A by
          field_simp]
        module
      rw [Finset.sum_product, Finset.sum_congr rfl fun u hu =>
        Finset.sum_congr rfl fun v hv => hterm u hu v hv]
      simp only [Finset.sum_add_distrib]
      rw [Finset.sum_comm (s := N) (t := P) (f := fun u v =>
        (w v / A * (w u * (c - ψ u))) • v)]
      simp only [← Finset.sum_smul, ← Finset.mul_sum, ← hAdef, hbal]
      rw [hsplitE]
      congr 1
      · exact Finset.sum_congr rfl fun u _ => by rw [div_mul_cancel₀ _ hApos.ne']
      · exact Finset.sum_congr rfl fun v _ => by rw [div_mul_cancel₀ _ hApos.ne']
    rw [← hcomb, ← Finset.centerMass_eq_of_sum_1 _ _ hμ1]
    refine Finset.centerMass_mem_convexHull _ hμ0 (by rw [hμ1]; exact one_pos) fun p hp => ?_
    simp only [crossSet, Finset.coe_image]
    exact mem_image_of_mem _ hp
  · refine convexHull_min (crossSet_subset s) ?_
    exact (convex_convexHull ℝ _).inter (convex_hyperplane ψ.isLinear c)

end QOU.MathlibExt.PL
