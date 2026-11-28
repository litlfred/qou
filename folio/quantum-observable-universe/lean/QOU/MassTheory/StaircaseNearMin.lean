import QOU.MassTheory.QHookTop
import Mathlib.Algebra.Polynomial.Expand
import Mathlib.Tactic.LinearCombination

/-!
# The shapes one cell above the minimum, and `a₁`

Third step of the partition count behind `conj:cyclotomic-boundary-at-keystone`
(earlier steps: `QOU.Mass.StaircaseMinimisers`, `StaircaseTopCoeff`, `QHookTop`).

For `n = T_m + r` cells, `N_min = N(stair m) + r m`. This file classifies the Young diagrams with
`N = N_min + 1` and counts them.

* `delta_eq`: `N s - N_min` is the excess of the cells above antidiagonal `m` plus the deficit of
  the staircase cells that `s` misses. Each term is at least `1`.
* `nearMin_classify`: so `N s = N_min + 1` forces one of two shapes. Either (`caseA`) `s` is
  `stair m`, plus `r - 1` cells on antidiagonal `m`, plus one cell `c` on antidiagonal `m + 1`
  resting on them. Or (`caseB`) `s` is `stair m` less one cell `b` of antidiagonal `m - 1`, plus
  `r + 1` cells on antidiagonal `m`, none sitting on `b`.
* `card_nearMin_eq`: for `m = k + 1`, there are
  `2 C(k+1, r-2) + (k+1) C(k, r-3) + (k+1) C(k, r+1)` of them (a binomial with negative lower
  index read as `0`). This is the `a₁` of the conjecture block with `j = k + 1`.
* `coeff_sum_sym_qHook_of_eq`: that count is the coefficient one step below the top of
  `∑_λ X^(N λ) g_λ(X²)`, where `g_λ = [n]! / ∏ [h]`. In the symmetric normalisation this sum is
  `q^(C(n,2)) S(n)`. As in `QHookTop`, the divisibility `[n]! = g_λ · ∏ [h]` is a hypothesis
  (`hg`), not proved here.

Not formalised here: the `δ = 2` count behind `a₂`.
-/

namespace QOU.Mass.StaircaseMinimisers

open Finset

/-- **Excess identity.** For `T_m + r` cells, `N s - N(stair m) - r m` is the excess of the cells
above antidiagonal `m` plus the deficit of the staircase cells that `s` misses. -/
theorem delta_eq {m r : ℕ} {s : Finset (ℕ × ℕ)} (hs : s.card = (stair m).card + r) :
    (N s : ℤ) - N (stair m) - r * m =
      ∑ a ∈ s.filter (fun c => m < val c), ((val a : ℤ) - m) +
        ∑ b ∈ stair m \ s, ((m : ℤ) - val b) := by
  classical
  set f : ℕ × ℕ → ℤ := fun c => (val c : ℤ) - m with hf
  have hNs : (N s : ℤ) - m * s.card = ∑ a ∈ s, f a := by
    rw [N, Nat.cast_sum, sum_sub_distrib, sum_const, nsmul_eq_mul]; ring
  have hNt : (N (stair m) : ℤ) - m * (stair m).card = ∑ a ∈ stair m, f a := by
    rw [N, Nat.cast_sum, sum_sub_distrib, sum_const, nsmul_eq_mul]; ring
  have hsplit : ∑ a ∈ s, f a = ∑ a ∈ s.filter (fun c => m < val c), f a +
      ∑ a ∈ s ∩ stair m, f a := by
    rw [← sum_filter_add_sum_filter_not s (fun c => m < val c)]
    congr 1
    symm
    apply sum_subset
    · intro c hc
      rw [mem_inter, mem_stair] at hc
      exact mem_filter.2 ⟨hc.1, not_lt.2 hc.2.le⟩
    · intro c hc hcn
      rw [mem_filter] at hc
      rw [mem_inter, mem_stair] at hcn
      have h1 := hc.2
      have h2 : ¬ val c < m := fun h => hcn ⟨hc.1, h⟩
      have : val c = m := by omega
      simp [hf, this]
  have hst : ∑ a ∈ stair m, f a = ∑ a ∈ s ∩ stair m, f a + ∑ a ∈ stair m \ s, f a := by
    rw [inter_comm]; exact (sum_inter_add_sum_diff _ _ _).symm
  have hneg : ∑ b ∈ stair m \ s, ((m : ℤ) - val b) = -∑ b ∈ stair m \ s, f b := by
    rw [← sum_neg_distrib]; apply sum_congr rfl; intro b _; simp [hf]
  rw [hneg]
  have hc : (s.card : ℤ) = (stair m).card + r := by exact_mod_cast hs
  linear_combination hNs - hNt + hsplit - hst + (m : ℤ) * hc

