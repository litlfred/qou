import QOU.MathlibExt.PhiBProd
import Mathlib.Analysis.SpecialFunctions.Log.Summable
import Mathlib.Topology.Algebra.InfiniteSum.Field

/-!
# `phiBProd` strip bounds from the product (growth-estimate epic, bricks G1 + G3)

Route-B bricks of the Faddeev keystone growth-estimate epic (`qou-mz4f`;
[scope](../../../../../docs/workplans/2026-07-26-faddeev-growth-estimate-epic-scope.md)).
The scoping survey established that `phiBProd`'s strip growth needs **no contour integral**:
input 1's product form gives it by elementary product-norm estimates already in Mathlib
(`Multipliable.norm_tprod`, `Real.rexp_tsum_eq_tprod`, `Real.log_le_sub_one_of_pos`).

* **G1** (`norm_tprod_numFactor_le` / `norm_tprod_denFactor_le`) — each infinite product's
  norm is bounded above by `exp` of the summed factor-log-norms, i.e.
  `‖∏' k, (1 + gₖ)‖ ≤ exp(∑' ‖gₖ‖)` (the general `norm_tprod_one_add_le`), applied off the
  zero lattices where all factors are nonzero. This is the numerator (and denominator)
  **upper** bound.
* **G3** (`norm_phiBProd_le_of_den_lower`) — the `phiBProd = num/den` strip bound, given a
  denominator **lower** bound `δ` (the G2 obligation, carried here as an explicit
  hypothesis): `‖phiBProd b z‖ ≤ exp(∑' ‖numFactorₖ − 1‖)/δ`.

G2 (the denominator lower bound that supplies `δ`) is the one remaining estimate; G3 is
stated conditionally on it so both G1 and the G3 assembly land now on the merged product
infrastructure.

Verified `lean`-direct against the pinned Mathlib `Log.Summable` + `InfiniteSum.Field`
cones + `PhiBProd`. Sorry-free.

-- Ref: [leitner2026] docs/workplans/2026-07-26-faddeev-growth-estimate-epic-scope.md
-/

open Complex
open QOU.MathlibExt.PhiBProd

namespace QOU.QBeta.PhiBProdStripBound

/-- **General product-norm upper bound.** For a norm-summable complex family `g` with no
vanishing factor `1 + gₖ`, `‖∏' k, (1 + gₖ)‖ ≤ exp(∑' k, ‖gₖ‖)`. Proof: `‖∏‖ = ∏‖·‖`
(`Multipliable.norm_tprod`); with all factors positive, `∏‖1+gₖ‖ = exp(∑ log‖1+gₖ‖)`
(`rexp_tsum_eq_tprod`); and `log‖1+gₖ‖ ≤ ‖1+gₖ‖ − 1 ≤ ‖gₖ‖`. -/
theorem norm_tprod_one_add_le {g : ℕ → ℂ} (hg : Summable (fun k => ‖g k‖))
    (hnz : ∀ k, 1 + g k ≠ 0) :
    ‖∏' k, (1 + g k)‖ ≤ Real.exp (∑' k, ‖g k‖) := by
  have hmul_factor : Multipliable (fun k => 1 + g k) := multipliable_one_add_of_summable hg
  rw [hmul_factor.norm_tprod]
  have hpos : ∀ k, 0 < ‖1 + g k‖ := fun k => norm_pos_iff.mpr (hnz k)
  have hlogsum : Summable (fun k => Real.log ‖1 + g k‖) := hg.summable_log_norm_one_add
  have heq : ∏' k, ‖1 + g k‖ = Real.exp (∑' k, Real.log ‖1 + g k‖) :=
    (Real.rexp_tsum_eq_tprod hpos hlogsum).symm
  rw [heq]
  refine Real.exp_le_exp.mpr (Summable.tsum_le_tsum (fun k => ?_) hlogsum hg)
  calc Real.log ‖1 + g k‖ ≤ ‖1 + g k‖ - 1 := Real.log_le_sub_one_of_pos (hpos k)
    _ ≤ ‖g k‖ := by
        have h := norm_add_le (1 : ℂ) (g k)
        simp only [norm_one] at h
        linarith

