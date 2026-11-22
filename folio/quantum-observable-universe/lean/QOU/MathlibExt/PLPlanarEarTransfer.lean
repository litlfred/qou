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

end QOU.MathlibExt.PL