/-- A lower set of `n` cells lies in `range n ×ˢ range n`. -/
theorem subset_range_of_isLowerSet {s : Finset (ℕ × ℕ)} (hs : IsLowerSet (s : Set (ℕ × ℕ))) :
    s ⊆ range s.card ×ˢ range s.card := by
  intro c hc
  have h1 : c.1 < s.card := by
    have : (range (c.1 + 1)).card ≤ s.card := by
      apply card_le_card_of_injOn (fun k => (k, 0))
      · intro k hk
        rw [coe_range, Set.mem_Iio] at hk
        exact hs (show ((k, 0) : ℕ × ℕ) ≤ c from ⟨by omega, Nat.zero_le _⟩) hc
      · intro a _ b _ h; simpa using h
    simpa using this
  have h2 : c.2 < s.card := by
    have : (range (c.2 + 1)).card ≤ s.card := by
      apply card_le_card_of_injOn (fun k => (0, k))
      · intro k hk
        rw [coe_range, Set.mem_Iio] at hk
        exact hs (show ((0, k) : ℕ × ℕ) ≤ c from ⟨Nat.zero_le _, by omega⟩) hc
      · intro a _ b _ h; simpa using h
    simpa using this
  simp [mem_product, h1, h2]

theorem mem_shapes_iff {n : ℕ} {s : Finset (ℕ × ℕ)} :
    s ∈ shapes n ↔ s.card = n ∧ IsLowerSet (s : Set (ℕ × ℕ)) := by
  rw [mem_shapes]
  constructor
  · rintro ⟨_, h1, h2⟩; exact ⟨h1, h2⟩
  · rintro ⟨h1, h2⟩; exact ⟨h1 ▸ subset_range_of_isLowerSet h2, h1, h2⟩

/-- Subsets of `U` of size `k` containing a fixed `P ⊆ U`. -/
theorem card_powersetCard_filter_superset {U P : Finset (ℕ × ℕ)} (hP : P ⊆ U) (k : ℕ) :
    ((U.powersetCard k).filter (fun R => P ⊆ R)).card =
      if P.card ≤ k then (U.card - P.card).choose (k - P.card) else 0 := by
  classical
  split_ifs with hk
  · rw [← card_sdiff_of_subset hP, ← card_powersetCard]
    refine card_nbij' (fun R => R \ P) (fun R => R ∪ P) ?_ ?_ ?_ ?_
    · intro R hR
      rw [mem_coe, mem_filter, mem_powersetCard] at hR
      rw [mem_coe, mem_powersetCard]
      refine ⟨sdiff_subset_sdiff hR.1.1 subset_rfl, ?_⟩
      rw [card_sdiff_of_subset hR.2, hR.1.2]
    · intro R hR
      rw [mem_coe, mem_powersetCard] at hR
      have hd : Disjoint R P := by
        rw [Finset.disjoint_left]; intro c hc hcP; exact (mem_sdiff.1 (hR.1 hc)).2 hcP
      rw [mem_coe, mem_filter, mem_powersetCard]
      refine ⟨⟨union_subset (hR.1.trans sdiff_subset) hP, ?_⟩, subset_union_right⟩
      rw [card_union_of_disjoint hd, hR.2]; omega
    · intro R hR
      rw [mem_coe, mem_filter] at hR
      exact sdiff_union_of_subset hR.2
    · intro R hR
      rw [mem_coe, mem_powersetCard] at hR
      have hd : Disjoint R P := by
        rw [Finset.disjoint_left]; intro c hc hcP; exact (mem_sdiff.1 (hR.1 hc)).2 hcP
      exact union_sdiff_cancel_right hd
  · rw [card_eq_zero, filter_eq_empty_iff]
    intro R hR hPR
    rw [mem_powersetCard] at hR
    have := card_le_card hPR
    omega

/-- Subsets of `U` of size `k` avoiding a fixed `P ⊆ U`. -/
theorem card_powersetCard_filter_disjoint {U P : Finset (ℕ × ℕ)} (hP : P ⊆ U) (k : ℕ) :
    ((U.powersetCard k).filter (fun R => Disjoint P R)).card = (U.card - P.card).choose k := by
  classical
  rw [← card_sdiff_of_subset hP, ← card_powersetCard]
  congr 1
  ext R
  simp only [mem_filter, mem_powersetCard, subset_sdiff]
  constructor
  · rintro ⟨⟨h1, h2⟩, h3⟩; exact ⟨⟨h1, h3.symm⟩, h2⟩
  · rintro ⟨⟨h1, h3⟩, h2⟩; exact ⟨⟨h1, h2⟩, h3.symm⟩


section Cells
open Finset.Nat

/-- Cells on antidiagonal `m` below `c` (the cells a cell `c` on antidiagonal `m+1` rests on). -/
def predsOf (m : ℕ) (c : ℕ × ℕ) : Finset (ℕ × ℕ) := (antidiagonal m).filter (· ≤ c)

/-- Cells on antidiagonal `m` above `b`. -/
def succsOf (m : ℕ) (b : ℕ × ℕ) : Finset (ℕ × ℕ) := (antidiagonal m).filter (b ≤ ·)

