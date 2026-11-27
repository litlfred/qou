/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLC1Estimates
import BraidKnotOctonion.PLPolygonalLink

set_option autoImplicit false

/-!
# Inscribed polygons of a C¹ image are simple (issue #8902, isotopy-to-Δ bridge)

Let `P` be a polygon in `E` and `g : E → F` differentiable. The **inscribed polygon**
`P.image g` has vertices `g (v i)`. When `P` is fine compared to how far `g` is from linear, the
inscribed polygon is simple.

## What is a DEFINITION here

* `Polygon.image g P` — the polygon with vertices `g ∘ P.v`.

## What is a THEOREM here

* `Polygon.exists_near_of_mem_image_edge` — every point of an inscribed edge is within
  `2 ε δ` of the `g`-image of a point of the source edge.
* `Polygon.isSimple_image` — **simplicity of the inscribed polygon.** The hypotheses are, for
  constants `δ, d, ε, M, κ`:
  * edges of `P` have length at most `δ`; non-adjacent edges are at distance at least `d`;
  * `‖a - b‖ ≤ M ‖g a - g b‖` on the carrier of `P`;
  * on edge `i`, `fderiv g` is within `ε` of `φ i` and of `φ (next i)`, and
    `‖u‖ ≤ M ‖φ i u‖` for all `u`;
  * at each vertex the two incident edges satisfy the angle bound with constant `κ`
    (`exists_pos_mul_le_norm_smul_sub`);
  * `4 M ε δ < d` and `M ε < κ`.
* `Polygon.disjoint_image_carrier` — the same estimate keeps two inscribed polygons apart when
  their sources are at distance at least `d`.

## What is NOT proved here

* That a C¹ ambient isotopy provides such constants uniformly in time, and that fine sample
  polygons exist. Those are the next steps of the bridge.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E F : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedAddCommGroup F] [NormedSpace ℝ F]

namespace Polygon

/-- **The inscribed polygon** with vertices `g ∘ P.v`. -/
def image (g : E → F) (P : Polygon E) : Polygon F := ⟨P.n, P.two_le, g ∘ P.v⟩

variable (g : E → F) (P : Polygon E)

@[simp] lemma image_n : (P.image g).n = P.n := rfl
lemma image_v (i : Fin (P.n + 1)) : (P.image g).v i = g (P.v i) := rfl
lemma image_next (i : Fin (P.n + 1)) : (P.image g).next i = P.next i := rfl

