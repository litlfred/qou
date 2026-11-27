import BraidKnotOctonion.YoungDiagramTailSecondInstance

/-!
# Depth-2 (`v = n − 2`) hook carriers

A cell `p` of a partition `l ⊢ n` has hook length `n − 2` exactly when its hook misses two cells.
This file finds every such cell and every partition that has one.

* The carrier is one of `(0,0)`, `(0,1)`, `(0,2)`, `(1,0)`, `(2,0)`.
* `(0,2)` sits on `[a]`; `(0,1)` on `[a, b]` with `b ≤ 2`; `(2,0)` on `1^m`; `(1,0)` on
  `(2, b, 1^c)` with `b ≤ 2`; `(0,0)` on `(a, 3, 1^c)` or `(a, 2, 2, 1^c)`.

The tail audit is `docs/audits/2026-11-27-covariance-kernel-depth-two-tail.md` (bean `qou-swk4`).
-/

set_option autoImplicit false

namespace QOU.BraidsAndKnots.DepthTwoHookClassification

open QOU.BraidsAndKnots.YoungDiagramKernel
open QOU.BraidsAndKnots.YoungDiagramTransposeBridge
open QOU.BraidsAndKnots.YoungDiagramKernelPincer
open QOU.BraidsAndKnots.HookArmLeg (armF legF mem_armF_iff mem_legF_iff card_hookUnion
  hookUnion_subset)

/-! ## Missed cells -/

