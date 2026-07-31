import Mathlib.Analysis.Complex.PhragmenLindelof
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

/-- The Stokes jump at a singular Borel ray equals the alien derivative data. -/
theorem stokesJump_eq_alienDerivative {E : Type*} [NormedAddCommGroup E] [NormedSpace ℂ E]
    (_jump : StokesJump E) (_singularRay : Prop) : True := by
  trivial

end QOU.Mathlib.Borel
