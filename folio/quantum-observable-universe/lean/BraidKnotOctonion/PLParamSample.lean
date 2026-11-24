/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import BraidKnotOctonion.PLSubdivide
import BraidKnotOctonion.PLAmbientIsotopy
import Mathlib.Data.Finset.Sort

set_option autoImplicit false

/-!
# Sampling a polygon at finitely many times (issue #8902, isotopy-to-Δ bridge)

A polygon `Q` with `N = n + 1` vertices has the standard parametrization `Q.param` of period
`1`, with vertex `i` at time `i / N`. Given a finite set `S ⊆ [0, 1)` of times, the **sample
list** `Q.sampleVerts S` lists `Q.param s` for `s ∈ S` in increasing order.

## What is a DEFINITION here

* `Polygon.vertexTimes Q` — the times `i / N` of the vertices.
* `Polygon.sampleVerts Q S` — `(S.sort (· ≤ ·)).map Q.param`.

## What is a THEOREM here

* `Polygon.param_piece` — on `[i / N, (i + 1) / N]` the parametrization is affine:
  `Q.param x = v i + (N x - i) • (v (i+1) - v i)`.
* `Polygon.param_mem_openSegment` — three increasing times on one piece give three points with
  the middle one in the open segment of the outer two.
* `Polygon.refines_sampleVerts` — **if `S ⊆ [0, 1)` contains all vertex times, the sample list
  refines the vertex list**: it is reached by insertions on edges and re-indexings.
* `PolygonalLink.reaches_sampleVerts` — so a component is Δ-equivalent to its sample.
* `Polygon.refines_reparam`, `PolygonalLink.reaches_reparam` — the same along an oriented
  reparametrization `φ`, when the times `fract (φ s)` hit every vertex time. This is the form
  met at the end of an ambient isotopy.
-/

namespace QOU.MathlibExt.PL

open Set

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

namespace Polygon

variable (Q : Polygon E)

lemma param_eq_pathRaw {x : ℝ} (h0 : 0 ≤ x) (h1 : x ≤ 1) : Q.param x = Q.pathRaw x := by
  rcases h1.lt_or_eq with h | rfl
  · rw [param, Int.fract_eq_self.mpr ⟨h0, h⟩]
  · rw [param, Int.fract_one, Q.pathRaw_zero, Q.pathRaw_one]

/-- **The parametrization is affine on each piece.** -/
lemma param_piece (i : Fin (Q.n + 1)) {x : ℝ} (h0 : (i : ℝ) / (Q.n + 1) ≤ x)
    (h1 : x ≤ ((i : ℝ) + 1) / (Q.n + 1)) :
    Q.param x = Q.v i + ((Q.n + 1 : ℝ) * x - i) • (Q.v (Q.next i) - Q.v i) := by
  have hN : (0 : ℝ) < Q.n + 1 := by positivity
  have hi : (i : ℝ) ≤ Q.n := by exact_mod_cast Nat.lt_succ_iff.mp i.isLt
  have hx0 : 0 ≤ x := le_trans (by positivity) h0
  have hx1 : x ≤ 1 := h1.trans (by rw [div_le_one hN]; linarith)
  rw [div_le_iff₀ hN] at h0
  rw [le_div_iff₀ hN] at h1
  have hu0 : 0 ≤ (Q.n + 1 : ℝ) * x - i := by linarith
  have hu1 : (Q.n + 1 : ℝ) * x - i ≤ 1 := by linarith
  have hx : x = ((i : ℝ) + ((Q.n + 1 : ℝ) * x - i)) / (Q.n + 1) := by field_simp; ring
  rw [Q.param_eq_pathRaw hx0 hx1]
  conv_lhs => rw [hx]
  rw [Q.pathRaw_piece i hu0 hu1]
  module

/-- The time of vertex `i`. -/
noncomputable def vtime (i : Fin (Q.n + 1)) : ℝ := (i : ℝ) / (Q.n + 1)