theorem predsOf_left (m : ℕ) : predsOf m (0, m + 1) = {(0, m)} := by
  ext ⟨a, b⟩; simp [predsOf, mem_antidiagonal, Prod.le_def]; omega

theorem predsOf_right (m : ℕ) : predsOf m (m + 1, 0) = {(m, 0)} := by
  ext ⟨a, b⟩; simp [predsOf, mem_antidiagonal, Prod.le_def]; omega

theorem predsOf_mid {a b m : ℕ} (h : a + b + 1 = m) :
    predsOf m (a + 1, b + 1) = {(a, b + 1), (a + 1, b)} := by
  ext ⟨x, y⟩; simp [predsOf, mem_antidiagonal, Prod.le_def]; omega

theorem succsOf_eq {a b m : ℕ} (h : a + b + 1 = m) :
    succsOf m (a, b) = {(a + 1, b), (a, b + 1)} := by
  ext ⟨x, y⟩; simp [succsOf, mem_antidiagonal, Prod.le_def]; omega

theorem predsOf_subset (m : ℕ) (c : ℕ × ℕ) : predsOf m c ⊆ antidiagonal m := filter_subset _ _
theorem succsOf_subset (m : ℕ) (b : ℕ × ℕ) : succsOf m b ⊆ antidiagonal m := filter_subset _ _

theorem card_filter_product {α β : Type*} (A : Finset α) (B : Finset β) (p : α × β → Prop)
    [DecidablePred p] :
    ((A ×ˢ B).filter p).card = ∑ a ∈ A, (B.filter (fun b => p (a, b))).card := by
  rw [card_filter, sum_product]
  apply sum_congr rfl; intro a _; rw [card_filter]


/-- Shapes one cell above the minimum, first kind: a cell `c` on antidiagonal `m + 1`
resting on `r - 1` cells of antidiagonal `m`. -/
def caseA (m r : ℕ) : Finset ((ℕ × ℕ) × Finset (ℕ × ℕ)) :=
  ((antidiagonal (m + 1)) ×ˢ ((antidiagonal m).powersetCard (r - 1))).filter
    (fun p => predsOf m p.1 ⊆ p.2)

/-- Shapes one cell above the minimum, second kind: the staircase less one cell `b` of
antidiagonal `m - 1`, plus `r + 1` cells of antidiagonal `m` none of which sits on `b`. -/
def caseB (m r : ℕ) : Finset ((ℕ × ℕ) × Finset (ℕ × ℕ)) :=
  ((antidiagonal (m - 1)) ×ˢ ((antidiagonal m).powersetCard (r + 1))).filter
    (fun p => Disjoint (succsOf m p.1) p.2)

