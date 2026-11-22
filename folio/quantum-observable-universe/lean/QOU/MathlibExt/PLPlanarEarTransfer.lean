/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPlanarEar

set_option autoImplicit false

/-!
# Ears transfer across a chord (issue #8902, Moise part B, step 1)

A polygon `P` cut along a chord into `Q₁` and `Q₂` (so `P.parity = Q₁.parity + Q₂.parity`).
An ear of `Q₁` away from the chord is an ear of `P`, provided each piece sees the other piece's
path as outside (`Q₁.parity = 0` there, and the same for `Q₂`).

## What is a THEOREM here

* `lineMap_mem_openTri` — moving a point of the closed triangle towards an interior point
  lands in the open triangle.
* `exists_openTri_parity` — a point of the closed triangle off a polygon has the parity of some
  point of the open triangle.
* `ear_transfer` — the transfer statement, for abstract pieces `Q₁`, `Q₂`.
-/

namespace QOU.MathlibExt.PL

open Set Polygon Filter Topology

lemma openTri_subset_hull {p q r : R2} (hD : cross p q r ≠ 0) {y : R2} (hy : y ∈ openTri p q r) :
    y ∈ convexHull ℝ {p, q, r} :=
  (mem_convexHull_triple_iff hD).mpr ⟨hy.1.le, hy.2.1.le, hy.2.2.le⟩

/-- The centroid lies in the open triangle. -/
lemma openTri_nonempty {p q r : R2} (hD : cross p q r ≠ 0) : ∃ c, c ∈ openTri p q r := by
  have hc : ∀ a b : R2, cross a b ((1 / 3 : ℝ) • p + (1 / 3 : ℝ) • q + (1 / 3 : ℝ) • r) =
      (1 / 3) * (cross a b p + cross a b q + cross a b r) := by
    intro a b; rw [cross_combo _ _ _ _ _ _ _ _ (by norm_num)]; ring
  have hD2 : 0 < cross p q r * cross p q r := mul_self_pos.mpr hD
  refine ⟨(1 / 3 : ℝ) • p + (1 / 3 : ℝ) • q + (1 / 3 : ℝ) • r, ?_, ?_, ?_⟩
  · rw [hc, cross_left, cross_right, cross_rot]; nlinarith
  · rw [hc, cross_left, cross_right, cross_rot2]; nlinarith
  · rw [hc, cross_left, cross_right]; nlinarith

/-- Moving a point of the closed triangle towards a point of the open triangle. -/
lemma lineMap_mem_openTri {p q r y c : R2} (hD : cross p q r ≠ 0)
    (hy : y ∈ convexHull ℝ {p, q, r}) (hc : c ∈ openTri p q r) {ε : ℝ} (hε : 0 < ε)
    (hε1 : ε ≤ 1) : (1 - ε) • y + ε • c ∈ openTri p q r := by
  obtain ⟨h1, h2, h3⟩ := (mem_convexHull_triple_iff hD).mp hy
  have e : ∀ u v : R2, cross u v ((1 - ε) • y + ε • c) * cross p q r =
      (1 - ε) * (cross u v y * cross p q r) + ε * (cross u v c * cross p q r) := by
    intro u v; rw [cross_lineMap u v y c (1 - ε) ε (by ring)]; ring
  have h0 : 0 ≤ 1 - ε := by linarith
  refine ⟨?_, ?_, ?_⟩
  · rw [e]; nlinarith [hc.1]
  · rw [e]; nlinarith [hc.2.1]
  · rw [e]; nlinarith [hc.2.2]

/-- A point of the closed triangle off `Q` has the parity of some point of the open triangle. -/
lemma exists_openTri_parity (Q : Polygon R2) {p q r y : R2} (hD : cross p q r ≠ 0)
    (hy : y ∈ convexHull ℝ {p, q, r}) (hyQ : y ∉ Q.carrier) :
    ∃ y' ∈ openTri p q r, Q.parity y' = Q.parity y := by
  obtain ⟨c, hc⟩ := openTri_nonempty hD
  have hcont : Continuous (fun ε : ℝ => (1 - ε) • y + ε • c) := by fun_prop
  have hf : Tendsto (fun ε : ℝ => (1 - ε) • y + ε • c) (𝓝[>] 0) (𝓝 y) := by
    have h0 := hcont.tendsto 0
    simp only [sub_zero, one_smul, zero_smul, add_zero] at h0
    exact h0.mono_left nhdsWithin_le_nhds
  have hev := (hf.eventually (Q.parity_eventually_eq hyQ)).and
    (Ioc_mem_nhdsGT (show (0 : ℝ) < 1 by norm_num))
  obtain ⟨ε, hpar, hε⟩ := hev.exists
  exact ⟨_, lineMap_mem_openTri hD hy hc hε.1 hε.2, hpar⟩

