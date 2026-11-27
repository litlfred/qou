/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLLipschitz
import BraidKnotOctonion.PLPrismPush
import BraidKnotOctonion.PLTriangulation
import Mathlib.Analysis.Convex.Combination
import Mathlib.Tactic.Module

set_option autoImplicit false

/-!
# PL slicing: planar time slices and hyperplane slices of simplicial complexes (#8902)

Consolidates both slicing foundations of the piecewise-linear knot-topology build:

1. **Time slices of a planar polyhedron** (Stage 2, PL isotopy ⇒ Δ-equivalence, consumed by
   `PLTies.lean`):
   * `AmbientIsotopy.isPL_edgeTrack` — `(t, s) ↦ H_t (a + s • (b - a))` is PL.
   * `slice_mem_iff`, `isPL_sliceLo`, `isPL_sliceHi` — strip slices of `polySet φ r` have PL
     endpoints in `t`.
2. **Hyperplane slices of simplices and 2-dimensional complexes** (Moise Part A, `#9072`):
   * `crossPt`, `crossSet`, `convexHull_inter_hyperplane` — a hyperplane missing the vertices of
     `s` cuts `convexHull ℝ s` in `convexHull ℝ (crossSet ψ c s)`.
   * `sliceComplex`, `sliceComplex_space`, `sliceComplex_vertex`, `sliceComplex_edge` — slicing a
     simplicial complex of dimension `≤ 2` yields a `≤ 1`-dimensional simplicial complex.
-/

namespace QOU.MathlibExt.PL

section TimeSlice

open Set

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

namespace AmbientIsotopy

