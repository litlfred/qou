import QOU.Mathlib.SYTFrobeniusDim
import QOU.Mathlib.SYTHookFormulaGeneral

/-!
# QOU.Mathlib.SYTFrobeniusKeystone — the divisor-free keystone identity for general (A)

`SYTFrobeniusDim` defined the manifestly-integer `frobeniusDim λ = Σ_σ sgn(σ)·multinomial(n; …)` and
`decide`-verified `dimHLF = frobeniusDim` for `n ≤ 5`.  This file pins the **divisor-free keystone**
that, proved in general, closes integrality *and* `dimHLF = frobeniusDim` *and* (with the merged
2-row machinery's Pascal step generalised) obligation (A):

    frobeniusDim l · betaFactProd l  =  (sz l)! · betaProdGap l                 (over ℤ)

`decide`-verified here for `n ≤ 5` (regression backstop).  Why this single identity suffices:

* the hook side `prodHooks l · betaProdGap l = betaFactProd l` is already sorry-free
  (`SYTHookFormulaBetaProd.prodHooks_mul_betaGapProd`).  Substituting it and cancelling the positive
  `betaProdGap` gives `frobeniusDim l · prodHooks l = (sz l)!`, hence **`prodHooks l ∣ (sz l)!`
  (integrality)** and **`dimHLF l = (sz l)!/prodHooks l = frobeniusDim l`** — both for free.

## The general proof (step 2b — the Matrix.det core)

Writing `β_i = l_i + (m−1−i)` and using `l_i − i + σ(i) = β_i − (m−1−σ(i))`, each multinomial term's
`β_i!/(l_i − i + σ(i))!` is the falling factorial `(β_i)_{m−1−σ(i)}`, so after cancelling the common
`(sz l)!` the identity becomes the **falling-factorial determinant = Vandermonde**:

    det( (β_i)_{falling, m−1−j} )_{i,j}  =  ∏_{i<j} (β_i − β_j)  =  betaProdGap l.

This is `Matrix.det_vandermonde` composed with the **unitriangular** column change from falling
factorials `(x)_{m−1}, …, (x)_0` to monomials `x^{m−1}, …, x^0` (which preserves the determinant).
The two remaining sub-tasks are (i) bridging `frobeniusDim`'s `allPerms` sum to `Matrix.det`'s
`Equiv.Perm` sum, and (ii) the falling-factorial→Vandermonde column reduction.  This is the multi-day
`Matrix.det` formalization flagged in bean `sy7b`; it wants a working LSP (the `lake`-destructive
sandbox makes `m×m` determinant proofs impractical via blind recompile-iteration).

Pure ℕ/ℤ combinatorics; nothing archimedean.
-/

namespace QOU.Mathlib.SYTEnum

open QOU.BraidKnot.IdentityI (sz)

/-- **Divisor-free keystone, `decide`-verified for `n ≤ 4` (sorry-free).**
`frobeniusDim l · betaFactProd l = (sz l)! · betaProdGap l`. -/
theorem frobeniusDim_betaFactProd_le4 :
    ∀ l ∈ shapesLE4,
      frobeniusDim l * (betaFactProd l : ℤ) = ((sz l).factorial : ℤ) * (betaProdGap l : ℤ) := by
  decide

set_option maxRecDepth 20000 in
/-- **Divisor-free keystone, `decide`-verified for `n = 5` (sorry-free).** -/
theorem frobeniusDim_betaFactProd_5 :
    ∀ l ∈ shapes5,
      frobeniusDim l * (betaFactProd l : ℤ) = ((sz l).factorial : ℤ) * (betaProdGap l : ℤ) := by
  decide

end QOU.Mathlib.SYTEnum
