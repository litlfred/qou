import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import QOU.BraidKnot.HardWallProjection
import QOU.BraidKnot.RoundedWaterfillExchange

/-!
# Assembling the two-sided `O(1)` excess bracket `M_n = A√(2n) + O(1)`

Bean `qou-fxym` (parent epic `qou-3e6w`).  `HardWallProjection.lean`,
`RoundedWaterfillExchange.lean`, and `StaircaseRowDeletedHook.lean` proved the individual
order-theoretic and combinatorial engines of the sharp-coefficient bound.  This module formalises
the four remaining assembly steps recorded in `qou-fxym`:

1. **Tangent-line pair bound (`pair_sum_ge_of_tangent`, `even_tail_le_weighted_sum`,
   `oneBody_sub_pair_le_of_tangent`).**  When each pair term at row distance `k` obeys the tangent
   inequality `ε(2k) − slope_k · (t_i − t_{i+k}) ≤ pairTerm k i` and each one-body term is bounded
   by `C = A + Σ_{k≥1} ε(2k)`, the difference `(Σ_i oneBody_i) − (Σ_{k,i} pairTerm_{k,i})` is at
   most `L · A + Σ_k k · ε(2k) + Σ_k slope_k · Δ_k(t)`, because `L · ε(2k) − (L − k) · ε(2k) =
   k · ε(2k)` for `k < L` and `L · ε(2k) ≤ k · ε(2k)` in the tail `k ≥ L`.
2. **Telescoping middle cancellation of `Δ_k(d)` (`sum_shiftDiff_eq_Ico`,
   `sum_shiftDiff_eq_head_sub_tail`, `abs_sum_shiftDiff_le`).**  For `k ≤ L`, the order-`k`
   shift-difference sum `Δ_k(d) = Σ_{i < L−k} (d_i − d_{i+k})` telescopes to the sum of the first
   `m_k = min(k, L − k)` coordinates minus the last `m_k` coordinates, so the middle cancels and
   `|Δ_k(d)|` is bounded by the head-plus-tail `ℓ¹` sum.
3. **Explicit rounded water-fill `q_i = max(w_i, c_i)` admissibility
   (`roundedWaterfill_monotone`, `shiftDiff_roundedWaterfill_nonpos`,
   `roundedWaterfill_ge_floor`, `roundedWaterfill_le_of_lt`, `roundedWaterfill_pythagoras`).**
   When the wall `w` and the rounded flat profile `c` (taking values in `[a, a+1]`) are monotone,
   `q = max(w, c)` is monotone (`Δ_k(q) ≤ 0`) and automatically satisfies the two hypotheses of
   `RoundedWaterfillExchange.rounded_pythagoras` for every `t ≥ w`.
4. **Hook-sum / `ε`-valued two-sided `O(1)` excess assembly (`coord_tradeoff_sum_le`,
   `rev_upper_bound_assembly`, `rev_lower_bound_assembly`, `rev_two_sided_excess_bracket`).**
   Composes `int_tradeoff` across coordinates and `extra_rows_tradeoff` on extra rows to obtain
   `Ψ ≤ A√(2n) + K₂`, composes the row-deleted staircase hook-sum lower bound (`rowDeleted_hookSum_ge`
   with `rem ≥ 0` and `F(n) ≤ C`) to obtain `Ψ(λ_{k,r}) ≥ A√(2n) − K₃`, and joins both halves into
   the two-sided bracket `−K₃ ≤ M_n − A√(2n) ≤ K₂`.

All statements are over a generic ordered commutative ring / field (§7c).

-- Ref: [leitner2026] computations/deltalambda/rev_bounded_excess_upper_bound_probe.py
-- Ref: [leitner2026] computations/deltalambda/rev_bounded_excess_lower_bound_probe.py
-/

namespace QOU.BraidKnot.RevBoundedExcessAssembly

open Finset QOU.BraidKnot.HardWallProjection QOU.BraidKnot.RoundedWaterfillExchange

