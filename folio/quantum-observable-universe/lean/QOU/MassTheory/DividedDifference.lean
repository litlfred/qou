/-
Copyright (c) 2026. Released under CC BY 4.0.

# Divided differences and the up/down branching identities on beta-sets

Stage 1 of the Jucys–Murphy class sums used by
`prop:habiro-tail-cyclotomic-iff-n-le-5` (the content-moment route of
Kerov / Okounkov–Vershik, done here by divided differences).

A partition with `ℓ` parts (zeros allowed) is a beta-set `S` of `ℓ` distinct
naturals.  Adding a box moves a bead `b ↦ b + 1`, removing one moves `b ↦ b - 1`.
The weights `wUp S b` and `wDown S b` below are the Vandermonde ratios of these
moves; the link to `f^λ = n! / ∏ hooks` is Stage 3 and is NOT proved here.

Proved here, sorry-free:
* `dd_insert`  : Newton's recursion for divided differences (via Lagrange partial fractions);
* `dd_pow`     : `dd_S (x^i) = 0` for `i < |S| - 1`, `= h_j(S)` at `i = |S| - 1 + j`, `j ≤ 4`;
* `T_closed`   : `dd_S (x^i ∏_{r∈R}(x - r))` in elementary/complete symmetric functions;
* `up_branch`  : `∑_b wUp S b = 1` when bead `0 ∈ S`;
* `down_branch`: `∑_b wDown S b = ∑ S - ℓ(ℓ-1)/2 = |λ|`.
-/
import Mathlib.LinearAlgebra.Lagrange
import Mathlib.Tactic

namespace QOU.Mass.DividedDifference
open Finset Polynomial

/-- Divided difference of `g` on the node set `S`. -/
noncomputable def dd (S : Finset ℚ) (g : ℚ → ℚ) : ℚ :=
  ∑ s ∈ S, g s * (∏ t ∈ S.erase s, (s - t))⁻¹

lemma dd_congr (S : Finset ℚ) {g g' : ℚ → ℚ} (h : ∀ s ∈ S, g s = g' s) : dd S g = dd S g' := by
  unfold dd; exact sum_congr rfl (fun s hs => by rw [h s hs])

lemma dd_singleton (a : ℚ) (g : ℚ → ℚ) : dd {a} g = g a := by simp [dd]

/-- Partial fractions: `∑_s 1/((a - s) ∏_{t ≠ s} (s - t)) = 1/∏_t (a - t)`. -/
lemma partial_fraction (S : Finset ℚ) (hS : S.Nonempty) {a : ℚ} (ha : a ∉ S) :
    ∑ s ∈ S, (∏ t ∈ S.erase s, (s - t))⁻¹ * (a - s)⁻¹ = (∏ t ∈ S, (a - t))⁻¹ := by
  have hx : ∀ i ∈ S, a ≠ id i := fun i hi h => ha (h ▸ hi)
  have key := Lagrange.eval_interpolate_not_at_node (s := S) (v := id) (r := 1) hx
  rw [Lagrange.interpolate_one (Set.injOn_id _) hS, eval_one, Lagrange.eval_nodal] at key
  have hne : (∏ t ∈ S, (a - t)) ≠ 0 :=
    prod_ne_zero_iff.mpr (fun t ht => sub_ne_zero.mpr (fun h => ha (h ▸ ht)))
  have e : ∑ s ∈ S, (∏ t ∈ S.erase s, (s - t))⁻¹ * (a - s)⁻¹
      = ∑ i ∈ S, Lagrange.nodalWeight S id i * (a - id i)⁻¹ * (1 : ℚ → ℚ) i := by
    refine sum_congr rfl (fun s _ => ?_)
    simp [Lagrange.nodalWeight, prod_inv_distrib]
  rw [e]
  simp only [id] at key ⊢
  exact eq_inv_of_mul_eq_one_right key.symm

