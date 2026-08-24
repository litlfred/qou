import QOU.SchurWeyl.SeminormalParam
import QOU.Mathlib.LagrangeCoeffSum

/-!
# QOU.SchurWeyl.SeminormalNodeForm — the seminormal entry in node coordinates

`sum_prod_qratio_weighted` proves the arithmetic the Markov property needs, with the seminormal
(Hoefsmit) entry appearing as the weight `Q·x_a/(Q·x_a − x_b)`.  This file is the translation: that
weight **is** `seminormalParam`, once the axial distance is written in terms of the nodes
`x_i = Q^{β_i}`.

| | |
|---|---|
| `seminormalParam_node_form` | `a(d) = (q − q⁻¹)·Q·x_a/(Q·x_a − x_b)` when `Q^d·x_b = Q·x_a` |
| `seminormalParam_one'` | the `d = 1` value `q`, in the form the `a = b` term uses |

**The hypothesis `Q^d·x_b = Q·x_a` is the content-to-β dictionary**, and it is where `d = β_a − β_b + 1`
enters: an addable cell in row `a` has content `β_a − (r−1)`, a removable corner in row `b` has
content `β_b − r`, and their difference is `β_a − β_b + 1`.

## Base ring (§7c)

`ℝ`, forced — `seminormalParam` is `ℝ`-valued.  Nothing archimedean is *used*: the proof is a
`field_simp`, and the statement would hold over any field.

LaTeX label: `lem:seminormal-node-form`
-/

namespace QOU.SchurWeyl

open Seminormal

/-- **The seminormal entry, in node coordinates.**

With `x_a`, `x_b` the nodes and `d` the axial distance, `Q^d·x_b = Q·x_a` turns

`a(d) = (q − q⁻¹)/(1 − q^{−2d})`  into  `(q − q⁻¹)·Q·x_a/(Q·x_a − x_b)`,

which is exactly the weight in `QOU.Mathlib.sum_prod_qratio_weighted`. -/
theorem seminormalParam_node_form (q : ℝ) (hq : q ≠ 0) (xa xb : ℝ) (hxb : xb ≠ 0) (d : ℤ)
    (hd : ((q ^ 2 : ℝ)) ^ d * xb = q ^ 2 * xa) (hden : q ^ 2 * xa - xb ≠ 0) :
    seminormalParam q d = (q - q⁻¹) * (q ^ 2 * xa) / (q ^ 2 * xa - xb) := by
  have hq2 : (q ^ 2 : ℝ) ≠ 0 := pow_ne_zero _ hq
  have hzp : (q ^ 2 : ℝ) ^ d ≠ 0 := zpow_ne_zero _ hq2
  have hxa : (q ^ 2 : ℝ) * xa ≠ 0 := by rw [← hd]; exact mul_ne_zero hzp hxb
  have hneg : q ^ (-2 * d) = (((q ^ 2 : ℝ)) ^ d)⁻¹ := by
    have hcast : ((q : ℝ) ^ (2 : ℕ)) = q ^ (2 : ℤ) := (zpow_natCast q 2).symm
    rw [hcast, ← zpow_mul, show (2 : ℤ) * d = -((-2) * d) from by ring, zpow_neg, inv_inv]
  have hxa' : xa ≠ 0 := fun hz => hxa (by rw [hz]; ring)
  have hinv : (((q ^ 2 : ℝ)) ^ d)⁻¹ = xb / (q ^ 2 * xa) := by
    rw [eq_div_iff hxa, ← hd, inv_mul_cancel_left₀ hzp]
  rw [Seminormal.seminormalParam, hneg, hinv,
    show (1 : ℝ) - xb / (q ^ 2 * xa) = (q ^ 2 * xa - xb) / (q ^ 2 * xa) from by field_simp,
    div_div_eq_mul_div]

/-- The `d = 1` value in the shape the `a = b` term of the corner identity produces:
`(q − q⁻¹)·Q/(Q − 1) = q`. -/
theorem seminormalParam_one' (q : ℝ) (hq : q ≠ 0) (hq2 : q ^ 2 - 1 ≠ 0) :
    (q - q⁻¹) * q ^ 2 / (q ^ 2 - 1) = q := by
  field_simp

end QOU.SchurWeyl