/-- **Ears transfer across a chord.** `P` splits into `Q₁`, `Q₂`; the corner `A V B` is an ear
of `Q₁` (conditions `e₂`, `e₃`, `e₄`); each piece sees the rest of `P` as outside (`S₁`, `S₂`);
and `m` is a point of the triangle on `P` but off `Q₂`. Then the corner is an ear of `P`. -/
theorem ear_transfer {P Q₁ Q₂ : Polygon R2} {A V B : R2} (hD : cross A V B ≠ 0)
    (hsplit : ∀ y, P.parity y = Q₁.parity y + Q₂.parity y)
    (hQ₂ : Q₂.carrier ⊆ P.carrier ∪ Q₁.carrier)
    (S₁ : ∀ y ∈ P.carrier, y ∉ Q₁.carrier → Q₁.parity y = 0)
    (S₂ : ∀ y ∈ P.carrier, y ∉ Q₂.carrier → Q₂.parity y = 0)
    (e₂ : ∀ y ∈ convexHull ℝ {A, V, B}, y ∈ Q₁.carrier → y ∈ P.carrier →
      y ∈ segment ℝ A V ∪ segment ℝ V B)
    (e₃ : ∀ y ∈ openTri A V B, Q₁.parity y = 1)
    (e₄ : Disjoint (openTri A V B) Q₁.carrier)
    {m : R2} (hmT : m ∈ convexHull ℝ {A, V, B}) (hmP : m ∈ P.carrier) (hmQ : m ∉ Q₂.carrier) :
    (convexHull ℝ {A, V, B} ∩ P.carrier ⊆ segment ℝ A V ∪ segment ℝ V B) ∧
      ∀ y ∈ openTri A V B, P.parity y = 1 := by
  have hsub : convexHull ℝ {A, V, B} ∩ P.carrier ⊆ segment ℝ A V ∪ segment ℝ V B := by
    rintro y ⟨hyT, hyP⟩
    by_cases hy1 : y ∈ Q₁.carrier
    · exact e₂ y hyT hy1 hyP
    · exfalso
      obtain ⟨y', hy', hpar⟩ := exists_openTri_parity Q₁ hD hyT hy1
      rw [e₃ y' hy', S₁ y hyP hy1] at hpar
      exact one_ne_zero hpar
  refine ⟨hsub, ?_⟩
  have hdisj : Disjoint (openTri A V B) Q₂.carrier := by
    rw [Set.disjoint_left]
    intro y hy hy2
    rcases hQ₂ hy2 with h | h
    · have hs := hsub ⟨openTri_subset_hull hD hy, h⟩
      exact Set.disjoint_left.mp (disjoint_openTri A V B) hy
        (by rw [triPoly_carrier]; exact Or.inl hs)
    · exact Set.disjoint_left.mp e₄ hy h
  obtain ⟨y', hy', hpar⟩ := exists_openTri_parity Q₂ hD hmT hmQ
  rw [S₂ m hmP hmQ] at hpar
  intro y hy
  rw [hsplit, e₃ y hy, Q₂.parity_const_of_isPreconnected (convex_openTri _ _ _).isPreconnected
    hdisj hy hy', hpar, add_zero]

/-! ### Ears of a polygon, and their transfer from a cut piece -/

/-- An **ear** at vertex `k`: the corner `w (k-1), w k, w (k+1)` is non-degenerate, its closed
triangle meets the polygon only in its two sides at `w k`, and its inside lies inside the
polygon (crossing parity `1`). -/
def Polygon.IsEar (Q : Polygon R2) (k : ℕ) : Prop :=
  cross (Q.w (k + Q.n)) (Q.w k) (Q.w (k + 1)) ≠ 0 ∧
  convexHull ℝ {Q.w (k + Q.n), Q.w k, Q.w (k + 1)} ∩ Q.carrier ⊆
    segment ℝ (Q.w (k + Q.n)) (Q.w k) ∪ segment ℝ (Q.w k) (Q.w (k + 1)) ∧
  ∀ y ∈ openTri (Q.w (k + Q.n)) (Q.w k) (Q.w (k + 1)), Q.parity y = 1

lemma seg_rotateBy (P : Polygon R2) (r j : ℕ) : (P.rotateBy r).seg j = P.seg (j + r) := by
  unfold seg; rw [w_rotateBy, w_rotateBy, show j + 1 + r = j + r + 1 by omega]

lemma carrier_cocut (P : Polygon R2) {β : ℕ} (hβn : β ≤ P.n) (h : 2 ≤ P.n + 1 - β) :
    (P.cocut β h).carrier =
      (⋃ j ∈ Finset.range (P.n + 1 - β), P.seg (j + β)) ∪ segment ℝ (P.w β) (P.w 0) := by
  unfold cocut
  rw [carrier_cut]
  simp only [seg_rotateBy, w_rotateBy, zero_add]
  rw [show P.n + 1 - β + β = P.n + 1 by omega, w_period]

lemma cut_two_eq (P : Polygon R2) (h : 2 ≤ 2) :
    P.cut 2 h = triPoly (P.w 0) (P.w 1) (P.w 2) := by
  unfold cut triPoly
  congr 1
  funext i
  fin_cases i <;> rfl

/-- The midpoint of an edge is not a vertex. -/
lemma midpoint_ne_w {P : Polygon R2} (hP : P.IsSimple) {k : ℕ} (hk : k + 1 ≤ P.n) {j : ℕ}
    (hj : j ≤ P.n) : (1 / 2 : ℝ) • P.w k + (1 / 2 : ℝ) • P.w (k + 1) ≠ P.w j := by
  intro he
  have hne : P.w k ≠ P.w (k + 1) := fun h => by
    have := hP.w_injOn (by omega) hk h; omega
  have hm : P.w j ∈ P.seg k := by
    rw [← he]; exact ⟨1 / 2, 1 / 2, by norm_num, by norm_num, by norm_num, rfl⟩
  have hmod : (k + 1) % (P.n + 1) = k + 1 := Nat.mod_eq_of_lt (by omega)
  have k1 : ∀ a b : R2, (1 / 2 : ℝ) • a + (1 / 2 : ℝ) • b = a → a = b := by
    intro a b h
    have e : b - a = (2 : ℝ) • ((1 / 2 : ℝ) • a + (1 / 2 : ℝ) • b - a) := by module
    rw [h, sub_self, smul_zero, sub_eq_zero] at e; exact e.symm
  have k2 : ∀ a b : R2, (1 / 2 : ℝ) • a + (1 / 2 : ℝ) • b = b → a = b := by
    intro a b h
    have e : a - b = (2 : ℝ) • ((1 / 2 : ℝ) • a + (1 / 2 : ℝ) • b - b) := by module
    rw [h, sub_self, smul_zero, sub_eq_zero] at e; exact e
  rcases hP.w_mem_seg hj (by omega) hm with h | h
  · subst h; exact hne (k1 _ _ he)
  · rw [hmod] at h; subst h; exact hne (k2 _ _ he)

/-- **An ear of a cut piece, away from the chord, is an ear of the polygon.** The hypotheses
`S₁`, `S₂` say that each piece sees the rest of `P` as outside. When the piece is a triangle
(`β = 2`) its middle vertex is used. -/
theorem isEar_of_cut {P : Polygon R2} (hP : P.IsSimple) {β : ℕ} (hβ : 2 ≤ β)
    (h2 : 2 ≤ P.n + 1 - β)
    (hchord : segment ℝ (P.w 0) (P.w β) ∩ P.carrier ⊆ {P.w 0, P.w β})
    (S₁ : ∀ y ∈ P.carrier, y ∉ (P.cut β hβ).carrier → (P.cut β hβ).parity y = 0)
    (S₂ : ∀ y ∈ P.carrier, y ∉ (P.cocut β h2).carrier → (P.cocut β h2).parity y = 0)
    {k : ℕ} (hk1 : 1 ≤ k) (hkβ : k < β) (hE : (P.cut β hβ).IsEar k ∨ β = 2) : P.IsEar k := by
  have hβn : β + 1 ≤ P.n := by omega
  have hwp : P.w (k + P.n) = P.w (k - 1) := by
    rw [show k + P.n = (k - 1) + (P.n + 1) by omega, w_add_period]
  have hw1 : (P.cut β hβ).w (k + (P.cut β hβ).n) = P.w (k - 1) := by
    rw [cut_n, cut_w, show k + β = (k - 1) + (β + 1) by omega, Nat.add_mod_right,
      Nat.mod_eq_of_lt (by omega)]
  have hwk : (P.cut β hβ).w k = P.w k := cut_w_of_le P (by omega)
  have hwk1 : (P.cut β hβ).w (k + 1) = P.w (k + 1) := cut_w_of_le P (by omega)
  obtain ⟨hD, e₂, e₃, e₄⟩ : cross (P.w (k - 1)) (P.w k) (P.w (k + 1)) ≠ 0 ∧
      (∀ y ∈ convexHull ℝ {P.w (k - 1), P.w k, P.w (k + 1)}, y ∈ (P.cut β hβ).carrier →
        y ∈ P.carrier → y ∈ segment ℝ (P.w (k - 1)) (P.w k) ∪ segment ℝ (P.w k) (P.w (k + 1))) ∧
      (∀ y ∈ openTri (P.w (k - 1)) (P.w k) (P.w (k + 1)), (P.cut β hβ).parity y = 1) ∧
      Disjoint (openTri (P.w (k - 1)) (P.w k) (P.w (k + 1))) (P.cut β hβ).carrier := by
    rcases hE with hE | hβ2
    · obtain ⟨d, sb, pa⟩ := hE
      rw [hw1, hwk, hwk1] at d sb pa
      refine ⟨d, fun y hy h1 _ => sb ⟨hy, h1⟩, pa, ?_⟩
      rw [Set.disjoint_left]
      intro y hy h1
      exact Set.disjoint_left.mp (disjoint_openTri _ _ _) hy
        (by rw [triPoly_carrier]; exact Or.inl (sb ⟨openTri_subset_hull d hy, h1⟩))
    · subst hβ2
      obtain rfl : k = 1 := by omega
      have hQ : P.cut 2 hβ = triPoly (P.w 0) (P.w 1) (P.w 2) := cut_two_eq P hβ
      have hQs := isSimple_cut hP hβ hβn hchord
      have d := cross_ne_zero_of_isSimple hQs rfl
      rw [cut_w_of_le P (by omega), cut_w_of_le P (by omega), cut_w_of_le P (by omega)] at d
      refine ⟨d, ?_, ?_, ?_⟩
      · intro y _ h1 hyP
        rw [hQ, triPoly_carrier] at h1
        rcases h1 with (h | h) | h
        · exact Or.inl h
        · exact Or.inr h
        · rw [segment_symm] at h
          rcases hchord ⟨h, hyP⟩ with rfl | rfl
          · exact Or.inl (left_mem_segment _ _ _)
          · exact Or.inr (right_mem_segment _ _ _)
      · intro y hy
        rw [hQ]
        exact triPoly_parity_eq_one d (openTri_subset_hull d hy)
          (fun h => Set.disjoint_left.mp (disjoint_openTri _ _ _) hy h)
      · rw [hQ]; exact disjoint_openTri _ _ _
  set m : R2 := (1 / 2 : ℝ) • P.w k + (1 / 2 : ℝ) • P.w (k + 1) with hm
  have hmseg : m ∈ P.seg k := ⟨1 / 2, 1 / 2, by norm_num, by norm_num, by norm_num, rfl⟩
  have hmP : m ∈ P.carrier := P.seg_subset_carrier (by omega) hmseg
  have hmT : m ∈ convexHull ℝ {P.w (k - 1), P.w k, P.w (k + 1)} :=
    segment_subset_convexHull (mem_insert_of_mem _ (mem_insert _ _))
      (mem_insert_of_mem _ (mem_insert_of_mem _ (mem_singleton _))) hmseg
  have hmQ : m ∉ (P.cocut β h2).carrier := by
    rw [carrier_cocut P (by omega) h2]
    rintro (h | h)
    · simp only [mem_iUnion, Finset.mem_range] at h
      obtain ⟨j, hj, hmj⟩ := h
      have hin : m ∈ P.seg k ∩ P.seg (j + β) := ⟨hmseg, hmj⟩
      rw [hP.seg_inter (by omega) (by omega) (by omega)] at hin
      split_ifs at hin
      · exact midpoint_ne_w hP (by omega) (by omega) hin
      · exact midpoint_ne_w hP (by omega) (by omega) hin
      · exact hin
    · rw [segment_symm] at h
      rcases hchord ⟨h, hmP⟩ with h | h
      · exact midpoint_ne_w hP (by omega) (Nat.zero_le _) h
      · exact midpoint_ne_w hP (by omega) (by omega) h
  have hQ₂ : (P.cocut β h2).carrier ⊆ P.carrier ∪ (P.cut β hβ).carrier := by
    rw [carrier_cocut P (by omega) h2, carrier_cut]
    rintro y (h | h)
    · simp only [mem_iUnion, Finset.mem_range] at h
      obtain ⟨j, hj, hy⟩ := h
      exact Or.inl (P.seg_subset_carrier (by omega) hy)
    · rw [segment_symm] at h
      exact Or.inr (Or.inr h)
  obtain ⟨hsub, hpar⟩ := ear_transfer hD (fun y => parity_split P hβ h2 y) hQ₂ S₁ S₂ e₂ e₃ e₄
    hmT hmP hmQ
  unfold Polygon.IsEar
  rw [hwp]
  exact ⟨hD, hsub, hpar⟩

lemma Polygon.ext_w {P Q : Polygon R2} (hn : P.n = Q.n) (hw : ∀ k, P.w k = Q.w k) : P = Q := by
  obtain ⟨n₁, h₁, v₁⟩ := P
  obtain ⟨n₂, h₂, v₂⟩ := Q
  simp only at hn
  subst hn
  congr 1
  funext i
  have := hw i
  simpa [Polygon.w, Nat.mod_eq_of_lt i.isLt] using this

lemma isEar_rotateBy (P : Polygon R2) (r k : ℕ) : (P.rotateBy r).IsEar k ↔ P.IsEar (k + r) := by
  unfold Polygon.IsEar
  simp only [w_rotateBy, rotateBy_n, carrier_rotateBy, parity_rotateBy]
  rw [show k + P.n + r = k + r + P.n by omega, show k + 1 + r = k + r + 1 by omega]

lemma cocut_cocut (P : Polygon R2) {β : ℕ} (hβ : 2 ≤ β) (h2 : 2 ≤ P.n + 1 - β)
    (h' : 2 ≤ (P.rotateBy β).n + 1 - (P.n + 1 - β)) :
    (P.rotateBy β).cocut (P.n + 1 - β) h' = P.cut β hβ := by
  have hb : (P.rotateBy β).n + 1 - (P.n + 1 - β) = β := by rw [rotateBy_n]; omega
  apply Polygon.ext_w
  · exact hb
  · intro k
    unfold cocut
    rw [cut_w, cut_w, w_rotateBy, w_rotateBy, hb, add_assoc,
      show P.n + 1 - β + β = P.n + 1 by omega, w_add_period]

/-- **An ear of the complementary piece, away from the chord, is an ear of the polygon.** -/
theorem isEar_of_cocut {P : Polygon R2} (hP : P.IsSimple) {β : ℕ} (hβ : 2 ≤ β)
    (h2 : 2 ≤ P.n + 1 - β)
    (hchord : segment ℝ (P.w 0) (P.w β) ∩ P.carrier ⊆ {P.w 0, P.w β})
    (S₁ : ∀ y ∈ P.carrier, y ∉ (P.cut β hβ).carrier → (P.cut β hβ).parity y = 0)
    (S₂ : ∀ y ∈ P.carrier, y ∉ (P.cocut β h2).carrier → (P.cocut β h2).parity y = 0)
    {k : ℕ} (hk1 : 1 ≤ k) (hkβ : k < P.n + 1 - β)
    (hE : (P.cocut β h2).IsEar k ∨ P.n + 1 - β = 2) : P.IsEar (k + β) := by
  have h' : 2 ≤ (P.rotateBy β).n + 1 - (P.n + 1 - β) := by rw [rotateBy_n]; omega
  have hcc := cocut_cocut P hβ h2 h'
  have hcut : (P.rotateBy β).cut (P.n + 1 - β) h2 = P.cocut β h2 := rfl
  rw [← isEar_rotateBy]
  refine isEar_of_cut (Polygon.isSimple_rotateBy P hP β) h2 h' ?_ ?_ ?_ hk1 hkβ ?_
  · rw [w_rotateBy, w_rotateBy, zero_add, show P.n + 1 - β + β = P.n + 1 by omega, w_period,
      carrier_rotateBy, segment_symm]
    intro y hy
    rcases hchord hy with h | h
    · exact Or.inr h
    · exact Or.inl h
  · rw [carrier_rotateBy, hcut]; exact S₂
  · rw [carrier_rotateBy, hcc]; exact S₁
  · rw [hcut]; exact hE

end QOU.MathlibExt.PL