/-- Summability of `‖numFactor − 1‖` on the branch `Im b² > 0` (the geometric factor norms). -/
private theorem summable_norm_numFactor_sub_one (b z : ℂ) (hβ : 0 < (b ^ 2).im) :
    Summable (fun k : ℕ => ‖numFactor b z k - 1‖) := by
  have hconv : (fun k : ℕ => ‖numFactor b z k - 1‖)
      = fun k : ℕ => ‖Complex.exp ((Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1)
          + 2 * (Real.pi : ℂ) * b * z)‖ := by
    funext k; unfold numFactor; rw [add_sub_cancel_left]
  rw [hconv]
  have hc : (2 * (Real.pi : ℂ) * I * b ^ 2).re < 0 := by
    have h : (2 * (Real.pi : ℂ) * I * b ^ 2).re = -(2 * Real.pi * (b ^ 2).im) := by
      simp [Complex.mul_re, Complex.mul_im]
    rw [h]; have : (0 : ℝ) < 2 * Real.pi * (b ^ 2).im := by positivity
    linarith
  have hnorm : (fun k : ℕ =>
      ‖Complex.exp ((Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1) + 2 * (Real.pi : ℂ) * b * z)‖)
      = fun k => Real.exp ((Real.pi : ℂ) * I * b ^ 2 + 2 * (Real.pi : ℂ) * b * z).re
          * Real.exp (2 * (Real.pi : ℂ) * I * b ^ 2).re ^ k := by
    funext k
    rw [show (Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1) + 2 * (Real.pi : ℂ) * b * z
        = ((Real.pi : ℂ) * I * b ^ 2 + 2 * (Real.pi : ℂ) * b * z)
          + (k : ℂ) * (2 * (Real.pi : ℂ) * I * b ^ 2) from by ring, Complex.norm_exp]
    have hre : (((Real.pi : ℂ) * I * b ^ 2 + 2 * (Real.pi : ℂ) * b * z)
        + (k : ℂ) * (2 * (Real.pi : ℂ) * I * b ^ 2)).re
        = ((Real.pi : ℂ) * I * b ^ 2 + 2 * (Real.pi : ℂ) * b * z).re
          + (k : ℝ) * (2 * (Real.pi : ℂ) * I * b ^ 2).re := by
      simp [Complex.add_re, Complex.mul_re, Complex.natCast_re, Complex.natCast_im]
    rw [hre, Real.exp_add, Real.exp_nat_mul]
  rw [hnorm]
  exact (summable_geometric_of_lt_one (Real.exp_pos _).le
    (Real.exp_lt_one_iff.mpr hc)).mul_left _

