/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.PLPlanarCornerEar

set_option autoImplicit false

/-!
# Two ears (issue #8902, Moise part B, step 1)

Every simple polygon with at least four vertices has an ear away from any given edge (Meisters'
two-ears theorem, in the form used for induction).

## What is a THEOREM here

* `exists_ear` — for a simple polygon `P` with `3 ≤ P.n` and any edge `w j, w (j+1)`, some ear's
  vertex is neither endpoint of that edge.

The proof works at the lowest-leftmost vertex `w 0`. Either the triangle at `w 0` holds another
vertex, and the deepest such vertex gives a chord (`exists_chord`, `chord_sides_outside`), or it
is empty and the corner is cut off (`empty_corner_split`). The ear comes from the piece that does
not hold the given edge, by induction (`isEar_of_cut`, `isEar_of_cocut`).
-/

namespace QOU.MathlibExt.PL

open Set Polygon

lemma isEar_mod (P : Polygon R2) (k : ℕ) : P.IsEar (k % (P.n + 1)) ↔ P.IsEar k := by
  have h : ∀ m x, P.IsEar (x + (P.n + 1) * m) ↔ P.IsEar x := by
    intro m
    induction m with
    | zero => intro x; simp
    | succ m ih =>
      intro x
      rw [Nat.mul_succ, ← add_assoc, isEar_add_period, ih]
  conv_rhs => rw [← Nat.mod_add_div k (P.n + 1)]
  exact (h _ _).symm

lemma w_succ_mod (P : Polygon R2) (j : ℕ) : P.w (j % (P.n + 1) + 1) = P.w (j + 1) := by
  rw [← P.w_mod (j % (P.n + 1) + 1), ← P.w_mod (j + 1)]
  congr 1
  simp [Nat.add_mod]

/-- Vertices with distinct indices in `0..n+1` (where `n + 1` is `0` again) are distinct. -/
lemma w_ne_of_idx {P : Polygon R2} (hP : P.IsSimple) {k m : ℕ} (hk : k ≤ P.n) (hm : m ≤ P.n + 1)
    (hkm : k ≠ m) (hk0 : m = P.n + 1 → k ≠ 0) : P.w k ≠ P.w m := by
  intro h
  by_cases hm' : m = P.n + 1
  · subst hm'
    rw [P.w_period] at h
    exact hk0 rfl (hP.w_injOn hk (Nat.zero_le _) h)
  · exact hkm (hP.w_injOn hk (by omega) h)

