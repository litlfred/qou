/-
Copyright (c) 2026. Released under CC BY 4.0.
-/
import QOU.MassTheory.UpDownMoments

/-!
# Branching on beta-sets (Jucys–Murphy sums, stage 3)

Links the stage-1 weights to the hook formula and sets up the up-down recursion.

* `hookProd_mul_D`, `w_eq_inv_hookProd`: `w(B) = ∏_{c<b} (b-c) / ∏ b! = 1 / ∏ hooks`
  (Frobenius), so `f^λ = n! · w(B)`;
* `w_up`, `w_down`: moving a bead `b ↦ b ± 1` multiplies `w` by `wUp` / `wDown`;
* `sum_addable_w`, `sum_removable_w`: the up and down branching rules for `w`
  (the latter is `f^λ = ∑_{□} f^{λ-□}`);
* `contentPow_up`, `contentPow_down`, `size_mv`: contents of the added/removed box;
* `parts L n`, `mem_parts`, `zero_mem_of_parts`: partitions of `n` with at most `L` parts;
* `sum_addable_eq_sum_removable`: the bijection (μ ⊢ n, addable) ↔ (λ ⊢ n+1, removable).
-/

namespace QOU.Mass.BetaBranching
open Finset QOU.Mass.DividedDifference QOU.Mass.HookContentBeta QOU.Mass.UpDownMoments

/-- Vandermonde product `∏_{c<b in B} (b - c)`. -/
def D (B : Finset ℕ) : ℚ := ∏ b ∈ B, ∏ c ∈ B.filter (· < b), ((b : ℚ) - c)

/-- `∏_{c∈A} |x - c|`, split by side. -/
def E (A : Finset ℕ) (x : ℕ) : ℚ :=
  (∏ c ∈ A.filter (· < x), ((x : ℚ) - c)) * ∏ c ∈ A.filter (x < ·), ((c : ℚ) - x)

lemma D_insert {A : Finset ℕ} {b : ℕ} (hb : b ∉ A) : D (insert b A) = D A * E A b := by
  unfold D E
  rw [prod_insert hb, filter_insert, if_neg (lt_irrefl b)]
  have h : ∀ d ∈ A, ∏ c ∈ (insert b A).filter (· < d), ((d : ℚ) - c)
      = (if b < d then (d : ℚ) - b else 1) * ∏ c ∈ A.filter (· < d), ((d : ℚ) - c) := by
    intro d hd
    rw [filter_insert]
    split_ifs with h1
    · rw [prod_insert (fun h => hb (mem_filter.mp h).1)]
    · rw [one_mul]
  rw [prod_congr rfl h, prod_mul_distrib, prod_ite, prod_const_one, mul_one]
  ring

lemma E_eq {A : Finset ℕ} {x : ℕ} (hx : x ∉ A) :
    E A x = (-1) ^ (A.filter (x < ·)).card * ∏ c ∈ A, ((x : ℚ) - c) := by
  unfold E
  rw [← prod_filter_mul_prod_filter_not A (fun c => c < x)]
  have hf : A.filter (fun c => ¬ c < x) = A.filter (x < ·) := by
    ext c; simp only [mem_filter]
    constructor
    · rintro ⟨hc, h⟩; exact ⟨hc, lt_of_le_of_ne (not_lt.mp h) (fun e => hx (e ▸ hc))⟩
    · rintro ⟨hc, h⟩; exact ⟨hc, not_lt.mpr h.le⟩
  rw [hf]
  have : ∏ c ∈ A.filter (x < ·), ((c : ℚ) - x)
      = (-1) ^ (A.filter (x < ·)).card * ∏ c ∈ A.filter (x < ·), ((x : ℚ) - c) := by
    rw [← prod_const, ← prod_mul_distrib]; exact prod_congr rfl (fun _ _ => by ring)
  rw [this]; ring

/-- The weight `w(B) = D(B) / ∏ b!`; `f^λ = n! w(B)`. -/
def w (B : Finset ℕ) : ℚ := D B / ∏ b ∈ B, (b.factorial : ℚ)

lemma prod_ne_zero_sub {A : Finset ℕ} {b : ℕ} (hb : b ∉ A) : ∏ c ∈ A, ((b : ℚ) - c) ≠ 0 :=
  prod_ne_zero_iff.mpr (fun c hc => sub_ne_zero.mpr (fun h => hb (by rw [Nat.cast_injective h]; exact hc)))