/-- Newton's recursion. -/
lemma dd_insert (S : Finset ℚ) (hS : S.Nonempty) {a : ℚ} (ha : a ∉ S) (g : ℚ → ℚ) :
    dd (insert a S) g = dd S (fun x => (g x - g a) / (x - a)) := by
  have pf := partial_fraction S hS ha
  unfold dd
  rw [sum_insert ha, erase_insert ha]
  have hrest : ∀ s ∈ S, g s * (∏ t ∈ (insert a S).erase s, (s - t))⁻¹
      = g s * (∏ t ∈ S.erase s, (s - t))⁻¹ * (s - a)⁻¹ := by
    intro s hs
    have hsa : s ≠ a := fun h => ha (h ▸ hs)
    rw [erase_insert_of_ne (Ne.symm hsa), prod_insert (fun h => ha (mem_of_mem_erase h)),
      mul_inv]; ring
  rw [sum_congr rfl hrest]
  have hsub : ∀ s ∈ S, (g s - g a) / (s - a) * (∏ t ∈ S.erase s, (s - t))⁻¹
      = g s * (∏ t ∈ S.erase s, (s - t))⁻¹ * (s - a)⁻¹
        + g a * ((∏ t ∈ S.erase s, (s - t))⁻¹ * (a - s)⁻¹) := by
    intro s hs
    have hsa : s - a ≠ 0 := sub_ne_zero.mpr (fun h => ha (h ▸ hs))
    have has : a - s ≠ 0 := sub_ne_zero.mpr (fun h => ha (h.symm ▸ hs))
    have : (a - s)⁻¹ = -(s - a)⁻¹ := by rw [← neg_sub, inv_neg]
    rw [this]; field_simp; ring
  rw [sum_congr rfl hsub, sum_add_distrib, ← mul_sum, pf]
  ring

lemma dd_lin (S : Finset ℚ) (m : ℕ) (c : ℕ → ℚ) :
    dd S (fun x => ∑ i ∈ range m, c i * x ^ i) = ∑ i ∈ range m, c i * dd S (fun x => x ^ i) := by
  unfold dd; simp_rw [sum_mul, mul_sum]; rw [sum_comm]
  exact sum_congr rfl (fun _ _ => sum_congr rfl (fun _ _ => by ring))

lemma dd_insert_pow (S : Finset ℚ) (hS : S.Nonempty) {a : ℚ} (ha : a ∉ S) (m : ℕ) :
    dd (insert a S) (fun x => x ^ m)
      = ∑ i ∈ range m, a ^ (m - 1 - i) * dd S (fun x => x ^ i) := by
  rw [dd_insert S hS ha, ← dd_lin]
  apply dd_congr
  intro s hs
  have hsa : s - a ≠ 0 := sub_ne_zero.mpr (fun h => ha (h ▸ hs))
  rw [div_eq_iff hsa, ← geom_sum₂_mul]
  congr 1; exact sum_congr rfl (fun i _ => by ring)

/-- Power sums of the nodes. -/
def q (j : ℕ) (S : Finset ℚ) : ℚ := ∑ s ∈ S, s ^ j

/-- Complete homogeneous symmetric polynomials `h_0, …, h_4` through power sums. -/
def hc (S : Finset ℚ) : ℕ → ℚ
  | 0 => 1
  | 1 => q 1 S
  | 2 => (q 1 S ^ 2 + q 2 S) / 2
  | 3 => (q 1 S ^ 3 + 3 * q 1 S * q 2 S + 2 * q 3 S) / 6
  | 4 => (q 1 S ^ 4 + 6 * q 1 S ^ 2 * q 2 S + 3 * q 2 S ^ 2 + 8 * q 1 S * q 3 S
      + 6 * q 4 S) / 24
  | _ => 0

lemma q_insert {a : ℚ} {S : Finset ℚ} (ha : a ∉ S) (j : ℕ) : q j (insert a S) = a ^ j + q j S := by
  simp [q, sum_insert ha]