/-- An ear of a piece, away from the piece's closing edge, at an index in `1 .. n - 1`. -/
lemma ear_in_range {Q : Polygon R2} (hQ : Q.IsSimple) {k' : ℕ} (hk' : Q.IsEar k')
    (h0 : Q.w k' ≠ Q.w Q.n) (h1 : Q.w k' ≠ Q.w (Q.n + 1)) :
    ∃ k, 1 ≤ k ∧ k < Q.n ∧ Q.IsEar k ∧ Q.w k = Q.w k' := by
  refine ⟨k' % (Q.n + 1), ?_, ?_, (isEar_mod Q k').mpr hk', Q.w_mod k'⟩
  · by_contra h
    have : k' % (Q.n + 1) = 0 := by omega
    apply h1; rw [← Q.w_mod k', this, Q.w_period]
  · have hlt := Nat.mod_lt k' (show 0 < Q.n + 1 by omega)
    by_contra h
    have : k' % (Q.n + 1) = Q.n := by omega
    apply h0; rw [← Q.w_mod k', this]

/-- The rotation by `β` of a polygon cut along a valid chord `[w 0, w β]` has a valid chord too,
so the complementary piece is simple. -/
lemma isSimple_cocut {P : Polygon R2} (hP : P.IsSimple) {β : ℕ} (hβ : 2 ≤ β)
    (h2 : 2 ≤ P.n + 1 - β) (h3 : 3 ≤ P.n + 1 - β)
    (hchord : segment ℝ (P.w 0) (P.w β) ∩ P.carrier ⊆ {P.w 0, P.w β}) :
    (P.cocut β h2).IsSimple := by
  have hRs := Polygon.isSimple_rotateBy P hP β
  have hRn : (P.rotateBy β).n = P.n := rotateBy_n P β
  have hR0 : (P.rotateBy β).w 0 = P.w β := by rw [w_rotateBy, zero_add]
  have hRγ : (P.rotateBy β).w (P.n + 1 - β) = P.w 0 := by
    rw [w_rotateBy, show P.n + 1 - β + β = P.n + 1 by omega, P.w_period]
  refine isSimple_cut hRs h2 (by omega) ?_
  rw [hR0, hRγ, carrier_rotateBy, segment_symm]
  intro y hy
  rcases hchord hy with h | h
  · exact Or.inr h
  · exact Or.inl h

/-- **One induction step, at a lowest-leftmost vertex.** -/
theorem exists_ear_step {P : Polygon R2} (hP : P.IsSimple) (hn : 3 ≤ P.n)
    (hlex : ∀ i, P.w 0 0 ≤ P.v i 0) (ha : LexLt (P.w 0) (P.w P.n)) (hb : LexLt (P.w 0) (P.w 1))
    (IH : ∀ Q : Polygon R2, Q.n < P.n → Q.IsSimple → 3 ≤ Q.n → ∀ j,
      ∃ k, Q.IsEar k ∧ Q.w k ≠ Q.w j ∧ Q.w k ≠ Q.w (j + 1))
    (j : ℕ) : ∃ k, P.IsEar k ∧ P.w k ≠ P.w j ∧ P.w k ≠ P.w (j + 1) := by
  rw [← P.w_mod j, ← w_succ_mod P j]
  set j₀ := j % (P.n + 1) with hj₀
  have hj₀n : j₀ ≤ P.n := Nat.lt_succ_iff.mp (Nat.mod_lt _ (Nat.succ_pos _))
  have hD := cross_ne_zero_of_lex hP ha hb
  by_cases hz : ∃ j, 2 ≤ j ∧ j ≤ P.n - 1 ∧ P.w j ∈ convexHull ℝ {P.w P.n, P.w 0, P.w 1}
  · obtain ⟨β, hβ2, hβn1, hchord, hD1, hA, hD2, hB⟩ := exists_chord hP hn hD hz
    have h2 : 2 ≤ P.n + 1 - β := by omega
    obtain ⟨S₁, S₂⟩ := chord_sides_outside hP hlex hβ2 h2 hchord hD1 hA hD2 hB
    by_cases hjβ : j₀ < β
    · -- the ear comes from the complementary piece
      by_cases hm : P.n + 1 - β = 2
      · refine ⟨1 + β, isEar_of_cocut hP hβ2 h2 hchord S₁ S₂ le_rfl (by omega) (Or.inr hm),
          w_ne_of_idx hP (by omega) (by omega) (by omega) (by omega),
          w_ne_of_idx hP (by omega) (by omega) (by omega) (by omega)⟩
      · have hQ := isSimple_cocut hP hβ2 h2 (by omega) hchord
        have hQn : (P.cocut β h2).n = P.n + 1 - β := cut_n _
        obtain ⟨k', hk', h0, h1⟩ := IH (P.cocut β h2) (by omega) hQ (by omega) (P.cocut β h2).n
        obtain ⟨k, hk1, hk2, hkE, -⟩ := ear_in_range hQ hk' h0 h1
        refine ⟨k + β, isEar_of_cocut hP hβ2 h2 hchord S₁ S₂ hk1 (by omega) (Or.inl hkE),
          w_ne_of_idx hP (by omega) (by omega) (by omega) (by omega),
          w_ne_of_idx hP (by omega) (by omega) (by omega) (by omega)⟩
    · -- the ear comes from the cut piece
      by_cases hβ3 : β = 2
      · refine ⟨1, isEar_of_cut hP hβ2 h2 hchord S₁ S₂ le_rfl (by omega) (Or.inr hβ3),
          w_ne_of_idx hP (by omega) (by omega) (by omega) (by omega),
          w_ne_of_idx hP (by omega) (by omega) (by omega) (by omega)⟩
      · have hQ := isSimple_cut hP hβ2 (by omega) hchord
        have hQn : (P.cut β hβ2).n = β := cut_n _
        obtain ⟨k', hk', h0, h1⟩ := IH (P.cut β hβ2) (by omega) hQ (by omega) (P.cut β hβ2).n
        obtain ⟨k, hk1, hk2, hkE, -⟩ := ear_in_range hQ hk' h0 h1
        refine ⟨k, isEar_of_cut hP hβ2 h2 hchord S₁ S₂ hk1 (by omega) (Or.inl hkE),
          w_ne_of_idx hP (by omega) (by omega) (by omega) (by omega),
          w_ne_of_idx hP (by omega) (by omega) (by omega) (by omega)⟩
  · push_neg at hz
    have hempty : ∀ j, 2 ≤ j → j ≤ P.n - 1 →
        P.w j ∉ convexHull ℝ {P.w P.n, P.w 0, P.w 1} := hz
    by_cases hj0 : j₀ ≠ 0 ∧ j₀ ≠ P.n
    · exact ⟨0, isEar_of_empty_corner hP hn hlex hD hempty,
        w_ne_of_idx hP (by omega) (by omega) (by omega) (by omega),
        w_ne_of_idx hP (by omega) (by omega) (by omega) (by omega)⟩
    obtain ⟨hβ, h2, hchord, S₁, S₂⟩ := empty_corner_split hP hn hlex hD hempty
    set R := P.rotateBy 1 with hR
    have hRs : R.IsSimple := Polygon.isSimple_rotateBy P hP 1
    have hRn : R.n = P.n := rotateBy_n P 1
    -- an ear of `R` at an index `k` in `1 .. n - 2` gives the ear `k + 1` of `P`
    suffices h : ∃ k, 1 ≤ k ∧ k < P.n - 1 ∧ R.IsEar k by
      obtain ⟨k, hk1, hk2, hkE⟩ := h
      rw [isEar_rotateBy] at hkE
      exact ⟨k + 1, hkE, w_ne_of_idx hP (by omega) (by omega) (by omega) (by omega),
        w_ne_of_idx hP (by omega) (by omega) (by omega) (by omega)⟩
    by_cases hβ3 : P.n - 1 = 2
    · exact ⟨1, le_rfl, by omega,
        isEar_of_cut hRs hβ (by rw [hRn]; omega) hchord S₁ S₂ le_rfl (by omega) (Or.inr hβ3)⟩
    · have hQ := isSimple_cut hRs hβ (by omega) hchord
      have hQn : (R.cut (P.n - 1) hβ).n = P.n - 1 := cut_n _
      obtain ⟨k', hk', h0, h1⟩ := IH (R.cut (P.n - 1) hβ) (by omega) hQ (by omega)
        (R.cut (P.n - 1) hβ).n
      obtain ⟨k, hk1, hk2, hkE, -⟩ := ear_in_range hQ hk' h0 h1
      exact ⟨k, hk1, by omega,
        isEar_of_cut hRs hβ (by rw [hRn]; omega) hchord S₁ S₂ hk1 (by omega) (Or.inl hkE)⟩

/-- **Two ears.** A simple polygon with at least four vertices has an ear whose vertex is
neither endpoint of any given edge. -/
theorem exists_ear (P : Polygon R2) (hP : P.IsSimple) (hn : 3 ≤ P.n) (j : ℕ) :
    ∃ k, P.IsEar k ∧ P.w k ≠ P.w j ∧ P.w k ≠ P.w (j + 1) := by
  suffices H : ∀ N, ∀ P : Polygon R2, P.n = N → P.IsSimple → 3 ≤ P.n → ∀ j,
      ∃ k, P.IsEar k ∧ P.w k ≠ P.w j ∧ P.w k ≠ P.w (j + 1) from H _ P rfl hP hn j
  intro N
  induction N using Nat.strong_induction_on with
  | _ N ih =>
  intro P hPN hP hn j
  obtain ⟨i, hi⟩ := exists_lexMin P hP
  set R := P.rotateBy i with hR
  have hRs : R.IsSimple := Polygon.isSimple_rotateBy P hP i
  have hRn : R.n = P.n := rotateBy_n P i
  have hw : ∀ k, R.w k = P.w (k + i) := fun k => w_rotateBy P i k
  have hR0 : R.w 0 = P.v i := by rw [hw, zero_add, w_coe]
  have hlexw : ∀ m, P.w m ≠ P.v i → LexLt (P.v i) (P.w m) := fun m hm =>
    hi _ (fun h => hm (by show P.v _ = _; rw [h]))
  have hle : ∀ m, P.v i 0 ≤ P.w m 0 := by
    intro m
    by_cases hm : P.w m = P.v i
    · rw [hm]
    · rcases hlexw m hm with h | h
      · exact h.le
      · exact h.1.le
  have hlexR : ∀ i', R.w 0 0 ≤ R.v i' 0 := by
    intro i'; rw [← w_coe R i', hw, hw, zero_add, w_coe P i]; exact hle _
  have haR : LexLt (R.w 0) (R.w R.n) := by
    rw [hR0, hw]
    refine hlexw _ fun h => hRs.w_n_ne_zero ?_
    rw [hw, hw, h, zero_add, w_coe]
  have hbR : LexLt (R.w 0) (R.w 1) := by
    rw [hR0, hw]
    refine hlexw _ fun h => (hRs.w_ne_succ (k := 0) (by omega)) ?_
    rw [hw, hw, zero_add, zero_add, h, w_coe]
  obtain ⟨k, hkE, hk1, hk2⟩ := exists_ear_step hRs (by omega) hlexR haR hbR
    (fun Q hQn hQs hQ3 => ih Q.n (by omega) Q rfl hQs hQ3) (j + (P.n + 1) - i)
  have hi' : (i : ℕ) ≤ P.n := Nat.lt_succ_iff.mp i.2
  refine ⟨k + i, (isEar_rotateBy P i k).mp hkE, ?_, ?_⟩
  · intro h; apply hk1
    rw [hw, hw, h, show j + (P.n + 1) - i + i = j + (P.n + 1) by omega, w_add_period]
  · intro h; apply hk2
    rw [hw, hw, h, show j + (P.n + 1) - i + 1 + i = (j + 1) + (P.n + 1) by omega, w_add_period]

end QOU.MathlibExt.PL