variable {ι R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-! ## Step (a): Tangent-line pair bound and the `S₂` tail inequality -/

/-- **Tangent-line lower bound on the pair sum.**  If every pair at neighbour order `k ∈ [1, L)`
and row `i < L − k` satisfies `epsEven k - slope k * (t i - t (i + k)) ≤ pairTerm k i`, then
summing over pairs gives `(L − k) · epsEven k − slope k · Δ_k(t)` at each order `k`. -/
theorem pair_sum_ge_of_tangent (L : ℕ) (epsEven slope t : ℕ → R) (pairTerm : ℕ → ℕ → R)
    (htang : ∀ k ∈ Ico 1 L, ∀ i ∈ range (L - k),
      epsEven k - slope k * (t i - t (i + k)) ≤ pairTerm k i) :
    ∑ k ∈ Ico 1 L,
      (((L : R) - (k : R)) * epsEven k - slope k * ∑ i ∈ range (L - k), (t i - t (i + k)))
      ≤ ∑ k ∈ Ico 1 L, ∑ i ∈ range (L - k), pairTerm k i := by
  refine sum_le_sum fun k hk => ?_
  have hkL : k ≤ L := (mem_Ico.mp hk).2.le
  have hcard : ((L - k : ℕ) : R) = (L : R) - (k : R) := Nat.cast_sub hkL
  have hrow := sum_le_sum (htang k hk)
  rw [sum_sub_distrib, sum_const, card_range, nsmul_eq_mul, hcard, ← mul_sum] at hrow
  exact hrow

/-- **Why `L · E₂ − Σ_{k<L} (L − k) ε(2k) ≤ S₂`.**  For `1 ≤ k < L` the coefficient of `ε(2k)` is
`L − (L − k) = k`, and in the tail `L ≤ k < N` we have `L · ε(2k) ≤ k · ε(2k)` since `ε(2k) ≥ 0`. -/
theorem even_tail_le_weighted_sum {L N : ℕ} (hLN : L ≤ N) (epsEven : ℕ → R)
    (heps : ∀ k ∈ Ico 1 N, 0 ≤ epsEven k) :
    (L : R) * (∑ k ∈ Ico 1 N, epsEven k)
      - ∑ k ∈ Ico 1 L, ((L : R) - (k : R)) * epsEven k
      ≤ ∑ k ∈ Ico 1 N, (k : R) * epsEven k := by
  obtain ⟨m, rfl⟩ := Nat.exists_eq_add_of_le hLN
  induction m with
  | zero =>
    simp only [Nat.add_zero]
    rw [mul_sum, ← sum_sub_distrib]
    refine le_of_eq (sum_congr rfl fun k _ => ?_)
    ring
  | succ m ih =>
    have heps' : ∀ k ∈ Ico 1 (L + m), 0 ≤ epsEven k := fun k hk => by
      have hk' := mem_Ico.mp hk
      exact heps k (mem_Ico.mpr ⟨hk'.1, by omega⟩)
    have hprev := ih (Nat.le_add_right L m) heps'
    rcases Nat.eq_zero_or_pos (L + m) with h0 | hpos
    · have hL0 : L = 0 := by omega
      have hm0 : m = 0 := by omega
      subst hL0; subst hm0
      simp
    · have htop1 := sum_Ico_succ_top (by omega : 1 ≤ L + m) epsEven
      have htop2 := sum_Ico_succ_top (by omega : 1 ≤ L + m) (fun k => (k : R) * epsEven k)
      have hnonneg : 0 ≤ epsEven (L + m) := heps (L + m) (mem_Ico.mpr ⟨by omega, by omega⟩)
      have hle : (L : R) ≤ ((L + m : ℕ) : R) := by exact_mod_cast Nat.le_add_right L m
      have hterm : (L : R) * epsEven (L + m) ≤ ((L + m : ℕ) : R) * epsEven (L + m) :=
        mul_le_mul_of_nonneg_right hle hnonneg
      rw [← Nat.add_assoc L m 1, htop1, htop2, mul_add]
      linarith

/-- **One-body minus pair sum upper bound.**  Combining `pair_sum_ge_of_tangent` and
`even_tail_le_weighted_sum` with the one-body ceiling `oneBody i ≤ A + E₂` yields
`Σ_i oneBody_i − Σ_{k,i} pairTerm_{k,i} ≤ L · A + S₂ + Σ_k slope_k · Δ_k(t)`. -/
theorem oneBody_sub_pair_le_of_tangent {L N : ℕ} (hLN : L ≤ N)
    (A : R) (oneBody epsEven slope t : ℕ → R) (pairTerm : ℕ → ℕ → R)
    (hone : ∀ i ∈ range L, oneBody i ≤ A + ∑ k ∈ Ico 1 N, epsEven k)
    (heps : ∀ k ∈ Ico 1 N, 0 ≤ epsEven k)
    (htang : ∀ k ∈ Ico 1 L, ∀ i ∈ range (L - k),
      epsEven k - slope k * (t i - t (i + k)) ≤ pairTerm k i) :
    (∑ i ∈ range L, oneBody i) - (∑ k ∈ Ico 1 L, ∑ i ∈ range (L - k), pairTerm k i)
      ≤ (L : R) * A + (∑ k ∈ Ico 1 N, (k : R) * epsEven k)
        + ∑ k ∈ Ico 1 L, slope k * ∑ i ∈ range (L - k), (t i - t (i + k)) := by
  have hob : ∑ i ∈ range L, oneBody i ≤ (L : R) * A + (L : R) * ∑ k ∈ Ico 1 N, epsEven k := by
    have h := sum_le_sum hone
    rw [sum_const, card_range, nsmul_eq_mul, mul_add] at h
    exact h
  have hpair := pair_sum_ge_of_tangent L epsEven slope t pairTerm htang
  rw [sum_sub_distrib] at hpair
  have htail := even_tail_le_weighted_sum hLN epsEven heps
  linarith

/-! ## Step (b): Telescoping middle cancellation of `Δ_k(d)` -/

/-- Reindexing the shifted sum: `Σ_{i < m} (d_i − d_{i+k}) = Σ_{i < m} d_i − Σ_{k ≤ i < m+k} d_i`. -/
theorem sum_shiftDiff_eq_Ico (m k : ℕ) (d : ℕ → R) :
    ∑ i ∈ range m, (d i - d (i + k)) = (∑ i ∈ range m, d i) - (∑ i ∈ Ico k (m + k), d i) := by
  induction m with
  | zero => simp
  | succ m ih =>
    have htop : m + 1 + k = m + k + 1 := by omega
    rw [sum_range_succ, sum_range_succ, htop, sum_Ico_succ_top (Nat.le_add_left k m)]
    linarith

/-- **Middle cancellation of `Δ_k(d)`.**  For `k ≤ L`, the neighbour-order-`k` difference sum
`Σ_{i < L−k} (d_i − d_{i+k})` telescopes to the sum of the first `m_k = min(k, L − k)` coordinates
minus the last `m_k` coordinates; the overlap `Ico k (L − k)` cancels when `2k ≤ L`. -/
theorem sum_shiftDiff_eq_head_sub_tail {L k : ℕ} (hk : k ≤ L) (d : ℕ → R) :
    ∑ i ∈ range (L - k), (d i - d (i + k))
      = (∑ i ∈ range (min k (L - k)), d i) - (∑ i ∈ Ico (L - min k (L - k)) L, d i) := by
  rw [sum_shiftDiff_eq_Ico (L - k) k d, Nat.sub_add_cancel hk]
  rcases le_total k (L - k) with h | h
  · rw [min_eq_left h]
    have h1 : ∑ i ∈ range (L - k), d i = (∑ i ∈ range k, d i) + (∑ i ∈ Ico k (L - k), d i) := by
      simpa only [Nat.Ico_zero_eq_range] using
        (sum_Ico_consecutive d (Nat.zero_le k) h).symm
    have h2 : ∑ i ∈ Ico k L, d i = (∑ i ∈ Ico k (L - k), d i) + (∑ i ∈ Ico (L - k) L, d i) :=
      (sum_Ico_consecutive d h (Nat.sub_le L k)).symm
    linarith
  · rw [min_eq_right h, Nat.sub_sub_self hk]

/-- **Absolute-value bound on `Δ_k(d)` via head and tail.**  Because the middle cancels,
`|Δ_k(d)|` is at most the `ℓ¹` sum of `d` over the first `min(k, L − k)` and last `min(k, L − k)`
coordinates. -/
theorem abs_sum_shiftDiff_le {L k : ℕ} (hk : k ≤ L) (d : ℕ → R) :
    |∑ i ∈ range (L - k), (d i - d (i + k))|
      ≤ (∑ i ∈ range (min k (L - k)), |d i|) + (∑ i ∈ Ico (L - min k (L - k)) L, |d i|) := by
  rw [sum_shiftDiff_eq_head_sub_tail hk d]
  have h1 := abs_sub (∑ i ∈ range (min k (L - k)), d i) (∑ i ∈ Ico (L - min k (L - k)) L, d i)
  have h2 := abs_sum_le_sum_abs d (range (min k (L - k)))
  have h3 := abs_sum_le_sum_abs d (Ico (L - min k (L - k)) L)
  linarith

/-! ## Step (c): Explicit rounded water-fill `q_i = max(w_i, c_i)` admissibility -/

/-- The explicit rounded water-fill profile `q_i = max(w_i, c_i)` built from a wall `w` and a
rounded flat profile `c`. -/
def roundedWaterfill (w c : ι → R) (i : ι) : R := max (w i) (c i)

omit [CommRing R] [IsStrictOrderedRing R] in
/-- If both the wall `w` and the rounded flat profile `c` are monotone, then
`roundedWaterfill w c` is monotone. -/
theorem roundedWaterfill_monotone {w c : ℕ → R} (hw : Monotone w) (hc : Monotone c) :
    Monotone (roundedWaterfill w c) :=
  fun _ _ hij => max_le_max (hw hij) (hc hij)

/-- Monotonicity of `roundedWaterfill w c` ensures `Δ_k(q) ≤ 0` for every neighbour order `k`. -/
theorem shiftDiff_roundedWaterfill_nonpos {w c : ℕ → R} (hw : Monotone w) (hc : Monotone c)
    (m k : ℕ) :
    ∑ i ∈ range m, (roundedWaterfill w c i - roundedWaterfill w c (i + k)) ≤ 0 :=
  shiftDiff_nonpos_of_monotone (roundedWaterfill w c) (roundedWaterfill_monotone hw hc) m k

/-- Consequently `Δ_k(t) ≤ Δ_k(t − q)` against the rounded water-fill `q = max(w, c)`. -/
theorem shiftDiff_le_of_roundedWaterfill (t w c : ℕ → R) (hw : Monotone w) (hc : Monotone c)
    (m k : ℕ) :
    ∑ i ∈ range m, (t i - t (i + k)) ≤
      ∑ i ∈ range m,
        ((t i - roundedWaterfill w c i) - (t (i + k) - roundedWaterfill w c (i + k))) :=
  shiftDiff_le_of_reference t (roundedWaterfill w c) (roundedWaterfill_monotone hw hc) m k

omit [CommRing R] [IsStrictOrderedRing R] in
/-- First hypothesis of `rounded_pythagoras`: `a ≤ c_i` implies `a ≤ max(w_i, c_i)`. -/
theorem roundedWaterfill_ge_floor (s : Finset ι) (w c : ι → R) (a : R)
    (hlow : ∀ i ∈ s, a ≤ c i) :
    ∀ i ∈ s, a ≤ roundedWaterfill w c i :=
  fun i hi => le_trans (hlow i hi) (le_max_right (w i) (c i))

omit [IsStrictOrderedRing R] in
/-- Second hypothesis of `rounded_pythagoras`: if `t` sits above the wall `w` (`w_i ≤ t_i`) and
`c_i ≤ a + 1`, then any coordinate where `t_i < max(w_i, c_i)` must lie in the flat part and
satisfy `max(w_i, c_i) ≤ a + 1`. -/
theorem roundedWaterfill_le_of_lt (s : Finset ι) (t w c : ι → R) (a : R)
    (htw : ∀ i ∈ s, w i ≤ t i) (hhi : ∀ i ∈ s, c i ≤ a + 1) :
    ∀ i ∈ s, t i < roundedWaterfill w c i → roundedWaterfill w c i ≤ a + 1 := by
  intro i hi hlt
  simp only [roundedWaterfill] at hlt ⊢
  rcases le_total (w i) (c i) with hwc | hcw
  · rw [max_eq_right hwc]
    exact hhi i hi
  · rw [max_eq_left hcw] at hlt
    exact absurd (htw i hi) (not_le.mpr hlt)

/-- **Discrete Pythagoras for the explicit rounded water-fill `q_i = max(w_i, c_i)`.**
Discharges both order hypotheses of `RoundedWaterfillExchange.rounded_pythagoras` from `w ≤ t`
and `a ≤ c ≤ a + 1`. -/
theorem roundedWaterfill_pythagoras (s : Finset ι) (t w c : ι → R) (a : R)
    (htw : ∀ i ∈ s, w i ≤ t i)
    (hlow : ∀ i ∈ s, a ≤ c i)
    (hhi : ∀ i ∈ s, c i ≤ a + 1)
    (hsum : ∑ i ∈ s, t i = ∑ i ∈ s, roundedWaterfill w c i) :
    ∑ i ∈ s, (roundedWaterfill w c i) ^ 2
      + ∑ i ∈ s, (t i - roundedWaterfill w c i) ^ 2
      - ∑ i ∈ s, |t i - roundedWaterfill w c i|
      ≤ ∑ i ∈ s, t i ^ 2 :=
  rounded_pythagoras s t (roundedWaterfill w c) a
    (roundedWaterfill_ge_floor s w c a hlow)
    (roundedWaterfill_le_of_lt s t w c a htw hhi)
    hsum

/-! ## Step (d): Two-sided `O(1)` excess assembly (`−K₃ ≤ M_n − A√(2n) ≤ K₂`) -/

/-- **Summed integer-grid coordinate trade-off (`K₁ = c₁ + c₀ c₁ / (2L)`).**
Summing `RoundedWaterfillExchange.int_tradeoff` over `i ∈ s` with `0 ≤ ω i ≤ c0` and
`∑ i ∈ s, ω i ≤ c1` bounds the total coordinate slack by `c1 + c0 * c1 / (2 * L)`. -/
theorem coord_tradeoff_sum_le {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (s : Finset ι) (ω : ι → F) (d : ι → ℕ) (L c0 c1 : F)
    (hL : 0 < L) (hc0 : 0 ≤ c0) (hω0 : ∀ i ∈ s, 0 ≤ ω i) (hωc0 : ∀ i ∈ s, ω i ≤ c0)
    (hsum : ∑ i ∈ s, ω i ≤ c1) :
    ∑ i ∈ s, (ω i * (d i : F) - L / 2 * ((d i : F) ^ 2 - (d i : F)))
      ≤ c1 + c0 * c1 / (2 * L) := by
  have hL2 : 0 < 2 * L := by linarith
  have hterm : ∀ i ∈ s,
      ω i * (d i : F) - L / 2 * ((d i : F) ^ 2 - (d i : F))
        ≤ ω i + (c0 / (2 * L)) * ω i := by
    intro i hi
    have hint := int_tradeoff (ω i) L (d i) (hω0 i hi) hL
    have hsq : ω i ^ 2 ≤ c0 * ω i := by
      have := mul_le_mul_of_nonneg_right (hωc0 i hi) (hω0 i hi)
      linarith [sq (ω i)]
    have hdiv : ω i ^ 2 / (2 * L) ≤ c0 * ω i / (2 * L) :=
      div_le_div_of_nonneg_right hsq hL2.le
    have hring : c0 * ω i / (2 * L) = (c0 / (2 * L)) * ω i := by ring
    linarith
  have h1 := sum_le_sum hterm
  rw [sum_add_distrib, ← mul_sum] at h1
  have hc0L : 0 ≤ c0 / (2 * L) := div_nonneg hc0 hL2.le
  have h2 : (c0 / (2 * L)) * (∑ i ∈ s, ω i) ≤ (c0 / (2 * L)) * c1 :=
    mul_le_mul_of_nonneg_left hsum hc0L
  have hring : (c0 / (2 * L)) * c1 = c0 * c1 / (2 * L) := by ring
  linarith

/-- **Upper-bound assembly (`Ψ(λ) ≤ A√(2n) + K₂`).**
Combining `coord_tradeoff_sum_le` (`≤ K₁`) and `extra_rows_tradeoff` (`≤ J`) with
`l ≤ k + j`, `k ≤ √(2n)`, and `ε(1) ≤ F(n)` bounds any shape's objective `Ψ` by
`A√(2n) + (S₂ + K₁ + J − ε(1))`. -/
theorem rev_upper_bound_assembly {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (s : Finset ι) (ω : ι → F) (d : ι → ℕ)
    (Psi A L S2 Fn eps1 c0 c1 sqrt2n l k j : F)
    (hL : 0 < L) (hA : 0 ≤ A) (hc0 : 0 ≤ c0)
    (hω0 : ∀ i ∈ s, 0 ≤ ω i) (hωc0 : ∀ i ∈ s, ω i ≤ c0) (hsum : ∑ i ∈ s, ω i ≤ c1)
    (hlkj : l ≤ k + j) (hk : k ≤ sqrt2n) (hFn : eps1 ≤ Fn)
    (hPsi : Psi ≤ l * A + S2 - Fn
      + (∑ i ∈ s, (ω i * (d i : F) - L / 2 * ((d i : F) ^ 2 - (d i : F))))
      - L / 2 * (j * (j - 1))) :
    Psi ≤ A * sqrt2n
      + (S2 + (c1 + c0 * c1 / (2 * L)) + (A + L / 2) ^ 2 / (2 * L) - eps1) := by
  have hcoord := coord_tradeoff_sum_le s ω d L c0 c1 hL hc0 hω0 hωc0 hsum
  have hextra := extra_rows_tradeoff A L j hL
  have hlkA : l * A ≤ k * A + j * A := by
    have := mul_le_mul_of_nonneg_right hlkj hA
    linarith
  have hkA : k * A ≤ A * sqrt2n := by
    have := mul_le_mul_of_nonneg_left hk hA
    linarith
  linarith

/-- **Lower-bound assembly (`Ψ(λ_{k,r}) ≥ A√(2n) − K₃`, with `K₃ = 3A/2 + 2B + C`).**
Given the row-deleted staircase hook-sum inequality `staircaseSum (k − r) + staircaseSum r ≤
shapeHookSum` (`StaircaseRowDeletedHook.rowDeleted_hookSum_ge`), the staircase lower bound
`A m − B ≤ staircaseSum m` (`rem_m ≥ 0`), the one-body upper bound `Fn ≤ C`, and
`√(2n) ≤ k + 3/2`, the shape's objective `shapeHookSum − Fn` is at least `A√(2n) − (3A/2 + 2B + C)`. -/
theorem rev_lower_bound_assembly {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    {k r : ℕ} (hr : r ≤ k)
    (staircaseSum : ℕ → F) (shapeHookSum Fn A B C sqrt2n : F)
    (hA : 0 ≤ A)
    (hdecomp : staircaseSum (k - r) + staircaseSum r ≤ shapeHookSum)
    (hstair_kr : A * ((k - r : ℕ) : F) - B ≤ staircaseSum (k - r))
    (hstair_r : A * (r : F) - B ≤ staircaseSum r)
    (hFn : Fn ≤ C)
    (hsqrt : sqrt2n ≤ (k : F) + 3 / 2) :
    A * sqrt2n - (3 * A / 2 + 2 * B + C) ≤ shapeHookSum - Fn := by
  have hcast : ((k - r : ℕ) : F) + (r : F) = (k : F) := by exact_mod_cast Nat.sub_add_cancel hr
  have hAsqrt : A * sqrt2n ≤ A * (k : F) + 3 * A / 2 := by
    have := mul_le_mul_of_nonneg_left hsqrt hA
    linarith
  have hsum_stair : A * (k : F) - 2 * B ≤ staircaseSum (k - r) + staircaseSum r := by
    linarith [hstair_kr, hstair_r, congrArg (A * ·) hcast]
  linarith

/-- **Two-sided `O(1)` excess bracket (`−K₃ ≤ M_n − A√(2n) ≤ K₂`).**
Combining `rev_upper_bound_assembly` (applied to an arbitrary maximiser reaching `Mn`) and
`rev_lower_bound_assembly` (applied to the candidate shape `λ_{k,r}` with `shapeHookSum − Fn ≤ Mn`)
places the excess `Mn − A√(2n)` inside the `n`-independent interval `[−K₃, K₂]`. -/
theorem rev_two_sided_excess_bracket {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    {k r : ℕ} (hr : r ≤ k)
    (s : Finset ι) (ω : ι → F) (d : ι → ℕ)
    (staircaseSum : ℕ → F)
    (Mn shapeHookSum A B C L S2 Fn eps1 c0 c1 sqrt2n l j : F)
    (hL : 0 < L) (hA : 0 ≤ A) (hc0 : 0 ≤ c0)
    (hω0 : ∀ i ∈ s, 0 ≤ ω i) (hωc0 : ∀ i ∈ s, ω i ≤ c0) (hsum : ∑ i ∈ s, ω i ≤ c1)
    (hlkj : l ≤ (k : F) + j) (hk : (k : F) ≤ sqrt2n) (hFn_low : eps1 ≤ Fn) (hFn_high : Fn ≤ C)
    (hMn_up : Mn ≤ l * A + S2 - Fn
      + (∑ i ∈ s, (ω i * (d i : F) - L / 2 * ((d i : F) ^ 2 - (d i : F))))
      - L / 2 * (j * (j - 1)))
    (hMn_low : shapeHookSum - Fn ≤ Mn)
    (hdecomp : staircaseSum (k - r) + staircaseSum r ≤ shapeHookSum)
    (hstair_kr : A * ((k - r : ℕ) : F) - B ≤ staircaseSum (k - r))
    (hstair_r : A * (r : F) - B ≤ staircaseSum r)
    (hsqrt : sqrt2n ≤ (k : F) + 3 / 2) :
    -(3 * A / 2 + 2 * B + C) ≤ Mn - A * sqrt2n ∧
      Mn - A * sqrt2n ≤ S2 + (c1 + c0 * c1 / (2 * L)) + (A + L / 2) ^ 2 / (2 * L) - eps1 := by
  have hup := rev_upper_bound_assembly s ω d Mn A L S2 Fn eps1 c0 c1 sqrt2n l (k : F) j
    hL hA hc0 hω0 hωc0 hsum hlkj hk hFn_low hMn_up
  have hlow := rev_lower_bound_assembly hr staircaseSum shapeHookSum Fn A B C sqrt2n
    hA hdecomp hstair_kr hstair_r hFn_high hsqrt
  exact ⟨by linarith, by linarith⟩

end QOU.BraidKnot.RevBoundedExcessAssembly
