import Mathlib.Tactic

/-!
# Hook and content power sums through beta-sets

A partition with `ℓ` parts is encoded by its beta-set `B`, `|B| = ℓ`: the element `b` with
`hi B b` elements above it is `λ_i + ℓ - 1 - i` for `i = hi B b`. Its hooks are the pairs
`g < b` with `b ∈ B`, `g ∉ B` [macdonald1995, Ch. I §1], and its row `i` has length
`b - lo B b` and contents `j - i`. On this model we prove, for every finite `B ⊆ ℕ`,

* `hook_two`:  `∑ h² = ∑ c² + n²`,
* `hook_four`: `∑ h⁴ = ∑ c⁴ + 12 n ∑ c² + n² - 12 (∑ c)²`,

the two hook identities used in the `q = 1` expansion of the Habiro tail
(`prop:habiro-tail-cyclotomic-iff-n-le-5`). The proof writes both sides through the power
sums of `B`: contents through Faulhaber polynomials and the rank bijection `hi : B → range ℓ`
(`sum_hi`), hooks through `∑_{g<b} (b-g)^k` minus the pair sum over `B`.
-/

namespace QOU.Mass.HookContentBeta
open Finset

/-- Faulhaber polynomials with `P k (x+1) - P k x = x^k`. -/
def P : ℕ → ℚ → ℚ
  | 0, x => x
  | 1, x => x * (x - 1) / 2
  | 2, x => x * (x - 1) * (2 * x - 1) / 6
  | 3, x => (x * (x - 1) / 2) ^ 2
  | 4, x => x * (x - 1) * (2 * x - 1) * (3 * x ^ 2 - 3 * x - 1) / 30
  | 5, x => x ^ 2 * (x - 1) ^ 2 * (2 * x ^ 2 - 2 * x - 1) / 12
  | _, _ => 0

lemma P_step (k : ℕ) (hk : k ≤ 5) (x : ℚ) : P k (x + 1) - P k x = x ^ k := by
  interval_cases k <;> simp only [P] <;> ring

lemma sum_shift_pow (k : ℕ) (hk : k ≤ 5) (h : ℚ) (L : ℕ) :
    ∑ j ∈ range L, ((j : ℚ) - h) ^ k = P k (L - h) - P k (-h) := by
  induction L with
  | zero => simp
  | succ L ih =>
    rw [sum_range_succ, ih]
    have := P_step k hk ((L : ℚ) - h)
    push_cast
    have e : (L : ℚ) + 1 - h = (L - h) + 1 := by ring
    rw [e]; linarith


/-- Number of elements of `B` below `b`. -/
def lo (B : Finset ℕ) (b : ℕ) : ℕ := (B.filter (· < b)).card
/-- Number of elements of `B` above `b`. -/
def hi (B : Finset ℕ) (b : ℕ) : ℕ := (B.filter (b < ·)).card

lemma lo_le (B : Finset ℕ) (b : ℕ) : lo B b ≤ b := by
  unfold lo
  calc (B.filter (· < b)).card ≤ (range b).card :=
        card_le_card (fun x hx => by simp at hx ⊢; exact hx.2)
    _ = b := card_range b

lemma lo_add_hi (B : Finset ℕ) {b : ℕ} (hb : b ∈ B) : lo B b + hi B b + 1 = B.card := by
  unfold lo hi
  have h1 := filter_card_add_filter_neg_card_eq_card (s := B) (fun x => x < b)
  have h2 : B.filter (fun x => ¬ x < b) = insert b (B.filter (b < ·)) := by
    ext x; simp only [mem_filter, mem_insert]
    constructor
    · rintro ⟨hx, h⟩; rcases Nat.lt_or_ge b x with h' | h'
      · exact Or.inr ⟨hx, h'⟩
      · left; omega
    · rintro (rfl | ⟨hx, h⟩)
      · exact ⟨hb, lt_irrefl _⟩
      · exact ⟨hx, by omega⟩
  have h3 : b ∉ B.filter (b < ·) := by simp
  rw [h2, card_insert_of_notMem h3] at h1
  omega

