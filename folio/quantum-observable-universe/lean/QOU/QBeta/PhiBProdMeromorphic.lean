import QOU.MathlibExt.PhiBProd
import Mathlib.Analysis.Meromorphic.Divisor

/-!
# `phiBProd` is meromorphic ⇐ its two products are analytic (brick toward `qou-7xvy`)

The divisor route to the Faddeev–Volkov uniqueness `hr_entire` input
(`QOU.QBeta.RatioEntireOfSameDivisor.entire_toMeromorphicNFOn_div_of_same_order`)
needs, for the concrete `Φ_b = phiBProd`, three facts: `MeromorphicOn (phiBProd b)`,
`meromorphicOrderAt (phiBProd b) ≠ ⊤`, and the same-divisor premise. This file
discharges the **first** of the three, reducing it to a single, honest, Mathlib-shaped
analytic input.

`phiBProd b = (fun z ↦ ∏' k, numFactor b z k) / (fun z ↦ ∏' k, denFactor b z k)` is a
quotient of two infinite products (definitionally). So

> if each product is **analytic on `ℂ`** (`AnalyticOnNhd`), then `phiBProd b` is
> **meromorphic on `ℂ`** — an analytic function divided by an analytic function is
> meromorphic (`AnalyticOnNhd.meromorphicOn` + `MeromorphicOn.div`).

The remaining open input is exactly **analyticity of the two `tprod`s** — i.e. *a
locally-uniformly-convergent infinite product of entire functions is entire*. `PhiBProd`
already proves the products are **`Multipliable`** (pointwise convergence, geometric
bounds for `Im b² > 0`); upgrading `Multipliable` to `AnalyticOnNhd` is the
infinite-product-analyticity fact that Mathlib does not yet package, and it is the honest
§3b-cond hypothesis carried here — **not** axiomatised, and strictly weaker than the
conclusion (analyticity of the factors, not proportionality of solutions).

Verified `lean`-direct against the pinned Meromorphic cone (`AnalyticOnNhd.meromorphicOn`,
`MeromorphicOn.div`) + `PhiBProd`. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-25-faddeev-uniqueness-keystone-state.md
-/

open Set
open QOU.MathlibExt.PhiBProd

namespace QOU.QBeta.PhiBProdMeromorphic

/-- **`phiBProd` is meromorphic on `ℂ` given analyticity of its two products.**
`phiBProd b = num / den` with `num z = ∏' k, numFactor b z k`,
`den z = ∏' k, denFactor b z k`; an analytic-÷-analytic quotient is meromorphic. This
discharges the `MeromorphicOn` input of the divisor-route brick (c) for the concrete
`Φ_b`, leaving only `AnalyticOnNhd` of the products (the infinite-product-analyticity
input) open. -/
theorem phiBProd_meromorphicOn_of_analytic
    (b : ℂ)
    (hnum : AnalyticOnNhd ℂ (fun z => ∏' k, numFactor b z k) univ)
    (hden : AnalyticOnNhd ℂ (fun z => ∏' k, denFactor b z k) univ) :
    MeromorphicOn (phiBProd b) univ := by
  have hfun : phiBProd b
      = (fun z => ∏' k, numFactor b z k) / (fun z => ∏' k, denFactor b z k) := by
    funext z; rfl
  rw [hfun]
  exact hnum.meromorphicOn.div hden.meromorphicOn

end QOU.QBeta.PhiBProdMeromorphic
