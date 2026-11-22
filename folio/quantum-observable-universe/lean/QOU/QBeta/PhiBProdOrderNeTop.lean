import QOU.MathlibExt.PhiBProd
import Mathlib.Analysis.Meromorphic.Divisor

/-!
# `phiBProd` is not locally zero ⇐ its two products are not locally zero (input 2 of 3)

The divisor route to the Faddeev–Volkov uniqueness `hr_entire` input
(`QOU.QBeta.RatioEntireOfSameDivisor.entire_toMeromorphicNFOn_div_of_same_order`, and the
capstone `FaddeevUniquenessCapstone.faddeevPhi_proportional_of_same_divisor`) needs, for
the concrete reference `Φ_b = phiBProd`, the hypothesis
`∀ z, meromorphicOrderAt (phiBProd b) z ≠ ⊤` — i.e. `phiBProd` is **not locally identically
zero** at any point (`ord = ⊤ ⇔ eventually zero`).

Since `phiBProd b = num / den` and `meromorphicOrderAt` is additive under products/inverses,

> `ord (phiBProd b) = ord num − ord den`,

which is `≠ ⊤` exactly when **both** products have finite order — i.e. neither the
numerator nor the denominator product is locally identically zero. This file reduces
input 2 to that single honest fact, `WithTop`-arithmetic closing the `≠ ⊤` from
`WithTop.add_ne_top` + `LinearOrderedAddCommGroupWithTop.neg_eq_top`.

Companion to `PhiBProdMeromorphic.phiBProd_meromorphicOn_of_analytic` (input 1). The two
together leave only input 3 (same divisor) + the shared open analytic input
(infinite-product analyticity / non-vanishing of the products) for the concrete `Φ_b`.

Verified `lean`-direct against the pinned Meromorphic cone + `PhiBProd`. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-25-faddeev-uniqueness-keystone-state.md
-/

open Set
open QOU.MathlibExt.PhiBProd

namespace QOU.QBeta.PhiBProdOrderNeTop

/-- **`phiBProd` has finite meromorphic order given both products are locally nonzero.**
If the numerator and denominator products are meromorphic on `ℂ` and neither is locally
identically zero (`meromorphicOrderAt … ≠ ⊤`), then `meromorphicOrderAt (phiBProd b) z ≠ ⊤`
at every `z`. This discharges input 2 of the divisor-route brick (c) for the concrete
`Φ_b`, reducing it to non-vanishing of the two products. -/
theorem phiBProd_order_ne_top_of_products
    (b : ℂ)
    (hnumM : MeromorphicOn (fun z => ∏' k, numFactor b z k) univ)
    (hdenM : MeromorphicOn (fun z => ∏' k, denFactor b z k) univ)
    (hnum0 : ∀ z, meromorphicOrderAt (fun z => ∏' k, numFactor b z k) z ≠ ⊤)
    (hden0 : ∀ z, meromorphicOrderAt (fun z => ∏' k, denFactor b z k) z ≠ ⊤)
    (z : ℂ) :
    meromorphicOrderAt (phiBProd b) z ≠ ⊤ := by
  have hfun : phiBProd b
      = (fun z => ∏' k, numFactor b z k) / (fun z => ∏' k, denFactor b z k) := by
    funext z; rfl
  rw [hfun, div_eq_mul_inv,
      meromorphicOrderAt_mul (hnumM z (mem_univ z)) (hdenM z (mem_univ z)).inv,
      meromorphicOrderAt_inv]
  refine WithTop.add_ne_top.mpr ⟨hnum0 z, ?_⟩
  rw [ne_eq, LinearOrderedAddCommGroupWithTop.neg_eq_top]
  exact hden0 z

end QOU.QBeta.PhiBProdOrderNeTop
