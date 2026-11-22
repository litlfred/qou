import Mathlib.Data.Nat.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.PSeries

/-!
# PSLQ certifies Cl_3(2π/5) - Cl_3(4π/5) is independent

Compiled formalisation of `prop:cl3-zeta5-pslq-independence`.
Sibling docstub at `braids-and-knots/cl3-zeta5-pslq-independence.lean`.

PSLQ is a numerical certification at fixed precision and norm
bound. The substantive content lives in `cl3-zeta5-pslq.witness.json`;
this Lean stub captures the certification parameters (precision,
norm bound) and the certified outcome (no integer relation found
at the given parameters).
-/

namespace QOU.BraidKnot.Cl3Zeta5PslqIndependence

open Real

/-- Abstract context for `prop:cl3-zeta5-pslq-independence`. -/
class Cl3Zeta5PslqIndependenceContext where
  /-- Decimal precision used by PSLQ (digits). -/
  pslq_precision_dps : ℕ
  /-- Norm-bound parameter used by PSLQ (≤ which any integer relation
      coefficient must lie). -/
  pslq_norm_bound : ℕ
  /-- Predicate "PSLQ found no integer relation at the given
      precision and norm bound on `(Cl_3(2π/5), Cl_3(4π/5), ζ_5)`". -/
  no_integer_relation_found : Prop
  /-- Manuscript claim — PSLQ certifies independence at substantial
      precision (≥ 1000 dps) and significant norm bound (≥ 10^10). -/
  claim_pslq_independence :
    1000 ≤ pslq_precision_dps ∧
    10 ^ 10 ≤ pslq_norm_bound ∧
    no_integer_relation_found


/-! ### What can be proved: the difference is a Dirichlet L-value

PSLQ is a finite-precision search, so "no integer relation" is not a Lean
statement.  What Lean can state is what the difference *is*.  Writing
`Cl₃(θ) = Σ_{n≥1} cos(nθ)/n³`, the coefficient `cos(2πn/5) − cos(4πn/5)` depends
only on `n mod 5` and equals `(√5/2)·χ₅(n)`, where `χ₅` is the quadratic
character mod 5 (`+1` on `n ≡ ±1`, `−1` on `n ≡ ±2`, `0` on `5 ∣ n`).  So

    Cl₃(2π/5) − Cl₃(4π/5) = (√5/2) · L(3, χ₅).

This is the precise sense in which the block's difference is a single real
period of `ℚ(ζ₅)`.  It does not prove independence from `ζ(3)` or `π³`, and
nothing here uses the PSLQ run.
-/

/-- The Clausen cosine series `Cl₃(θ) = Σ_{n≥1} cos(nθ)/n³`. -/
noncomputable def clausenCos3 (θ : ℝ) : ℝ :=
  ∑' n : ℕ, Real.cos ((n + 1 : ℝ) * θ) / ((n : ℝ) + 1) ^ 3

/-- The quadratic (Legendre) character modulo 5, as a real-valued function. -/
def chi5 (n : ℕ) : ℝ :=
  if n % 5 = 1 ∨ n % 5 = 4 then 1 else if n % 5 = 2 ∨ n % 5 = 3 then -1 else 0

private lemma cos_two_pi_div_five : Real.cos (2 * π / 5) = (Real.sqrt 5 - 1) / 4 := by
  have h := Real.cos_pi_div_five
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num)
  rw [show 2 * π / 5 = 2 * (π / 5) by ring, Real.cos_two_mul, h]
  nlinarith [h5]

private lemma cos_four_pi_div_five : Real.cos (4 * π / 5) = -((1 + Real.sqrt 5) / 4) := by
  rw [show 4 * π / 5 = π - π / 5 by ring, Real.cos_pi_sub, Real.cos_pi_div_five]

private lemma cos_six_pi_div_five : Real.cos (6 * π / 5) = -((1 + Real.sqrt 5) / 4) := by
  rw [show 6 * π / 5 = π / 5 + π by ring, Real.cos_add_pi, Real.cos_pi_div_five]

private lemma cos_eight_pi_div_five : Real.cos (8 * π / 5) = (Real.sqrt 5 - 1) / 4 := by
  rw [show 8 * π / 5 = -(2 * π / 5) + 2 * π by ring, Real.cos_add_two_pi, Real.cos_neg,
    cos_two_pi_div_five]