/-- Summing a function of the upper rank over `B` is summing it over `range B.card`. -/
lemma sum_hi (B : Finset ℕ) (f : ℕ → ℚ) :
    ∑ b ∈ B, f (hi B b) = ∑ i ∈ range B.card, f i := by
  induction B using Finset.induction_on_max generalizing f with
  | h0 => simp
  | step a s ha ih =>
    have hna : a ∉ s := fun h => lt_irrefl a (ha a h)
    rw [sum_insert hna, card_insert_of_notMem hna, sum_range_succ']
    have hia : hi (insert a s) a = 0 := by
      unfold hi; rw [card_eq_zero]; ext x
      simp only [mem_filter, mem_insert, notMem_empty, iff_false, not_and]
      rintro (rfl | hx) h
      · exact lt_irrefl _ h
      · exact lt_asymm h (ha x hx)
    have his : ∀ x ∈ s, hi (insert a s) x = hi s x + 1 := by
      intro x hx; unfold hi
      have : (insert a s).filter (x < ·) = insert a (s.filter (x < ·)) := by
        rw [filter_insert, if_pos (ha x hx)]
      rw [this, card_insert_of_notMem (by simp [hna])]
    rw [hia, sum_congr rfl (fun x hx => by rw [his x hx]), ih (fun i => f (i + 1))]
    ring

/-- Number of cells of the partition with beta-set `B`. -/
def size (B : Finset ℕ) : ℚ := ∑ b ∈ B, ((b : ℚ) - lo B b)

/-- `∑ h^k` over the hooks: pairs `g < b` with `b ∈ B`, `g ∉ B`. -/
def hookPow (k : ℕ) (B : Finset ℕ) : ℚ :=
  ∑ b ∈ B, ∑ g ∈ (range b).filter (· ∉ B), ((b : ℚ) - g) ^ k

/-- `∑ c^k` over the contents: the row of `b` has length `b - lo B b` and index `hi B b`. -/
def contentPow (k : ℕ) (B : Finset ℕ) : ℚ :=
  ∑ b ∈ B, ∑ j ∈ range (b - lo B b), ((j : ℚ) - hi B b) ^ k

lemma lo_cast (B : Finset ℕ) {b : ℕ} (hb : b ∈ B) :
    (lo B b : ℚ) = B.card - 1 - hi B b := by
  have := lo_add_hi B hb
  have : (lo B b : ℚ) + hi B b + 1 = B.card := by exact_mod_cast this
  linarith

lemma size_eq (B : Finset ℕ) :
    size B = ∑ b ∈ B, (b : ℚ) - ∑ i ∈ range B.card, ((B.card : ℚ) - 1 - i) := by
  unfold size
  rw [sum_sub_distrib, sum_congr rfl (fun b hb => lo_cast B hb),
    ← sum_hi B (fun i => (B.card : ℚ) - 1 - i)]

lemma contentPow_eq (k : ℕ) (hk : k ≤ 5) (B : Finset ℕ) :
    contentPow k B = ∑ b ∈ B, P k ((b : ℚ) - B.card + 1)
      - ∑ i ∈ range B.card, P k (-(i : ℚ)) := by
  unfold contentPow
  rw [← sum_hi B (fun i => P k (-(i : ℚ))), ← sum_sub_distrib]
  refine sum_congr rfl (fun b hb => ?_)
  rw [sum_shift_pow k hk, Nat.cast_sub (lo_le B b), lo_cast B hb]
  congr 1; ring_nf

lemma hookPow_eq (k : ℕ) (hk : k ≤ 5) (B : Finset ℕ) :
    hookPow k B = ∑ b ∈ B, (P k ((b : ℚ) + 1) - P k 1)
      - ∑ b ∈ B, ∑ c ∈ B.filter (· < b), ((b : ℚ) - c) ^ k := by
  unfold hookPow
  rw [← sum_sub_distrib]
  refine sum_congr rfl (fun b _ => ?_)
  have hsplit := sum_filter_add_sum_filter_not (range b) (· ∈ B) (fun g => ((b : ℚ) - g) ^ k)
  have hin : (range b).filter (· ∈ B) = B.filter (· < b) := by
    ext x; simp [and_comm]
  rw [hin] at hsplit
  have hall : ∑ g ∈ range b, ((b : ℚ) - g) ^ k = P k ((b : ℚ) + 1) - P k 1 := by
    rw [← sum_range_reflect]
    have : ∀ j ∈ range b, ((b : ℚ) - ((b - 1 - j : ℕ) : ℚ)) ^ k = ((j : ℚ) - (-1)) ^ k := by
      intro j hj; rw [mem_range] at hj
      rw [Nat.cast_sub (by omega), Nat.cast_sub (by omega)]; push_cast; ring
    rw [sum_congr rfl this, sum_shift_pow k hk]; congr 1; ring_nf
  linarith

/-- The power sums of a beta-set. -/
def pw (j : ℕ) (B : Finset ℕ) : ℚ := ∑ b ∈ B, (b : ℚ) ^ j

lemma sum_poly (S : Finset ℕ) (f : ℕ → ℚ) (a0 a1 a2 a3 a4 a5 a6 : ℚ)
    (hf : ∀ x, f x = a0 + a1 * x + a2 * x ^ 2 + a3 * x ^ 3 + a4 * x ^ 4 + a5 * x ^ 5
      + a6 * x ^ 6) :
    ∑ x ∈ S, f x = a0 * S.card + a1 * pw 1 S + a2 * pw 2 S + a3 * pw 3 S + a4 * pw 4 S
      + a5 * pw 5 S + a6 * pw 6 S := by
  simp only [hf, pw, sum_add_distrib, ← mul_sum, sum_const, nsmul_eq_mul]; ring_nf

lemma pw_range (j : ℕ) (hj : j ≤ 5) (L : ℕ) : pw j (range L) = P j L := by
  unfold pw
  have := sum_shift_pow j hj 0 L
  simp only [sub_zero, neg_zero] at this
  rw [this]
  interval_cases j <;> simp [P]

lemma pair_sym (k : ℕ) (hk : Even k) (hk0 : k ≠ 0) (B : Finset ℕ) :
    ∑ b ∈ B, ∑ c ∈ B, ((b : ℚ) - c) ^ k
      = 2 * ∑ b ∈ B, ∑ c ∈ B.filter (· < b), ((b : ℚ) - c) ^ k := by
  have e1 : ∀ b c : ℕ, ((b : ℚ) - c) ^ k
      = (if c < b then ((b : ℚ) - c) ^ k else 0) + (if b < c then ((c : ℚ) - b) ^ k else 0) := by
    intro b c
    rcases lt_trichotomy c b with h | h | h
    · simp [h, not_lt.mpr h.le]
    · subst h; simp [hk0]
    · simp [h, not_lt.mpr h.le]; rw [← neg_sub, hk.neg_pow]
  simp_rw [sum_filter]
  rw [sum_congr rfl (fun b _ => sum_congr rfl (fun c _ => e1 b c))]
  simp only [sum_add_distrib]
  rw [sum_comm (s := B) (t := B) (f := fun b c => if b < c then ((c : ℚ) - b) ^ k else 0)]
  ring

lemma sumA1_1 (B : Finset ℕ) :
    ∑ b ∈ B, (P 1 ((b : ℚ) + 1) - P 1 1) = (0) * B.card + (1/2) * pw 1 B + (1/2) * pw 2 B + (0) * pw 3 B + (0) * pw 4 B + (0) * pw 5 B + (0) * pw 6 B := by
  rw [sum_poly B (fun b => P 1 ((b : ℚ) + 1) - P 1 1) (0) (1/2) (1/2) (0) (0) (0) (0)
    (fun b => by simp only [P]; ring)]

lemma sumA3_1 (B : Finset ℕ) :
    ∑ b ∈ B, P 1 ((b : ℚ) - B.card + 1) = ((B.card : ℚ)^2/2 - (B.card : ℚ)/2) * B.card + (1/2 - (B.card : ℚ)) * pw 1 B + (1/2) * pw 2 B + (0) * pw 3 B + (0) * pw 4 B + (0) * pw 5 B + (0) * pw 6 B := by
  rw [sum_poly B (fun b => P 1 ((b : ℚ) - B.card + 1)) ((B.card : ℚ)^2/2 - (B.card : ℚ)/2) (1/2 - (B.card : ℚ)) (1/2) (0) (0) (0) (0)
    (fun b => by simp only [P]; ring)]

lemma sumA4_1 (B : Finset ℕ) :
    ∑ i ∈ range B.card, P 1 (-(i : ℚ)) = ((B.card : ℚ)^3/6 - (B.card : ℚ)/6) := by
  rw [sum_poly (range B.card) (fun i => P 1 (-(i : ℚ))) (0) (1/2) (1/2) (0) (0) (0) (0)
    (fun i => by simp only [P]; ring)]
  simp only [card_range, pw_range 1 (by norm_num), pw_range 2 (by norm_num), pw_range 3 (by norm_num),
    pw_range 4 (by norm_num), pw_range 5 (by norm_num), P]
  ring

lemma sumA1_2 (B : Finset ℕ) :
    ∑ b ∈ B, (P 2 ((b : ℚ) + 1) - P 2 1) = (0) * B.card + (1/6) * pw 1 B + (1/2) * pw 2 B + (1/3) * pw 3 B + (0) * pw 4 B + (0) * pw 5 B + (0) * pw 6 B := by
  rw [sum_poly B (fun b => P 2 ((b : ℚ) + 1) - P 2 1) (0) (1/6) (1/2) (1/3) (0) (0) (0)
    (fun b => by simp only [P]; ring)]

lemma sumA3_2 (B : Finset ℕ) :
    ∑ b ∈ B, P 2 ((b : ℚ) - B.card + 1) = (-(B.card : ℚ)^3/3 + (B.card : ℚ)^2/2 - (B.card : ℚ)/6) * B.card + ((B.card : ℚ)^2 - (B.card : ℚ) + 1/6) * pw 1 B + (1/2 - (B.card : ℚ)) * pw 2 B + (1/3) * pw 3 B + (0) * pw 4 B + (0) * pw 5 B + (0) * pw 6 B := by
  rw [sum_poly B (fun b => P 2 ((b : ℚ) - B.card + 1)) (-(B.card : ℚ)^3/3 + (B.card : ℚ)^2/2 - (B.card : ℚ)/6) ((B.card : ℚ)^2 - (B.card : ℚ) + 1/6) (1/2 - (B.card : ℚ)) (1/3) (0) (0) (0)
    (fun b => by simp only [P]; ring)]

lemma sumA4_2 (B : Finset ℕ) :
    ∑ i ∈ range B.card, P 2 (-(i : ℚ)) = (-(B.card : ℚ)^4/12 + (B.card : ℚ)^2/12) := by
  rw [sum_poly (range B.card) (fun i => P 2 (-(i : ℚ))) (0) (-1/6) (-1/2) (-1/3) (0) (0) (0)
    (fun i => by simp only [P]; ring)]
  simp only [card_range, pw_range 1 (by norm_num), pw_range 2 (by norm_num), pw_range 3 (by norm_num),
    pw_range 4 (by norm_num), pw_range 5 (by norm_num), P]
  ring

lemma sumA1_4 (B : Finset ℕ) :
    ∑ b ∈ B, (P 4 ((b : ℚ) + 1) - P 4 1) = (0) * B.card + (-1/30) * pw 1 B + (0) * pw 2 B + (1/3) * pw 3 B + (1/2) * pw 4 B + (1/5) * pw 5 B + (0) * pw 6 B := by
  rw [sum_poly B (fun b => P 4 ((b : ℚ) + 1) - P 4 1) (0) (-1/30) (0) (1/3) (1/2) (1/5) (0)
    (fun b => by simp only [P]; ring)]

lemma sumA3_4 (B : Finset ℕ) :
    ∑ b ∈ B, P 4 ((b : ℚ) - B.card + 1) = (-(B.card : ℚ)^5/5 + (B.card : ℚ)^4/2 - (B.card : ℚ)^3/3 + (B.card : ℚ)/30) * B.card + ((B.card : ℚ)^4 - 2*(B.card : ℚ)^3 + (B.card : ℚ)^2 - 1/30) * pw 1 B + (-2*(B.card : ℚ)^3 + 3*(B.card : ℚ)^2 - (B.card : ℚ)) * pw 2 B + (2*(B.card : ℚ)^2 - 2*(B.card : ℚ) + 1/3) * pw 3 B + (1/2 - (B.card : ℚ)) * pw 4 B + (1/5) * pw 5 B + (0) * pw 6 B := by
  rw [sum_poly B (fun b => P 4 ((b : ℚ) - B.card + 1)) (-(B.card : ℚ)^5/5 + (B.card : ℚ)^4/2 - (B.card : ℚ)^3/3 + (B.card : ℚ)/30) ((B.card : ℚ)^4 - 2*(B.card : ℚ)^3 + (B.card : ℚ)^2 - 1/30) (-2*(B.card : ℚ)^3 + 3*(B.card : ℚ)^2 - (B.card : ℚ)) (2*(B.card : ℚ)^2 - 2*(B.card : ℚ) + 1/3) (1/2 - (B.card : ℚ)) (1/5) (0)
    (fun b => by simp only [P]; ring)]

lemma sumA4_4 (B : Finset ℕ) :
    ∑ i ∈ range B.card, P 4 (-(i : ℚ)) = (-(B.card : ℚ)^6/30 + (B.card : ℚ)^4/12 - (B.card : ℚ)^2/20) := by
  rw [sum_poly (range B.card) (fun i => P 4 (-(i : ℚ))) (0) (1/30) (0) (-1/3) (-1/2) (-1/5) (0)
    (fun i => by simp only [P]; ring)]
  simp only [card_range, pw_range 1 (by norm_num), pw_range 2 (by norm_num), pw_range 3 (by norm_num),
    pw_range 4 (by norm_num), pw_range 5 (by norm_num), P]
  ring

lemma sumA2_2 (B : Finset ℕ) :
    ∑ b ∈ B, ∑ c ∈ B, ((b : ℚ) - c) ^ 2 = (1) * pw 2 B * (B.card : ℚ) + (-2) * pw 1 B * pw 1 B + (1) * (B.card : ℚ) * pw 2 B := by
  have hin : ∀ b : ℕ, ∑ c ∈ B, ((b : ℚ) - c) ^ 2 = (1 * (b : ℚ) ^ 2) * ((B.card : ℕ) : ℚ) + (-2 * (b : ℚ) ^ 1) * pw 1 B + (1 * (b : ℚ) ^ 0) * pw 2 B + 0 * pw 3 B + 0 * pw 4 B + 0 * pw 5 B + 0 * pw 6 B :=
    fun b => sum_poly B (fun c => ((b : ℚ) - c) ^ 2) (1 * (b : ℚ) ^ 2) (-2 * (b : ℚ) ^ 1) (1 * (b : ℚ) ^ 0) 0 0 0 0 (fun c => by ring)
  rw [sum_congr rfl (fun b _ => hin b)]
  rw [sum_poly B _ (1 * pw 2 B) (-2 * pw 1 B) (1 * (B.card : ℚ)) 0 0 0 0 (fun b => by ring)]
  ring

lemma sumA2_4 (B : Finset ℕ) :
    ∑ b ∈ B, ∑ c ∈ B, ((b : ℚ) - c) ^ 4 = (1) * pw 4 B * (B.card : ℚ) + (-4) * pw 3 B * pw 1 B + (6) * pw 2 B * pw 2 B + (-4) * pw 1 B * pw 3 B + (1) * (B.card : ℚ) * pw 4 B := by
  have hin : ∀ b : ℕ, ∑ c ∈ B, ((b : ℚ) - c) ^ 4 = (1 * (b : ℚ) ^ 4) * ((B.card : ℕ) : ℚ) + (-4 * (b : ℚ) ^ 3) * pw 1 B + (6 * (b : ℚ) ^ 2) * pw 2 B + (-4 * (b : ℚ) ^ 1) * pw 3 B + (1 * (b : ℚ) ^ 0) * pw 4 B + 0 * pw 5 B + 0 * pw 6 B :=
    fun b => sum_poly B (fun c => ((b : ℚ) - c) ^ 4) (1 * (b : ℚ) ^ 4) (-4 * (b : ℚ) ^ 3) (6 * (b : ℚ) ^ 2) (-4 * (b : ℚ) ^ 1) (1 * (b : ℚ) ^ 0) 0 0 (fun c => by ring)
  rw [sum_congr rfl (fun b _ => hin b)]
  rw [sum_poly B _ (1 * pw 4 B) (-4 * pw 3 B) (6 * pw 2 B) (-4 * pw 1 B) (1 * (B.card : ℚ)) 0 0 (fun b => by ring)]
  ring

lemma pairLow (k : ℕ) (hk : Even k) (hk0 : k ≠ 0) (B : Finset ℕ) :
    ∑ b ∈ B, ∑ c ∈ B.filter (· < b), ((b : ℚ) - c) ^ k
      = (∑ b ∈ B, ∑ c ∈ B, ((b : ℚ) - c) ^ k) / 2 := by
  rw [pair_sym k hk hk0 B]; ring

lemma size_pw (B : Finset ℕ) :
    size B = pw 1 B - ((B.card : ℚ) * (B.card - 1) / 2) := by
  rw [size_eq]
  rw [sum_poly (range B.card) (fun i => (B.card : ℚ) - 1 - i) ((B.card : ℚ) - 1) (-1) 0 0 0 0 0
    (fun i => by ring)]
  rw [card_range, pw_range 1 (by norm_num)]
  simp only [P, pw, pow_one]
  ring

/-- **Quadratic hook identity.** For every partition (beta-set `B`),
`∑ h² = ∑ c² + n²`. -/
theorem hook_two (B : Finset ℕ) : hookPow 2 B = contentPow 2 B + size B ^ 2 := by
  rw [hookPow_eq 2 (by norm_num), contentPow_eq 2 (by norm_num), size_pw,
    pairLow 2 even_two two_ne_zero, sumA1_2, sumA2_2, sumA3_2, sumA4_2]
  ring

/-- **Quartic hook identity.** For every partition,
`∑ h⁴ = ∑ c⁴ + 12 n ∑ c² + n² - 12 (∑ c)²`. -/
theorem hook_four (B : Finset ℕ) :
    hookPow 4 B = contentPow 4 B + 12 * size B * contentPow 2 B + size B ^ 2
      - 12 * contentPow 1 B ^ 2 := by
  rw [hookPow_eq 4 (by norm_num), contentPow_eq 4 (by norm_num), contentPow_eq 2 (by norm_num),
    contentPow_eq 1 (by norm_num), size_pw,
    pairLow 4 (by decide) (by norm_num), sumA1_4, sumA2_4, sumA3_4, sumA4_4, sumA3_2, sumA4_2,
    sumA3_1, sumA4_1]
  ring

end QOU.Mass.HookContentBeta
