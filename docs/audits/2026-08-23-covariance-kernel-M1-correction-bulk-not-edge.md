# Covariance-kernel epic (`qou-x631`) — M₁>0: correcting "edge-sensitive" → bulk-dominated; extend to n≤67

**Date:** 2026-08-23 · **Branch:** `claude/m1-kappa-edge-scaling-2026-08-23` · **Tier:** correction of
a prior characterization + extended exact verification · **Discipline:** scope-(a); no fit; nothing
wired; no `c_k`; L2 unchanged. **Epic:** `qou-x631`; gap `qou-k5r5`.

## Two results

### 1. `M₁ > 0` exact for `60 < n ≤ 67`
The exact `Fraction` covariance gives `κ_n > κ = 128/(225π²)` (hence `M₁ = κ_n·n^{5/2} > 0`) for
**every `13 ≤ n ≤ 67`** — extending the previous `n ≤ 60`. The crossing stays at `n₀ = 13`; the gap
`κ_n − κ` is positive and declining slowly (`≈ 0.001317` at n=65). No sign of recrossing.

### 2. Correcting the "edge-sensitive" label — the dominant correction is **bulk `n^{-1/2}`**, not edge
The [prior audit](2026-08-22-covariance-kernel-M1-sign-attempt-wall.md) guessed the `κ_n − κ`
correction was **edge (Tracy–Widom) dominated**. A scaling estimate shows that is **wrong**:

- **Edge contribution.** The Tracy–Widom edge enters `Σh` through `λ₁² = 4n + 4n^{2/3}χ + …`
  (`χ = TW`, `O(1)`), so `δ(Σh)_edge ~ n^{2/3}χ`. It enters `ω₃ = Σc²` through the extreme content
  `≈ λ₁ ≈ 2√n`: `∂Σc²/∂λ₁ ≈ (2√n)² = 4n`, so `δ(ω₃)_edge ~ 4n·n^{1/6}χ = 4n^{7/6}χ`. Both driven by the
  *same* `χ`, hence `Cov_edge ~ n^{2/3}·n^{7/6} = n^{11/6}`, i.e. **relative order `n^{-2/3}`** vs the
  leader `κn^{5/2}`.
- **Bulk second-order.** The standard CLT correction is relative order `~ n^{-1/2}`.
- **`−2/3 < −1/2`**, so the edge is **subleading**. The dominant correction is **bulk**, and the sign
  question `κ_n → κ` from above is a **bulk second-order Kerov-CLT** statement — *not* a Tracy–Widom
  edge problem. This is meaningfully more tractable than the prior (incorrect) characterization, and it
  **retracts the "edge-sensitive wall" framing**.

## Honest limits on the coefficient (no over-claim)

Empirically `κ_n − κ > 0` throughout (exact, n≤67), and a **2-term** fit
`κ_n − κ = a₁n^{-1/2} + a₂n^{-1}` gives `a₁ ≈ 0.013–0.015 > 0` at the top pairs. **But the coefficient
is NOT numerically pinned:** a **3-term** fit (n=44,52,60) collapses `a₁` to `≈ 0.002` with large
`a₂ ≈ 0.15`, `a₃ ≈ −0.63` — the series is **deeply pre-asymptotic** at reachable `n` (recall
`κ_n − κ` only peaks at `n≈32`). So:

- **Defensible:** `M₁>0` exact to n≤67; the correction is **bulk-dominated** (edge subleading, by
  scaling); `κ_n − κ > 0` empirically.
- **NOT claimed:** a specific value or even a firm exponent for the correction — the fits disagree
  (`a₁` from `0.002` to `0.017` depending on model). The magnitude/exponent are numerically
  unresolved at n≤67.

## Refined frontier

Prove `κ_n ≥ κ` for `n ≥ 13` via the **bulk** second-order Kerov-CLT: show the leading correction
coefficient (the `n^{-1/2}` term of `κ_n`, equivalently the `n²` term of `M₁`) is `≥ 0`. This is the
`c_N > c_P` deficit-coefficient comparison (deficit audit), now correctly scoped as a **bulk** (not
edge) computation. Still open, still hard, but no longer mis-attributed to Tracy–Widom.

## Compute

- Extended exact verification + fits: [`wlambda_covariance_epic_M1_onesided_kappa_bound.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_onesided_kappa_bound.py),
  [`wlambda_covariance_epic_M1_secondorder_fit.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_secondorder_fit.py) (exit 0; exact `Fraction`; NO float64).

## Cross-references

- Prior "edge-sensitive" audit (CORRECTED by this one): [`2026-08-22-covariance-kernel-M1-sign-attempt-wall.md`](2026-08-22-covariance-kernel-M1-sign-attempt-wall.md)
- One-sided reframing: [`2026-08-22-covariance-kernel-M1-onesided-reframing.md`](2026-08-22-covariance-kernel-M1-onesided-reframing.md)
- κ derivation: [`2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md`](2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md)
- Gap bean `qou-k5r5`.