/-- `dd S (x^i) = 0` below `|S| - 1`, and `dd S (x^(|S|-1+j)) = h_j(S)` for `j ≤ 4`. -/
theorem dd_pow (S : Finset ℚ) (hS : S.Nonempty) :
    (∀ i, i + 1 < S.card → dd S (fun x => x ^ i) = 0) ∧
    (∀ j ≤ 4, dd S (fun x => x ^ (S.card - 1 + j)) = hc S j) := by
  induction hS using Finset.Nonempty.cons_induction with
  | singleton a =>
    refine ⟨fun i hi => by simp at hi, fun j hj => ?_⟩
    rw [dd_singleton]
    interval_cases j <;> simp [hc, q] <;> ring
  | cons a S ha hS ih =>
    obtain ⟨ih0, ih1⟩ := ih
    rw [cons_eq_insert, card_insert_of_notMem ha]
    have hk : 1 ≤ S.card := hS.card_pos
    refine ⟨fun i hi => ?_, fun j hj => ?_⟩
    · rw [dd_insert_pow S hS ha]
      exact sum_eq_zero (fun i' hi' => by
        rw [mem_range] at hi'; rw [ih0 i' (by omega), mul_zero])
    · rw [dd_insert_pow S hS ha]
      have hsplit : S.card + 1 - 1 + j = (S.card - 1) + (j + 1) := by omega
      rw [hsplit, sum_range_add]
      rw [sum_eq_zero (fun i' hi' => by rw [mem_range] at hi'; rw [ih0 i' (by omega), mul_zero]),
        zero_add]
      have h' : ∀ t ∈ range (j + 1), a ^ (S.card - 1 + (j + 1) - 1 - (S.card - 1 + t))
          * dd S (fun x => x ^ (S.card - 1 + t)) = a ^ (j - t) * hc S t := by
        intro t ht; rw [mem_range] at ht
        rw [ih1 t (by omega)]; congr 2; omega
      rw [sum_congr rfl h']
      interval_cases j <;> simp [sum_range_succ, hc, q_insert ha] <;> ring



lemma dd_sub (S : Finset ℚ) (f g : ℚ → ℚ) : dd S (fun x => f x - g x) = dd S f - dd S g := by
  unfold dd; rw [← sum_sub_distrib]; exact sum_congr rfl (fun _ _ => by ring)

lemma dd_const_mul (S : Finset ℚ) (c : ℚ) (f : ℚ → ℚ) : dd S (fun x => c * f x) = c * dd S f := by
  unfold dd; rw [mul_sum]; exact sum_congr rfl (fun _ _ => by ring)

/-- Elementary symmetric polynomials `e_0, …, e_4` through power sums. -/
def ec (R : Finset ℚ) : ℕ → ℚ
  | 0 => 1
  | 1 => q 1 R
  | 2 => (q 1 R ^ 2 - q 2 R) / 2
  | 3 => (q 1 R ^ 3 - 3 * q 1 R * q 2 R + 2 * q 3 R) / 6
  | 4 => (q 1 R ^ 4 - 6 * q 1 R ^ 2 * q 2 R + 3 * q 2 R ^ 2 + 8 * q 1 R * q 3 R
      - 6 * q 4 R) / 24
  | _ => 0

/-- `T S R i = dd_S (x^i ∏_{r∈R} (x - r))`. -/
noncomputable def T (S R : Finset ℚ) (i : ℕ) : ℚ := dd S (fun x => x ^ i * ∏ r ∈ R, (x - r))

lemma T_insert (S R : Finset ℚ) {r : ℚ} (hr : r ∉ R) (i : ℕ) :
    T S (insert r R) i = T S R (i + 1) - r * T S R i := by
  unfold T
  rw [← dd_const_mul, ← dd_sub]
  apply dd_congr; intro x _
  rw [prod_insert hr]; ring

/-- The value of `T` at excess degree `d ≤ 4`. -/
def G (S R : Finset ℚ) (d : ℕ) : ℚ := ∑ j ∈ range (d + 1), (-1) ^ j * ec R j * hc S (d - j)

theorem T_closed (S : Finset ℚ) (hS : S.Nonempty) (R : Finset ℚ) :
    (∀ i, i + R.card + 1 < S.card → T S R i = 0) ∧
    (∀ d ≤ 4, ∀ i, i + R.card = S.card - 1 + d → T S R i = G S R d) := by
  induction R using Finset.induction_on with
  | empty =>
    obtain ⟨h0, h1⟩ := dd_pow S hS
    refine ⟨fun i hi => ?_, fun d hd i hi => ?_⟩
    · simp only [T, prod_empty, mul_one]; exact h0 i (by simpa using hi)
    · simp only [T, prod_empty, mul_one]
      simp only [card_empty, add_zero] at hi
      rw [hi, h1 d hd]
      interval_cases d <;> simp [G, sum_range_succ, ec, q]
  | insert r R hr ih =>
    obtain ⟨ih0, ih1⟩ := ih
    rw [card_insert_of_notMem hr]
    refine ⟨fun i hi => ?_, fun d hd i hi => ?_⟩
    · rw [T_insert S R hr, ih0 (i + 1) (by omega), ih0 i (by omega), mul_zero, sub_zero]
    · rw [T_insert S R hr, ih1 d hd (i + 1) (by omega)]
      have hq : ∀ j, q j (insert r R) = r ^ j + q j R := fun j => q_insert hr j
      rcases Nat.eq_zero_or_pos d with rfl | hdpos
      · rw [ih0 i (by have := hS.card_pos; omega)]
        simp [G, ec]
      · rw [ih1 (d - 1) (by omega) i (by omega)]
        obtain ⟨d', rfl⟩ : ∃ d', d = d' + 1 := ⟨d - 1, by omega⟩
        simp only [Nat.add_sub_cancel]
        have hd3 : d' ≤ 3 := by omega
        interval_cases d' <;> simp [G, sum_range_succ, ec, hq] <;> ring

/-! ### Branching weights on a beta-set -/

/-- Weight of adding a box at bead `b` (ratio `w(B ∖ b ∪ (b+1)) / w(B)`). -/
noncomputable def wUp (S : Finset ℚ) (b : ℚ) : ℚ :=
  (b + 1)⁻¹ * ∏ c ∈ S.erase b, ((b + 1 - c) / (b - c))

/-- Weight of removing a box at bead `b` (ratio `n · w(B ∖ b ∪ (b-1)) / w(B)`). -/
noncomputable def wDown (S : Finset ℚ) (b : ℚ) : ℚ :=
  b * ∏ c ∈ S.erase b, ((b - 1 - c) / (b - c))

/-- Up-nodes: `R = {c - 1 : c ∈ S, c ≠ 0}`. -/
def upNodes (S : Finset ℚ) : Finset ℚ := (S.erase 0).image (fun c => c - 1)

/-- Down-nodes: `R = {c + 1 : c ∈ S}`. -/
def downNodes (S : Finset ℚ) : Finset ℚ := S.image (fun c => c + 1)

lemma card_upNodes (S : Finset ℚ) : (upNodes S).card = (S.erase 0).card :=
  card_image_of_injective _ (fun a b h => by simpa using h)

lemma card_downNodes (S : Finset ℚ) : (downNodes S).card = S.card :=
  card_image_of_injective _ (fun a b h => by simpa using h)

lemma wUp_eq (S : Finset ℚ) (h0 : (0 : ℚ) ∈ S) (hpos : ∀ s ∈ S, 0 ≤ s) {b : ℚ} (hb : b ∈ S) :
    wUp S b = (∏ r ∈ upNodes S, (b - r)) * (∏ c ∈ S.erase b, (b - c))⁻¹ := by
  unfold wUp upNodes
  rw [prod_image (fun x _ y _ h => by simpa using h), prod_div_distrib, div_eq_mul_inv, ← mul_assoc]
  congr 1
  have hb1 : b + 1 ≠ 0 := by have := hpos b hb; positivity
  by_cases hb0 : b = 0
  · subst hb0; simp only [zero_add, inv_one, one_mul]
    exact prod_congr rfl (fun c _ => by ring)
  · have e1 : S.erase b = insert 0 ((S.erase b).erase 0) :=
      (insert_erase (mem_erase.mpr ⟨fun h => hb0 h.symm, h0⟩)).symm
    have e2 : S.erase 0 = insert b ((S.erase 0).erase b) :=
      (insert_erase (mem_erase.mpr ⟨hb0, hb⟩)).symm
    rw [e1, e2, prod_insert (notMem_erase _ _), prod_insert (notMem_erase _ _),
      erase_right_comm]
    field_simp
    ring_nf

lemma wDown_eq (S : Finset ℚ) {b : ℚ} (hb : b ∈ S) :
    wDown S b = -(b * ∏ r ∈ downNodes S, (b - r)) * (∏ c ∈ S.erase b, (b - c))⁻¹ := by
  unfold wDown downNodes
  rw [prod_image (fun x _ y _ h => by simpa using h), prod_div_distrib, div_eq_mul_inv]
  rw [← insert_erase hb, prod_insert (notMem_erase _ _), erase_insert (notMem_erase _ _)]
  ring_nf

/-- Up moments are divided differences. -/
lemma sum_wUp_mul (S : Finset ℚ) (h0 : (0 : ℚ) ∈ S) (hpos : ∀ s ∈ S, 0 ≤ s) (φ : ℚ → ℚ) :
    ∑ b ∈ S, wUp S b * φ b = dd S (fun x => φ x * ∏ r ∈ upNodes S, (x - r)) := by
  unfold dd; exact sum_congr rfl (fun b hb => by rw [wUp_eq S h0 hpos hb]; ring)

lemma sum_wDown_mul (S : Finset ℚ) (φ : ℚ → ℚ) :
    ∑ b ∈ S, wDown S b * φ b = dd S (fun x => -(φ x * x * ∏ r ∈ downNodes S, (x - r))) := by
  unfold dd; exact sum_congr rfl (fun b hb => by rw [wDown_eq S hb]; ring)

lemma q_downNodes (S : Finset ℚ) (j : ℕ) :
    q j (downNodes S) = ∑ c ∈ S, (c + 1) ^ j := by
  unfold q downNodes; rw [sum_image (fun x _ y _ h => by simpa using h)]

/-- The up-branching identity: `∑_b wUp = 1` (needs bead `0` present). -/
theorem up_branch (S : Finset ℚ) (h0 : (0 : ℚ) ∈ S) (hpos : ∀ s ∈ S, 0 ≤ s) :
    ∑ b ∈ S, wUp S b = 1 := by
  have hS : S.Nonempty := ⟨0, h0⟩
  have := sum_wUp_mul S h0 hpos (fun _ => 1)
  simp only [mul_one, one_mul] at this
  rw [this]
  have hT := (T_closed S hS (upNodes S)).2 0 (by norm_num) 0
    (by rw [card_upNodes, card_erase_of_mem h0]; omega)
  simpa [T, G, ec, hc] using hT

/-- The down-branching identity: `∑_b wDown = |λ|`, with `|λ| = ∑ b - ℓ(ℓ-1)/2`. -/
theorem down_branch (S : Finset ℚ) (hS : S.Nonempty) :
    ∑ b ∈ S, wDown S b = q 1 S - (S.card : ℚ) * (S.card - 1) / 2 := by
  have := sum_wDown_mul S (fun _ => 1)
  simp only [mul_one, one_mul] at this
  rw [this]
  have hneg : dd S (fun x => -(x * ∏ r ∈ downNodes S, (x - r)))
      = -T S (downNodes S) 1 := by
    rw [T, show -dd S (fun x => x ^ 1 * ∏ r ∈ downNodes S, (x - r))
        = (-1) * dd S (fun x => x ^ 1 * ∏ r ∈ downNodes S, (x - r)) by ring, ← dd_const_mul]
    exact dd_congr S (fun x _ => by ring)
  rw [hneg, (T_closed S hS (downNodes S)).2 2 (by norm_num) 1
    (by rw [card_downNodes]; have := hS.card_pos; omega)]
  have h1 : q 1 (downNodes S) = q 1 S + S.card := by
    rw [q_downNodes]; simp [q, sum_add_distrib]
  have h2 : q 2 (downNodes S) = q 2 S + 2 * q 1 S + S.card := by
    rw [q_downNodes]; simp only [q]
    rw [show (∑ c ∈ S, (c + 1) ^ 2) = ∑ c ∈ S, (c ^ 2 + 2 * c ^ 1 + 1) from
      sum_congr rfl (fun c _ => by ring)]
    simp [sum_add_distrib, mul_sum]
  simp only [G, sum_range_succ, ec, hc, h1, h2]
  norm_num
  ring

end QOU.Mass.DividedDifference