/-- Summability of `‖denFactor − 1‖` on the branch `Im b² > 0`. -/
private theorem summable_norm_denFactor_sub_one (b z : ℂ) (hβ : 0 < (b ^ 2).im) :
    Summable (fun k : ℕ => ‖denFactor b z k - 1‖) := by
  have hconv : (fun k : ℕ => ‖denFactor b z k - 1‖)
      = fun k : ℕ => ‖Complex.exp (-((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1)
          + 2 * (Real.pi : ℂ) * z / b)‖ := by
    funext k; unfold denFactor; rw [add_sub_cancel_left]
  rw [hconv]
  have hc : (-(2 * (Real.pi : ℂ) * I) / b ^ 2).re < 0 := by
    have h1 : (-(2 * (Real.pi : ℂ) * I) / b ^ 2).re
        = -(2 * Real.pi * (b ^ 2).im) / Complex.normSq (b ^ 2) := by
      simp [Complex.div_re, Complex.mul_re, Complex.mul_im, neg_div]
    have hns : 0 < Complex.normSq (b ^ 2) :=
      Complex.normSq_pos.mpr (fun h => by simp [h] at hβ)
    rw [h1]; have : (0 : ℝ) < 2 * Real.pi * (b ^ 2).im := by positivity
    exact div_neg_of_neg_of_pos (by linarith) hns
  have hnorm : (fun k : ℕ =>
      ‖Complex.exp (-((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1) + 2 * (Real.pi : ℂ) * z / b)‖)
      = fun k => Real.exp (-((Real.pi : ℂ) * I) / b ^ 2 + 2 * (Real.pi : ℂ) * z / b).re
          * Real.exp (-(2 * (Real.pi : ℂ) * I) / b ^ 2).re ^ k := by
    funext k
    rw [show -((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1) + 2 * (Real.pi : ℂ) * z / b
        = (-((Real.pi : ℂ) * I) / b ^ 2 + 2 * (Real.pi : ℂ) * z / b)
          + (k : ℂ) * (-(2 * (Real.pi : ℂ) * I) / b ^ 2) from by ring, Complex.norm_exp]
    have hre : ((-((Real.pi : ℂ) * I) / b ^ 2 + 2 * (Real.pi : ℂ) * z / b)
        + (k : ℂ) * (-(2 * (Real.pi : ℂ) * I) / b ^ 2)).re
        = (-((Real.pi : ℂ) * I) / b ^ 2 + 2 * (Real.pi : ℂ) * z / b).re
          + (k : ℝ) * (-(2 * (Real.pi : ℂ) * I) / b ^ 2).re := by
      simp [Complex.add_re, Complex.mul_re, Complex.natCast_re, Complex.natCast_im]
    rw [hre, Real.exp_add, Real.exp_nat_mul]
  rw [hnorm]
  exact (summable_geometric_of_lt_one (Real.exp_pos _).le
    (Real.exp_lt_one_iff.mpr hc)).mul_left _

/-- **G1 (numerator upper bound).** Off the `b`-zero-lattice (all `numFactor` nonzero), the
numerator product is bounded by `exp` of the summed factor-log-norms. -/
theorem norm_tprod_numFactor_le (b z : ℂ) (hβ : 0 < (b ^ 2).im)
    (hnz : ∀ k, numFactor b z k ≠ 0) :
    ‖∏' k, numFactor b z k‖ ≤ Real.exp (∑' k, ‖numFactor b z k - 1‖) := by
  have hg : Summable (fun k => ‖(fun j => numFactor b z j - 1) k‖) := by
    simpa using summable_norm_numFactor_sub_one b z hβ
  have hkey := norm_tprod_one_add_le hg (g := fun k => numFactor b z k - 1)
    (by intro k; simpa [add_sub_cancel] using hnz k)
  simpa [add_sub_cancel] using hkey

/-- **G1 (denominator upper bound).** Off the dual lattice (all `denFactor` nonzero). -/
theorem norm_tprod_denFactor_le (b z : ℂ) (hβ : 0 < (b ^ 2).im)
    (hnz : ∀ k, denFactor b z k ≠ 0) :
    ‖∏' k, denFactor b z k‖ ≤ Real.exp (∑' k, ‖denFactor b z k - 1‖) := by
  have hg : Summable (fun k => ‖(fun j => denFactor b z j - 1) k‖) := by
    simpa using summable_norm_denFactor_sub_one b z hβ
  have hkey := norm_tprod_one_add_le hg (g := fun k => denFactor b z k - 1)
    (by intro k; simpa [add_sub_cancel] using hnz k)
  simpa [add_sub_cancel] using hkey

/-- **G3 (phiBProd strip bound).** Given a denominator **lower** bound `δ > 0` (the G2
obligation), the ratio `phiBProd = num/den` is bounded on the strip by
`exp(∑' ‖numFactorₖ − 1‖)/δ`. Off the `b`-zero-lattice for the numerator; the `δ`
hypothesis carries the denominator's non-vanishing. -/
theorem norm_phiBProd_le_of_den_lower (b z : ℂ) (hβ : 0 < (b ^ 2).im)
    (hnum_nz : ∀ k, numFactor b z k ≠ 0)
    {δ : ℝ} (hδ : 0 < δ) (hden : δ ≤ ‖∏' k, denFactor b z k‖) :
    ‖phiBProd b z‖ ≤ Real.exp (∑' k, ‖numFactor b z k - 1‖) / δ := by
  rw [phiBProd, norm_div]
  exact div_le_div₀ (by positivity) (norm_tprod_numFactor_le b z hβ hnum_nz) hδ hden

end QOU.QBeta.PhiBProdStripBound
