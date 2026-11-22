import Mathlib.Analysis.Complex.LocallyUniformLimit
import QOU.QBeta.PhiBProdFactorAnalytic

/-!
# Local-uniform limit of analytic functions is analytic (infinite-product-analyticity infra)

The second half of the infinite-product-analyticity gap for `phiBProd` (input 1). The first
half — each factor entire, every finite partial product entire — is
`PhiBProdFactorAnalytic` (merged). This file supplies the **analytic-limit step**:

* `analyticOnNhd_of_tendstoLocallyUniformlyOn` — a sequence of functions analytic on an open
  set `s ⊆ ℂ` that converges **locally uniformly** to `g` has analytic limit `g`. Proof:
  the limit is holomorphic (`TendstoLocallyUniformlyOn.differentiableOn`, the Weierstrass
  convergence theorem) and holomorphic-on-open ⇒ analytic (`DifferentiableOn.analyticOnNhd`,
  the Cauchy-integral bridge).

Applied to `phiBProd`: the partial products `∏_{k<n} numFactor b · k` are entire
(`PhiBProdFactorAnalytic.analyticOnNhd_numPartial`), so **if** they converge locally
uniformly to `fun z => ∏' k, numFactor b z k`, that infinite product is entire —
discharging the `AnalyticOnNhd` hypothesis of `PhiBProdMeromorphic.phiBProd_meromorphicOn_of_analytic`
(input 1). The sole remaining input is that local-uniform convergence
(`phiBProd_num_analytic_of_tendsto`, `..._den_...`), available in principle from `PhiBProd`'s
geometric `Multipliable` bounds for `Im b² > 0`.

Verified `lean`-direct against the Mathlib `LocallyUniformLimit` + `Complex.Analytic` cones
(built from pinned source) + `PhiBProd`. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-25-faddeev-uniqueness-keystone-state.md
-/

open Set Filter Topology
open QOU.MathlibExt.PhiBProd

namespace QOU.QBeta.LocalUniformLimitEntire

/-- **Local-uniform limit of analytic functions is analytic** (Weierstrass + Cauchy).
A sequence `F n` analytic on an open `s ⊆ ℂ`, converging locally uniformly to `g`, has an
analytic limit `g`. -/
theorem analyticOnNhd_of_tendstoLocallyUniformlyOn
    {F : ℕ → ℂ → ℂ} {g : ℂ → ℂ} {s : Set ℂ} (hs : IsOpen s)
    (hF : ∀ n, AnalyticOnNhd ℂ (F n) s)
    (hlim : TendstoLocallyUniformlyOn F g Filter.atTop s) :
    AnalyticOnNhd ℂ g s := by
  have hdiff : DifferentiableOn ℂ g s :=
    hlim.differentiableOn (Filter.Eventually.of_forall fun n => (hF n).differentiableOn) hs
  exact hdiff.analyticOnNhd hs

/-- **The numerator infinite product is entire, given local-uniform convergence.** The
partial products `∏_{k ∈ range n} numFactor b · k` are entire (`analyticOnNhd_numPartial`);
if they converge locally uniformly to the `tprod`, that product is entire. -/
theorem phiBProd_num_analytic_of_tendsto (b : ℂ)
    (hconv : TendstoLocallyUniformlyOn
      (fun n z => ∏ k ∈ Finset.range n, numFactor b z k)
      (fun z => ∏' k, numFactor b z k) Filter.atTop univ) :
    AnalyticOnNhd ℂ (fun z => ∏' k, numFactor b z k) univ :=
  analyticOnNhd_of_tendstoLocallyUniformlyOn isOpen_univ
    (fun n => PhiBProdFactorAnalytic.analyticOnNhd_numPartial b (Finset.range n)) hconv

/-- **The denominator infinite product is entire, given local-uniform convergence.** -/
theorem phiBProd_den_analytic_of_tendsto (b : ℂ)
    (hconv : TendstoLocallyUniformlyOn
      (fun n z => ∏ k ∈ Finset.range n, denFactor b z k)
      (fun z => ∏' k, denFactor b z k) Filter.atTop univ) :
    AnalyticOnNhd ℂ (fun z => ∏' k, denFactor b z k) univ :=
  analyticOnNhd_of_tendstoLocallyUniformlyOn isOpen_univ
    (fun n => PhiBProdFactorAnalytic.analyticOnNhd_denPartial b (Finset.range n)) hconv

end QOU.QBeta.LocalUniformLimitEntire