variable {L L' : PolygonalLink E}

/-- **The edge track is PL**: `(t, s) ↦ H_t (a + s • (b - a))`. -/
theorem isPL_edgeTrack (I : AmbientIsotopy L L') (h : IsPL I.track) (a b : E) :
    IsPL (fun p : ℝ × ℝ => I.track (p.1, a + p.2 • (b - a))) := by
  have hin : IsPL (fun p : ℝ × ℝ => (p.1, a + p.2 • (b - a))) :=
    IsPL.fst.prodMk ((IsPL.const a).add (IsPL.snd.smul_const (b - a)))
  exact h.comp hin

end AmbientIsotopy

/-! ### Slices -/

variable {ι : Type} [Fintype ι] (φ : ι → ℝ × ℝ →L[ℝ] ℝ) (r : ι → ℝ)

/-- Time coefficient of a constraint. -/
def tc (i : ι) : ℝ := φ i (1, 0)

/-- Space coefficient of a constraint. -/
def sc (i : ι) : ℝ := φ i (0, 1)

omit [Fintype ι] in
lemma apply_eq (i : ι) (t s : ℝ) : φ i (t, s) = tc φ i * t + sc φ i * s := by
  have : ((t, s) : ℝ × ℝ) = t • ((1 : ℝ), (0 : ℝ)) + s • ((0 : ℝ), (1 : ℝ)) := by
    ext <;> simp
  rw [this, map_add, map_smul, map_smul, smul_eq_mul, smul_eq_mul, tc, sc, mul_comm t,
    mul_comm s]

/-- Lower bound coming from constraint `i` (`0` if it gives none). -/
noncomputable def loTerm (i : ι) (t : ℝ) : ℝ :=
  if sc φ i < 0 then (r i - tc φ i * t) / sc φ i else 0

/-- Upper bound coming from constraint `i` (`1` if it gives none). -/
noncomputable def hiTerm (i : ι) (t : ℝ) : ℝ :=
  if 0 < sc φ i then (r i - tc φ i * t) / sc φ i else 1

/-- **Lower slice endpoint** in the strip `0 ≤ s ≤ 1`. -/
noncomputable def sliceLo (t : ℝ) : ℝ := Finset.univ.fold max 0 (fun i => loTerm φ r i t)

/-- **Upper slice endpoint** in the strip `0 ≤ s ≤ 1`. -/
noncomputable def sliceHi (t : ℝ) : ℝ := Finset.univ.fold min 1 (fun i => hiTerm φ r i t)

/-- The time-only conditions (constraints not involving `s`). -/
def timeOK (t : ℝ) : Prop := ∀ i, sc φ i = 0 → tc φ i * t ≤ r i

omit [Fintype ι] in
lemma constraint_iff (i : ι) {t s : ℝ} (hs0 : 0 ≤ s) (hs1 : s ≤ 1) :
    φ i (t, s) ≤ r i ↔
      (sc φ i = 0 → tc φ i * t ≤ r i) ∧ loTerm φ r i t ≤ s ∧ s ≤ hiTerm φ r i t := by
  rw [apply_eq]
  unfold loTerm hiTerm
  rcases lt_trichotomy (sc φ i) 0 with hn | hz | hp
  · rw [if_pos hn, if_neg (not_lt.2 hn.le), div_le_iff_of_neg hn]
    constructor
    · intro h; exact ⟨fun h0 => absurd h0 hn.ne, by linarith, hs1⟩
    · rintro ⟨-, h, -⟩; linarith
  · simp only [hz, lt_irrefl, if_false, zero_mul, add_zero, forall_const]
    exact ⟨fun h => ⟨h, hs0, hs1⟩, fun h => h.1⟩
  · rw [if_neg (not_lt.2 hp.le), if_pos hp, le_div_iff₀ hp]
    constructor
    · intro h; exact ⟨fun h0 => absurd h0 hp.ne', hs0, by linarith⟩
    · rintro ⟨-, -, h⟩; linarith

/-- **The slice of a polyhedron in the strip.** -/
theorem slice_mem_iff (t s : ℝ) :
    ((t, s) ∈ polySet φ r ∧ 0 ≤ s ∧ s ≤ 1) ↔ timeOK φ r t ∧ sliceLo φ r t ≤ s ∧ s ≤ sliceHi φ r t := by
  unfold sliceLo sliceHi timeOK polySet
  rw [Finset.fold_max_le, Finset.le_fold_min]
  simp only [Finset.mem_univ, forall_const, mem_setOf_eq]
  constructor
  · rintro ⟨h, hs0, hs1⟩
    have hc := fun i => (constraint_iff φ r i hs0 hs1).1 (h i)
    exact ⟨fun i => (hc i).1, ⟨hs0, fun i => (hc i).2.1⟩, ⟨hs1, fun i => (hc i).2.2⟩⟩
  · rintro ⟨ht, ⟨hs0, hlo⟩, ⟨hs1, hhi⟩⟩
    exact ⟨fun i => (constraint_iff φ r i hs0 hs1).2 ⟨ht i, hlo i, hhi i⟩, hs0, hs1⟩

omit [Fintype ι] in
lemma isPL_ratio (i : ι) : IsPL (fun t : ℝ => (r i - tc φ i * t) / sc φ i) := by
  have h := (IsPL.const (E := ℝ) (r i / sc φ i)).add (IsPL.id.smul_const (-(tc φ i) / sc φ i))
  convert h using 1
  funext t
  simp only [id, smul_eq_mul]
  ring

/-- **The lower slice endpoint is PL in time.** -/
theorem isPL_sliceLo : IsPL (sliceLo φ r) := by
  refine IsPL.fold_max _ _ (fun i => ?_)
  unfold loTerm
  split_ifs
  · exact isPL_ratio φ r i
  · exact IsPL.const 0

omit [Fintype ι] in
/-- A finite `fold min` of real PL functions is PL. -/
lemma isPL_fold_min {κ : Type*} (S : Finset κ) (c : ℝ) {h : κ → ℝ → ℝ} (hh : ∀ i, IsPL (h i)) :
    IsPL (fun x => S.fold min c (fun i => h i x)) := by
  classical
  induction S using Finset.induction_on with
  | empty => simpa using IsPL.const (E := ℝ) c
  | insert a S ha ih =>
    simp only [Finset.fold_insert ha]
    exact (hh a).min ih

/-- **The upper slice endpoint is PL in time.** -/
theorem isPL_sliceHi : IsPL (sliceHi φ r) := by
  refine isPL_fold_min _ _ (fun i => ?_)
  unfold hiTerm
  split_ifs
  · exact isPL_ratio φ r i
  · exact IsPL.const 1


end TimeSlice

section HyperplaneSlice

open Set Geometry

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

/-! ### Combinatorics of `crossSet` -/

lemma mem_crossSet [DecidableEq E] {s : Finset E} {x : E} :
    x ∈ crossSet ψ c s ↔ ∃ u ∈ s, ∃ v ∈ s, ψ u < c ∧ c < ψ v ∧ crossPt ψ c u v = x := by
  simp only [crossSet, Finset.mem_image, Finset.mem_product, Finset.mem_filter, Prod.exists]
  constructor
  · rintro ⟨u, v, ⟨⟨hu, hu'⟩, hv, hv'⟩, rfl⟩
    exact ⟨u, hu, v, hv, hu', hv', rfl⟩
  · rintro ⟨u, hu, v, hv, hu', hv', rfl⟩
    exact ⟨u, v, ⟨⟨hu, hu'⟩, hv, hv'⟩, rfl⟩

lemma crossSet_mono [DecidableEq E] {s t : Finset E} (h : s ⊆ t) :
    crossSet ψ c s ⊆ crossSet ψ c t := by
  intro x hx
  obtain ⟨u, hu, v, hv, hu', hv', rfl⟩ := mem_crossSet.mp hx
  exact mem_crossSet.mpr ⟨u, h hu, v, h hv, hu', hv', rfl⟩

lemma crossSet_pair [DecidableEq E] {u v : E} (hu : ψ u < c) (hv : c < ψ v) :
    crossSet ψ c {u, v} = {crossPt ψ c u v} := by
  ext x
  rw [mem_crossSet, Finset.mem_singleton]
  constructor
  · rintro ⟨a, ha, b, hb, ha', hb', rfl⟩
    simp only [Finset.mem_insert, Finset.mem_singleton] at ha hb
    rcases ha with rfl | rfl
    · rcases hb with rfl | rfl
      · exact absurd ha' (not_lt.mpr hb'.le)
      · rfl
    · exact absurd ha' (not_lt.mpr hv.le)
  · rintro rfl
    exact ⟨u, by simp, v, by simp, hu, hv, rfl⟩

lemma card_filter_add_le (s : Finset E) :
    (s.filter fun u => ψ u < c).card + (s.filter fun v => c < ψ v).card ≤ s.card := by
  classical
  have h := Finset.filter_card_add_filter_neg_card_eq_card (s := s) (fun x => ψ x < c)
  have : (s.filter fun v => c < ψ v).card ≤ (s.filter fun x => ¬ ψ x < c).card :=
    Finset.card_le_card fun x hx => by
      simp only [Finset.mem_filter] at hx ⊢
      exact ⟨hx.1, not_lt.mpr hx.2.le⟩
  omega

lemma card_crossSet_le_mul [DecidableEq E] (s : Finset E) :
    (crossSet ψ c s).card ≤
      (s.filter fun u => ψ u < c).card * (s.filter fun v => c < ψ v).card :=
  Finset.card_image_le.trans (Finset.card_product _ _).le

/-- A face with at most three vertices crosses a hyperplane in at most two points. -/
lemma card_crossSet_le_two [DecidableEq E] {s : Finset E} (hs : s.card ≤ 3) :
    (crossSet ψ c s).card ≤ 2 := by
  have h1 := card_crossSet_le_mul (ψ := ψ) (c := c) s
  have h2 := card_filter_add_le (ψ := ψ) (c := c) s
  have key : ∀ a b : ℕ, a + b ≤ 3 → a * b ≤ 2 := by
    intro a b h
    have : a ≤ 3 := by omega
    interval_cases a <;> omega
  exact h1.trans (key _ _ (h2.trans hs))

/-- Two crossing points need at least three vertices. -/
lemma three_le_card_of_card_crossSet [DecidableEq E] {s : Finset E}
    (hs : 2 ≤ (crossSet ψ c s).card) : 3 ≤ s.card := by
  have h1 := card_crossSet_le_mul (ψ := ψ) (c := c) s
  have h2 := card_filter_add_le (ψ := ψ) (c := c) s
  have key : ∀ a b : ℕ, 2 ≤ a * b → 3 ≤ a + b := by
    intro a b h
    by_contra hab
    have : a ≤ 2 := by omega
    interval_cases a <;> omega
  exact (key _ _ (hs.trans h1)).trans h2

/-- A finite set of at most two points is affinely independent. -/
lemma affineIndependent_of_card_le_two {t : Finset E} (ht : t.card ≤ 2) :
    AffineIndependent ℝ ((↑) : t → E) := by
  classical
  rcases Nat.lt_or_ge t.card 2 with h | h
  · haveI : Subsingleton t := Finset.card_le_one_iff_subsingleton_coe.mp (by omega)
    exact affineIndependent_of_subsingleton ℝ _
  · obtain ⟨a, b, hab, rfl⟩ := Finset.card_eq_two.mp (le_antisymm ht h)
    refine (affineIndependent_of_ne ℝ hab).range.mono ?_
    intro x hx
    have hx' : x ∈ ({a, b} : Finset E) := hx
    rw [Finset.mem_insert, Finset.mem_singleton] at hx'
    rcases hx' with rfl | rfl
    · exact ⟨0, rfl⟩
    · exact ⟨1, rfl⟩

/-! ### The slice of a complex of dimension at most two -/

/-- **The slice complex**: the faces are the crossing sets of the faces of `K`. For `K` of
dimension at most two (faces with at most three vertices) these are points and segments. -/
noncomputable def sliceComplex [DecidableEq E] (K : SimplicialComplex ℝ E)
    (hdim : ∀ s ∈ K.faces, s.card ≤ 3) (hgen : ∀ s ∈ K.faces, ∀ v ∈ s, ψ v ≠ c) :
    SimplicialComplex ℝ E where
  faces := {σ | ∃ τ ∈ K.faces, crossSet ψ c τ = σ ∧ σ.Nonempty}
  empty_notMem := fun ⟨_, _, _, h⟩ => Finset.not_nonempty_empty h
  indep := by
    rintro σ ⟨τ, hτ, rfl, -⟩
    exact affineIndependent_of_card_le_two (card_crossSet_le_two (hdim τ hτ))
  down_closed := by
    rintro σ t ⟨τ, hτ, rfl, hne⟩ hts ht
    by_cases heq : t = crossSet ψ c τ
    · exact ⟨τ, hτ, heq.symm, heq ▸ hne⟩
    have hlt : t.card < (crossSet ψ c τ).card :=
      Finset.card_lt_card (Finset.ssubset_iff_subset_ne.mpr ⟨hts, heq⟩)
    have h2 := card_crossSet_le_two (ψ := ψ) (c := c) (hdim τ hτ)
    have hpos : 0 < t.card := Finset.card_pos.mpr (Finset.nonempty_iff_ne_empty.mpr ht)
    obtain ⟨x, rfl⟩ := Finset.card_eq_one.mp (show t.card = 1 by omega)
    obtain ⟨u, hu, v, hv, hu', hv', rfl⟩ := mem_crossSet.mp (hts (Finset.mem_singleton_self x))
    refine ⟨{u, v}, K.down_closed hτ ?_ (by simp), crossSet_pair hu' hv',
      Finset.singleton_nonempty _⟩
    exact Finset.insert_subset hu (Finset.singleton_subset_iff.mpr hv)
  inter_subset_convexHull := by
    rintro _ _ ⟨τ, hτ, rfl, -⟩ ⟨τ', hτ', rfl, -⟩
    rw [← convexHull_inter_hyperplane τ (hgen τ hτ),
      ← convexHull_inter_hyperplane τ' (hgen τ' hτ')]
    rintro x ⟨⟨hx, hxψ⟩, hx', -⟩
    have hint := K.inter_subset_convexHull hτ hτ' ⟨hx, hx'⟩
    rw [← Finset.coe_inter] at hint
    have h2 : x ∈ convexHull ℝ ↑(crossSet ψ c (τ ∩ τ')) := by
      rw [← convexHull_inter_hyperplane _ fun v hv => hgen τ hτ v (Finset.mem_inter.mp hv).1]
      exact ⟨hint, hxψ⟩
    refine convexHull_mono ?_ h2
    rw [← Finset.coe_inter]
    exact Finset.coe_subset.mpr (Finset.subset_inter (crossSet_mono Finset.inter_subset_left)
      (crossSet_mono Finset.inter_subset_right))

section sliceComplex

variable [DecidableEq E] {K : SimplicialComplex ℝ E} {hdim : ∀ s ∈ K.faces, s.card ≤ 3}
  {hgen : ∀ s ∈ K.faces, ∀ v ∈ s, ψ v ≠ c}

lemma mem_sliceComplex_faces {σ : Finset E} :
    σ ∈ (sliceComplex K hdim hgen).faces ↔ ∃ τ ∈ K.faces, crossSet ψ c τ = σ ∧ σ.Nonempty :=
  Iff.rfl

/-- **The slice is a complex of dimension at most one.** -/
lemma sliceComplex_card_le_two {σ : Finset E} (hσ : σ ∈ (sliceComplex K hdim hgen).faces) :
    σ.card ≤ 2 := by
  obtain ⟨τ, hτ, rfl, -⟩ := hσ
  exact card_crossSet_le_two (hdim τ hτ)

lemma sliceComplex_faces_finite (hK : K.faces.Finite) :
    (sliceComplex K hdim hgen).faces.Finite :=
  (hK.image (crossSet ψ c)).subset fun _ ⟨τ, hτ, h, _⟩ => ⟨τ, hτ, h⟩

/-- **The slice of the space**: `S.space = K.space ∩ {ψ = c}`. -/
theorem sliceComplex_space :
    (sliceComplex K hdim hgen).space = K.space ∩ {x | ψ x = c} := by
  ext x
  simp only [SimplicialComplex.mem_space_iff, mem_inter_iff, mem_setOf_eq]
  constructor
  · rintro ⟨_, ⟨τ, hτ, rfl, -⟩, hx⟩
    rw [← convexHull_inter_hyperplane τ (hgen τ hτ)] at hx
    exact ⟨⟨τ, hτ, hx.1⟩, hx.2⟩
  · rintro ⟨⟨τ, hτ, hx⟩, hψ⟩
    have hmem : x ∈ convexHull ℝ ↑(crossSet ψ c τ) := by
      rw [← convexHull_inter_hyperplane τ (hgen τ hτ)]
      exact ⟨hx, hψ⟩
    refine ⟨crossSet ψ c τ, ⟨τ, hτ, rfl, ?_⟩, hmem⟩
    by_contra h
    rw [Finset.not_nonempty_iff_eq_empty] at h
    rw [h, Finset.coe_empty, convexHull_empty] at hmem
    exact hmem

/-- **Each vertex of the slice lies on an edge of `K`**, where that edge crosses `{ψ = c}`. -/
theorem sliceComplex_vertex {x : E} (hx : {x} ∈ (sliceComplex K hdim hgen).faces) :
    ∃ u v, ({u, v} : Finset E) ∈ K.faces ∧ ψ u < c ∧ c < ψ v ∧ x = crossPt ψ c u v := by
  obtain ⟨τ, hτ, h, -⟩ := hx
  obtain ⟨u, hu, v, hv, hu', hv', hx⟩ :=
    mem_crossSet.mp (h ▸ Finset.mem_singleton_self x : x ∈ crossSet ψ c τ)
  exact ⟨u, v, K.down_closed hτ (Finset.insert_subset hu (Finset.singleton_subset_iff.mpr hv))
    (by simp), hu', hv', hx.symm⟩

/-- **Each edge of the slice lies in a triangle of `K`**: it is the crossing set of a face of
`K` with three vertices. -/
theorem sliceComplex_edge {σ : Finset E} (hσ : σ ∈ (sliceComplex K hdim hgen).faces)
    (h2 : σ.card = 2) : ∃ τ ∈ K.faces, τ.card = 3 ∧ crossSet ψ c τ = σ ∧
      convexHull ℝ (σ : Set E) ⊆ convexHull ℝ (τ : Set E) := by
  obtain ⟨τ, hτ, rfl, -⟩ := hσ
  refine ⟨τ, hτ, le_antisymm (hdim τ hτ) (three_le_card_of_card_crossSet h2.ge), rfl, ?_⟩
  rw [← convexHull_inter_hyperplane τ (hgen τ hτ)]
  exact inter_subset_left

end sliceComplex


end HyperplaneSlice

end QOU.MathlibExt.PL