theorem card_caseA (k r : ℕ) (hr : 1 ≤ r) :
    (caseA (k + 1) r).card = 2 * (if 2 ≤ r then (k + 1).choose (r - 2) else 0) +
      (k + 1) * (if 3 ≤ r then k.choose (r - 3) else 0) := by
  rw [caseA, card_filter_product, sum_antidiagonal_succ, sum_antidiagonal_succ']
  have hF : ∀ c : ℕ × ℕ,
      (((antidiagonal (k + 1)).powersetCard (r - 1)).filter (fun R => predsOf (k + 1) c ⊆ R)).card =
        if (predsOf (k + 1) c).card ≤ r - 1 then
          (k + 2 - (predsOf (k + 1) c).card).choose (r - 1 - (predsOf (k + 1) c).card) else 0 := by
    intro c
    rw [card_powersetCard_filter_superset (predsOf_subset _ _), Nat.card_antidiagonal]
  simp only [hF]
  rw [predsOf_left, predsOf_right]
  simp only [card_singleton]
  have h1 : (if 1 ≤ r - 1 then (k + 2 - 1).choose (r - 1 - 1) else 0) =
      if 2 ≤ r then (k + 1).choose (r - 2) else 0 := by
    by_cases h : 2 ≤ r
    · rw [if_pos (by omega), if_pos h]; congr 1
    · rw [if_neg (by omega), if_neg h]
  rw [h1]
  have h2 : ∀ p ∈ antidiagonal k,
      (if (predsOf (k + 1) (p.1 + 1, p.2 + 1)).card ≤ r - 1 then
          (k + 2 - (predsOf (k + 1) (p.1 + 1, p.2 + 1)).card).choose
            (r - 1 - (predsOf (k + 1) (p.1 + 1, p.2 + 1)).card) else 0) =
        if 3 ≤ r then k.choose (r - 3) else 0 := by
    intro p hp
    have hp' : p.1 + p.2 + 1 = k + 1 := by rw [mem_antidiagonal] at hp; omega
    rw [predsOf_mid hp', card_pair (by simp)]
    by_cases h : 3 ≤ r
    · rw [if_pos (by omega), if_pos h]; congr 1
    · rw [if_neg (by omega), if_neg h]
  rw [sum_congr rfl h2, sum_const, Nat.card_antidiagonal, smul_eq_mul]
  ring

theorem card_caseB (k r : ℕ) :
    (caseB (k + 1) r).card = (k + 1) * k.choose (r + 1) := by
  rw [caseB, card_filter_product, Nat.add_sub_cancel]
  have h : ∀ b ∈ antidiagonal k,
      (((antidiagonal (k + 1)).powersetCard (r + 1)).filter
        (fun R => Disjoint (succsOf (k + 1) b) R)).card = k.choose (r + 1) := by
    intro b hb
    have hb' : b.1 + b.2 + 1 = k + 1 := by rw [mem_antidiagonal] at hb; omega
    rw [card_powersetCard_filter_disjoint (succsOf_subset _ _), succsOf_eq hb',
      card_pair (by simp), Nat.card_antidiagonal]
    congr 1
  rw [sum_congr rfl h, sum_const, Nat.card_antidiagonal, smul_eq_mul]

/-! ### The shapes one cell above the minimum -/

/-- The shape of a first-kind pair: `stair m ∪ R ∪ {c}`. -/
def shapeA (m : ℕ) (p : (ℕ × ℕ) × Finset (ℕ × ℕ)) : Finset (ℕ × ℕ) := insert p.1 (stair m ∪ p.2)

/-- The shape of a second-kind pair: `(stair m \ {b}) ∪ R`. -/
def shapeB (m : ℕ) (p : (ℕ × ℕ) × Finset (ℕ × ℕ)) : Finset (ℕ × ℕ) := (stair m).erase p.1 ∪ p.2

theorem val_le_of_le {d a : ℕ × ℕ} (h : d ≤ a) : val d ≤ val a := by
  obtain ⟨h1, h2⟩ := h; simp only [val]; omega

theorem val_lt_of_lt {d a : ℕ × ℕ} (h : d ≤ a) (hne : d ≠ a) : val d < val a := by
  obtain ⟨h1, h2⟩ := h
  simp only [val]
  by_contra hc
  exact hne (Prod.ext (by omega) (by omega))

theorem disjoint_stair {m : ℕ} {R : Finset (ℕ × ℕ)} (hR : R ⊆ antidiagonal m) :
    Disjoint (stair m) R := by
  rw [Finset.disjoint_left]
  intro c hc hcR
  rw [mem_stair, val, mem_antidiagonal.1 (hR hcR)] at hc
  exact lt_irrefl _ hc

theorem N_insert {c : ℕ × ℕ} {t : Finset (ℕ × ℕ)} (hc : c ∉ t) : N (insert c t) = val c + N t := by
  rw [N, sum_insert hc, ← N]

theorem mem_caseA {m r : ℕ} {p : (ℕ × ℕ) × Finset (ℕ × ℕ)} :
    p ∈ caseA m r ↔ val p.1 = m + 1 ∧ p.2 ⊆ antidiagonal m ∧ p.2.card = r - 1 ∧
      predsOf m p.1 ⊆ p.2 := by
  simp [caseA, mem_antidiagonal, val, and_assoc]

theorem mem_caseB {m r : ℕ} {p : (ℕ × ℕ) × Finset (ℕ × ℕ)} :
    p ∈ caseB m r ↔ val p.1 = m - 1 ∧ p.2 ⊆ antidiagonal m ∧ p.2.card = r + 1 ∧
      Disjoint (succsOf m p.1) p.2 := by
  simp [caseB, mem_antidiagonal, val, and_assoc]

/-- The defining set of the `δ = 1` count. -/
noncomputable def nearMin (m r : ℕ) : Finset (Finset (ℕ × ℕ)) := by
  classical
  exact (shapes ((stair m).card + r)).filter (fun s => N s = N (stair m) + r * m + 1)

theorem mem_nearMin {m r : ℕ} {s : Finset (ℕ × ℕ)} :
    s ∈ nearMin m r ↔ s.card = (stair m).card + r ∧ IsLowerSet (s : Set (ℕ × ℕ)) ∧
      N s = N (stair m) + r * m + 1 := by
  classical
  simp [nearMin, mem_shapes_iff, and_assoc]

theorem shapeA_mem {m r : ℕ} (hr : 1 ≤ r) {p : (ℕ × ℕ) × Finset (ℕ × ℕ)} (hp : p ∈ caseA m r) :
    shapeA m p ∈ nearMin m r := by
  obtain ⟨hc, hR, hcard, hpred⟩ := mem_caseA.1 hp
  have hcn : p.1 ∉ stair m ∪ p.2 := by
    intro h
    rcases mem_union.1 h with h | h
    · rw [mem_stair] at h; omega
    · have := mem_antidiagonal.1 (hR h); simp only [val] at hc; omega
  rw [mem_nearMin, shapeA]
  refine ⟨?_, ?_, ?_⟩
  · rw [card_insert_of_notMem hcn, card_union_of_disjoint (disjoint_stair hR), hcard]; omega
  · intro a b hba ha
    simp only [coe_insert, coe_union, Set.mem_insert_iff, Set.mem_union, mem_coe] at ha ⊢
    rcases ha with rfl | ha
    · rcases eq_or_ne b p.1 with rfl | hne
      · exact Or.inl rfl
      · right
        have hlt := val_lt_of_lt hba hne
        rcases Nat.lt_or_ge (val b) m with h | h
        · exact Or.inl (mem_stair.2 h)
        · right
          apply hpred
          rw [predsOf, mem_filter, mem_antidiagonal]
          exact ⟨by simp only [val] at h hlt hc ⊢; omega, hba⟩
    · right
      have := isLowerSet_stair_union hR hba (by simpa using ha)
      simpa using this
  · rw [N_insert hcn, N_stair_union hR, hcard, hc]
    rcases r with _ | r
    · omega
    · simp only [Nat.add_sub_cancel]; ring

theorem shapeB_mem {m r : ℕ} (hm : 1 ≤ m) {p : (ℕ × ℕ) × Finset (ℕ × ℕ)} (hp : p ∈ caseB m r) :
    shapeB m p ∈ nearMin m r := by
  obtain ⟨hb, hR, hcard, hdis⟩ := mem_caseB.1 hp
  have hbs : p.1 ∈ stair m := by rw [mem_stair]; omega
  have hdisj : Disjoint ((stair m).erase p.1) p.2 :=
    Finset.disjoint_of_subset_left (erase_subset _ _) (disjoint_stair hR)
  rw [mem_nearMin, shapeB]
  refine ⟨?_, ?_, ?_⟩
  · rw [card_union_of_disjoint hdisj, card_erase_of_mem hbs, hcard]
    have : 1 ≤ (stair m).card := card_pos.2 ⟨_, hbs⟩
    omega
  · intro a d hda ha
    simp only [coe_union, Set.mem_union, mem_coe] at ha ⊢
    rcases eq_or_ne d a with rfl | hne
    · exact ha
    left
    have hlt := val_lt_of_lt hda hne
    have hdb : d ≠ p.1 := by
      rintro rfl
      rcases ha with ha | ha
      · have h1 := mem_stair.1 (mem_of_mem_erase ha)
        omega
      · exact (Finset.disjoint_left.1 hdis)
          (mem_filter.2 ⟨hR ha, hda⟩) ha
    refine mem_erase.2 ⟨hdb, mem_stair.2 ?_⟩
    rcases ha with ha | ha
    · exact lt_trans hlt (mem_stair.1 (mem_of_mem_erase ha))
    · rw [show val a = m from mem_antidiagonal.1 (hR ha)] at hlt; exact hlt
  · have h1 : N ((stair m).erase p.1) + val p.1 = N (stair m) := by
      rw [N, N]; exact sum_erase_add _ _ hbs
    rw [N, sum_union hdisj, ← N, ← N]
    have h2 : N p.2 = (r + 1) * m := by
      rw [N, sum_congr rfl (g := fun _ => m) (fun c hc => show val c = m from mem_antidiagonal.1 (hR hc)), sum_const,
        hcard, smul_eq_mul]
    rw [h2]
    obtain ⟨k, rfl⟩ : ∃ k, m = k + 1 := ⟨m - 1, by omega⟩
    simp only [Nat.add_sub_cancel] at hb
    rw [hb] at h1
    nlinarith [h1]

theorem filter_val_shapeA {m : ℕ} {p : (ℕ × ℕ) × Finset (ℕ × ℕ)} (hc : val p.1 = m + 1)
    (hR : p.2 ⊆ antidiagonal m) : (shapeA m p).filter (fun x => val x = m) = p.2 := by
  ext x
  simp only [shapeA, mem_filter, mem_insert, mem_union, mem_stair]
  constructor
  · rintro ⟨h | h | h, hv⟩
    · subst h; omega
    · omega
    · exact h
  · intro h; exact ⟨Or.inr (Or.inr h), mem_antidiagonal.1 (hR h)⟩

theorem filter_val_shapeB {m : ℕ} {p : (ℕ × ℕ) × Finset (ℕ × ℕ)}
    (hR : p.2 ⊆ antidiagonal m) : (shapeB m p).filter (fun x => val x = m) = p.2 := by
  ext x
  simp only [shapeB, mem_filter, mem_union, mem_erase, mem_stair]
  constructor
  · rintro ⟨h | h, hv⟩
    · omega
    · exact h
  · intro h; exact ⟨Or.inr h, mem_antidiagonal.1 (hR h)⟩

theorem shapeA_injOn (m r : ℕ) : Set.InjOn (shapeA m) (caseA m r) := by
  intro p hp q hq hpq
  obtain ⟨hpc, hpR, -, -⟩ := mem_caseA.1 hp
  obtain ⟨hqc, hqR, -, -⟩ := mem_caseA.1 hq
  have h2 : p.2 = q.2 := by
    rw [← filter_val_shapeA hpc hpR, ← filter_val_shapeA hqc hqR, hpq]
  have h1 : p.1 = q.1 := by
    have : p.1 ∈ shapeA m q := hpq ▸ mem_insert_self _ _
    simp only [shapeA, mem_insert, mem_union, mem_stair] at this
    rcases this with h | h | h
    · exact h
    · omega
    · have := mem_antidiagonal.1 (hqR h); simp only [val] at hpc; omega
  exact Prod.ext h1 h2

theorem shapeB_injOn {m r : ℕ} (hm : 1 ≤ m) : Set.InjOn (shapeB m) (caseB m r) := by
  intro p hp q hq hpq
  obtain ⟨hpb, hpR, -, -⟩ := mem_caseB.1 hp
  obtain ⟨hqb, hqR, -, -⟩ := mem_caseB.1 hq
  have h2 : p.2 = q.2 := by
    rw [← filter_val_shapeB hpR, ← filter_val_shapeB hqR, hpq]
  have h1 : p.1 = q.1 := by
    by_contra hne
    have hin : p.1 ∈ shapeB m q := mem_union_left _ (mem_erase.2 ⟨hne, mem_stair.2 (by omega)⟩)
    rw [← hpq] at hin
    simp only [shapeB, mem_union, mem_erase] at hin
    rcases hin with h | h
    · exact h.1 rfl
    · have := mem_antidiagonal.1 (hpR h); simp only [val] at hpb; omega
  exact Prod.ext h1 h2

/-- **Classification of the shapes one cell above the minimum.** -/
theorem nearMin_classify {m r : ℕ} {s : Finset (ℕ × ℕ)} (hs : s ∈ nearMin m r) :
    (∃ p ∈ caseA m r, shapeA m p = s) ∨ (∃ p ∈ caseB m r, shapeB m p = s) := by
  classical
  obtain ⟨hcard, hlow, hN⟩ := mem_nearMin.1 hs
  have hd := delta_eq hcard
  set X := s.filter (fun c => m < val c) with hX
  set Y := stair m \ s with hY
  have hsum : ∑ a ∈ X, ((val a : ℤ) - m) + ∑ b ∈ Y, ((m : ℤ) - val b) = 1 := by
    rw [← hd, hN]; push_cast; ring
  have hXc : (X.card : ℤ) ≤ ∑ a ∈ X, ((val a : ℤ) - m) := by
    have := card_nsmul_le_sum X (fun a => (val a : ℤ) - m) 1 (fun a ha => by
      have := (mem_filter.1 ha).2; simp only; omega)
    simpa using this
  have hYc : (Y.card : ℤ) ≤ ∑ b ∈ Y, ((m : ℤ) - val b) := by
    have := card_nsmul_le_sum Y (fun b => (m : ℤ) - val b) 1 (fun b hb => by
      have := mem_stair.1 (mem_sdiff.1 hb).1; simp only; omega)
    simpa using this
  set R := s.filter (fun x => val x = m) with hRdef
  have hRsub : R ⊆ antidiagonal m := fun x hx => mem_antidiagonal.2 (mem_filter.1 hx).2
  have hRs : R ⊆ s := filter_subset _ _
  rcases Nat.eq_zero_or_pos X.card with hX0 | hX0
  · -- no cell above antidiagonal `m`: one staircase cell is missing
    right
    rw [card_eq_zero] at hX0
    rw [hX0, sum_empty, zero_add] at hsum
    have hY1 : Y.card = 1 := by
      have hpos : 0 < Y.card := by
        rcases Nat.eq_zero_or_pos Y.card with h | h
        · rw [card_eq_zero] at h; rw [h, sum_empty] at hsum; exact absurd hsum (by norm_num)
        · exact h
      omega
    obtain ⟨b, hYb⟩ := card_eq_one.1 hY1
    rw [hYb, sum_singleton] at hsum
    have hbY : b ∈ Y := hYb ▸ mem_singleton_self b
    have hbst := (mem_sdiff.1 hbY).1
    have hbs := (mem_sdiff.1 hbY).2
    have hseq : shapeB m (b, R) = s := by
      ext x
      simp only [shapeB, mem_union, mem_erase]
      constructor
      · rintro (⟨hxb, hx⟩ | hx)
        · by_contra hxs
          have : x ∈ Y := mem_sdiff.2 ⟨hx, hxs⟩
          rw [hYb, mem_singleton] at this
          exact hxb this
        · exact hRs hx
      · intro hx
        rcases lt_trichotomy (val x) m with h | h | h
        · exact Or.inl ⟨fun hxb => hbs (hxb ▸ hx), mem_stair.2 h⟩
        · exact Or.inr (mem_filter.2 ⟨hx, h⟩)
        · have : x ∈ X := mem_filter.2 ⟨hx, h⟩
          rw [hX0] at this; exact absurd this (notMem_empty _)
    refine ⟨(b, R), mem_caseB.2 ⟨?_, hRsub, ?_, ?_⟩, hseq⟩
    · simp only; omega
    · have hdisj : Disjoint ((stair m).erase b) R :=
        Finset.disjoint_of_subset_left (erase_subset _ _) (disjoint_stair hRsub)
      have := hcard
      rw [← hseq, shapeB, card_union_of_disjoint hdisj, card_erase_of_mem hbst] at this
      have : 1 ≤ (stair m).card := card_pos.2 ⟨_, hbst⟩
      simp only at *
      omega
    · rw [Finset.disjoint_left]
      intro d hd hdR
      exact hbs (hlow (mem_filter.1 hd).2 (hRs hdR))
  · -- one cell above antidiagonal `m`, and the staircase is complete
    left
    have hX1 : X.card = 1 := by omega
    have hY0 : Y = ∅ := by
      rw [← card_eq_zero]; omega
    obtain ⟨c, hXc'⟩ := card_eq_one.1 hX1
    rw [hY0, sum_empty, add_zero, hXc', sum_singleton] at hsum
    have hcX : c ∈ X := hXc' ▸ mem_singleton_self c
    have hcs := (mem_filter.1 hcX).1
    have hst : stair m ⊆ s := sdiff_eq_empty_iff_subset.1 hY0
    have hcv : val c = m + 1 := by omega
    have hcn : c ∉ stair m ∪ R := by
      intro h
      rcases mem_union.1 h with h | h
      · rw [mem_stair] at h; omega
      · have := (mem_filter.1 h).2; omega
    have hseq : shapeA m (c, R) = s := by
      ext x
      simp only [shapeA, mem_insert, mem_union]
      constructor
      · rintro (rfl | hx | hx)
        · exact hcs
        · exact hst hx
        · exact hRs hx
      · intro hx
        rcases lt_trichotomy (val x) m with h | h | h
        · exact Or.inr (Or.inl (mem_stair.2 h))
        · exact Or.inr (Or.inr (mem_filter.2 ⟨hx, h⟩))
        · have : x ∈ X := mem_filter.2 ⟨hx, h⟩
          rw [hXc', mem_singleton] at this
          exact Or.inl this
    refine ⟨(c, R), mem_caseA.2 ⟨hcv, hRsub, ?_, ?_⟩, hseq⟩
    · have := hcard
      rw [← hseq, shapeA, card_insert_of_notMem hcn,
        card_union_of_disjoint (disjoint_stair hRsub)] at this
      simp only at *
      omega
    · intro d hd
      rw [predsOf, mem_filter, mem_antidiagonal] at hd
      exact mem_filter.2 ⟨hlow hd.2 hcs, hd.1⟩

/-- `nearMin m r` is the disjoint union of the two families. -/
theorem card_nearMin {m r : ℕ} (hm : 1 ≤ m) (hr : 1 ≤ r) :
    (nearMin m r).card = (caseA m r).card + (caseB m r).card := by
  classical
  have heq : nearMin m r = (caseA m r).image (shapeA m) ∪ (caseB m r).image (shapeB m) := by
    ext s
    simp only [mem_union, mem_image]
    constructor
    · intro hs; exact nearMin_classify hs
    · rintro (⟨p, hp, rfl⟩ | ⟨p, hp, rfl⟩)
      · exact shapeA_mem hr hp
      · exact shapeB_mem hm hp
  have hdisj : Disjoint ((caseA m r).image (shapeA m)) ((caseB m r).image (shapeB m)) := by
    rw [Finset.disjoint_left]
    rintro s hsA hsB
    obtain ⟨p, hp, rfl⟩ := mem_image.1 hsA
    obtain ⟨q, hq, hpq⟩ := mem_image.1 hsB
    have hc := (mem_caseA.1 hp).1
    have hin : p.1 ∈ shapeB m q := hpq ▸ mem_insert_self _ _
    simp only [shapeB, mem_union, mem_erase, mem_stair] at hin
    rcases hin with h | h
    · omega
    · have := mem_antidiagonal.1 ((mem_caseB.1 hq).2.1 h); simp only [val] at hc; omega
  rw [heq, card_union_of_disjoint hdisj, card_image_of_injOn (shapeA_injOn m r),
    card_image_of_injOn (shapeB_injOn hm)]

/-- **The `δ = 1` count.** For `n = T_{k+1} + r` with `r ≥ 1`, the number of Young diagrams with
`n` cells and `N = N_min + 1` is `2 C(k+1, r-2) + (k+1) C(k, r-3) + (k+1) C(k, r+1)`, binomials
with negative lower index read as `0`. This is `a₁` of `conj:cyclotomic-boundary-at-keystone`
with `j = k + 1`. -/
theorem card_nearMin_eq (k r : ℕ) (hr : 1 ≤ r) :
    (nearMin (k + 1) r).card =
      2 * (if 2 ≤ r then (k + 1).choose (r - 2) else 0) +
        (k + 1) * (if 3 ≤ r then k.choose (r - 3) else 0) + (k + 1) * k.choose (r + 1) := by
  rw [card_nearMin (by omega) hr, card_caseA k r hr, card_caseB k r]

end Cells

section Coeff

open Polynomial

/-- **The coefficient one step below the top, symmetric normalisation.** Let `g i` be monic of
degree `M - N i`, and put `F i = X^(N i) · g i (X²)`, of degree `2M - N i`. Then the coefficient
of `∑ F i` at `2M - N_min - 1` counts the `i` with `N i = N_min + 1`: the minimisers contribute
nothing there, because `g (X²)` has no odd powers. -/
theorem coeff_sum_expand_eq_card {ι : Type*} (I : Finset ι) (Nf : ι → ℕ) (g : ι → ℤ[X])
    (M Nmin : ℕ) (hM1 : 1 ≤ M) (hM : ∀ i ∈ I, Nf i ≤ M) (hmin : ∀ i ∈ I, Nmin ≤ Nf i)
    (hmon : ∀ i ∈ I, (g i).Monic) (hdeg : ∀ i ∈ I, (g i).natDegree = M - Nf i) :
    (∑ i ∈ I, X ^ Nf i * expand ℤ 2 (g i)).coeff (2 * M - Nmin - 1) =
      ((I.filter (fun i => Nf i = Nmin + 1)).card : ℤ) := by
  classical
  rw [finset_sum_coeff, card_eq_sum_ones, Nat.cast_sum, sum_filter]
  refine sum_congr rfl (fun i hi => ?_)
  have h1 := hM i hi
  have h2 := hmin i hi
  have h3 := hdeg i hi
  rw [coeff_X_pow_mul', coeff_expand (by norm_num)]
  by_cases h : Nf i = Nmin + 1
  · rw [if_pos h, if_pos (by omega), if_pos (by omega)]
    have : (2 * M - Nmin - 1 - Nf i) / 2 = (g i).natDegree := by omega
    rw [this, (hmon i hi).coeff_natDegree]
    simp
  · rw [if_neg h]
    split_ifs with ha hb
    · apply coeff_eq_zero_of_natDegree_lt
      rcases Nat.lt_or_ge (Nf i) (Nmin + 1) with hlt | hge
      · exfalso
        have hN : Nf i = Nmin := by omega
        obtain ⟨c, hc⟩ := hb
        omega
      · omega
    · rfl
    · rfl

/-- **`a₁` as a coefficient.** With `g λ` the quotient `[n]! / ∏ [h]` in the variable `X = q²`
(given here as a hypothesis, `hg`), `X^(N λ) g λ (X²)` is `q^(C(n,2)) dim_q λ` in the symmetric
normalisation. The coefficient of their sum one step below the top is the `δ = 1` count. -/
theorem coeff_sum_sym_qHook_of_eq (k r : ℕ) (hr : 1 ≤ r) (hr' : r ≤ k + 2) (g : Finset (ℕ × ℕ) → ℤ[X])
    (hg : ∀ s ∈ shapes ((stair (k + 1)).card + r),
      qfact ((stair (k + 1)).card + r) = g s * hookProd s) :
    (∑ s ∈ shapes ((stair (k + 1)).card + r), X ^ N s * expand ℤ 2 (g s)).coeff
        (2 * (((stair (k + 1)).card + r) * ((stair (k + 1)).card + r - 1) / 2) -
          (N (stair (k + 1)) + r * (k + 1)) - 1) =
      ((2 * (if 2 ≤ r then (k + 1).choose (r - 2) else 0) +
        (k + 1) * (if 3 ≤ r then k.choose (r - 3) else 0) + (k + 1) * k.choose (r + 1) : ℕ) : ℤ) := by
  classical
  set n := (stair (k + 1)).card + r with hn
  have key : ∀ s ∈ shapes n, (g s).Monic ∧ (g s).natDegree = n * (n - 1) / 2 - N s ∧
      N s ≤ n * (n - 1) / 2 := by
    intro s hs
    obtain ⟨hcard, hlow⟩ := mem_shapes_iff.1 hs
    have := qHook_top_of_eq hlow (hcard ▸ hg s hs)
    rw [hcard] at this
    exact this
  have hn2 : 2 ≤ n := by
    have := two_mul_card_stair (k + 1)
    nlinarith
  have hM1 : 1 ≤ n * (n - 1) / 2 := by
    have : 2 ≤ n * (n - 1) := by nlinarith [Nat.sub_add_cancel (show 1 ≤ n by omega)]
    omega
  rw [coeff_sum_expand_eq_card _ N g _ _ hM1 (fun s hs => (key s hs).2.2)
    (fun s hs => le_N_of_card (by omega) (mem_shapes_iff.1 hs).1) (fun s hs => (key s hs).1)
    (fun s hs => (key s hs).2.1), ← card_nearMin_eq k r hr]
  rfl

end Coeff

end QOU.Mass.StaircaseMinimisers