lemma param_vtime (i : Fin (Q.n + 1)) : Q.param (Q.vtime i) = Q.v i := by
  have hN : (0 : ℝ) < Q.n + 1 := by positivity
  rw [vtime, Q.param_piece i le_rfl (by gcongr; linarith)]
  rw [show (Q.n + 1 : ℝ) * ((i : ℝ) / (Q.n + 1)) - i = 0 by field_simp; ring, zero_smul,
    add_zero]

lemma vtime_strictMono : StrictMono Q.vtime := fun i j h => by
  have hN : (0 : ℝ) < Q.n + 1 := by positivity
  simp only [vtime]
  exact div_lt_div_of_pos_right (by exact_mod_cast h) hN

lemma vtime_mem_Ico (i : Fin (Q.n + 1)) : Q.vtime i ∈ Ico (0 : ℝ) 1 := by
  have hN : (0 : ℝ) < Q.n + 1 := by positivity
  have hi : (i : ℝ) ≤ Q.n := by exact_mod_cast Nat.lt_succ_iff.mp i.isLt
  exact ⟨by simp only [vtime]; positivity, by rw [vtime, div_lt_one hN]; linarith⟩

/-- The vertex times. -/
noncomputable def vertexTimes : Finset ℝ := Finset.univ.image Q.vtime

/-- The sample list. -/
noncomputable def sampleVerts (S : Finset ℝ) : List E := (S.sort (· ≤ ·)).map Q.param

lemma length_sampleVerts (S : Finset ℝ) : (Q.sampleVerts S).length = S.card := by
  simp [sampleVerts]

lemma sort_vertexTimes : Q.vertexTimes.sort (· ≤ ·) = List.ofFn Q.vtime := by
  have hinj := Q.vtime_strictMono.injective
  apply List.eq_of_perm_of_sorted (r := (· ≤ ·))
  · rw [List.perm_ext_iff_of_nodup (Finset.sort_nodup _ _) (List.nodup_ofFn.mpr hinj)]
    intro a
    rw [Finset.mem_sort, List.mem_ofFn]
    simp [vertexTimes]
  · exact Finset.sort_sorted _ _
  · exact List.pairwise_ofFn.mpr fun i j h => (Q.vtime_strictMono h).le

lemma sampleVerts_vertexTimes : Q.sampleVerts Q.vertexTimes = List.ofFn Q.v := by
  rw [sampleVerts, sort_vertexTimes, List.map_ofFn]
  congr 1
  funext i
  exact Q.param_vtime i

/-- **Three increasing times on one piece.** -/
lemma param_mem_openSegment (i : Fin (Q.n + 1)) {p σ q : ℝ} (hp : (i : ℝ) / (Q.n + 1) ≤ p)
    (hpσ : p < σ) (hσq : σ < q) (hq : q ≤ ((i : ℝ) + 1) / (Q.n + 1)) :
    Q.param σ ∈ openSegment ℝ (Q.param p) (Q.param q) := by
  rw [Q.param_piece i hp (by linarith), Q.param_piece i (x := σ) (by linarith) (by linarith),
    Q.param_piece i (x := q) (by linarith) hq]
  have hqp : 0 < q - p := by linarith
  refine ⟨(q - σ) / (q - p), (σ - p) / (q - p), div_pos (by linarith) hqp,
    div_pos (by linarith) hqp, by field_simp; ring, ?_⟩
  set a := (q - σ) / (q - p)
  set b := (σ - p) / (q - p)
  have hab : a + b = 1 := by simp only [a, b]; field_simp; ring
  have hc : a * ((Q.n + 1 : ℝ) * p - i) + b * ((Q.n + 1 : ℝ) * q - i) =
      (Q.n + 1 : ℝ) * σ - i := by simp only [a, b]; field_simp; ring
  calc a • (Q.v i + ((Q.n + 1 : ℝ) * p - i) • (Q.v (Q.next i) - Q.v i)) +
        b • (Q.v i + ((Q.n + 1 : ℝ) * q - i) • (Q.v (Q.next i) - Q.v i))
      = (a + b) • Q.v i + (a * ((Q.n + 1 : ℝ) * p - i) + b * ((Q.n + 1 : ℝ) * q - i)) •
          (Q.v (Q.next i) - Q.v i) := by module
    _ = _ := by rw [hab, hc, one_smul]

