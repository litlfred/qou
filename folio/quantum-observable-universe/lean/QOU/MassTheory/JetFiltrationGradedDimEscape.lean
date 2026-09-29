/-
# Jet-filtration graded dimension ESCAPES the C(A,2) exchange-determinant cap

`QOU.MassTheory.SaturationRhoCap` machine-verified that the isospin-even
exchange-**determinant** cumulant is capped: `ρ_A = b_A/b_2 ≤ C(A,2)`, i.e.
`ρ₃ ≤ 3` and `ρ₄ ≤ 6`.  Because the isospin-corrected strong targets are
`ρ_strong(3) ≈ 3.81 > 3` and `ρ_strong(4) ≈ 13.03 > 6`, **no** `−ln det`
of an exchange matrix reaches them for any `m` (a proved scope-(b) exclusion
of the whole determinant-cumulant family).

This file records the complementary **positive** fact for the genuinely
different (NON-determinant) object of PR #(this branch): the **jet-filtration
graded dimension** — the Poincaré polynomial of the `S_A` coinvariant algebra
/ principal (Coxeter-length) filtration on `H_A(q)`,

    W_A(q) = ∏_{k=1}^{A} [k]_q ,   [k]_q = 1 + q + ⋯ + q^{k−1} ,

with `ρ_grad(A) = W_A(q)/W_2(q)`.  Unlike the sub-extensive `−ln det`, the
graded dimension grows factorially, so it is **not** bounded by `C(A,2)`.

The A=4 ratio is `ρ_grad(4) = [3]_q · [4]_q`.  We prove it is `≥ 12` for every
`q ≥ 1`, hence **strictly exceeds the determinant cap of 6** — the graded
dimension escapes the `SaturationRhoCap` ceiling.  Combined with
`saturation_rho_cap_four` (`det-route ρ₄ ≤ 6`), this exhibits an object that can
reach the strong target `ρ_strong(4) ≈ 13.03`, which the determinant provably
cannot.  Base ring `ℝ` per §7c (an ordering inequality on `1 ≤ q`).

Scope note: this proves the graded dimension **escapes** the cap; it does **not**
claim the graded dimension *lands* the strong targets — the accompanying probe
`deltalambda_jet_filtration_magnitude_probe.py` is an explicit scope-(a) honest
negative (it overshoots the A=3→A=4 growth).  Nothing wired.
-/
import Mathlib.Tactic

namespace QOU.MassTheory

/-- `[3]_q = 1 + q + q²`, the `A=3` graded-dimension ratio `W_3/W_2`. -/
def q3 (q : ℝ) : ℝ := 1 + q + q ^ 2

/-- `[4]_q = 1 + q + q² + q³`. -/
def q4 (q : ℝ) : ℝ := 1 + q + q ^ 2 + q ^ 3

/-- **A=3 graded-dim ratio meets the strong regime `> 3`-threshold direction.**
For `q ≥ 1`, `ρ_grad(3) = [3]_q ≥ 3`; equality at `q = 1` (the classical
coinvariant ratio `3!/2! = 3`).  The strong target `3.81` needs `q > 1`. -/
theorem jet_graded_rho3_ge_three (q : ℝ) (hq : 1 ≤ q) : 3 ≤ q3 q := by
  have h0 : 0 ≤ q - 1 := by linarith
  have : q3 q - 3 = (q - 1) * (q + 2) := by unfold q3; ring
  nlinarith [mul_nonneg h0 (by linarith : (0 : ℝ) ≤ q + 2), this]

/-- **A=4 graded-dim ratio ESCAPES the determinant cap.**
For `q ≥ 1`, `ρ_grad(4) = [3]_q · [4]_q ≥ 12 > 6 = C(4,2)`.  So the
jet-filtration graded dimension strictly exceeds the `SaturationRhoCap`
ceiling `saturation_rho_cap_four` proves for the `−ln det` cumulant — it is a
NON-determinant object that can reach the strong target `ρ_strong(4) ≈ 13.03`
the determinant provably cannot.  Equality `= 12` at `q = 1` (`4!/2! = 12`). -/
theorem jet_graded_rho4_ge_twelve (q : ℝ) (hq : 1 ≤ q) : 12 ≤ q3 q * q4 q := by
  have h0 : 0 ≤ q - 1 := by linarith
  have hq0 : 0 ≤ q := by linarith
  -- (1+q+q²)(1+q+q²+q³) − 12 factors with (q−1) and manifestly non-negative cofactors.
  have key : q3 q * q4 q - 12
      = (q - 1) * (q ^ 4 + 3 * q ^ 3 + 6 * q ^ 2 + 9 * q + 11) := by
    unfold q3 q4; ring
  have hcof : 0 ≤ q ^ 4 + 3 * q ^ 3 + 6 * q ^ 2 + 9 * q + 11 := by positivity
  nlinarith [mul_nonneg h0 hcof, key]

/-- **The escape, stated against the cap constant.** For `q ≥ 1` the
graded-dim A=4 ratio strictly exceeds the determinant cap `6 = C(4,2)`
(`SaturationRhoCap.saturation_rho_cap_four` bounds the `−ln det` ρ₄ by `6`;
here the graded ρ₄ is `≥ 12 > 6`). -/
theorem jet_graded_rho4_exceeds_det_cap (q : ℝ) (hq : 1 ≤ q) :
    (6 : ℝ) < q3 q * q4 q := by
  have := jet_graded_rho4_ge_twelve q hq
  linarith

end QOU.MassTheory
