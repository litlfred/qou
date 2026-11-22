import QOU.QBeta.PhiBProdStripBound
import Mathlib.Analysis.SpecialFunctions.Log.Summable
import Mathlib.Topology.Algebra.InfiniteSum.Field

/-!
# `phiBProd` denominator lower bound ⇒ unconditional strip bound (growth epic, brick G2 + G3)

Route-B brick **G2** of the Faddeev growth-estimate epic (`qou-mz4f`): the denominator
product's **lower** bound, the one genuine estimate the scoping doc flagged. Combined with
G1 (`PhiBProdStripBound`, merged) it discharges the `δ` hypothesis of the conditional G3,
giving the **unconditional** `phiBProd` strip bound.

* `norm_tprod_one_add_ge` (general): `exp(∑' log(1 − ‖gₖ‖)) ≤ ‖∏' (1 + gₖ)‖` when every
  `‖gₖ‖ < 1` — from `‖1 + g‖ ≥ 1 − ‖g‖ > 0`, `log` monotone, and `∏‖·‖ = exp(∑ log‖·‖)`.
* **G2** — `norm_tprod_denFactor_ge`: the denominator lower bound, valid where every
  `‖denFactorₖ − 1‖ < 1` (deep-strip regime, e.g. large `Im z` in the dual direction).
* **G3 unconditional** — `norm_phiBProd_le`: `‖phiBProd b z‖ ≤ exp(∑' ‖numFactorₖ − 1‖) ·
  exp(−∑' log(1 − ‖denFactorₖ − 1‖))`, with **no carried `δ` hypothesis** — the denominator
  lower bound supplies it internally.

Verified `lean`-direct against the pinned Mathlib `Log.Summable` + `InfiniteSum.Field`
cones + `PhiBProd`. Sorry-free.

-- Ref: [leitner2026] docs/workplans/2026-07-26-faddeev-growth-estimate-epic-scope.md
-/

open Complex
open QOU.MathlibExt.PhiBProd
open QOU.QBeta.PhiBProdStripBound

namespace QOU.QBeta.PhiBProdStripLowerBound

/-- **General product-norm lower bound.** For a norm-summable complex family `g` with every
`‖gₖ‖ < 1`, `exp(∑' k, log(1 − ‖gₖ‖)) ≤ ‖∏' k, (1 + gₖ)‖`. Proof: `‖∏‖ = ∏‖·‖`; each
`‖1 + gₖ‖ ≥ 1 − ‖gₖ‖ > 0`; `log` monotone; `∏‖1+gₖ‖ = exp(∑ log‖1+gₖ‖)`. -/
theorem norm_tprod_one_add_ge {g : ℕ → ℂ} (hg : Summable (fun k => ‖g k‖))
    (hsmall : ∀ k, ‖g k‖ < 1) :
    Real.exp (∑' k, Real.log (1 - ‖g k‖)) ≤ ‖∏' k, (1 + g k)‖ := by
  have hmul : Multipliable (fun k => 1 + g k) := multipliable_one_add_of_summable hg
  rw [hmul.norm_tprod]
  have hpos2 : ∀ k, 0 < 1 - ‖g k‖ := fun k => by linarith [hsmall k]
  have hge : ∀ k, 1 - ‖g k‖ ≤ ‖1 + g k‖ := by
    intro k
    have h := norm_sub_norm_le (1 : ℂ) (-g k)
    simp only [norm_one, norm_neg, sub_neg_eq_add] at h
    exact h
  have hpos1 : ∀ k, 0 < ‖1 + g k‖ := fun k => lt_of_lt_of_le (hpos2 k) (hge k)
  have hlogsum1 : Summable (fun k => Real.log ‖1 + g k‖) := hg.summable_log_norm_one_add
  have hlogsum2 : Summable (fun k => Real.log (1 - ‖g k‖)) := by
    have h := Real.summable_log_one_add_of_summable (f := fun k => -‖g k‖) hg.neg
    simpa [sub_eq_add_neg] using h
  have heq : ∏' k, ‖1 + g k‖ = Real.exp (∑' k, Real.log ‖1 + g k‖) :=
    (Real.rexp_tsum_eq_tprod hpos1 hlogsum1).symm
  rw [heq]
  exact Real.exp_le_exp.mpr
    (Summable.tsum_le_tsum (fun k => Real.log_le_log (hpos2 k) (hge k)) hlogsum2 hlogsum1)

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

/-- **G2 (denominator lower bound).** In the deep-strip regime where every
`‖denFactorₖ − 1‖ < 1`, the denominator product is bounded below by
`exp(∑' log(1 − ‖denFactorₖ − 1‖)) > 0`. -/
theorem norm_tprod_denFactor_ge (b z : ℂ) (hβ : 0 < (b ^ 2).im)
    (hsmall : ∀ k, ‖denFactor b z k - 1‖ < 1) :
    Real.exp (∑' k, Real.log (1 - ‖denFactor b z k - 1‖)) ≤ ‖∏' k, denFactor b z k‖ := by
  have hg : Summable (fun k => ‖(fun j => denFactor b z j - 1) k‖) := by
    simpa using summable_norm_denFactor_sub_one b z hβ
  have hkey := norm_tprod_one_add_ge hg (g := fun k => denFactor b z k - 1)
    (by simpa using hsmall)
  simpa [add_sub_cancel] using hkey

/-- **G3 (unconditional `phiBProd` strip bound).** In the deep-strip regime (numerator off
its zero lattice, denominator factors `< 1` in norm), `phiBProd = num/den` obeys the explicit
two-sided-product strip bound with **no carried `δ`** — the denominator lower bound G2
supplies it. -/
theorem norm_phiBProd_le (b z : ℂ) (hβ : 0 < (b ^ 2).im)
    (hnum_nz : ∀ k, numFactor b z k ≠ 0)
    (hden_small : ∀ k, ‖denFactor b z k - 1‖ < 1) :
    ‖phiBProd b z‖
      ≤ Real.exp (∑' k, ‖numFactor b z k - 1‖)
        / Real.exp (∑' k, Real.log (1 - ‖denFactor b z k - 1‖)) := by
  exact norm_phiBProd_le_of_den_lower b z hβ hnum_nz (Real.exp_pos _)
    (norm_tprod_denFactor_ge b z hβ hden_small)

end QOU.QBeta.PhiBProdStripLowerBound