lemma param_one : Q.param 1 = Q.param 0 := by
  simp [param]

/-- **One insertion.** -/
theorem refines_insert (S : Finset ℝ) (hS : ∀ x ∈ S, 0 ≤ x ∧ x < 1)
    (hV : Q.vertexTimes ⊆ S) {σ : ℝ} (hσ : σ ∉ S) (hσ0 : 0 ≤ σ) (hσ1 : σ < 1) :
    Refines (Q.sampleVerts S) (Q.sampleVerts (insert σ S)) := by
  set l := S.sort (· ≤ ·) with hl
  have hlt : l.Sorted (· < ·) := Finset.sort_sorted_lt S
  set l₁ := l.filter (fun x => decide (x < σ))
  set l₂ := l.filter (fun x => decide (σ < x))
  have hmem1 : ∀ x, x ∈ l₁ ↔ x ∈ S ∧ x < σ := fun x => by simp [l₁, l]
  have hmem2 : ∀ x, x ∈ l₂ ↔ x ∈ S ∧ σ < x := fun x => by simp [l₂, l]
  have hs1 : l₁.Sorted (· < ·) := hlt.filter _
  have hs2 : l₂.Sorted (· < ·) := hlt.filter _
  have hcross : ∀ a ∈ l₁, ∀ b ∈ l₂, a < b := fun a ha b hb =>
    ((hmem1 a).mp ha).2.trans ((hmem2 b).mp hb).2
  have hne_σ : ∀ x ∈ S, x ≠ σ := fun x hx h => hσ (h ▸ hx)
  -- `l = l₁ ++ l₂`
  have hsplit : l = l₁ ++ l₂ := by
    apply List.eq_of_perm_of_sorted (r := (· < ·)) _ hlt
    · exact List.pairwise_append.mpr ⟨hs1, hs2, hcross⟩
    · rw [List.perm_ext_iff_of_nodup (hlt.nodup)
        (List.pairwise_append.mpr ⟨hs1, hs2, hcross⟩).nodup]
      intro x
      rw [List.mem_append, hmem1, hmem2]
      simp only [l, Finset.mem_sort]
      constructor
      · intro hx
        rcases lt_or_gt_of_ne (hne_σ x hx) with h | h
        · exact Or.inl ⟨hx, h⟩
        · exact Or.inr ⟨hx, h⟩
      · rintro (h | h) <;> exact h.1
  -- the sorted insert
  have hsplit' : (insert σ S).sort (· ≤ ·) = l₁ ++ σ :: l₂ := by
    have hsorted : (l₁ ++ σ :: l₂).Sorted (· < ·) := by
      refine List.pairwise_append.mpr ⟨hs1, List.pairwise_cons.mpr
        ⟨fun b hb => ((hmem2 b).mp hb).2, hs2⟩, fun a ha b hb => ?_⟩
      rcases List.mem_cons.mp hb with rfl | hb
      · exact ((hmem1 a).mp ha).2
      · exact hcross a ha b hb
    apply List.eq_of_perm_of_sorted (r := (· < ·)) _ (Finset.sort_sorted_lt _) hsorted
    rw [List.perm_ext_iff_of_nodup (Finset.sort_nodup _ _) hsorted.nodup]
    intro x
    rw [Finset.mem_sort, Finset.mem_insert, List.mem_append, List.mem_cons, hmem1, hmem2]
    constructor
    · rintro (rfl | hx)
      · exact Or.inr (Or.inl rfl)
      · rcases lt_or_gt_of_ne (hne_σ x hx) with h | h
        · exact Or.inl ⟨hx, h⟩
        · exact Or.inr (Or.inr ⟨hx, h⟩)
    · rintro (h | rfl | h)
      · exact Or.inr h.1
      · exact Or.inl rfl
      · exact Or.inr h.1
  -- the vertex time `0` is below `σ`
  have h0S : (0 : ℝ) ∈ S := by
    have := hV (Finset.mem_image_of_mem Q.vtime (Finset.mem_univ 0))
    simpa [vtime] using this
  have h0σ : 0 < σ := lt_of_le_of_ne hσ0 (fun h => hσ (h ▸ h0S))
  have h0l₁ : (0 : ℝ) ∈ l₁ := (hmem1 0).mpr ⟨h0S, h0σ⟩
  have hl₁ne : l₁ ≠ [] := List.ne_nil_of_mem h0l₁
  set p := l₁.getLast hl₁ne
  have hpl₁ : p ∈ l₁ := List.getLast_mem hl₁ne
  have hp_max : ∀ x ∈ l₁, x ≤ p := by
    intro x hx
    have e := List.dropLast_append_getLast hl₁ne
    rw [← e] at hx hs1
    rcases List.mem_append.mp hx with hx | hx
    · exact ((List.pairwise_append.mp hs1).2.2 x hx p (List.mem_singleton_self _)).le
    · rw [List.mem_singleton.mp hx]
  have hpσ : p < σ := ((hmem1 p).mp hpl₁).2
  -- the piece containing `σ`
  obtain ⟨i, u, hu0, hu1, hσe⟩ := Q.exists_piece hσ0 hσ1
  have hN : (0 : ℝ) < Q.n + 1 := by positivity
  have hu0' : 0 < u := by
    refine lt_of_le_of_ne hu0 fun hu => hσ ?_
    rw [hσe, ← hu, add_zero]
    exact hV (Finset.mem_image_of_mem Q.vtime (Finset.mem_univ i))
  have hiσ : (i : ℝ) / (Q.n + 1) < σ := by
    rw [hσe]; exact div_lt_div_of_pos_right (by linarith) hN
  have hσi : σ < ((i : ℝ) + 1) / (Q.n + 1) := by
    rw [hσe]; exact div_lt_div_of_pos_right (by linarith) hN
  have hip : (i : ℝ) / (Q.n + 1) ≤ p := by
    refine hp_max _ ((hmem1 _).mpr ⟨hV (Finset.mem_image_of_mem Q.vtime (Finset.mem_univ i)), hiσ⟩)
  have hA : Q.sampleVerts S = l₁.map Q.param ++ l₂.map Q.param := by
    rw [sampleVerts, ← hl, hsplit, List.map_append]
  have hA' : Q.sampleVerts (insert σ S) = l₁.map Q.param ++ Q.param σ :: l₂.map Q.param := by
    rw [sampleVerts, hsplit', List.map_append, List.map_cons]
  have hAne : l₁.map Q.param ≠ [] := by simpa using hl₁ne
  have hAlast : (l₁.map Q.param).getLast hAne = Q.param p := by
    rw [List.getLast_map]
  rw [hA, hA']
  rcases hl₂ : l₂ with _ | ⟨q, r⟩
  · -- `σ` is the last sample: insert on the closing edge
    have hin : (i : ℕ) = Q.n := by
      by_contra hne
      have hi' : (i : ℕ) + 1 < Q.n + 1 := by have := i.isLt; omega
      have hmem : Q.vtime ⟨(i : ℕ) + 1, hi'⟩ ∈ l₂ := by
        refine (hmem2 _).mpr ⟨hV (Finset.mem_image_of_mem Q.vtime (Finset.mem_univ _)), ?_⟩
        simpa [vtime] using hσi
      rw [hl₂] at hmem
      simp at hmem
    have hq1 : ((i : ℝ) + 1) / (Q.n + 1) = 1 := by
      rw [show (i : ℝ) = Q.n by exact_mod_cast hin, div_self hN.ne']
    have hhead : (l₁.map Q.param).head hAne = Q.param 1 := by
      rw [List.head_map, param_one]
      congr 1
      have hh := List.head_mem hl₁ne
      have hle : l₁.head hl₁ne ≤ 0 := by
        obtain ⟨a, t, ht⟩ := List.exists_cons_of_ne_nil hl₁ne
        have : l₁.head hl₁ne = a := by simp [ht]
        rw [this]
        have h0' := h0l₁
        rw [ht] at h0' hs1
        rcases List.mem_cons.mp h0' with h | h
        · exact h.symm.le
        · exact (List.pairwise_cons.mp hs1).1 0 h |>.le
      exact le_antisymm hle (hS _ ((hmem1 _).mp hh).1).1
    have hc : Q.param σ ∈ openSegment ℝ ((l₁.map Q.param).getLast hAne)
        ((l₁.map Q.param).head hAne) := by
      rw [hAlast, hhead]
      exact Q.param_mem_openSegment i hip hpσ (by linarith [hσi, hq1]) hq1.ge
    have := Refines.insert hAne (Q.param σ) hc (Refines.refl (l₁.map Q.param))
    simpa using this
  · -- rotate, insert, rotate back
    have hqS : q ∈ l₂ := by rw [hl₂]; exact List.mem_cons_self
    have hσq : σ < q := ((hmem2 q).mp hqS).2
    have hq_le : q ≤ ((i : ℝ) + 1) / (Q.n + 1) := by
      by_cases hin : (i : ℕ) + 1 < Q.n + 1
      · have hmem : Q.vtime ⟨(i : ℕ) + 1, hin⟩ ∈ l₂ := by
          refine (hmem2 _).mpr ⟨hV (Finset.mem_image_of_mem Q.vtime (Finset.mem_univ _)), ?_⟩
          simpa [vtime] using hσi
        have hs2' := hs2
        rw [hl₂] at hmem hs2'
        rcases List.mem_cons.mp hmem with h | h
        · rw [← h]; simp [vtime]
        · have := (List.pairwise_cons.mp hs2').1 _ h
          simp only [vtime, Nat.cast_add, Nat.cast_one] at this
          exact this.le
      · have hin' : (i : ℕ) = Q.n := by have := i.isLt; omega
        rw [show (i : ℝ) = Q.n by exact_mod_cast hin', div_self hN.ne']
        exact (hS q ((hmem2 q).mp hqS).1).2.le
    simp only [List.map_cons]
    set A := l₁.map Q.param
    set B := Q.param q :: r.map Q.param
    have h1 := (Refines.refl (A ++ B)).rotate A.length
    rw [List.rotate_append_length_eq] at h1
    have hBAne : B ++ A ≠ [] := by simp [B]
    have hc : Q.param σ ∈ openSegment ℝ ((B ++ A).getLast hBAne) ((B ++ A).head hBAne) := by
      rw [List.getLast_append_of_ne_nil hBAne hAne, hAlast]
      simp only [B, List.head_cons, List.cons_append]
      exact Q.param_mem_openSegment i hip hpσ hσq hq_le
    have h2 := (h1.insert hBAne (Q.param σ) hc).rotate B.length
    rw [List.append_assoc, List.rotate_append_length_eq, List.append_assoc] at h2
    simpa using h2

/-- **The sample list refines the vertex list**, when `S ⊆ [0, 1)` contains every vertex
time. -/
theorem refines_sampleVerts (S : Finset ℝ) (hS : ∀ x ∈ S, 0 ≤ x ∧ x < 1)
    (hV : Q.vertexTimes ⊆ S) : Refines (List.ofFn Q.v) (Q.sampleVerts S) := by
  classical
  have key : ∀ T : Finset ℝ, (∀ x ∈ T, 0 ≤ x ∧ x < 1) →
      Refines (List.ofFn Q.v) (Q.sampleVerts (Q.vertexTimes ∪ T)) := by
    intro T
    induction T using Finset.induction_on with
    | empty =>
      intro _
      rw [Finset.union_empty, sampleVerts_vertexTimes]
      exact Refines.refl _
    | insert σ T hσT ih =>
      intro hT
      have ih' := ih fun x hx => hT x (Finset.mem_insert_of_mem hx)
      rw [Finset.union_insert]
      by_cases hmem : σ ∈ Q.vertexTimes ∪ T
      · rw [Finset.insert_eq_of_mem hmem]; exact ih'
      · refine ih'.trans (Q.refines_insert _ (fun x hx => ?_) Finset.subset_union_left hmem
          (hT σ (Finset.mem_insert_self _ _)).1 (hT σ (Finset.mem_insert_self _ _)).2)
        rcases Finset.mem_union.mp hx with hx | hx
        · obtain ⟨j, -, rfl⟩ := Finset.mem_image.mp hx
          exact Q.vtime_mem_Ico j
        · exact hT x (Finset.mem_insert_of_mem hx)
  have := key S hS
  rwa [Finset.union_eq_right.mpr hV] at this

lemma card_vertexTimes : Q.vertexTimes.card = Q.n + 1 := by
  rw [vertexTimes, Finset.card_image_of_injective _ Q.vtime_strictMono.injective,
    Finset.card_univ, Fintype.card_fin]

lemma three_le_card {S : Finset ℝ} (hV : Q.vertexTimes ⊆ S) : 3 ≤ S.card := by
  have := Finset.card_le_card hV
  rw [card_vertexTimes] at this
  have := Q.two_le
  omega

/-- **Sampling after an oriented reparametrization.** If `φ` is an oriented reparametrization and
the times `fract (φ s)`, `s ∈ S`, hit every vertex time, the list `Q.param (φ s)` over the sorted
`S` refines the vertex list. It is a rotation of the sample at `fract ∘ φ '' S`. -/
theorem refines_reparam (S : Finset ℝ) (hS : ∀ x ∈ S, 0 ≤ x ∧ x < 1) {φ : ℝ → ℝ}
    (hφ : OrientedReparam φ) (hV : ∀ i, ∃ s ∈ S, Int.fract (φ s) = Q.vtime i) :
    Refines (List.ofFn Q.v) ((S.sort (· ≤ ·)).map fun s => Q.param (φ s)) := by
  classical
  set f : ℝ → ℝ := fun s => Int.fract (φ s)
  set S' := S.image f
  have hS' : ∀ x ∈ S', 0 ≤ x ∧ x < 1 := by
    intro x hx
    obtain ⟨s, -, rfl⟩ := Finset.mem_image.mp hx
    exact ⟨Int.fract_nonneg _, Int.fract_lt_one _⟩
  have hV' : Q.vertexTimes ⊆ S' := by
    intro x hx
    obtain ⟨i, -, rfl⟩ := Finset.mem_image.mp hx
    obtain ⟨s, hs, he⟩ := hV i
    exact Finset.mem_image.mpr ⟨s, hs, he⟩
  have href := Q.refines_sampleVerts S' hS' hV'
  set z := ⌊φ 0⌋
  have hφ1 : φ 1 = φ 0 + 1 := by simpa using hφ.add_one 0
  have hrange : ∀ s ∈ S, φ 0 ≤ φ s ∧ φ s < φ 0 + 1 := fun s hs =>
    ⟨hφ.strictMono.monotone (hS s hs).1, hφ1 ▸ hφ.strictMono (hS s hs).2⟩
  have hz0 : (z : ℝ) ≤ φ 0 := Int.floor_le _
  have hz1 : φ 0 < z + 1 := Int.lt_floor_add_one _
  set p : ℝ → Bool := fun s => decide (φ s < z + 1)
  set l := S.sort (· ≤ ·) with hl
  have hlt : l.Sorted (· < ·) := Finset.sort_sorted_lt S
  have hlS : ∀ s ∈ l, s ∈ S := fun s hs => (Finset.mem_sort _).mp hs
  have hfa : ∀ s ∈ S, p s = true → f s = φ s - z := by
    intro s hs hp
    have := hrange s hs
    simp only [p, decide_eq_true_eq] at hp
    simp only [f, Int.fract, Int.floor_eq_iff.mpr ⟨by linarith, hp⟩]
  have hfb : ∀ s ∈ S, p s = false → f s = φ s - (z + 1) := by
    intro s hs hp
    have := hrange s hs
    simp only [p, decide_eq_false_iff_not, not_lt] at hp
    have hfl : ⌊φ s⌋ = z + 1 := Int.floor_eq_iff.mpr ⟨by push_cast; linarith, by push_cast; linarith⟩
    simp only [f, Int.fract, hfl]; push_cast; ring
  set la := l.filter p
  set lb := l.filter (fun s => !p s)
  have hcross : ∀ a ∈ la, ∀ b ∈ lb, a < b := by
    intro a ha b hb
    simp only [la, lb, List.mem_filter, p, decide_eq_true_eq, Bool.not_eq_true',
      decide_eq_false_iff_not, not_lt] at ha hb
    by_contra h
    push_neg at h
    have := hφ.strictMono.monotone h
    linarith [ha.2, hb.2]
  have hsplit : l = la ++ lb := by
    apply List.eq_of_perm_of_sorted (r := (· < ·)) _ hlt
    · exact List.pairwise_append.mpr ⟨hlt.filter _, hlt.filter _, hcross⟩
    · exact (List.filter_append_perm p l).symm
  -- the sorted sample at `S'`
  have hsort : S'.sort (· ≤ ·) = lb.map f ++ la.map f := by
    have hsa : (la.map f).Sorted (· < ·) := by
      refine List.pairwise_map.mpr ((hlt.filter p).imp_of_mem fun {a b} ha hb hab => ?_)
      have ha' := List.mem_filter.mp ha
      have hb' := List.mem_filter.mp hb
      rw [hfa a (hlS a ha'.1) ha'.2, hfa b (hlS b hb'.1) hb'.2]
      linarith [hφ.strictMono hab]
    have hsb : (lb.map f).Sorted (· < ·) := by
      refine List.pairwise_map.mpr ((hlt.filter _).imp_of_mem fun {a b} ha hb hab => ?_)
      have ha' := List.mem_filter.mp ha
      have hb' := List.mem_filter.mp hb
      rw [hfb a (hlS a ha'.1) (by simpa using ha'.2), hfb b (hlS b hb'.1) (by simpa using hb'.2)]
      linarith [hφ.strictMono hab]
    have hsorted : (lb.map f ++ la.map f).Sorted (· < ·) := by
      refine List.pairwise_append.mpr ⟨hsb, hsa, fun x hx y hy => ?_⟩
      obtain ⟨b, hb, rfl⟩ := List.mem_map.mp hx
      obtain ⟨a, ha, rfl⟩ := List.mem_map.mp hy
      have ha' := List.mem_filter.mp ha
      have hb' := List.mem_filter.mp hb
      rw [hfb b (hlS b hb'.1) (by simpa using hb'.2), hfa a (hlS a ha'.1) ha'.2]
      have := hrange a (hlS a ha'.1)
      have := hrange b (hlS b hb'.1)
      linarith
    apply List.eq_of_perm_of_sorted (r := (· < ·)) _ (Finset.sort_sorted_lt _) hsorted
    rw [List.perm_ext_iff_of_nodup (Finset.sort_nodup _ _) hsorted.nodup]
    intro x
    rw [Finset.mem_sort, Finset.mem_image, List.perm_append_comm.mem_iff, ← List.map_append,
      ← hsplit, List.mem_map]
    simp only [l, Finset.mem_sort]
  have hparam : ∀ s, Q.param (φ s) = Q.param (f s) := fun s => by
    simp only [f, param, Int.fract_fract]
  have hmap : (l.map fun s => Q.param (φ s)) = la.map (Q.param ∘ f) ++ lb.map (Q.param ∘ f) := by
    rw [hsplit, List.map_append]
    congr 1 <;> exact List.map_congr_left fun s _ => hparam s
  rw [hmap]
  have hS'v : Q.sampleVerts S' = lb.map (Q.param ∘ f) ++ la.map (Q.param ∘ f) := by
    rw [sampleVerts, hsort, List.map_append, List.map_map, List.map_map]
  rw [hS'v] at href
  have := href.rotate (lb.map (Q.param ∘ f)).length
  rwa [List.rotate_append_length_eq] at this

lemma card_le_of_reparam (S : Finset ℝ) {φ : ℝ → ℝ}
    (hV : ∀ i, ∃ s ∈ S, Int.fract (φ s) = Q.vtime i) : 3 ≤ S.card := by
  classical
  have hsub : Q.vertexTimes ⊆ S.image fun s => Int.fract (φ s) := by
    intro x hx
    obtain ⟨i, -, rfl⟩ := Finset.mem_image.mp hx
    obtain ⟨s, hs, he⟩ := hV i
    exact Finset.mem_image.mpr ⟨s, hs, he⟩
  exact (Q.three_le_card hsub).trans Finset.card_image_le

end Polygon

namespace PolygonalLink

variable (L : PolygonalLink E) (m : Fin L.k)

/-- **A component is Δ-equivalent to its sample** at any finite set of times in `[0, 1)`
containing the vertex times. -/
theorem reaches_sampleVerts (S : Finset ℝ) (hS : ∀ x ∈ S, 0 ≤ x ∧ x < 1)
    (hV : (L.comp m).vertexTimes ⊆ S) :
    L.Reaches m (Polygon.ofList ((L.comp m).sampleVerts S)
      (by rw [Polygon.length_sampleVerts]; exact (L.comp m).three_le_card hV)) := by
  have hm : L.comp m = Polygon.ofList (List.ofFn (L.comp m).v) (by
      simp only [List.length_ofFn]; have := (L.comp m).two_le; omega) :=
    (Polygon.ofList_ofFn _).symm
  exact Reaches.of_refines L m ((L.comp m).refines_sampleVerts S hS hV) _ hm

/-- **The `t = 1` end.** A component is Δ-equivalent to its sample along an oriented
reparametrization, when the reparametrized times hit every vertex time. -/
theorem reaches_reparam (S : Finset ℝ) (hS : ∀ x ∈ S, 0 ≤ x ∧ x < 1) {φ : ℝ → ℝ}
    (hφ : OrientedReparam φ) (hV : ∀ i, ∃ s ∈ S, Int.fract (φ s) = (L.comp m).vtime i) :
    L.Reaches m (Polygon.ofList ((S.sort (· ≤ ·)).map fun s => (L.comp m).param (φ s))
      (by simp only [List.length_map, Finset.length_sort]
          exact (L.comp m).card_le_of_reparam S hV)) := by
  have hm : L.comp m = Polygon.ofList (List.ofFn (L.comp m).v) (by
      simp only [List.length_ofFn]; have := (L.comp m).two_le; omega) :=
    (Polygon.ofList_ofFn _).symm
  exact Reaches.of_refines L m ((L.comp m).refines_reparam S hS hφ hV) _ hm

end PolygonalLink

end QOU.MathlibExt.PL