/-- Rows of a sorted list get shorter going down. -/
theorem getD_anti (l : List ℕ) (hs : l.Sorted (· ≥ ·)) {i i' : ℕ} (h : i' ≤ i) :
    l.getD i 0 ≤ l.getD i' 0 := by
  by_cases hi : i < l.length
  · have hi' : i' < l.length := lt_of_le_of_lt h hi
    rw [List.getD_eq_getElem _ _ hi, List.getD_eq_getElem _ _ hi']
    rcases eq_or_lt_of_le h with hEq | hLt
    · subst hEq; exact le_refl _
    · exact List.Sorted.rel_get_of_lt hs hLt
  · rw [List.getD_eq_default _ _ (by omega)]
    exact Nat.zero_le _

/-- A cell up and to the left of a cell is a cell. -/
theorem cell_mono (l : List ℕ) (hs : l.Sorted (· ≥ ·)) {i j i' j' : ℕ}
    (h : (i, j) ∈ cells l) (hi : i' ≤ i) (hj : j' ≤ j) : (i', j') ∈ cells l := by
  rw [mem_cells] at h ⊢
  dsimp only at h ⊢
  have := getD_anti l hs hi
  omega

/-- A cell off the arm and off the strict leg of `p` is outside its hook. -/
theorem not_mem_hook (l : List ℕ) (p q : ℕ × ℕ) (h1 : q.1 ≠ p.1 ∨ q.2 < p.2)
    (h2 : q.2 ≠ p.2 ∨ q.1 ≤ p.1) : q ∉ armF l p ∪ legF l p := by
  intro hm
  rcases Finset.mem_union.mp hm with ha | hl
  · obtain ⟨a1, a2, _⟩ := (mem_armF_iff l p q).mp ha
    omega
  · obtain ⟨b1, b2, _⟩ := (mem_legF_iff l p q).mp hl
    omega

/-- At `hookLen = n − 2` the hook misses exactly two cells. -/
theorem card_sdiff_two (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (p : ℕ × ℕ)
    (hp : p ∈ cells l) (heq : hookLen l p + 2 = l.sum) :
    ((cells l) \ (armF l p ∪ legF l p)).card = 2 := by
  rw [Finset.card_sdiff, Finset.inter_eq_left.mpr (hookUnion_subset l hs p), card_cells,
    card_hookUnion l hs p hp]
  omega

/-- The hook of a depth-2 carrier cannot miss three distinct cells. -/
theorem no_three (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (p : ℕ × ℕ)
    (hp : p ∈ cells l) (heq : hookLen l p + 2 = l.sum) (q1 q2 q3 : ℕ × ℕ)
    (h1 : q1 ∈ cells l) (h2 : q2 ∈ cells l) (h3 : q3 ∈ cells l)
    (n1 : q1 ∉ armF l p ∪ legF l p) (n2 : q2 ∉ armF l p ∪ legF l p)
    (n3 : q3 ∉ armF l p ∪ legF l p) (d12 : q1 ≠ q2) (d13 : q1 ≠ q3) (d23 : q2 ≠ q3) :
    False := by
  have hsub : ({q1, q2, q3} : Finset (ℕ × ℕ)) ⊆ (cells l) \ (armF l p ∪ legF l p) := by
    intro x hx
    simp only [Finset.mem_insert, Finset.mem_singleton] at hx
    rcases hx with rfl | rfl | rfl
    · exact Finset.mem_sdiff.mpr ⟨h1, n1⟩
    · exact Finset.mem_sdiff.mpr ⟨h2, n2⟩
    · exact Finset.mem_sdiff.mpr ⟨h3, n3⟩
  have hc := Finset.card_le_card hsub
  rw [card_sdiff_two l hs p hp heq, Finset.card_eq_three.mpr ⟨q1, q2, q3, d12, d13, d23, rfl⟩]
    at hc
  omega

/-- A missed cell has a second missed cell beside it. -/
theorem exists_other (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (p : ℕ × ℕ)
    (hp : p ∈ cells l) (heq : hookLen l p + 2 = l.sum) (q : ℕ × ℕ) (hq : q ∈ cells l)
    (nq : q ∉ armF l p ∪ legF l p) :
    ∃ z, z ∈ cells l ∧ z ∉ armF l p ∪ legF l p ∧ z ≠ q := by
  obtain ⟨x, y, hxy, hS⟩ := Finset.card_eq_two.mp (card_sdiff_two l hs p hp heq)
  have hqS : q ∈ (cells l) \ (armF l p ∪ legF l p) := Finset.mem_sdiff.mpr ⟨hq, nq⟩
  have hxS : x ∈ (cells l) \ (armF l p ∪ legF l p) := by rw [hS]; simp
  have hyS : y ∈ (cells l) \ (armF l p ∪ legF l p) := by rw [hS]; simp
  by_cases hqx : q = x
  · exact ⟨y, (Finset.mem_sdiff.mp hyS).1, (Finset.mem_sdiff.mp hyS).2,
      fun h => hxy (hqx ▸ h.symm)⟩
  · exact ⟨x, (Finset.mem_sdiff.mp hxS).1, (Finset.mem_sdiff.mp hxS).2, fun h => hqx h.symm⟩

/-- Positive entries at most one form a column of ones. -/
theorem eq_rep_of_getD_le_one (t : List ℕ) (hpos : ∀ x ∈ t, 0 < x)
    (h : ∀ i, t.getD i 0 ≤ 1) : t = List.replicate t.length 1 := by
  refine List.eq_replicate_iff.mpr ⟨rfl, fun x hx => ?_⟩
  obtain ⟨k, hk, rfl⟩ := List.mem_iff_getElem.mp hx
  have h1 := h k
  rw [List.getD_eq_getElem _ _ hk] at h1
  have := hpos _ hx
  omega

/-! ## Where the carrier sits -/

/-- A depth-2 carrier lies in row 0 within two columns of the corner, or in column 0 within two
rows of it. -/
theorem carrier_position (l : List ℕ) (hs : l.Sorted (· ≥ ·)) (p : ℕ × ℕ)
    (hp : p ∈ cells l) (heq : hookLen l p + 2 = l.sum) :
    (p.1 = 0 ∧ p.2 ≤ 2) ∨ (p.2 = 0 ∧ p.1 ≤ 2) := by
  obtain ⟨i, j⟩ := p
  dsimp only
  have hc : ∀ a b : ℕ, a ≤ i → b ≤ j → (a, b) ∈ cells l := fun a b ha hb =>
    cell_mono l hs hp ha hb
  by_cases hi : i = 0
  · subst hi
    by_contra hj
    exact no_three l hs (0, j) hp heq (0, 0) (0, 1) (0, 2) (hc 0 0 le_rfl (by omega))
      (hc 0 1 le_rfl (by omega)) (hc 0 2 le_rfl (by omega))
      (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
      (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
      (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
      (by simp) (by simp) (by simp)
  by_cases hj : j = 0
  · subst hj
    by_contra hi'
    exact no_three l hs (i, 0) hp heq (0, 0) (1, 0) (2, 0) (hc 0 0 (by omega) le_rfl)
      (hc 1 0 (by omega) le_rfl) (hc 2 0 (by omega) le_rfl)
      (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
      (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
      (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
      (by simp) (by simp) (by simp)
  exfalso
  exact no_three l hs (i, j) hp heq (0, 0) (0, j) (i, 0) (hc 0 0 (by omega) (by omega))
    (hc 0 j (by omega) le_rfl) (hc i 0 le_rfl (by omega))
    (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
    (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
    (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
    (by simp; omega) (by simp; omega) (by simp; omega)

/-! ## The shape behind each carrier -/

/-- Carrier `(0,2)`: the single row `[a]`, `a ≥ 3`. -/
theorem shape_of_carrier_zero_two (l : List ℕ) (hs : l.Sorted (· ≥ ·))
    (hpos : ∀ x ∈ l, 0 < x) (hp : ((0 : ℕ), (2 : ℕ)) ∈ cells l)
    (heq : hookLen l (0, 2) + 2 = l.sum) : ∃ a, 3 ≤ a ∧ l = [a] := by
  have h1 : l.getD 1 0 = 0 := by
    by_contra h
    exact no_three l hs (0, 2) hp heq (0, 0) (0, 1) (1, 0) (cell_mono l hs hp le_rfl (by omega))
      (cell_mono l hs hp le_rfl (by omega)) (by rw [mem_cells]; dsimp only; omega)
      (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
      (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
      (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
      (by simp) (by simp) (by simp)
  rw [mem_cells] at hp
  dsimp only at hp
  rcases l with _ | ⟨a, _ | ⟨b, t⟩⟩
  · simp at hp
  · exact ⟨a, by simpa using hp, rfl⟩
  · have := hpos b (by simp)
    simp at h1
    omega

/-- Carrier `(0,1)`: a two-row shape `[a, b]` with `b ≤ 2`. -/
theorem shape_of_carrier_zero_one (l : List ℕ) (hs : l.Sorted (· ≥ ·))
    (hpos : ∀ x ∈ l, 0 < x) (hp : ((0 : ℕ), (1 : ℕ)) ∈ cells l)
    (heq : hookLen l (0, 1) + 2 = l.sum) :
    ∃ a b, 2 ≤ a ∧ 1 ≤ b ∧ b ≤ 2 ∧ l = [a, b] := by
  have h00 : ((0 : ℕ), (0 : ℕ)) ∈ cells l := cell_mono l hs hp le_rfl (by omega)
  have n00 : ((0 : ℕ), (0 : ℕ)) ∉ armF l (0, 1) ∪ legF l (0, 1) :=
    not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega)
  obtain ⟨z, hz, nz, hz0⟩ := exists_other l hs (0, 1) hp heq (0, 0) h00 n00
  have hz1 : 1 ≤ z.1 := by
    by_contra hcon
    apply nz
    apply Finset.mem_union_left
    rw [mem_armF_iff]
    have hz2 : z.2 ≠ 0 := fun h => hz0 (Prod.ext (by dsimp only; omega) h)
    rw [mem_cells] at hz
    refine ⟨by dsimp only; omega, by dsimp only; omega, ?_⟩
    have : z.1 = 0 := by omega
    rw [this] at hz
    exact hz
  have h10 : ((1 : ℕ), (0 : ℕ)) ∈ cells l := cell_mono l hs (i := z.1) (j := z.2)
    (by simpa using hz) hz1 (Nat.zero_le _)
  have n10 : ((1 : ℕ), (0 : ℕ)) ∉ armF l (0, 1) ∪ legF l (0, 1) :=
    not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega)
  have h2 : l.getD 2 0 = 0 := by
    by_contra h
    exact no_three l hs (0, 1) hp heq (0, 0) (1, 0) (2, 0) h00 h10
      (by rw [mem_cells]; dsimp only; omega) n00 n10
      (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
      (by simp) (by simp) (by simp)
  have h12 : l.getD 1 0 ≤ 2 := by
    by_contra h
    exact no_three l hs (0, 1) hp heq (0, 0) (1, 0) (1, 2) h00 h10
      (by rw [mem_cells]; dsimp only; omega) n00 n10
      (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
      (by simp) (by simp) (by simp)
  rw [mem_cells] at hp h10
  dsimp only at hp h10
  rcases l with _ | ⟨a, _ | ⟨b, _ | ⟨c, t⟩⟩⟩
  · simp at hp
  · simp at h10
  · exact ⟨a, b, by simpa using hp, by simpa using h10, by simpa using h12, rfl⟩
  · have := hpos c (by simp)
    simp at h2
    omega

/-- Carrier `(2,0)`: the single column `1^m`, `m ≥ 3`. -/
theorem shape_of_carrier_two_zero (l : List ℕ) (hs : l.Sorted (· ≥ ·))
    (hpos : ∀ x ∈ l, 0 < x) (hp : ((2 : ℕ), (0 : ℕ)) ∈ cells l)
    (heq : hookLen l (2, 0) + 2 = l.sum) : ∃ m, 3 ≤ m ∧ l = List.replicate m 1 := by
  have h0 : l.getD 0 0 ≤ 1 := by
    by_contra h
    exact no_three l hs (2, 0) hp heq (0, 0) (1, 0) (0, 1) (cell_mono l hs hp (by omega) le_rfl)
      (cell_mono l hs hp (by omega) le_rfl) (by rw [mem_cells]; dsimp only; omega)
      (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
      (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
      (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
      (by simp) (by simp) (by simp)
  have hall : ∀ i, l.getD i 0 ≤ 1 := fun i => le_trans (getD_anti l hs (Nat.zero_le i)) h0
  have hrep := eq_rep_of_getD_le_one l hpos hall
  refine ⟨l.length, ?_, hrep⟩
  rw [mem_cells] at hp
  dsimp only at hp
  by_contra h
  rw [List.getD_eq_default _ _ (by omega)] at hp
  omega

/-- Carrier `(1,0)`: the shape `(2, b, 1^c)` with `b ≤ 2`. -/
theorem shape_of_carrier_one_zero (l : List ℕ) (hs : l.Sorted (· ≥ ·))
    (hpos : ∀ x ∈ l, 0 < x) (hp : ((1 : ℕ), (0 : ℕ)) ∈ cells l)
    (heq : hookLen l (1, 0) + 2 = l.sum) :
    ∃ b c, 1 ≤ b ∧ b ≤ 2 ∧ l = 2 :: b :: List.replicate c 1 := by
  have h00 : ((0 : ℕ), (0 : ℕ)) ∈ cells l := cell_mono l hs hp (by omega) le_rfl
  have n00 : ((0 : ℕ), (0 : ℕ)) ∉ armF l (1, 0) ∪ legF l (1, 0) :=
    not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega)
  obtain ⟨z, hz, nz, hz0⟩ := exists_other l hs (1, 0) hp heq (0, 0) h00 n00
  have hz2 : 1 ≤ z.2 := by
    by_contra hcon
    have hz2' : z.2 = 0 := by omega
    have hz1 : z.1 ≠ 0 := fun h => hz0 (Prod.ext h hz2')
    apply nz
    have hzc := hz
    rw [mem_cells] at hzc
    by_cases h1 : z.1 = 1
    · apply Finset.mem_union_left
      rw [mem_armF_iff]
      refine ⟨h1, by dsimp only; omega, ?_⟩
      rw [← h1]
      exact hzc
    · apply Finset.mem_union_right
      rw [mem_legF_iff]
      refine ⟨hz2', by dsimp only; omega, ?_⟩
      rw [conj_getD l hs]
      exact (lt_countP_iff l hs 0 z.1).mpr (hz2' ▸ hzc)
  have h01 : ((0 : ℕ), (1 : ℕ)) ∈ cells l := cell_mono l hs (i := z.1) (j := z.2)
    (by simpa using hz) (Nat.zero_le _) hz2
  have n01 : ((0 : ℕ), (1 : ℕ)) ∉ armF l (1, 0) ∪ legF l (1, 0) :=
    not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega)
  have h0 : l.getD 0 0 ≤ 2 := by
    by_contra h
    exact no_three l hs (1, 0) hp heq (0, 0) (0, 1) (0, 2) h00 h01
      (by rw [mem_cells]; dsimp only; omega) n00 n01
      (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
      (by simp) (by simp) (by simp)
  have h2 : l.getD 2 0 ≤ 1 := by
    by_contra h
    exact no_three l hs (1, 0) hp heq (0, 0) (0, 1) (2, 1) h00 h01
      (by rw [mem_cells]; dsimp only; omega) n00 n01
      (not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega))
      (by simp) (by simp) (by simp)
  have hrows : ∀ i, 2 ≤ i → l.getD i 0 ≤ 1 := fun i hi => le_trans (getD_anti l hs hi) h2
  rw [mem_cells] at hp h01
  dsimp only at hp h01
  rcases l with _ | ⟨a, _ | ⟨b, t⟩⟩
  · simp at hp
  · simp at hp
  · simp only [List.getD_cons_zero, List.getD_cons_succ] at h0 h01 hp
    have hb : b ≤ a := (List.sorted_cons.mp hs).1 b (by simp)
    have ht : t = List.replicate t.length 1 := eq_rep_of_getD_le_one t
      (fun x hx => hpos x (by simp [hx])) (fun i => by
        have := hrows (i + 2) (by omega)
        simpa using this)
    exact ⟨b, t.length, hp, by omega, by rw [show a = 2 by omega, ← ht]⟩

/-- Carrier `(0,0)`: the shape `(a, 3, 1^c)` with `a ≥ 3`, or `(a, 2, 2, 1^c)` with `a ≥ 2`. -/
theorem shape_of_carrier_zero_zero (l : List ℕ) (hs : l.Sorted (· ≥ ·))
    (hpos : ∀ x ∈ l, 0 < x) (hp : ((0 : ℕ), (0 : ℕ)) ∈ cells l)
    (heq : hookLen l (0, 0) + 2 = l.sum) :
    (∃ a c, 3 ≤ a ∧ l = a :: 3 :: List.replicate c 1) ∨
      (∃ a c, 2 ≤ a ∧ l = a :: 2 :: 2 :: List.replicate c 1) := by
  have hin : ∀ q : ℕ × ℕ, q ∈ cells l → q ∉ armF l (0, 0) ∪ legF l (0, 0) →
      1 ≤ q.1 ∧ 1 ≤ q.2 := by
    intro q hq hn
    by_contra hcon
    exact hn (QOU.BraidsAndKnots.DepthOneHookClassification.mem_hookUnion_origin_of_fst_or_snd_zero
      l hs q hq (by omega))
  have nh : ∀ a b : ℕ, 1 ≤ a → 1 ≤ b → ((a, b) : ℕ × ℕ) ∉ armF l (0, 0) ∪ legF l (0, 0) :=
    fun a b ha hb => not_mem_hook l _ _ (by dsimp only; omega) (by dsimp only; omega)
  obtain ⟨x, y, hxy, hS⟩ := Finset.card_eq_two.mp (card_sdiff_two l hs (0, 0) hp heq)
  have hxS : x ∈ (cells l) \ (armF l (0, 0) ∪ legF l (0, 0)) := by rw [hS]; simp
  have hyS : y ∈ (cells l) \ (armF l (0, 0) ∪ legF l (0, 0)) := by rw [hS]; simp
  obtain ⟨hx, nx⟩ := Finset.mem_sdiff.mp hxS
  obtain ⟨hy, ny⟩ := Finset.mem_sdiff.mp hyS
  have hx1 := hin x hx nx
  have hy1 := hin y hy ny
  have h11 : ((1 : ℕ), (1 : ℕ)) ∈ cells l := cell_mono l hs (i := x.1) (j := x.2)
    (by simpa using hx) hx1.1 hx1.2
  -- one of the two missed cells is not `(1,1)`
  obtain ⟨z, hz, hz1, hzne⟩ : ∃ z : ℕ × ℕ, z ∈ cells l ∧ (1 ≤ z.1 ∧ 1 ≤ z.2) ∧
      z ≠ ((1 : ℕ), (1 : ℕ)) := by
    by_cases hx11 : x = (1, 1)
    · exact ⟨y, hy, hy1, fun h => hxy (hx11.trans h.symm)⟩
    · exact ⟨x, hx, hx1, hx11⟩
  have hor : ((1 : ℕ), (2 : ℕ)) ∈ cells l ∨ ((2 : ℕ), (1 : ℕ)) ∈ cells l := by
    by_cases hz2 : 2 ≤ z.2
    · exact Or.inl (cell_mono l hs (i := z.1) (j := z.2) (by simpa using hz) hz1.1 hz2)
    · have hz2' : z.2 = 1 := by omega
      have hz1' : 2 ≤ z.1 := by
        by_contra h
        exact hzne (Prod.ext (by dsimp only; omega) hz2')
      exact Or.inr (cell_mono l hs (i := z.1) (j := z.2) (by simpa using hz) hz1' (by omega))
  have three : ∀ a b c d e f : ℕ, ((a, b) : ℕ × ℕ) ∈ cells l → ((c, d) : ℕ × ℕ) ∈ cells l →
      ((e, f) : ℕ × ℕ) ∈ cells l → 1 ≤ a → 1 ≤ b → 1 ≤ c → 1 ≤ d → 1 ≤ e → 1 ≤ f →
      ((a, b) : ℕ × ℕ) ≠ (c, d) → ((a, b) : ℕ × ℕ) ≠ (e, f) → ((c, d) : ℕ × ℕ) ≠ (e, f) →
      False :=
    fun a b c d e f h1 h2 h3 ha hb hc hd he hf d1 d2 d3 =>
      no_three l hs (0, 0) hp heq _ _ _ h1 h2 h3 (nh a b ha hb) (nh c d hc hd) (nh e f he hf)
        d1 d2 d3
  have hpos' : ∀ (a b : ℕ) (t : List ℕ), l = a :: b :: t → ∀ x ∈ t, 0 < x := by
    intro a b t hl x hx
    exact hpos x (by rw [hl]; simp [hx])
  rcases hor with h12 | h21
  · -- family `(a, 3, 1^c)`
    have h21 : ((2 : ℕ), (1 : ℕ)) ∉ cells l := fun h21 =>
      three 1 1 1 2 2 1 h11 h12 h21 le_rfl le_rfl le_rfl (by omega) (by omega) le_rfl
        (by simp) (by simp) (by simp)
    have h13 : ((1 : ℕ), (3 : ℕ)) ∉ cells l := fun h13 =>
      three 1 1 1 2 1 3 h11 h12 h13 le_rfl le_rfl le_rfl (by omega) le_rfl (by omega)
        (by simp) (by simp) (by simp)
    rw [mem_cells] at h12 h21 h13
    dsimp only at h12 h21 h13
    have hrows : ∀ i, 2 ≤ i → l.getD i 0 ≤ 1 := fun i hi => by
      have := getD_anti l hs hi; omega
    left
    rcases l with _ | ⟨a, _ | ⟨b, t⟩⟩
    · simp at h12
    · simp at h12
    · simp only [List.getD_cons_succ, List.getD_cons_zero] at h12 h13
      have hb : b ≤ a := (List.sorted_cons.mp hs).1 b (by simp)
      have ht : t = List.replicate t.length 1 := eq_rep_of_getD_le_one t
        (hpos' a b t rfl) (fun i => by simpa using hrows (i + 2) (by omega))
      exact ⟨a, t.length, by omega, by rw [show b = 3 by omega, ← ht]⟩
  · -- family `(a, 2, 2, 1^c)`
    have h12 : ((1 : ℕ), (2 : ℕ)) ∉ cells l := fun h12 =>
      three 1 1 1 2 2 1 h11 h12 h21 le_rfl le_rfl le_rfl (by omega) (by omega) le_rfl
        (by simp) (by simp) (by simp)
    have h31 : ((3 : ℕ), (1 : ℕ)) ∉ cells l := fun h31 =>
      three 1 1 2 1 3 1 h11 h21 h31 le_rfl le_rfl (by omega) le_rfl (by omega) le_rfl
        (by simp) (by simp) (by simp)
    rw [mem_cells] at h12 h21 h31
    dsimp only at h12 h21 h31
    have h21' := getD_anti l hs (show 1 ≤ 2 by omega)
    have hrows : ∀ i, 3 ≤ i → l.getD i 0 ≤ 1 := fun i hi => by
      have := getD_anti l hs hi; omega
    right
    rcases l with _ | ⟨a, _ | ⟨b, _ | ⟨c, t⟩⟩⟩
    · simp at h21
    · simp at h21
    · simp at h21
    · simp only [List.getD_cons_succ, List.getD_cons_zero] at h12 h21 h21'
      have hb : b ≤ a := (List.sorted_cons.mp hs).1 b (by simp)
      have ht : t = List.replicate t.length 1 := eq_rep_of_getD_le_one t
        (fun x hx => hpos x (by simp [hx])) (fun i => by simpa using hrows (i + 3) (by omega))
      exact ⟨a, t.length, by omega, by rw [show b = 2 by omega, show c = 2 by omega, ← ht]⟩

end QOU.BraidsAndKnots.DepthTwoHookClassification