lemma prod_erase_cS (B : Finset ℕ) (b : ℕ) (f : ℚ → ℚ) :
    ∏ c ∈ (cS B).erase (b : ℚ), f c = ∏ c ∈ B.erase b, f (c : ℚ) := by
  unfold cS
  rw [← image_erase cast_inj, prod_image (fun x _ y _ h => cast_inj h)]

/-- Moving bead `b ↦ b+1` multiplies the weight by `wUp`. -/
theorem w_up {B : Finset ℕ} {b : ℕ} (hb : b ∈ B) (hb1 : b + 1 ∉ B) :
    w (insert (b + 1) (B.erase b)) = w B * wUp (cS B) b := by
  set A := B.erase b
  have hbA : b ∉ A := notMem_erase b B
  have hb1A : b + 1 ∉ A := fun h => hb1 (mem_of_mem_erase h)
  have hB : B = insert b A := (insert_erase hb).symm
  have hfil : A.filter (b + 1 < ·) = A.filter (b < ·) := by
    ext c; simp only [mem_filter]
    constructor
    · rintro ⟨hc, h⟩; exact ⟨hc, by omega⟩
    · rintro ⟨hc, h⟩; refine ⟨hc, ?_⟩
      rcases Nat.lt_or_ge (b + 1) c with h' | h'
      · exact h'
      · exact absurd (by rw [show c = b + 1 by omega] at hc; exact hc) hb1A
  unfold w
  conv_rhs => rw [hB]
  rw [D_insert hb1A, D_insert hbA, E_eq hb1A, E_eq hbA, hfil, prod_insert hb1A,
    prod_insert hbA, wUp, prod_erase_cS, erase_insert hbA, prod_div_distrib, Nat.factorial_succ]
  have hne := prod_ne_zero_sub hbA
  have h1 : (b : ℚ) + 1 ≠ 0 := by positivity
  have hf : (b.factorial : ℚ) ≠ 0 := by positivity
  have hfA : ∏ x ∈ A, (x.factorial : ℚ) ≠ 0 := prod_ne_zero_iff.mpr (fun _ _ => by positivity)
  push_cast
  field_simp

/-- Moving bead `b ↦ b-1` multiplies the weight by `wDown`. -/
theorem w_down {B : Finset ℕ} {b : ℕ} (hb : b ∈ B) (h1 : 1 ≤ b) (hb1 : b - 1 ∉ B) :
    w (insert (b - 1) (B.erase b)) = w B * wDown (cS B) b := by
  set A := B.erase b
  have hbA : b ∉ A := notMem_erase b B
  have hb1A : b - 1 ∉ A := fun h => hb1 (mem_of_mem_erase h)
  have hB : B = insert b A := (insert_erase hb).symm
  have hfil : A.filter (b - 1 < ·) = A.filter (b < ·) := by
    ext c; simp only [mem_filter]
    constructor
    · rintro ⟨hc, h⟩; refine ⟨hc, ?_⟩
      rcases Nat.lt_or_ge b c with h' | h'
      · exact h'
      · exact absurd (by rw [show c = b by omega] at hc; exact hc) hbA
    · rintro ⟨hc, h⟩; exact ⟨hc, by omega⟩
  unfold w
  conv_rhs => rw [hB]
  rw [D_insert hb1A, D_insert hbA, E_eq hb1A, E_eq hbA, hfil, prod_insert hb1A,
    prod_insert hbA, wDown, prod_erase_cS, erase_insert hbA, prod_div_distrib,
    ← Nat.mul_factorial_pred (show b ≠ 0 by omega)]
  have hne := prod_ne_zero_sub hbA
  have hf : ((b - 1).factorial : ℚ) ≠ 0 := by positivity
  have hb0 : (b : ℚ) ≠ 0 := by exact_mod_cast (show b ≠ 0 by omega)
  have hfA : ∏ x ∈ A, (x.factorial : ℚ) ≠ 0 := prod_ne_zero_iff.mpr (fun _ _ => by positivity)
  rw [Nat.cast_sub h1]
  push_cast
  field_simp

/-- Hooks: `∏_{b∈B} ∏_{g<b, g∉B} (b - g)`. -/
def hookProd (B : Finset ℕ) : ℚ := ∏ b ∈ B, ∏ g ∈ (range b).filter (· ∉ B), ((b : ℚ) - g)