lemma mem_edge_iff {i : Fin (P.n + 1)} {x : E} :
    x ∈ P.edge i ↔ ∃ s ∈ Icc (0 : ℝ) 1, P.v i + s • (P.v (P.next i) - P.v i) = x := by
  rw [edge, segment_eq_image']; rfl

set_option backward.isDefEq.respectTransparency false in
/-- Every point of an inscribed edge is close to the image of a point of the source edge. -/
theorem exists_near_of_mem_image_edge {φ : E →L[ℝ] F} {ε : ℝ} {i : Fin (P.n + 1)}
    (hd : ∀ z ∈ P.edge i, DifferentiableAt ℝ g z)
    (hε : ∀ z ∈ P.edge i, ‖fderiv ℝ g z - φ‖ ≤ ε) {p : F} (hp : p ∈ (P.image g).edge i) :
    ∃ a ∈ P.edge i, ‖g a - p‖ ≤ 2 * ε * ‖P.v (P.next i) - P.v i‖ := by
  rw [mem_edge_iff] at hp
  obtain ⟨s, ⟨hs0, hs1⟩, rfl⟩ := hp
  refine ⟨P.v i + s • (P.v (P.next i) - P.v i), (P.mem_edge_iff).mpr ⟨s, ⟨hs0, hs1⟩, rfl⟩, ?_⟩
  exact norm_chord_sub_le (f := g) hd hε hs0 hs1

/-- **Inscribed polygons of sources at distance `d` are disjoint.** -/
theorem disjoint_image_carrier (Q : Polygon E) {ε δ d M : ℝ} (hM : 0 ≤ M)
    (φP : Fin (P.n + 1) → E →L[ℝ] F) (φQ : Fin (Q.n + 1) → E →L[ℝ] F)
    (hdP : ∀ i, ∀ z ∈ P.edge i, DifferentiableAt ℝ g z)
    (hdQ : ∀ i, ∀ z ∈ Q.edge i, DifferentiableAt ℝ g z)
    (hεP : ∀ i, ∀ z ∈ P.edge i, ‖fderiv ℝ g z - φP i‖ ≤ ε)
    (hεQ : ∀ i, ∀ z ∈ Q.edge i, ‖fderiv ℝ g z - φQ i‖ ≤ ε)
    (hlenP : ∀ i, ‖P.v (P.next i) - P.v i‖ ≤ δ) (hlenQ : ∀ i, ‖Q.v (Q.next i) - Q.v i‖ ≤ δ)
    (hlip : ∀ a ∈ P.carrier, ∀ b ∈ Q.carrier, ‖a - b‖ ≤ M * ‖g a - g b‖)
    (hsep : ∀ a ∈ P.carrier, ∀ b ∈ Q.carrier, d ≤ ‖a - b‖) (h4 : 4 * M * ε * δ < d) :
    Disjoint (P.image g).carrier (Q.image g).carrier := by
  rw [Set.disjoint_left]
  intro p hp hq
  simp only [carrier, mem_iUnion] at hp hq
  obtain ⟨i, hi⟩ := hp
  obtain ⟨j, hj⟩ := hq
  obtain ⟨a, ha, hga⟩ := P.exists_near_of_mem_image_edge g (hdP i) (hεP i) hi
  obtain ⟨b, hb, hgb⟩ := Q.exists_near_of_mem_image_edge g (hdQ j) (hεQ j) hj
  have hε : 0 ≤ ε := (norm_nonneg _).trans (hεP i _ (left_mem_segment ℝ _ _))
  have hab : ‖g a - g b‖ ≤ 4 * ε * δ := by
    calc ‖g a - g b‖ = ‖(g a - p) - (g b - p)‖ := by congr 1; abel
      _ ≤ ‖g a - p‖ + ‖g b - p‖ := norm_sub_le _ _
      _ ≤ 2 * ε * δ + 2 * ε * δ := by
          gcongr
          · exact hga.trans (mul_le_mul_of_nonneg_left (hlenP i) (by positivity))
          · exact hgb.trans (mul_le_mul_of_nonneg_left (hlenQ j) (by positivity))
      _ = 4 * ε * δ := by ring
  have h1 := hsep a (subset_iUnion P.edge i ha) b (subset_iUnion Q.edge j hb)
  have h2 := hlip a (subset_iUnion P.edge i ha) b (subset_iUnion Q.edge j hb)
  have h3 := mul_le_mul_of_nonneg_left hab hM
  nlinarith

set_option backward.isDefEq.respectTransparency false in
/-- **The inscribed polygon is simple.** -/
theorem isSimple_image {ε δ d M κ : ℝ} (hM : 0 ≤ M) (hinj : Function.Injective P.v)
    (φ : Fin (P.n + 1) → E →L[ℝ] F)
    (hd : ∀ i, ∀ z ∈ P.edge i, DifferentiableAt ℝ g z)
    (hε : ∀ i, ∀ z ∈ P.edge i,
      ‖fderiv ℝ g z - φ i‖ ≤ ε ∧ ‖fderiv ℝ g z - φ (P.next i)‖ ≤ ε)
    (hinv : ∀ i u, ‖u‖ ≤ M * ‖φ i u‖)
    (hlen : ∀ i, ‖P.v (P.next i) - P.v i‖ ≤ δ)
    (hlip : ∀ a ∈ P.carrier, ∀ b ∈ P.carrier, ‖a - b‖ ≤ M * ‖g a - g b‖)
    (hsep : ∀ i j, i ≠ j → j ≠ P.next i → i ≠ P.next j →
      ∀ a ∈ P.edge i, ∀ b ∈ P.edge j, d ≤ ‖a - b‖)
    (hangle : ∀ i α β, 0 ≤ α → 0 ≤ β →
      κ * (α * ‖P.v i - P.v (P.next i)‖ + β * ‖P.v (P.next (P.next i)) - P.v (P.next i)‖) ≤
        ‖α • (P.v i - P.v (P.next i)) - β • (P.v (P.next (P.next i)) - P.v (P.next i))‖)
    (h4 : 4 * M * ε * δ < d) (hκ : M * ε < κ) :
    (P.image g).IsSimple := by
  have hginj : Function.Injective (g ∘ P.v) := by
    intro i j hij
    by_contra hne
    have := hlip _ (P.vertex_mem_carrier i) _ (P.vertex_mem_carrier j)
    simp only [Function.comp_apply] at hij
    rw [hij, sub_self, norm_zero, mul_zero, norm_le_zero_iff, sub_eq_zero] at this
    exact hne (hinj this)
  refine (P.image g).isSimple_of hginj ?_ ?_
  · -- adjacent edges
    intro i
    set j := P.next i
    set k := P.next j
    ext p
    simp only [mem_inter_iff, mem_singleton_iff]
    constructor
    · rintro ⟨hp1, hp2⟩
      rw [mem_edge_iff] at hp1 hp2
      obtain ⟨s, ⟨hs0, hs1⟩, hs⟩ := hp1
      obtain ⟨t, ⟨ht0, ht1⟩, ht⟩ := hp2
      simp only [image_v, image_next] at hs ht
      set u := P.v i - P.v j
      set w := P.v k - P.v j
      set e1 := g (P.v i) - g (P.v j) - φ j u
      set e2 := g (P.v k) - g (P.v j) - φ j w
      have he1 : ‖e1‖ ≤ ε * ‖u‖ := by
        refine norm_sub_sub_le (fun z hz => hd i z ?_) (fun z hz => (hε i z ?_).2) <;>
          rwa [edge, segment_symm]
      have he2 : ‖e2‖ ≤ ε * ‖w‖ := norm_sub_sub_le (fun z hz => hd j z hz)
        (fun z hz => (hε j z hz).1)
      set α := 1 - s
      set β := t
      have hα : 0 ≤ α := by simp only [α]; linarith
      have hrel : φ j (α • u - β • w) = β • e2 - α • e1 := by
        have h' : g (P.v i) + s • (g (P.v j) - g (P.v i)) =
            g (P.v j) + t • (g (P.v k) - g (P.v j)) := hs.trans ht.symm
        have hab : α • (g (P.v i) - g (P.v j)) = β • (g (P.v k) - g (P.v j)) := by
          have e : α • (g (P.v i) - g (P.v j)) =
              (g (P.v i) + s • (g (P.v j) - g (P.v i))) - g (P.v j) := by
            simp only [α]; module
          rw [e, h']; simp only [β]; abel
        have key : ∀ A B C D : F, α • A = β • B →
            β • (B - D) - α • (A - C) = α • C - β • D := by
          intro A B C D h; rw [smul_sub, smul_sub, h]; abel
        rw [key _ _ _ _ hab, map_sub, map_smul, map_smul]
      have hupper : ‖α • u - β • w‖ ≤ M * ε * (α * ‖u‖ + β * ‖w‖) := by
        calc ‖α • u - β • w‖ ≤ M * ‖φ j (α • u - β • w)‖ := hinv j _
          _ = M * ‖β • e2 - α • e1‖ := by rw [hrel]
          _ ≤ M * (β * (ε * ‖w‖) + α * (ε * ‖u‖)) := by
              gcongr
              calc ‖β • e2 - α • e1‖ ≤ ‖β • e2‖ + ‖α • e1‖ := norm_sub_le _ _
                _ = β * ‖e2‖ + α * ‖e1‖ := by
                    rw [norm_smul, norm_smul, Real.norm_of_nonneg ht0, Real.norm_of_nonneg hα]
                _ ≤ _ := by gcongr
          _ = M * ε * (α * ‖u‖ + β * ‖w‖) := by ring
      have hlower := hangle i α β hα ht0
      have hX : α * ‖u‖ + β * ‖w‖ = 0 := by
        have hX0 : 0 ≤ α * ‖u‖ + β * ‖w‖ := by positivity
        by_contra hne
        have hpos : 0 < α * ‖u‖ + β * ‖w‖ := lt_of_le_of_ne hX0 (Ne.symm hne)
        have := hlower.trans hupper
        nlinarith
      have hu : 0 < ‖u‖ := norm_pos_iff.mpr (sub_ne_zero.mpr (hinj.ne (P.next_ne i).symm))
      have hα0 : α = 0 := by
        have h1 : 0 ≤ α * ‖u‖ := by positivity
        have h2 : 0 ≤ β * ‖w‖ := by positivity
        have : α * ‖u‖ = 0 := by linarith
        rcases mul_eq_zero.mp this with h | h
        · exact h
        · linarith
      have hs1' : s = 1 := by simp only [α] at hα0; linarith
      rw [← hs, hs1', one_smul, add_sub_cancel]
      rfl
    · rintro rfl
      exact ⟨right_mem_segment ℝ _ _, left_mem_segment ℝ _ _⟩
  · -- non-adjacent edges
    intro i j hij h1 h2
    rw [Set.disjoint_left]
    intro p hp hq
    have hε0 : 0 ≤ ε := (norm_nonneg _).trans (hε i _ (left_mem_segment ℝ _ _)).1
    obtain ⟨a, ha, hga⟩ := P.exists_near_of_mem_image_edge g (hd i)
      (fun z hz => (hε i z hz).1) hp
    obtain ⟨b, hb, hgb⟩ := P.exists_near_of_mem_image_edge g (hd j)
      (fun z hz => (hε j z hz).1) hq
    have hab : ‖g a - g b‖ ≤ 4 * ε * δ := by
      calc ‖g a - g b‖ = ‖(g a - p) - (g b - p)‖ := by congr 1; abel
        _ ≤ ‖g a - p‖ + ‖g b - p‖ := norm_sub_le _ _
        _ ≤ 2 * ε * δ + 2 * ε * δ := by
            gcongr
            · exact hga.trans (mul_le_mul_of_nonneg_left (hlen i) (by positivity))
            · exact hgb.trans (mul_le_mul_of_nonneg_left (hlen j) (by positivity))
        _ = 4 * ε * δ := by ring
    have e1 := hsep i j hij h1 h2 a ha b hb
    have e2 := hlip a (subset_iUnion P.edge i ha) b (subset_iUnion P.edge j hb)
    have e3 := mul_le_mul_of_nonneg_left hab hM
    nlinarith

end Polygon

end QOU.MathlibExt.PL
