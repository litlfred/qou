import Mathlib.Analysis.Complex.PhragmenLindelof
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import QOU.Mathlib.BorelWatson
import QOU.Mathlib.BorelWatsonUniqueness

namespace QOU.Mathlib.Borel

open Real Filter Asymptotics Complex Bornology
open scoped Topology Real Nat

/-- A Stokes jump at angle θ is the difference of two directional Borel sums. -/
structure StokesJump (E : Type*) [NormedAddCommGroup E] [NormedSpace ℂ E] where
  theta : ℝ
  sumLeft : ℝ → E
  sumRight : ℝ → E

/-- A Stokes jump satisfies `|jump(x)| ≤ C·exp(−b·x^s)` for `s > 1, b > 0`. -/
def StokesJumpBound {E : Type*} [NormedAddCommGroup E] (jump : ℝ → E) : Prop :=
  ∃ C b s : ℝ, 0 < b ∧ 1 < s ∧ ∀ᶠ x in atTop, ‖jump x‖ ≤ C * Real.exp (-b * x ^ s)

/-! ### Helper: √t ≤ exp(t/2) for t ≥ 0

    Proof: `√t ≤ exp(t/2)` ⟺ `(√t)² ≤ (exp(t/2))²` (both sides ≥ 0)
    ⟺ `t ≤ exp(t)`, which follows from `1 + t ≤ exp(t)`. -/

private lemma sqrt_le_exp_half {t : ℝ} (_ht : 0 ≤ t) :
    Real.sqrt t ≤ Real.exp (t / 2) := by
  rw [← Real.sqrt_sq (Real.exp_pos (t / 2)).le]
  apply Real.sqrt_le_sqrt
  rw [sq, ← Real.exp_add, add_halves]
  linarith [Real.add_one_le_exp t]

/-- Gevrey-1 remainder bound implies Stokes jump bound.

    **Proof.** Apply `gevrey1_remainder_expDecay` with ε = x^{−s}, giving
    `‖jump x‖ ≤ C·e²·√(x^s)·exp(−x^s)`. Then `√(x^s) ≤ exp(x^s/2)` by
    `sqrt_le_exp_half`, so `‖jump x‖ ≤ C·e²·exp(−x^s/2)`. -/
theorem gevrey_difference_stokesJumpBound {E : Type*} [NormedAddCommGroup E]
    (jump : ℝ → E) (s : ℝ) (hs : 1 < s) (C : ℝ) (hC : 0 ≤ C)
    (h_gevrey : ∀ᶠ x in atTop, ∀ N : ℕ, ‖jump x‖ ≤ C * (N ! : ℝ) * (x ^ (-s)) ^ N) :
    StokesJumpBound jump := by
  -- Witnesses: C' = C * e², b = 1/2, s' = s
  refine ⟨C * Real.exp 2, 1 / 2, s, one_half_pos, hs, ?_⟩
  filter_upwards [h_gevrey, Filter.eventually_ge_atTop 2] with x hgev hx2
  have hx_pos : (0 : ℝ) < x := by linarith
  have hx_nonneg : (0 : ℝ) ≤ x := hx_pos.le
  have hs_pos : (0 : ℝ) < s := by linarith
  -- Set ε = x^(-s)
  set ε := (x : ℝ) ^ (-s) with hε_def
  have hε_pos : 0 < ε := Real.rpow_pos_of_pos hx_pos (-s)
  have hε_le1 : ε ≤ 1 :=
    Real.rpow_le_one_of_one_le_of_nonpos (by linarith : (1 : ℝ) ≤ x) (by linarith : -s ≤ 0)
  -- Step 1: Apply gevrey1_remainder_expDecay
  have happ := gevrey1_remainder_expDecay hC hε_pos hε_le1 (norm_nonneg _) (fun N => hgev N)
  -- happ: ‖jump x‖ ≤ C * e² / √ε * exp(-1/ε)
  -- Step 2: Key identity — 1/ε = x^s
  have hε_eq : ε = (x ^ s)⁻¹ := by
    rw [hε_def, Real.rpow_neg hx_nonneg]
  have h_inv_ε : 1 / ε = x ^ s := by
    rw [hε_eq, one_div, inv_inv]
  -- Step 3: Key identity — √ε = (√(x^s))⁻¹
  have hxs_pos : 0 < x ^ s := Real.rpow_pos_of_pos hx_pos s
  have h_sqrt_ε : Real.sqrt ε = (Real.sqrt (x ^ s))⁻¹ := by
    rw [hε_eq, Real.sqrt_inv]
  -- Step 4: Transform happ using these identities
  have h_bound : ‖jump x‖ ≤ C * Real.exp 2 * Real.sqrt (x ^ s) * Real.exp (-(x ^ s)) := by
    calc ‖jump x‖
      ≤ C * Real.exp 2 / Real.sqrt ε * Real.exp (-1 / ε) := happ
      _ = C * Real.exp 2 / Real.sqrt ε * Real.exp (-(x ^ s)) := by
          rw [show (-1 : ℝ) / ε = -(x ^ s) from by rw [neg_div, h_inv_ε]]
      _ = C * Real.exp 2 * (Real.sqrt ε)⁻¹ * Real.exp (-(x ^ s)) := by
          rw [div_eq_mul_inv]
      _ = C * Real.exp 2 * ((Real.sqrt (x ^ s))⁻¹)⁻¹ * Real.exp (-(x ^ s)) := by
          rw [h_sqrt_ε]
      _ = C * Real.exp 2 * Real.sqrt (x ^ s) * Real.exp (-(x ^ s)) := by
          rw [inv_inv]
  -- Step 5: Apply √(x^s) ≤ exp(x^s/2) via sqrt_le_exp_half
  have hxs_nonneg : 0 ≤ x ^ s := hxs_pos.le
  have h_sqrt_bound : Real.sqrt (x ^ s) ≤ Real.exp ((x ^ s) / 2) :=
    sqrt_le_exp_half hxs_nonneg
  -- Step 6: Combine
  calc ‖jump x‖
    ≤ C * Real.exp 2 * Real.sqrt (x ^ s) * Real.exp (-(x ^ s)) := h_bound
    _ ≤ C * Real.exp 2 * Real.exp ((x ^ s) / 2) * Real.exp (-(x ^ s)) := by
        gcongr
    _ = C * Real.exp 2 * (Real.exp ((x ^ s) / 2) * Real.exp (-(x ^ s))) := by ring
    _ = C * Real.exp 2 * Real.exp ((x ^ s) / 2 + -(x ^ s)) := by
        rw [Real.exp_add]
    _ = C * Real.exp 2 * Real.exp (-(x ^ s) / 2) := by
        ring_nf
    _ = C * Real.exp 2 * Real.exp (-(1 / 2) * x ^ s) := by
        ring_nf