/-- **Frobenius.** `∏ hooks · ∏_{c<b} (b - c) = ∏ b!`, so `w B = 1 / ∏ hooks`. -/
theorem hookProd_mul_D (B : Finset ℕ) : hookProd B * D B = ∏ b ∈ B, (b.factorial : ℚ) := by
  unfold hookProd D
  rw [← prod_mul_distrib]
  refine prod_congr rfl (fun b hb => ?_)
  have e : B.filter (· < b) = (range b).filter (· ∈ B) := by
    ext c; simp [and_comm]
  rw [e, mul_comm, prod_filter_mul_prod_filter_not]
  rw [← prod_range_reflect]
  have : ∀ j ∈ range b, ((b : ℚ) - ((b - 1 - j : ℕ) : ℚ)) = ((j + 1 : ℕ) : ℚ) := by
    intro j hj; rw [mem_range] at hj
    rw [Nat.cast_sub (by omega), Nat.cast_sub (by omega)]; push_cast; ring
  rw [prod_congr rfl this, ← Nat.cast_prod, prod_range_add_one_eq_factorial]

theorem w_eq_inv_hookProd (B : Finset ℕ) : w B = (hookProd B)⁻¹ := by
  have h := hookProd_mul_D B
  have hF : ∏ b ∈ B, (b.factorial : ℚ) ≠ 0 := prod_ne_zero_iff.mpr (fun _ _ => by positivity)
  have hH : hookProd B ≠ 0 := fun h0 => hF (by rw [← h, h0, zero_mul])
  have hD : D B ≠ 0 := fun h0 => hF (by rw [← h, h0, mul_zero])
  unfold w; rw [← h]; field_simp

/-! ### Moves on beta-sets: size, contents, card -/

