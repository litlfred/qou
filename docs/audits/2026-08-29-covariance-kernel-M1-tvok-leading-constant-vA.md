# Covariance-kernel epic (`qou-x631`) — M₁>0 machinery `qou-tvok` step 1: the exact leading constant `v_A = 8/π²`

**Date:** 2026-08-29 · **Branch:** `claude/m1-tvok-vA-leading-constant-2026-08-29` · **Tier:** rigorous
closed-form derivation (modulo the cited IO Kerov CLT) + triple numerical verification · **Discipline:**
no fit (derived in closed form, then checked); nothing wired; no `c_k`; L2 unchanged. **Epic:**
`qou-h315`; gap `qou-k5r5`.

## Result

The leading constant of the descent-DPP variance of `Σ|c|` is **exactly**

> **`v_A := lim_{θ→∞} Var(Σ|c|)/θ² = 8/π² = 0.8105694691…`**

This is the first *complete, rigorous* brick of the `qou-tvok` machinery (the explicit finite-n bound
`|V_A/θ² − v_A| ≤ C_A θ^{−p}`): the constant it converges *to* is now pinned in closed form. The
remainder `C_A` + rate is the rest of `qou-tvok`.

## Derivation (rigorous modulo the IO Kerov CLT)

1. **IO Kerov CLT (cited theorem, Ivanov–Olshanski):** for a linear statistic with test function `f`,
   the limiting variance is `Σ_{k≥1} f̂_k² / k`, where `f̂_k = (2/π)∫₀^π f(2cos φ) sin(kφ) sin φ dφ`
   is the modified-Chebyshev coefficient (the #5901 / `κ`-derivation convention). For `Σ|c|` the test
   function is `f(x) = |x|`.

2. **Closed form of the coefficients (elementary integral).** Even `k` vanish (|x| is even); for odd
   `k = 2m+1`,
   > `Â_{2m+1} = 8·(−1)^{m+1} / (π·((2m+1)² − 4))`.
   Derived by splitting `|2cos φ| sin φ = ±sin 2φ` at `φ=π/2` and integrating
   `sin 2φ · sin kφ` (product-to-sum); verified against the numerical integral to `1e-42`.

3. **Hence** `v_A = Σ_{m≥0} Â_{2m+1}²/(2m+1) = (64/π²)·Σ_{n odd≥1} 1/[n(n²−4)²]`.

4. **Elementary rational-series identity (partial fractions + telescoping) — no analysis:**
   > `Σ_{n odd≥1} 1/[n(n²−4)²] = 1/8`.
   With `1/(n(n²−4)²) = 1/(16n) − 1/(32(n−2)) − 1/(32(n+2)) + 1/(32(n−2)²) − 1/(32(n+2)²)`:
   - **Linear parts:** the coefficient of the divergent `Σ_{odd} 1/j` is `1/16 − 1/32 − 1/32 = 0` (it
     **cancels**); the shift boundary terms (`j=−1` entering via `n−2`, and the `j=1` restored via
     `n+2`) leave `1/32 + 1/32 = 1/16`.
   - **Quadratic parts:** the `Σ_{odd} 1/j² = π²/8` **cancels** between the `(n−2)²` and `(n+2)²`
     sums; the boundary terms `1/(−1)²` and `1/1²` leave `(1+1)/32 = 1/16`.
   - **Total `1/16 + 1/16 = 1/8`.** Both the divergent linear tail and the `π²/8` quadratic tail
     cancel exactly, so the result is purely rational.

5. **Therefore** `v_A = (64/π²)·(1/8) = 8/π²`. ∎ (modulo step 1's cited CLT)

## Verification (exact / mpmath 40–60 dps; NO float64)

`wlambda_covariance_epic_M1_tvok_vA_leading_constant.py`, exit 0, all checks pass:

| check | result |
|---|---|
| A. closed-form `Â_k` vs the integral (odd `k≤11`) | agree to `1e-42` |
| B. `Σ_k Â_k²/k` (explicit, to `k=9999`) vs `8/π²` | `8.1e-17` |
| C. `Σ_{n odd} 1/[n(n²−4)²]` vs `1/8` | `0` (exact); partial-fraction termwise `1e-42` |
| D. descent-DPP `V_A/θ²` Richardson vs `8/π²` (independent route) | `9e-8` |

Three independent routes (IO Chebyshev sum, the closed-form rational series, the descent-DPP
measurement) agree on `8/π²`.

## Scope — what this is and is not

- **Is:** the exact leading constant `v_A = 8/π²`, in closed form, derived (not fitted), triple-checked.
  Steps 2 and 4 are fully elementary and Lean-formalizable (step 4's finite partial-fraction identity
  is a `field_simp; ring` fact; the infinite telescoping is a `tsum` manipulation). Step 1 is the cited
  IO CLT.
- **Is not:** the finite-`n` bound. The remainder `|V_A/θ² − v_A| ≤ C_A θ^{−p}` — its constant `C_A`
  and rate `p` (bulk Euler–Maclaurin via `CompositeEulerMaclaurin` + the Airy-edge term via the
  Gaussian bounds) — remains open in `qou-tvok`; the sub-leading exponent is still undetermined
  (PR #5939 retraction). This brick pins the *target* of that bound.

## Compute

- [`wlambda_covariance_epic_M1_tvok_vA_leading_constant.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_tvok_vA_leading_constant.py)
  (exit 0; NO float64).

## Cross-references

- Machinery inventory + route: [`2026-08-29-covariance-kernel-M1-machinery-inventory-and-route.md`](2026-08-29-covariance-kernel-M1-machinery-inventory-and-route.md)
- Kink-cancellation retraction (why the sub-leading exponent is open): [`2026-08-29-covariance-kernel-M1-debye-kink-cancellation.md`](2026-08-29-covariance-kernel-M1-debye-kink-cancellation.md)
- Epic `qou-h315`; task `qou-tvok`; gap `qou-k5r5`.