/-- **The coefficient identity.**  For every `m`,
`cos(2πm/5) − cos(4πm/5) = (√5/2)·χ₅(m)`. -/
theorem cos_diff_eq_chi5 (m : ℕ) :
    Real.cos ((m : ℝ) * (2 * π / 5)) - Real.cos ((m : ℝ) * (4 * π / 5))
      = Real.sqrt 5 / 2 * chi5 m := by
  obtain ⟨k, r, hr, rfl⟩ : ∃ k r, r < 5 ∧ m = 5 * k + r :=
    ⟨m / 5, m % 5, Nat.mod_lt _ (by norm_num), (Nat.div_add_mod m 5).symm⟩
  have e1 : ((5 * k + r : ℕ) : ℝ) * (2 * π / 5) = (r : ℝ) * (2 * π / 5) + (k : ℕ) * (2 * π) := by
    push_cast; ring
  have e2 : ((5 * k + r : ℕ) : ℝ) * (4 * π / 5)
      = (r : ℝ) * (4 * π / 5) + ((2 * k : ℕ) : ℝ) * (2 * π) := by
    push_cast; ring
  rw [e1, e2, Real.cos_add_nat_mul_two_pi, Real.cos_add_nat_mul_two_pi]
  have hmod : (5 * k + r) % 5 = r := by omega
  unfold chi5
  rw [hmod]
  interval_cases r
  · simp
  · simp only [Nat.cast_one, one_mul, cos_two_pi_div_five, cos_four_pi_div_five]
    norm_num; ring
  · have a : (2 : ℝ) * (2 * π / 5) = 4 * π / 5 := by ring
    have b : (2 : ℝ) * (4 * π / 5) = 8 * π / 5 := by ring
    simp only [Nat.cast_ofNat, a, b, cos_four_pi_div_five, cos_eight_pi_div_five]
    norm_num; ring
  · have a : (3 : ℝ) * (2 * π / 5) = 6 * π / 5 := by ring
    have b : (3 : ℝ) * (4 * π / 5) = 2 * π / 5 + (1 : ℕ) * (2 * π) := by push_cast; ring
    simp only [Nat.cast_ofNat, a, b, Real.cos_add_nat_mul_two_pi, cos_six_pi_div_five,
      cos_two_pi_div_five]
    norm_num; ring
  · have a : (4 : ℝ) * (2 * π / 5) = 8 * π / 5 := by ring
    have b : (4 : ℝ) * (4 * π / 5) = 6 * π / 5 + (1 : ℕ) * (2 * π) := by push_cast; ring
    simp only [Nat.cast_ofNat, a, b, Real.cos_add_nat_mul_two_pi, cos_eight_pi_div_five,
      cos_six_pi_div_five]
    norm_num; ring

private lemma summable_cube_bound (f : ℕ → ℝ) (hf : ∀ n, |f n| ≤ 1) :
    Summable (fun n : ℕ => f n / ((n : ℝ) + 1) ^ 3) := by
  have hs : Summable (fun n : ℕ => 1 / ((n : ℝ) + 1) ^ 3) := by
    have := (summable_nat_add_iff 1).mpr (Real.summable_one_div_nat_pow.mpr (by norm_num : 1 < 3))
    simpa [Nat.cast_add, Nat.cast_one] using this
  refine Summable.of_norm_bounded hs fun n => ?_
  rw [Real.norm_eq_abs, abs_div, abs_of_pos (by positivity : (0 : ℝ) < ((n : ℝ) + 1) ^ 3)]
  exact div_le_div_of_nonneg_right (hf n) (by positivity)

/-- **The difference is `(√5/2)·L(3, χ₅)`** ([`prop:cl3-zeta5-pslq-independence`],
the structural half).

    Cl₃(2π/5) − Cl₃(4π/5) = (√5/2) · Σ_{n≥1} χ₅(n)/n³. -/
theorem cl3_diff_eq_sqrt5_L3_chi5 :
    clausenCos3 (2 * π / 5) - clausenCos3 (4 * π / 5)
      = Real.sqrt 5 / 2 * ∑' n : ℕ, chi5 (n + 1) / ((n : ℝ) + 1) ^ 3 := by
  unfold clausenCos3
  have hs : ∀ θ : ℝ, Summable (fun n : ℕ => Real.cos ((n + 1 : ℝ) * θ) / ((n : ℝ) + 1) ^ 3) :=
    fun θ => summable_cube_bound _ fun n => Real.abs_cos_le_one _
  rw [← (hs _).tsum_sub (hs _), ← tsum_mul_left]
  refine tsum_congr fun n => ?_
  have h := cos_diff_eq_chi5 (n + 1)
  push_cast at h
  rw [← sub_div, h, mul_div_assoc]

/-! ### Removed 2026-08-30 — self-assuming projections

- `pslq_independence` — body was `ctx.claim_pslq_independence`: the conclusion was the projected
  field verbatim, so the declaration restated its own hypothesis.

**Why removal.** The content is not lost: it stays in the class field each
declaration projected, which asserts the same proposition under the same
hypotheses. Only the restatement goes. That is the disposition the vacuity
ledger records for this category — *"drop the pseudo-theorem and project the
field at use sites"* — and there were no use sites: each had **zero references
anywhere in the corpus**, including in this file. A caller wanting the fact
writes the projection directly, which is what the removed body did.
Bean `qou-z9ws`.
-/

end QOU.BraidKnot.Cl3Zeta5PslqIndependence
