import QOU.QBeta.PhiBProdProductConvergence
import QOU.QBeta.PhiBProdDivisor
import QOU.QBeta.PhiBProdOrderNeTop
import Mathlib.Analysis.Analytic.IsolatedZeros
import Mathlib.Analysis.Analytic.Uniqueness
import Mathlib.Analysis.Meromorphic.Order

/-!
# `phiBProd`'s zeros are isolated (G5 specialization: discharges `hΦ₂_iso`)

Discharges the `hΦ₂_iso` input of `FaddeevStripGrowthUniqueness.faddeevPhi_proportional_of_stripGrowth`
for the concrete substrate `phiBProd`: `∀ z, ∀ᶠ w in 𝓝[≠] z, phiBProd b w ≠ 0`.

The chain, all on the branch `Im b² > 0`:
1. **Non-vanishing witness at `z = 0`.** Each `numFactor b 0 k` / `denFactor b 0 k` is nonzero:
   the exponent's real part is `< 0` (`Re(πi b²(2k+1)) = −π·Im(b²)·(2k+1)` for the numerator;
   the modular-dual sign for the denominator), so `‖exp‖ < 1 = ‖−1‖`, hence `1 + exp ≠ 0`. By
   `tprod_{num,den}Factor_ne_zero` (PR #4304), the two products are nonzero at `0`.
2. **Products have order ≠ ⊤.** Each product is entire (`analyticOnNhd_{num,den}_tprod`, #4296)
   and not identically zero (step 1), so by the identity theorem it is not locally zero at any
   `z`; `meromorphicOrderAt_ne_top_iff_eventually_ne_zero` gives order ≠ ⊤ everywhere.
3. **`phiBProd` order ≠ ⊤** via `phiBProd_order_ne_top_of_products` (#4225).
4. **Zeros isolated** via `meromorphicOrderAt_ne_top_iff_eventually_ne_zero` again, now for
   `phiBProd`.

Verified `lean`-direct against the pinned Mathlib cones + the merged `phiBProd` chain.
Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-26-faddeev-keystone-7xvy-canonical-arc.md
-/

open Complex Filter Topology Set
open QOU.MathlibExt.PhiBProd
open QOU.QBeta.PhiBProdProductConvergence
open QOU.QBeta.PhiBProdDivisor

namespace QOU.QBeta.PhiBProdZeroIsolation

/-- Each numerator factor is nonzero at `z = 0`: the exponent's real part
`−π·Im(b²)·(2k+1) < 0`, so `‖exp‖ < 1 = ‖−1‖`. -/
theorem numFactor_zero_ne_zero (b : ℂ) (hβ : 0 < (b ^ 2).im) (k : ℕ) :
    numFactor b 0 k ≠ 0 := by
  unfold numFactor
  have hre : ((Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1) + 2 * (Real.pi : ℂ) * b * 0).re
      = -(Real.pi * (b ^ 2).im * (2 * k + 1)) := by
    simp [Complex.add_re, Complex.mul_re, Complex.mul_im]
  have hnorm : ‖Complex.exp ((Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * b * 0)‖ < 1 := by
    rw [Complex.norm_exp, hre]
    apply Real.exp_lt_one_iff.mpr
    have : (0 : ℝ) < Real.pi * (b ^ 2).im * (2 * k + 1) := by positivity
    linarith
  intro h
  have he : Complex.exp ((Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * b * 0) = -1 := by linear_combination h
  rw [he] at hnorm; simp at hnorm

/-- Each denominator factor is nonzero at `z = 0` (modular-dual sign). -/
theorem denFactor_zero_ne_zero (b : ℂ) (hβ : 0 < (b ^ 2).im) (k : ℕ) :
    denFactor b 0 k ≠ 0 := by
  unfold denFactor
  have hns : 0 < Complex.normSq (b ^ 2) :=
    Complex.normSq_pos.mpr (fun h => by simp [h] at hβ)
  have hre : (-((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1) + 2 * (Real.pi : ℂ) * 0 / b).re
      = -(Real.pi * (b ^ 2).im * (2 * k + 1)) / Complex.normSq (b ^ 2) := by
    simp [Complex.add_re, Complex.div_re, Complex.mul_re, Complex.mul_im, Complex.normSq]
    ring
  have hnorm : ‖Complex.exp (-((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * 0 / b)‖ < 1 := by
    rw [Complex.norm_exp, hre]
    apply Real.exp_lt_one_iff.mpr
    have hnum : (0 : ℝ) < Real.pi * (b ^ 2).im * (2 * k + 1) := by positivity
    exact div_neg_of_neg_of_pos (by linarith) hns
  intro h
  have he : Complex.exp (-((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * 0 / b) = -1 := by linear_combination h
  rw [he] at hnorm; simp at hnorm

/-- The numerator product has order ≠ ⊤ everywhere: entire and (via the `z = 0` witness) not
identically zero, so not locally zero at any `z`. -/
theorem num_order_ne_top (b : ℂ) (hβ : 0 < (b ^ 2).im) (z : ℂ) :
    meromorphicOrderAt (fun z => ∏' k, numFactor b z k) z ≠ ⊤ := by
  have hana : AnalyticOnNhd ℂ (fun z => ∏' k, numFactor b z k) univ :=
    analyticOnNhd_num_tprod b hβ
  have hanaz : AnalyticAt ℂ (fun z => ∏' k, numFactor b z k) z := hana z (mem_univ z)
  rcases hanaz.eventually_eq_zero_or_eventually_ne_zero with hzero | hne
  · exfalso
    have heqOn : EqOn (fun z => ∏' k, numFactor b z k) 0 univ :=
      hana.eqOn_zero_of_preconnected_of_eventuallyEq_zero isPreconnected_univ (mem_univ z) hzero
    exact tprod_numFactor_ne_zero b 0 hβ (numFactor_zero_ne_zero b hβ) (heqOn (mem_univ 0))
  · rw [meromorphicOrderAt_ne_top_iff_eventually_ne_zero hanaz.meromorphicAt]; exact hne

/-- The denominator product has order ≠ ⊤ everywhere. -/
theorem den_order_ne_top (b : ℂ) (hβ : 0 < (b ^ 2).im) (z : ℂ) :
    meromorphicOrderAt (fun z => ∏' k, denFactor b z k) z ≠ ⊤ := by
  have hana : AnalyticOnNhd ℂ (fun z => ∏' k, denFactor b z k) univ :=
    analyticOnNhd_den_tprod b hβ
  have hanaz : AnalyticAt ℂ (fun z => ∏' k, denFactor b z k) z := hana z (mem_univ z)
  rcases hanaz.eventually_eq_zero_or_eventually_ne_zero with hzero | hne
  · exfalso
    have heqOn : EqOn (fun z => ∏' k, denFactor b z k) 0 univ :=
      hana.eqOn_zero_of_preconnected_of_eventuallyEq_zero isPreconnected_univ (mem_univ z) hzero
    exact tprod_denFactor_ne_zero b 0 hβ (denFactor_zero_ne_zero b hβ) (heqOn (mem_univ 0))
  · rw [meromorphicOrderAt_ne_top_iff_eventually_ne_zero hanaz.meromorphicAt]; exact hne

/-- **`phiBProd`'s order is finite everywhere** (branch `Im b² > 0`). -/
theorem phiBProd_order_ne_top (b : ℂ) (hβ : 0 < (b ^ 2).im) (z : ℂ) :
    meromorphicOrderAt (phiBProd b) z ≠ ⊤ :=
  PhiBProdOrderNeTop.phiBProd_order_ne_top_of_products b
    (analyticOnNhd_num_tprod b hβ).meromorphicOn (analyticOnNhd_den_tprod b hβ).meromorphicOn
    (num_order_ne_top b hβ) (den_order_ne_top b hβ) z

/-- **`phiBProd`'s zeros are isolated** (branch `Im b² > 0`): `∀ z, ∀ᶠ w in 𝓝[≠] z,
phiBProd b w ≠ 0`. This discharges the `hΦ₂_iso` input of the G5 uniqueness assembly. -/
theorem phiBProd_eventually_ne_zero (b : ℂ) (hβ : 0 < (b ^ 2).im) (z : ℂ) :
    ∀ᶠ w in 𝓝[≠] z, phiBProd b w ≠ 0 := by
  have hmer : MeromorphicAt (phiBProd b) z := phiBProd_meromorphicOn b hβ z (mem_univ z)
  exact (meromorphicOrderAt_ne_top_iff_eventually_ne_zero hmer).mp (phiBProd_order_ne_top b hβ z)

end QOU.QBeta.PhiBProdZeroIsolation
