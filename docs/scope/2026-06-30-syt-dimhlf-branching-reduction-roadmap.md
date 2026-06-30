# sy7b — `dimHLF_branching` reduced to one β-Lagrange identity (roadmap)

**Bean:** `sy7b` (SYT HLF: close `dimAitkenIdentity` via the branching bijection).
**Date:** 2026-06-30. **Status:** roadmap — the proof is multi-session; this records the
exact remaining target and the infra that already exists for it.

## Where the general HLF stands

`SYTBranchingComplete.numSYTenum_eq_dimHLF_of_dimHLF_branching` proves the general
hook-length formula (`numSYTenum = dimHLF`, hence `dimAitkenIdentity`) **conditional on a
single obligation**:

> **(A)** `dimHLF_branching`:  `∀ m` sorted, `0 < sz m`,
> `dimHLF m = branchSum dimHLF m = Σ_{i removable corner} dimHLF (decrementRow m i)`.

Obligation (B), the standard-tableau corner bijection, is **done sorry-free**
(`SYTBranchingComplete.numSYTenum_branching`). Only (A) remains. The 2-row case is proved
(`SYTBranching2Row.dimHLF_branching_pair`); the bounded `decide` backstops reach m ≤ 6
(`SYTHookFormulaGeneral.dimAitkenIdentity_le4/_5/_6`).

## The reduction: (A) ⟺ one rational-function (Lagrange) identity

Work in β-numbers `β_i = λ_i + (m−1−i)` (strictly decreasing, `β_0 > … > β_{m−1} ≥ 0`).
The hook side is already sorry-free
(`SYTHookFormulaGeneral.prodHooks_mul_betaProdGap`:
`prodHooks · betaProdGap = betaFactProd`), so

    dimHLF λ = n! / prodHooks λ = n! · betaProdGap λ / betaFactProd λ
             = n! · ∏_{i<j}(β_i − β_j) / ∏_i β_i! .

Removing the corner in row `i` sends `λ_i → λ_i − 1`, i.e. `n → n−1`, `β_i → β_i − 1`
(others fixed). Hence

    dimHLF(λ − c_i) / dimHLF(λ)
      = (1/n) · β_i · ∏_{j≠i} (β_i − 1 − β_j)/(β_i − β_j) ,

using `(n−1)!/n! = 1/n`, the gap ratio `V(β^{(i)})/V(β) = ∏_{j≠i}(β_i−1−β_j)/(β_i−β_j)`, and
`∏β_j! / ∏β^{(i)}_j! = β_i!/(β_i−1)! = β_i`. **Non-corner rows vanish automatically:** if row
`i` is *not* a removable corner then `β_i − 1 = β_{i+1}`, so the factor `(β_i − 1 − β_{i+1}) = 0`
kills that summand (this is the already-proved `SYTBetaLagrange.betaLagrange_term_zero` /
GNW `betaLagrange_term_zero` mechanism). Summing over **all** `i` therefore equals summing
over corners, and (A) becomes:

> **(A′) — the target identity.** For distinct `β_0 > … > β_{m−1}`,
> `Σ_{i=0}^{m−1} β_i · ∏_{j≠i} (β_i − 1 − β_j)/(β_i − β_j)  =  n`,
> where `n = Σ_i β_i − m(m−1)/2 = Σ_i λ_i`.

This is a pure Lagrange/partial-fractions identity in `ℚ(β)` — **exactly the GNW
`gnwHookIdentity` core** (the sole remaining gap of the GNW route, #3099). So the branching
route and the GNW route bottleneck on the *same* identity (A′); closing (A′) closes both.

## The infra that already exists for (A′)

`SYTBetaLagrange.lean` is the polynomial toolbox built for exactly this:

* `betaLagrange` + `sum_betaVec_sub` (per #3099) already assemble
  `Σ_i β_i · ∏_{j≠i}(β_i−1−β_j)/(vWeight β_i) = sz l` — the **same shape as (A′)** modulo the
  `vWeight` vs the Vandermonde denominator `∏_{j≠i}(β_i − β_j)`.
* `sum_eval_div_eq_of_decomp` + `bigPoly_decomp` — the Lagrange decomposition
  `Σ_i p(β_i)/∏_{j≠i}(β_i−β_j) = leading coeff` for `deg p < k`.
* `sum_shift` : `Σ(β_j + 1) = Σ β_j + k` — the `m(m−1)/2` / `n` bookkeeping on the RHS.
* `betaLagrange_term_zero` — the non-corner vanishing used above.

## Remaining work (the multi-session piece)

1. **Prove (A′)** for general `m` from the `SYTBetaLagrange` machinery: identify the
   numerator polynomial `p(x) = x · ∏_{j}(x − 1 − β_j)/(x − β_j)`-style decomposition, apply
   `sum_eval_div_eq_of_decomp` / `bigPoly_decomp`, and reconcile `vWeight` with the
   Vandermonde denominator. This is the genuine combinatorics-of-`ℚ` core.
2. **Bridge (A′) → (A)** `dimHLF_branching` over `ℕ`: the `dimHLF` are `ℕ`-valued
   factorial/`prodHooks` quotients, so the `ℚ`-identity (A′) must be transported through the
   integrality infra (`dimHLF_pair`-style, `SYTDimHLFPair`) — clearing denominators exactly,
   not via floor division.

**Recommended next-session shape:** prove `dimHLF_branching` *conditional* on a clean
`betaLagrangeIdentity` hypothesis (the §3b-cond scaffold pattern) first — that closes the
general HLF modulo one named `ℚ`-lemma and is independently mergeable — then discharge
`betaLagrangeIdentity` from `SYTBetaLagrange`. Closing (A′) retires the `08a2` keystone's
SYT-dimension half (and the GNW route simultaneously).
