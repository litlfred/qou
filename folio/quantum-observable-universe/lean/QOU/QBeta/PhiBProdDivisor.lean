import QOU.MathlibExt.PhiBProd
import Mathlib.Analysis.SpecialFunctions.Log.Summable

/-!
# `phiBProd`'s products have no spurious zeros (divisor-rigidity narrowing)

Formalize-first narrowing of the sole remaining keystone input (`qou-7xvy`). Input 1
(#4296) closed `MeromorphicOn (phiBProd b)` via the infinite-product-analyticity route.
The remaining open input is the **divisor rigidity** of the physical `Φ_b`: that the ratio
`Ψ / phiBProd` of two solutions is entire (`hr_entire`) / bounded (`hbdd`) — which needs
the state-integral growth estimate.

This file supplies the **`phiBProd`-side half** of that divisor computation, unconditionally
on the branch `Im b² > 0`: the two infinite products are **nonzero wherever all their
factors are nonzero** — a convergent product `∏(1 + fₖ)` with `∑‖fₖ‖ < ∞` and no vanishing
factor does not vanish (`tprod_one_add_ne_zero_of_summable`). Combined with
`FaddeevQuantumDilogarithm.phi_b_zero` (each vanishing factor is a genuine zero of `Φ_b`),
this pins `phiBProd`'s zero/pole divisor to **exactly** the explicit shifted lattices where
`numFactor` / `denFactor` vanish — no hidden zeros, no hidden poles.

This concretizes the abstract divisor-rigidity hypothesis: the remaining `hr_entire` input
is now "`Ψ` vanishes exactly on `phiBProd`'s explicit `b`-lattice and has poles exactly on
the dual lattice", a checkable statement about `Ψ`, rather than an abstract order match. It
does **not** close the input (the `Ψ`-side divisor still needs the growth estimate); it is
the honest, formalizable narrowing.

Verified `lean`-direct against the pinned Mathlib `Log.Summable` cone + `PhiBProd`. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-25-faddeev-uniqueness-keystone-state.md
-/

open Complex
open QOU.MathlibExt.PhiBProd

namespace QOU.QBeta.PhiBProdDivisor

/-- Summability of the numerator factor exponentials' norms on the branch `Im b² > 0`
(the geometric `q`-suppression, `Re(2πi b²) < 0`). -/
private theorem summable_norm_numExp (b z : ℂ) (hβ : 0 < (b ^ 2).im) :
    Summable (fun k : ℕ =>
      ‖Complex.exp ((Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1)
        + 2 * (Real.pi : ℂ) * b * z)‖) := by
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

/-- Summability of the denominator (modular-dual) factor exponentials' norms
(`Re(−2πi/b²) < 0` on the branch). -/
private theorem summable_norm_denExp (b z : ℂ) (hβ : 0 < (b ^ 2).im) :
    Summable (fun k : ℕ =>
      ‖Complex.exp (-((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1)
        + 2 * (Real.pi : ℂ) * z / b)‖) := by
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

/-- **The numerator product has no spurious zeros.** On the branch `Im b² > 0`, if every
`numFactor b z k ≠ 0` (i.e. `z` is off the `b`-zero-lattice), the whole product
`∏' k, numFactor b z k ≠ 0`. So `phiBProd`'s numerator vanishes *exactly* where a factor
does — no hidden zeros. -/
theorem tprod_numFactor_ne_zero (b z : ℂ) (hβ : 0 < (b ^ 2).im)
    (hz : ∀ k, numFactor b z k ≠ 0) :
    (∏' k, numFactor b z k) ≠ 0 :=
  tprod_one_add_ne_zero_of_summable hz (summable_norm_numExp b z hβ)

/-- **The denominator product has no spurious zeros** (hence `phiBProd` has no spurious
poles). On the branch `Im b² > 0`, if every `denFactor b z k ≠ 0` (`z` off the dual
lattice), then `∏' k, denFactor b z k ≠ 0`. -/
theorem tprod_denFactor_ne_zero (b z : ℂ) (hβ : 0 < (b ^ 2).im)
    (hz : ∀ k, denFactor b z k ≠ 0) :
    (∏' k, denFactor b z k) ≠ 0 :=
  tprod_one_add_ne_zero_of_summable hz (summable_norm_denExp b z hβ)

/-- **`phiBProd` is nonzero off the union of the two lattices.** Where every numerator and
denominator factor is nonzero, `phiBProd b z = (∏ num)/(∏ den) ≠ 0`: it has neither a zero
(numerator nonvanishing) nor a pole (denominator nonvanishing) there. This is the
`phiBProd`-side divisor computation the divisor-rigidity input consumes. -/
theorem phiBProd_ne_zero_off_lattice (b z : ℂ) (hβ : 0 < (b ^ 2).im)
    (hnum : ∀ k, numFactor b z k ≠ 0) (hden : ∀ k, denFactor b z k ≠ 0) :
    phiBProd b z ≠ 0 := by
  rw [phiBProd, div_ne_zero_iff]
  exact ⟨tprod_numFactor_ne_zero b z hβ hnum, tprod_denFactor_ne_zero b z hβ hden⟩

end QOU.QBeta.PhiBProdDivisor
