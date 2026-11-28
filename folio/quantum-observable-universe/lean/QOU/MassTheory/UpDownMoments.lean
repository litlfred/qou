/-
Copyright (c) 2026. Released under CC BY 4.0.
-/
import QOU.MassTheory.DividedDifference
import QOU.MassTheory.HookContentBeta

/-!
# Content moments of added and removed boxes (Jucys–Murphy sums, stage 2)

On a beta-set `B ∋ 0` with `ℓ = |B|` beads (partition `λ ⊢ n`), adding a box at bead `b`
creates content `b - ℓ + 1`, removing one at `b` deletes content `b - ℓ`.

* `up_moments`: the add-box weights `wUp` (stage 1) have moments
  `1, 0, n, 2∑c, n(n+1)/2 + 3∑c²` (Kerov's transition measure, degrees `0..4`);
* `telescope` and `interlace_moments`: `∑_{add} c^m - ∑_{rem} c^m` equals
  `1, 0, 2n, 6∑c, 2n + 12∑c²` for `m = 0..4`;
* `sum_wUp_addable`: the up weights vanish off the addable beads.

The identification of `wUp` with `f^{λ+□}/((n+1) f^λ)` is stage 3, not proved here.
-/

namespace QOU.Mass.UpDownMoments
open Finset QOU.Mass.DividedDifference QOU.Mass.HookContentBeta

/-- The beta-set as rational nodes. -/
def cS (B : Finset ℕ) : Finset ℚ := B.image (Nat.cast : ℕ → ℚ)

lemma cast_inj : Function.Injective (Nat.cast : ℕ → ℚ) := Nat.cast_injective

lemma card_cS (B : Finset ℕ) : (cS B).card = B.card := card_image_of_injective _ cast_inj

lemma q_cS (j : ℕ) (B : Finset ℕ) : q j (cS B) = pw j B := by
  unfold q cS pw; rw [sum_image (fun x _ y _ h => cast_inj h)]

lemma zero_mem_cS {B : Finset ℕ} (h0 : 0 ∈ B) : (0 : ℚ) ∈ cS B :=
  mem_image.mpr ⟨0, h0, by simp⟩

lemma nonneg_cS (B : Finset ℕ) : ∀ s ∈ cS B, (0 : ℚ) ≤ s := by
  intro s hs; obtain ⟨b, _, rfl⟩ := mem_image.mp hs; positivity

lemma q_upNodes (j : ℕ) {B : Finset ℕ} (h0 : 0 ∈ B) :
    q j (upNodes (cS B)) = ∑ b ∈ B, ((b : ℚ) - 1) ^ j - (-1) ^ j := by
  unfold q upNodes
  rw [sum_image (fun x _ y _ h => by simpa using h)]
  have : ∑ c ∈ cS B, (c - 1) ^ j = ∑ b ∈ B, ((b : ℚ) - 1) ^ j := by
    unfold cS; rw [sum_image (fun x _ y _ h => cast_inj h)]
  rw [← this, ← sum_erase_add _ _ (zero_mem_cS h0)]
  simp

lemma dd_sum {ι : Type*} (S : Finset ℚ) (s : Finset ι) (f : ι → ℚ → ℚ) :
    dd S (fun x => ∑ i ∈ s, f i x) = ∑ i ∈ s, dd S (f i) := by
  unfold dd; simp_rw [sum_mul]; rw [sum_comm]

/-- Up moments as a combination of the `G`'s. -/
lemma up_dd (B : Finset ℕ) (h0 : 0 ∈ B) (k : ℕ) (hk : k ≤ 4) :
    ∑ b ∈ B, wUp (cS B) b * ((b : ℚ) - B.card + 1) ^ k
      = ∑ i ∈ range (k + 1), (k.choose i : ℚ) * (1 - (B.card : ℚ)) ^ (k - i)
          * G (cS B) (upNodes (cS B)) i := by
  have hS : (cS B).Nonempty := ⟨0, zero_mem_cS h0⟩
  have e1 : ∑ b ∈ B, wUp (cS B) b * ((b : ℚ) - B.card + 1) ^ k
      = ∑ s ∈ cS B, wUp (cS B) s * (s + (1 - B.card)) ^ k := by
    unfold cS; rw [sum_image (fun x _ y _ h => cast_inj h)]
    exact sum_congr rfl (fun b _ => by ring_nf)
  rw [e1, sum_wUp_mul _ (zero_mem_cS h0) (nonneg_cS B)]
  have e2 : (fun x => (x + (1 - (B.card : ℚ))) ^ k * ∏ r ∈ upNodes (cS B), (x - r))
      = fun x => ∑ i ∈ range (k + 1), (k.choose i : ℚ) * (1 - (B.card : ℚ)) ^ (k - i)
          * (x ^ i * ∏ r ∈ upNodes (cS B), (x - r)) := by
    funext x; rw [add_pow, sum_mul]
    exact sum_congr rfl (fun i _ => by ring)
  rw [e2, dd_sum]
  refine sum_congr rfl (fun i hi => ?_)
  rw [mem_range] at hi
  rw [dd_const_mul]
  congr 1
  have hc : (upNodes (cS B)).card = (cS B).card - 1 := by
    rw [card_upNodes, card_erase_of_mem (zero_mem_cS h0)]
  exact (T_closed (cS B) hS (upNodes (cS B))).2 i (by omega) i (by
    rw [hc]; have := hS.card_pos; omega)

lemma sub_one_pw_1 (B : Finset ℕ) :
    ∑ b ∈ B, ((b : ℚ) - 1) ^ 1 = (-1) * (B.card : ℚ) + (1) * pw 1 B + (0) * pw 2 B + (0) * pw 3 B + (0) * pw 4 B + (0) * pw 5 B + (0) * pw 6 B :=
  sum_poly B (fun b => ((b : ℚ) - 1) ^ 1) (-1) (1) (0) (0) (0) (0) (0) (fun x => by ring)

lemma sub_one_pw_2 (B : Finset ℕ) :
    ∑ b ∈ B, ((b : ℚ) - 1) ^ 2 = (1) * (B.card : ℚ) + (-2) * pw 1 B + (1) * pw 2 B + (0) * pw 3 B + (0) * pw 4 B + (0) * pw 5 B + (0) * pw 6 B :=
  sum_poly B (fun b => ((b : ℚ) - 1) ^ 2) (1) (-2) (1) (0) (0) (0) (0) (fun x => by ring)

lemma sub_one_pw_3 (B : Finset ℕ) :
    ∑ b ∈ B, ((b : ℚ) - 1) ^ 3 = (-1) * (B.card : ℚ) + (3) * pw 1 B + (-3) * pw 2 B + (1) * pw 3 B + (0) * pw 4 B + (0) * pw 5 B + (0) * pw 6 B :=
  sum_poly B (fun b => ((b : ℚ) - 1) ^ 3) (-1) (3) (-3) (1) (0) (0) (0) (fun x => by ring)

lemma sub_one_pw_4 (B : Finset ℕ) :
    ∑ b ∈ B, ((b : ℚ) - 1) ^ 4 = (1) * (B.card : ℚ) + (-4) * pw 1 B + (6) * pw 2 B + (-4) * pw 3 B + (1) * pw 4 B + (0) * pw 5 B + (0) * pw 6 B :=
  sum_poly B (fun b => ((b : ℚ) - 1) ^ 4) (1) (-4) (6) (-4) (1) (0) (0) (fun x => by ring)

lemma upNodes_q (B : Finset ℕ) (h0 : 0 ∈ B) :
    q 1 (upNodes (cS B)) = pw 1 B - B.card + 1 ∧
    q 2 (upNodes (cS B)) = pw 2 B - 2 * pw 1 B + B.card - 1 ∧
    q 3 (upNodes (cS B)) = pw 3 B - 3 * pw 2 B + 3 * pw 1 B - B.card + 1 ∧
    q 4 (upNodes (cS B)) = pw 4 B - 4 * pw 3 B + 6 * pw 2 B - 4 * pw 1 B + B.card - 1 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
  · rw [q_upNodes _ h0]
    first | rw [sub_one_pw_1] | rw [sub_one_pw_2] | rw [sub_one_pw_3] | rw [sub_one_pw_4]
    ring

/-- `∑ λ`-moments of the up (transition) measure, as polynomials in beta power sums. -/
lemma up_moment_pw (B : Finset ℕ) (h0 : 0 ∈ B) (k : ℕ) (hk : k ≤ 4) :
    ∑ b ∈ B, wUp (cS B) b * ((b : ℚ) - B.card + 1) ^ k = match k with
      | 0 => 1
      | 1 => 0
      | 2 => (-(B.card : ℚ) ^ 2 + B.card + 2 * pw 1 B) / 2
      | 3 => -(-2 * (B.card : ℚ) ^ 3 + 3 * B.card ^ 2 + 6 * B.card * pw 1 B - B.card
               - 3 * pw 1 B - 3 * pw 2 B) / 3
      | 4 => (-5 * (B.card : ℚ) ^ 4 + 10 * B.card ^ 3 + 20 * B.card ^ 2 * pw 1 B
               - 7 * B.card ^ 2 - 20 * B.card * pw 1 B - 24 * B.card * pw 2 B + 2 * B.card
               + 4 * pw 1 B ^ 2 + 8 * pw 1 B + 12 * pw 2 B + 8 * pw 3 B) / 8
      | _ => 0 := by
  rw [up_dd B h0 k hk]
  obtain ⟨u1, u2, u3, u4⟩ := upNodes_q B h0
  have c1 := q_cS 1 B; have c2 := q_cS 2 B; have c3 := q_cS 3 B; have c4 := q_cS 4 B
  interval_cases k <;>
    simp only [G, sum_range_succ, sum_range_zero, ec, hc, u1, u2, u3, u4, c1, c2, c3, c4,
      Nat.choose, Nat.reduceAdd, Nat.reduceSub] <;> push_cast <;> ring

lemma C1_pw (B : Finset ℕ) : contentPow 1 B
    = ((B.card : ℚ)^2/2 - (B.card : ℚ)/2) * B.card + (1/2 - (B.card : ℚ)) * pw 1 B
      + (1/2) * pw 2 B - ((B.card : ℚ)^3/6 - (B.card : ℚ)/6) := by
  rw [contentPow_eq 1 (by norm_num), sumA3_1, sumA4_1]; ring

lemma C2_pw (B : Finset ℕ) : contentPow 2 B
    = (∑ b ∈ B, P 2 ((b : ℚ) - B.card + 1)) - ∑ i ∈ range B.card, P 2 (-(i : ℚ)) :=
  contentPow_eq 2 (by norm_num) B

/-- **Up moments in contents.** For a partition with beta-set `B ∋ 0`, the add-box weights
have total mass `1`, mean content `0`, second moment `n`, third `2 ∑ c`, fourth
`n(n+1)/2 + 3 ∑ c²`. -/
theorem up_moments (B : Finset ℕ) (h0 : 0 ∈ B) :
    ∑ b ∈ B, wUp (cS B) b = 1 ∧
    ∑ b ∈ B, wUp (cS B) b * ((b : ℚ) - B.card + 1) = 0 ∧
    ∑ b ∈ B, wUp (cS B) b * ((b : ℚ) - B.card + 1) ^ 2 = size B ∧
    ∑ b ∈ B, wUp (cS B) b * ((b : ℚ) - B.card + 1) ^ 3 = 2 * contentPow 1 B ∧
    ∑ b ∈ B, wUp (cS B) b * ((b : ℚ) - B.card + 1) ^ 4
      = size B ^ 2 / 2 + size B / 2 + 3 * contentPow 2 B := by
  have m0 := up_moment_pw B h0 0 (by norm_num)
  have m1 := up_moment_pw B h0 1 (by norm_num)
  have m2 := up_moment_pw B h0 2 (by norm_num)
  have m3 := up_moment_pw B h0 3 (by norm_num)
  have m4 := up_moment_pw B h0 4 (by norm_num)
  simp only [pow_zero, mul_one, pow_one] at m0 m1
  refine ⟨m0, m1, ?_, ?_, ?_⟩
  · rw [m2, size_pw]; ring
  · rw [m3, C1_pw]; ring
  · rw [m4, size_pw, C2_pw, sumA3_2, sumA4_2]; ring

lemma tel_pw_1 (B : Finset ℕ) :
    ∑ b ∈ B, (((b : ℚ) - B.card + 1) ^ 1 - ((b : ℚ) - B.card) ^ 1) = (1) * (B.card : ℚ) + (0) * pw 1 B + (0) * pw 2 B + (0) * pw 3 B + (0) * pw 4 B + (0) * pw 5 B + (0) * pw 6 B :=
  sum_poly B (fun b => ((b : ℚ) - B.card + 1) ^ 1 - ((b : ℚ) - B.card) ^ 1) (1) (0) (0) (0) (0) (0) (0)
    (fun x => by ring)

lemma tel_pw_2 (B : Finset ℕ) :
    ∑ b ∈ B, (((b : ℚ) - B.card + 1) ^ 2 - ((b : ℚ) - B.card) ^ 2) = (1 - 2*(B.card : ℚ)) * (B.card : ℚ) + (2) * pw 1 B + (0) * pw 2 B + (0) * pw 3 B + (0) * pw 4 B + (0) * pw 5 B + (0) * pw 6 B :=
  sum_poly B (fun b => ((b : ℚ) - B.card + 1) ^ 2 - ((b : ℚ) - B.card) ^ 2) (1 - 2*(B.card : ℚ)) (2) (0) (0) (0) (0) (0)
    (fun x => by ring)

lemma tel_pw_3 (B : Finset ℕ) :
    ∑ b ∈ B, (((b : ℚ) - B.card + 1) ^ 3 - ((b : ℚ) - B.card) ^ 3) = (3*(B.card : ℚ)^2 - 3*(B.card : ℚ) + 1) * (B.card : ℚ) + (-3*(2*(B.card : ℚ) - 1)) * pw 1 B + (3) * pw 2 B + (0) * pw 3 B + (0) * pw 4 B + (0) * pw 5 B + (0) * pw 6 B :=
  sum_poly B (fun b => ((b : ℚ) - B.card + 1) ^ 3 - ((b : ℚ) - B.card) ^ 3) (3*(B.card : ℚ)^2 - 3*(B.card : ℚ) + 1) (-3*(2*(B.card : ℚ) - 1)) (3) (0) (0) (0) (0)
    (fun x => by ring)

lemma tel_pw_4 (B : Finset ℕ) :
    ∑ b ∈ B, (((b : ℚ) - B.card + 1) ^ 4 - ((b : ℚ) - B.card) ^ 4) = (-(2*(B.card : ℚ) - 1)*(2*(B.card : ℚ)^2 - 2*(B.card : ℚ) + 1)) * (B.card : ℚ) + (4*(3*(B.card : ℚ)^2 - 3*(B.card : ℚ) + 1)) * pw 1 B + (-6*(2*(B.card : ℚ) - 1)) * pw 2 B + (4) * pw 3 B + (0) * pw 4 B + (0) * pw 5 B + (0) * pw 6 B :=
  sum_poly B (fun b => ((b : ℚ) - B.card + 1) ^ 4 - ((b : ℚ) - B.card) ^ 4) (-(2*(B.card : ℚ) - 1)*(2*(B.card : ℚ)^2 - 2*(B.card : ℚ) + 1)) (4*(3*(B.card : ℚ)^2 - 3*(B.card : ℚ) + 1)) (-6*(2*(B.card : ℚ) - 1)) (4) (0) (0) (0)
    (fun x => by ring)

/-- Addable beads: `b ∈ B`, `b + 1 ∉ B`. -/
def addable (B : Finset ℕ) : Finset ℕ := B.filter (fun b => b + 1 ∉ B)
/-- Removable beads: `b ∈ B`, `b ≥ 1`, `b - 1 ∉ B`. -/
def removable (B : Finset ℕ) : Finset ℕ := B.filter (fun b => 1 ≤ b ∧ b - 1 ∉ B)

/-- **Interlacing telescope.** With `0 ∈ B`,
`∑_{add} g(c) - ∑_{rem} g(c) = ∑_{b∈B} (g(b-ℓ+1) - g(b-ℓ)) + g(-ℓ)`; the content of the
box added at `b` is `b - ℓ + 1`, of the box removed at `b` is `b - ℓ`. -/
theorem telescope (B : Finset ℕ) (h0 : 0 ∈ B) (g : ℚ → ℚ) :
    ∑ b ∈ addable B, g ((b : ℚ) - B.card + 1) - ∑ b ∈ removable B, g ((b : ℚ) - B.card)
      = ∑ b ∈ B, (g ((b : ℚ) - B.card + 1) - g ((b : ℚ) - B.card)) + g (-(B.card : ℚ)) := by
  set A1 := B.filter (fun b => b + 1 ∈ B)
  set A2 := B.filter (fun b => 1 ≤ b ∧ b - 1 ∈ B)
  have hadd : ∑ b ∈ addable B, g ((b : ℚ) - B.card + 1)
      = ∑ b ∈ B, g ((b : ℚ) - B.card + 1) - ∑ b ∈ A1, g ((b : ℚ) - B.card + 1) := by
    rw [← sum_filter_add_sum_filter_not B (fun b => b + 1 ∈ B)]; unfold addable; ring
  have hnot : B.filter (fun b => ¬(1 ≤ b ∧ b - 1 ∉ B)) = insert 0 A2 := by
    ext b; simp only [mem_filter, mem_insert, A2]
    constructor
    · rintro ⟨hb, hn⟩
      by_cases hb0 : b = 0
      · exact Or.inl hb0
      · right; refine ⟨hb, by omega, ?_⟩; by_contra h; exact hn ⟨by omega, h⟩
    · rintro (rfl | ⟨hb, h1, h2⟩)
      · exact ⟨h0, by omega⟩
      · exact ⟨hb, fun ⟨_, h⟩ => h h2⟩
  have h0A2 : 0 ∉ A2 := by simp [A2]
  have hrem : ∑ b ∈ removable B, g ((b : ℚ) - B.card)
      = ∑ b ∈ B, g ((b : ℚ) - B.card) - g (-(B.card : ℚ)) - ∑ b ∈ A2, g ((b : ℚ) - B.card) := by
    rw [← sum_filter_add_sum_filter_not B (fun b => 1 ≤ b ∧ b - 1 ∉ B), hnot,
      sum_insert h0A2]
    unfold removable; simp only [Nat.cast_zero, zero_sub]; ring
  have hbij : ∑ b ∈ A2, g ((b : ℚ) - B.card) = ∑ b ∈ A1, g ((b : ℚ) - B.card + 1) := by
    symm
    refine sum_nbij' (· + 1) (· - 1) ?_ ?_ ?_ ?_ ?_
    · intro a ha; simp only [A1, A2, mem_filter] at ha ⊢
      exact ⟨ha.2, by omega, by simpa using ha.1⟩
    · intro a ha; simp only [A1, A2, mem_filter] at ha ⊢
      exact ⟨ha.2.2, by rw [Nat.sub_add_cancel ha.2.1]; exact ha.1⟩
    · intro a _; simp
    · intro a ha; simp only [A2, mem_filter] at ha; dsimp only; omega
    · intro a _; push_cast; ring_nf
  rw [hadd, hrem, hbij, sum_sub_distrib]; ring

/-- **Interlacing moments.** `∑_{add} c^m - ∑_{rem} c^m` for `m ≤ 4`. -/
theorem interlace_moments (B : Finset ℕ) (h0 : 0 ∈ B) :
    ((addable B).card : ℚ) - (removable B).card = 1 ∧
    ∑ b ∈ addable B, ((b : ℚ) - B.card + 1) - ∑ b ∈ removable B, ((b : ℚ) - B.card) = 0 ∧
    ∑ b ∈ addable B, ((b : ℚ) - B.card + 1) ^ 2 - ∑ b ∈ removable B, ((b : ℚ) - B.card) ^ 2
      = 2 * size B ∧
    ∑ b ∈ addable B, ((b : ℚ) - B.card + 1) ^ 3 - ∑ b ∈ removable B, ((b : ℚ) - B.card) ^ 3
      = 6 * contentPow 1 B ∧
    ∑ b ∈ addable B, ((b : ℚ) - B.card + 1) ^ 4 - ∑ b ∈ removable B, ((b : ℚ) - B.card) ^ 4
      = 2 * size B + 12 * contentPow 2 B := by
  have t0 := telescope B h0 (fun _ => 1)
  have t1 := telescope B h0 (fun c => c)
  have t2 := telescope B h0 (fun c => c ^ 2)
  have t3 := telescope B h0 (fun c => c ^ 3)
  have t4 := telescope B h0 (fun c => c ^ 4)
  simp only [sum_const, nsmul_eq_mul, mul_one, sub_self, mul_zero, zero_add] at t0
  refine ⟨t0, ?_, ?_, ?_, ?_⟩
  · simp only at t1
    rw [t1]; simp
  · simp only at t2; rw [t2, tel_pw_2, size_pw]; ring
  · simp only at t3; rw [t3, tel_pw_3, C1_pw]; ring
  · simp only at t4; rw [t4, tel_pw_4, size_pw, C2_pw, sumA3_2, sumA4_2]; ring

lemma wUp_eq_zero (S : Finset ℚ) {b : ℚ} (hb : b + 1 ∈ S) : wUp S b = 0 := by
  unfold wUp
  rw [prod_eq_zero (i := b + 1) (mem_erase.mpr ⟨by linarith, hb⟩) (by simp), mul_zero]

lemma wDown_eq_zero (S : Finset ℚ) {b : ℚ} (hb : b - 1 ∈ S) : wDown S b = 0 := by
  unfold wDown
  rw [prod_eq_zero (i := b - 1) (mem_erase.mpr ⟨by linarith, hb⟩) (by simp), mul_zero]

/-- The up weights live on the addable beads. -/
lemma sum_wUp_addable (B : Finset ℕ) (φ : ℚ → ℚ) :
    ∑ b ∈ B, wUp (cS B) b * φ b = ∑ b ∈ addable B, wUp (cS B) b * φ b := by
  unfold addable
  rw [← sum_filter_add_sum_filter_not B (fun b => b + 1 ∉ B), add_eq_left]
  refine sum_eq_zero (fun b hb => ?_)
  rw [mem_filter, not_not] at hb
  have : ((b : ℚ) + 1) ∈ cS B := mem_image.mpr ⟨b + 1, hb.2, by push_cast; rfl⟩
  rw [wUp_eq_zero _ this, zero_mul]

end QOU.Mass.UpDownMoments
