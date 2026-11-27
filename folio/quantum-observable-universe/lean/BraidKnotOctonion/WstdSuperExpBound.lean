import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Ring.Basic
import Mathlib.Tactic

/-!
# QOU.BraidsAndKnots.WstdSuperExpBound — the pigeonhole cube–square lower bound

The rigorous core (C) of the super-exponential lower bound on the GAP-A-3 tower weight
`w_std(k) = E_Planch[f^{λ/(2,1)}]` (Δ_λ magnitude leg). The full argument (compute probe
`computations/deltalambda/wlambda_wstd_superexp_lower_bound.py`, audit
`docs/audits/2026-07-18-wstd-superexp-lower-bound.md`) reduces the growth bound to this clean
inequality applied with `aᵢ = f^λ`, `S = ∑(f^λ)² = k!`, `N = p(k)`:

    S³ ≤ N³ · (∑ aᵢ³)²      ⇒     ∑(f^λ)³ ≥ (k!)^{3/2} / p(k)^{3/2},

whence `Σ(f^λ)³/k! ≥ √(k!)/p(k)^{3/2} → ∞` super-exponentially (Stirling).

Proof: pigeonhole (some square `aⱼ²` is ≥ the mean `S/N`), then `∑ aᵢ³ ≥ aⱼ³` (single
nonneg term ≤ sum) and cube/square monotonicity give `S³ ≤ (N·aⱼ²)³ = N³(aⱼ³)² ≤ N³(∑aᵢ³)²`.

Base ring: `ℝ` (archimedean — ordering, a real square-sum bound; genuinely post-wall).
Sorry-free.
-/

namespace QOU.BraidsAndKnots.WstdSuperExpBound

open Finset

/-- **Pigeonhole cube–square lower bound** (rpow-free form of `∑ aᵢ³ ≥ (S/N)^{3/2}`).
For a nonnegative real family `a : ι → ℝ` over a nonempty finite index type with `∑ aᵢ² = S`
and `N = card ι`, the cube sum obeys `S³ ≤ N³·(∑ aᵢ³)²`. -/
theorem cube_sum_sq_ge {ι : Type*} [Fintype ι] [Nonempty ι]
    (a : ι → ℝ) (ha : ∀ i, 0 ≤ a i) (S : ℝ) (hS : ∑ i, a i ^ 2 = S) :
    S ^ 3 ≤ (Fintype.card ι : ℝ) ^ 3 * (∑ i, a i ^ 3) ^ 2 := by
  have hNpos : (0 : ℝ) < (Fintype.card ι : ℝ) := by exact_mod_cast Fintype.card_pos
  set N : ℝ := (Fintype.card ι : ℝ) with hNdef
  have hSnn : 0 ≤ S := hS ▸ Finset.sum_nonneg (fun i _ => sq_nonneg (a i))
  -- pigeonhole: some jth square is ≥ the average S/N, i.e. S ≤ N * a j ^ 2
  have key : ∃ j : ι, S ≤ N * a j ^ 2 := by
    by_contra h
    push_neg at h
    -- h : ∀ j, N * a j ^ 2 < S
    have hlt : ∑ i, a i ^ 2 < ∑ _i : ι, S / N := by
      apply Finset.sum_lt_sum_of_nonempty univ_nonempty
      intro i _
      have hi := h i
      rw [lt_div_iff₀ hNpos, mul_comm]
      exact hi
    rw [hS, Finset.sum_const, card_univ, nsmul_eq_mul, ← hNdef,
        mul_div_cancel₀ _ (ne_of_gt hNpos)] at hlt
    exact lt_irrefl S hlt
  obtain ⟨j, hj⟩ := key
  have hterm : a j ^ 3 ≤ ∑ i, a i ^ 3 :=
    Finset.single_le_sum (fun i _ => pow_nonneg (ha i) 3) (mem_univ j)
  have hcube_nn : 0 ≤ a j ^ 3 := pow_nonneg (ha j) 3
  have hNa_nn : 0 ≤ N * a j ^ 2 := by positivity
  calc S ^ 3 ≤ (N * a j ^ 2) ^ 3 := by
              exact pow_le_pow_left₀ hSnn hj 3
    _ = N ^ 3 * (a j ^ 3) ^ 2 := by ring
    _ ≤ N ^ 3 * (∑ i, a i ^ 3) ^ 2 := by
              apply mul_le_mul_of_nonneg_left _ (by positivity)
              exact pow_le_pow_left₀ hcube_nn hterm 2

/-- **Algebraic transfer (B)+(D).** From the exact Plancherel identity
`cube = 2·w_std + 2·e` (B, with `e = E_Planch[f^{λ/(3)}]`) together with `0 ≤ e` and the
dominance `e ≤ w_std` (D), the tower weight carries at least a quarter of the cube moment:
`cube ≤ 4·w_std`. Combined with a lower bound `L ≤ cube` (the pigeonhole `cube_sum_sq_ge`,
applied with `L = √(k!)/p(k)^{3/2}`), this gives `L/4 ≤ w_std` — the super-exponential
lower bound on `w_std`, modulo the (SYT-combinatorial) identity `cube = 2w+2e` and the
inequality `e ≤ w`. -/
theorem wstd_ge_quarter_lower_bound {wstd e cube L : ℝ}
    (hid : cube = 2 * wstd + 2 * e) (_he : 0 ≤ e) (hdom : e ≤ wstd) (hL : L ≤ cube) :
    L / 4 ≤ wstd := by linarith

end QOU.BraidsAndKnots.WstdSuperExpBound
