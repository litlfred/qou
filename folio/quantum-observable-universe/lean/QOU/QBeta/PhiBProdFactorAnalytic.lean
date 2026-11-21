import QOU.MathlibExt.PhiBProd
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic
import Mathlib.Analysis.Analytic.Constructions

/-!
# The `phiBProd` factors are entire; finite partial products are entire (input-1 infra)

`PhiBProdMeromorphic.phiBProd_meromorphicOn_of_analytic` (input 1, merged #4223) discharges
`MeromorphicOn (phiBProd b)` *given* that the two infinite products are analytic on `ℂ`.
This file builds the **infrastructure floor** of that hypothesis: each individual factor is
**entire** (a composite `1 + exp(affine in z)`), and every **finite partial product** is
entire (`Finset.analyticOnNhd_prod`).

The remaining gap to the *infinite* product's analyticity is the analytic-limit step —
a locally-uniformly-convergent product of entire functions is entire
(`Mathlib.Analysis.Complex.LocallyUniformLimit`) — plus the partial-products → `tprod`
local-uniform convergence estimate (available from `PhiBProd`'s geometric `Multipliable`
bounds for `Im b² > 0`). This file lands the factor/partial-product half unconditionally;
the convergence half is the named next infra brick.

Verified `lean`-direct against the pinned Mathlib `Complex.Analytic` cone (built from source)
+ `PhiBProd`. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-25-faddeev-uniqueness-keystone-state.md
-/

open Set Complex
open QOU.MathlibExt.PhiBProd

namespace QOU.QBeta.PhiBProdFactorAnalytic

/-- **Each numerator factor `1 + q^{2k+1} e^{2πbz}` is entire**: a constant plus the
exponential of an affine function of `z`. -/
theorem analyticOnNhd_numFactor (b : ℂ) (k : ℕ) :
    AnalyticOnNhd ℂ (fun z => numFactor b z k) univ := by
  unfold numFactor
  have hlin : AnalyticOnNhd ℂ (fun z : ℂ => 2 * (Real.pi : ℂ) * b * z) univ := by
    have h : (fun z : ℂ => 2 * (Real.pi : ℂ) * b * z)
        = fun z : ℂ => (2 * (Real.pi : ℂ) * b) * z := by funext z; ring
    rw [h]
    exact AnalyticOnNhd.mul (analyticOnNhd_const (v := 2 * (Real.pi : ℂ) * b)) analyticOnNhd_id
  have hE : AnalyticOnNhd ℂ (fun z : ℂ =>
      (Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1) + 2 * (Real.pi : ℂ) * b * z) univ :=
    AnalyticOnNhd.add (analyticOnNhd_const (v := _)) hlin
  exact AnalyticOnNhd.add (analyticOnNhd_const (v := (1 : ℂ))) hE.cexp

/-- **Each denominator (modular-dual) factor is entire.** -/
theorem analyticOnNhd_denFactor (b : ℂ) (k : ℕ) :
    AnalyticOnNhd ℂ (fun z => denFactor b z k) univ := by
  unfold denFactor
  have hlin : AnalyticOnNhd ℂ (fun z : ℂ => 2 * (Real.pi : ℂ) * z / b) univ := by
    have h : (fun z : ℂ => 2 * (Real.pi : ℂ) * z / b)
        = fun z : ℂ => (2 * (Real.pi : ℂ) / b) * z := by funext z; ring
    rw [h]
    exact AnalyticOnNhd.mul (analyticOnNhd_const (v := 2 * (Real.pi : ℂ) / b)) analyticOnNhd_id
  have hE : AnalyticOnNhd ℂ (fun z : ℂ =>
      -((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1) + 2 * (Real.pi : ℂ) * z / b) univ :=
    AnalyticOnNhd.add (analyticOnNhd_const (v := _)) hlin
  exact AnalyticOnNhd.add (analyticOnNhd_const (v := (1 : ℂ))) hE.cexp

/-- **Every finite partial numerator product is entire** — a finite product of entire
factors. The `AnalyticOnNhd` of the *infinite* product then reduces to the
local-uniform-limit step. -/
theorem analyticOnNhd_numPartial (b : ℂ) (N : Finset ℕ) :
    AnalyticOnNhd ℂ (fun z => ∏ k ∈ N, numFactor b z k) univ := by
  have heq : (fun z : ℂ => ∏ k ∈ N, numFactor b z k)
      = ∏ n ∈ N, (fun z : ℂ => numFactor b z n) := by
    funext z; rw [Finset.prod_apply]
  rw [heq]
  exact Finset.analyticOnNhd_prod N (fun k _ => analyticOnNhd_numFactor b k)

/-- **Every finite partial denominator product is entire.** -/
theorem analyticOnNhd_denPartial (b : ℂ) (N : Finset ℕ) :
    AnalyticOnNhd ℂ (fun z => ∏ k ∈ N, denFactor b z k) univ := by
  have heq : (fun z : ℂ => ∏ k ∈ N, denFactor b z k)
      = ∏ n ∈ N, (fun z : ℂ => denFactor b z n) := by
    funext z; rw [Finset.prod_apply]
  rw [heq]
  exact Finset.analyticOnNhd_prod N (fun k _ => analyticOnNhd_denFactor b k)

end QOU.QBeta.PhiBProdFactorAnalytic