/-- **A Stokes jump is beyond all orders.**  If `‖jump x‖ ≤ C·exp(−b·x^s)` with
    `b > 0`, `s > 1`, then `x^N·‖jump x‖ → 0` for **every** real `N` — the jump
    decays faster than any power of `x`.

    This is the reason alien calculus exists.  A formal asymptotic series in
    `x^{-1}` sees only the powers; a term killed by every power is invisible to
    it.  So two functions with the *same* asymptotic expansion can differ by a
    Stokes jump, the expansion cannot distinguish them, and the alien derivative
    is the invariant that can.  `gevrey_difference_stokesJumpBound` above supplies
    the hypothesis from a Gevrey-1 remainder bound; this consumes it.

    Note `C ≥ 0` is not assumed — it follows, since `‖jump x‖ ≥ 0` and the
    exponential is positive wherever the bound holds.

    Replaces a `: True := trivial` placeholder that carried the docstring "the
    Stokes jump at a singular Borel ray equals the alien derivative data" while
    concluding nothing (AGENTS.md §1a).  That equality is the bridge equation and
    is *not* proved here; this is the one-directional fact the file's own
    machinery does establish.  Nothing in the corpus referenced the placeholder.

    -- Ref: [ecalle1981] Fonctions résurgentes, tome I
    -- Ref: [sauzin2014] https://arxiv.org/abs/1405.0356 -/
theorem stokesJump_beyondAllOrders {E : Type*} [NormedAddCommGroup E]
    {jump : ℝ → E} (h : StokesJumpBound jump) (N : ℝ) :
    Tendsto (fun x : ℝ => x ^ N * ‖jump x‖) atTop (𝓝 0) := by
  obtain ⟨C, b, s, hb, hs, hbound⟩ := h
  -- `x^N·exp(−b·x^s)` is `o(exp(−x/2))`, which tends to `0`.
  have hexp : Tendsto (fun x : ℝ => Real.exp (-(1 / 2) * x)) atTop (𝓝 0) :=
    Real.tendsto_exp_atBot.comp
      (Filter.Tendsto.const_mul_atTop_of_neg (by norm_num : (-(1 / 2) : ℝ) < 0) tendsto_id)
  have hmaj : Tendsto (fun x : ℝ => C * (x ^ N * Real.exp (-b * x ^ s))) atTop (𝓝 0) := by
    have := ((_root_.rpow_mul_exp_neg_mul_rpow_isLittleO_exp_neg N hs hb).isBigO).trans_tendsto hexp
    simpa using this.const_mul C
  refine squeeze_zero' ?_ ?_ hmaj
  · filter_upwards [Filter.eventually_ge_atTop (0 : ℝ)] with x hx
    exact mul_nonneg (Real.rpow_nonneg hx N) (norm_nonneg _)
  · filter_upwards [hbound, Filter.eventually_ge_atTop (0 : ℝ)] with x hx hx0
    calc x ^ N * ‖jump x‖
        ≤ x ^ N * (C * Real.exp (-b * x ^ s)) :=
          mul_le_mul_of_nonneg_left hx (Real.rpow_nonneg hx0 N)
      _ = C * (x ^ N * Real.exp (-b * x ^ s)) := by ring

end QOU.Mathlib.Borel