/-- Replace bead `b` by `b'`. -/
def mv (B : Finset ℕ) (b b' : ℕ) : Finset ℕ := insert b' (B.erase b)

lemma sum_mv {B : Finset ℕ} {b b' : ℕ} (hb : b ∈ B) (hb' : b' ∉ B) (f : ℕ → ℚ) :
    ∑ x ∈ mv B b b', f x = ∑ x ∈ B, f x - f b + f b' := by
  unfold mv
  rw [sum_insert (fun h => hb' (mem_of_mem_erase h)), ← sum_erase_add _ _ hb]; ring

lemma card_mv {B : Finset ℕ} {b b' : ℕ} (hb : b ∈ B) (hb' : b' ∉ B) :
    (mv B b b').card = B.card := by
  unfold mv
  rw [card_insert_of_notMem (fun h => hb' (mem_of_mem_erase h)), card_erase_of_mem hb]
  have := card_pos.mpr ⟨b, hb⟩; omega

lemma size_mv {B : Finset ℕ} {b b' : ℕ} (hb : b ∈ B) (hb' : b' ∉ B) :
    size (mv B b b') = size B + b' - b := by
  rw [size_pw, size_pw, card_mv hb hb']
  unfold pw; rw [sum_mv hb hb' (fun x => (x : ℚ) ^ 1)]; ring

lemma contentPow_mv (k : ℕ) (hk : k ≤ 5) {B : Finset ℕ} {b b' : ℕ} (hb : b ∈ B) (hb' : b' ∉ B) :
    contentPow k (mv B b b') = contentPow k B - P k ((b : ℚ) - B.card + 1)
      + P k ((b' : ℚ) - B.card + 1) := by
  rw [contentPow_eq k hk, contentPow_eq k hk, card_mv hb hb',
    sum_mv hb hb' (fun x => P k ((x : ℚ) - B.card + 1))]; ring

/-- Adding a box at bead `b` adds the content `b - ℓ + 1`. -/
lemma contentPow_up (k : ℕ) (hk : k ≤ 5) {B : Finset ℕ} {b : ℕ} (hb : b ∈ B) (hb1 : b + 1 ∉ B) :
    contentPow k (mv B b (b + 1)) = contentPow k B + ((b : ℚ) - B.card + 1) ^ k := by
  rw [contentPow_mv k hk hb hb1, ← P_step k hk]; push_cast; ring_nf

/-- Removing a box at bead `b` removes the content `b - ℓ`. -/
lemma contentPow_down (k : ℕ) (hk : k ≤ 5) {B : Finset ℕ} {b : ℕ} (hb : b ∈ B) (h1 : 1 ≤ b)
    (hb1 : b - 1 ∉ B) :
    contentPow k (mv B b (b - 1)) = contentPow k B - ((b : ℚ) - B.card) ^ k := by
  rw [contentPow_mv k hk hb hb1, Nat.cast_sub h1,
    show ((b : ℚ) - ((1 : ℕ) : ℚ) - B.card + 1) = (b : ℚ) - B.card by push_cast; ring]
  have hp := P_step k hk ((b : ℚ) - B.card)
  linarith

/-! ### Partitions of `n` with at most `L` parts -/

lemma term_le_size (B : Finset ℕ) {b : ℕ} (hb : b ∈ B) : (b : ℚ) - lo B b ≤ size B := by
  unfold size
  exact single_le_sum (f := fun x : ℕ => (x : ℚ) - lo B x)
    (fun x _ => by have := lo_le B x; simp only [sub_nonneg]; exact_mod_cast this) hb

lemma lt_of_size {B : Finset ℕ} {n : ℕ} (hn : size B = n) {b : ℕ} (hb : b ∈ B) :
    b < n + B.card := by
  have h1 := term_le_size B hb
  have h2 := lo_add_hi B hb
  have : (b : ℚ) ≤ n + lo B b := by linarith
  have : b ≤ n + lo B b := by exact_mod_cast this
  omega

/-- Beta-sets with `L` beads and size `n`: partitions of `n` with at most `L` parts. -/
def parts (L n : ℕ) : Finset (Finset ℕ) :=
  ((range (n + L)).powersetCard L).filter (fun B => size B = n)

lemma mem_parts {L n : ℕ} {B : Finset ℕ} : B ∈ parts L n ↔ B.card = L ∧ size B = n := by
  unfold parts
  rw [mem_filter, mem_powersetCard]
  constructor
  · rintro ⟨⟨_, h⟩, h'⟩; exact ⟨h, h'⟩
  · rintro ⟨h, h'⟩
    refine ⟨⟨fun b hb => ?_, h⟩, h'⟩
    rw [mem_range, ← h]; exact lt_of_size h' hb

/-- With more beads than boxes, bead `0` is present. -/
lemma zero_mem_of_parts {L n : ℕ} {B : Finset ℕ} (hB : B ∈ parts L n) (hL : n < L) : 0 ∈ B := by
  obtain ⟨hc, hs⟩ := mem_parts.mp hB
  by_contra h0
  have key : ∀ b ∈ B, (1 : ℚ) ≤ (b : ℚ) - lo B b := by
    intro b hb
    have hsub : B.filter (· < b) ⊆ (range b).erase 0 := by
      intro c hc'; rw [mem_filter] at hc'
      exact mem_erase.mpr ⟨fun e => h0 (e ▸ hc'.1), mem_range.mpr hc'.2⟩
    have hb0 : b ≠ 0 := fun e => h0 (e ▸ hb)
    have := card_le_card hsub
    rw [card_erase_of_mem (mem_range.mpr (Nat.pos_of_ne_zero hb0)), card_range] at this
    have : lo B b + 1 ≤ b := by unfold lo; omega
    have : ((lo B b : ℕ) : ℚ) + 1 ≤ b := by exact_mod_cast this
    linarith
  have : (B.card : ℚ) ≤ size B := by
    unfold size
    calc (B.card : ℚ) = ∑ _b ∈ B, (1 : ℚ) := by simp
      _ ≤ _ := sum_le_sum key
  rw [hs, hc] at this
  have : L ≤ n := by exact_mod_cast this
  omega

lemma mv_mv {B : Finset ℕ} {b b' : ℕ} (hb : b ∈ B) (hb' : b' ∉ B) : mv (mv B b b') b' b = B := by
  unfold mv
  rw [erase_insert (fun h => hb' (mem_of_mem_erase h)), insert_erase hb]

lemma mem_mv_self (B : Finset ℕ) (b b' : ℕ) : b' ∈ mv B b b' := mem_insert_self _ _

lemma notMem_mv {B : Finset ℕ} {b b' : ℕ} (h : b ≠ b') : b ∉ mv B b b' := by
  unfold mv; simp [h]

/-- **Add/remove bijection.** Pairs (partition of `n`, addable bead) correspond to pairs
(partition of `n+1`, removable bead). -/
theorem sum_addable_eq_sum_removable (L n : ℕ) (ψ : Finset ℕ → ℕ → ℚ) :
    ∑ B ∈ parts L n, ∑ b ∈ addable B, ψ B b
      = ∑ B ∈ parts L (n + 1), ∑ b ∈ removable B, ψ (mv B b (b - 1)) (b - 1) := by
  rw [sum_sigma', sum_sigma']
  refine sum_nbij' (fun p => ⟨mv p.1 p.2 (p.2 + 1), p.2 + 1⟩)
    (fun p => ⟨mv p.1 p.2 (p.2 - 1), p.2 - 1⟩) ?_ ?_ ?_ ?_ ?_
  · rintro ⟨B, b⟩ hp
    simp only [mem_sigma, addable, mem_filter] at hp
    obtain ⟨hB, hb, hb1⟩ := hp
    obtain ⟨hc, hs⟩ := mem_parts.mp hB
    simp only [mem_sigma, removable, mem_filter]
    refine ⟨mem_parts.mpr ⟨by rw [card_mv hb hb1, hc], by rw [size_mv hb hb1, hs]; push_cast; ring⟩,
      mem_mv_self _ _ _, by omega, ?_⟩
    simpa using notMem_mv (B := B) (show b ≠ b + 1 by omega)
  · rintro ⟨B, b⟩ hp
    simp only [mem_sigma, removable, mem_filter] at hp
    obtain ⟨hB, hb, h1, hb1⟩ := hp
    obtain ⟨hc, hs⟩ := mem_parts.mp hB
    simp only [mem_sigma, addable, mem_filter]
    refine ⟨mem_parts.mpr ⟨by rw [card_mv hb hb1, hc], ?_⟩, mem_mv_self _ _ _, ?_⟩
    · rw [size_mv hb hb1, hs, Nat.cast_sub h1]; push_cast; ring
    · rw [Nat.sub_add_cancel h1]; exact notMem_mv (show b ≠ b - 1 by omega)
  · rintro ⟨B, b⟩ hp
    simp only [mem_sigma, addable, mem_filter] at hp
    simp only [Nat.add_sub_cancel, mv_mv hp.2.1 hp.2.2]
  · rintro ⟨B, b⟩ hp
    simp only [mem_sigma, removable, mem_filter] at hp
    simp only [Nat.sub_add_cancel hp.2.2.1, mv_mv hp.2.1 hp.2.2.2]
  · rintro ⟨B, b⟩ hp
    simp only [mem_sigma, addable, mem_filter] at hp
    simp only [Nat.add_sub_cancel, mv_mv hp.2.1 hp.2.2]

/-! ### Branching rules for the weight `w = 1 / ∏ hooks` -/

/-- **Up branching** with a test function. -/
theorem sum_addable_w (B : Finset ℕ) (φ : ℚ → ℚ) :
    ∑ b ∈ addable B, w (mv B b (b + 1)) * φ b = w B * ∑ b ∈ B, wUp (cS B) b * φ b := by
  rw [sum_wUp_addable, mul_sum]
  refine sum_congr rfl (fun b hb => ?_)
  rw [addable, mem_filter] at hb
  rw [mv, w_up hb.1 hb.2]; ring

/-- **Down branching.** `∑_{removable} w(λ - □) = n · w(λ)`, i.e. `f^λ = ∑ f^{λ-□}`. -/
theorem sum_removable_w (B : Finset ℕ) (hB : B.Nonempty) :
    ∑ b ∈ removable B, w (mv B b (b - 1)) = w B * size B := by
  have hrw : ∑ b ∈ removable B, w (mv B b (b - 1))
      = w B * ∑ b ∈ removable B, wDown (cS B) b := by
    rw [mul_sum]; refine sum_congr rfl (fun b hb => ?_)
    rw [removable, mem_filter] at hb
    rw [mv, w_down hb.1 hb.2.1 hb.2.2]
  have hzero : ∑ b ∈ removable B, wDown (cS B) b = ∑ b ∈ B, wDown (cS B) b := by
    unfold removable
    rw [← sum_filter_add_sum_filter_not B (fun b => 1 ≤ b ∧ b - 1 ∉ B), left_eq_add]
    refine sum_eq_zero (fun b hb => ?_)
    rw [mem_filter] at hb
    by_cases h1 : 1 ≤ b
    · have hm : b - 1 ∈ B := by by_contra h; exact hb.2 ⟨h1, h⟩
      have : (b : ℚ) - 1 ∈ cS B := mem_image.mpr ⟨b - 1, hm, by rw [Nat.cast_sub h1]; simp⟩
      exact wDown_eq_zero _ this
    · have : b = 0 := by omega
      subst this; simp [wDown]
  have himg : ∑ b ∈ B, wDown (cS B) b = ∑ s ∈ cS B, wDown (cS B) s := by
    unfold cS; rw [sum_image (fun x _ y _ h => cast_inj h)]
  have hne : (cS B).Nonempty := hB.image _
  rw [hrw, hzero, himg, down_branch _ hne, q_cS, card_cS, size_pw]

end QOU.Mass.BetaBranching
