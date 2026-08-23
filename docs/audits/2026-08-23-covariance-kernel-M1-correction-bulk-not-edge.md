# Covariance-kernel epic (`qou-x631`) — M₁>0: exact to n≤67, Lean-proved k≤7; correction order UNDETERMINED (edge n^{-2/3} vs bulk, unranked)

**Date:** 2026-08-23 · **Branch:** `claude/m1-kappa-edge-scaling-2026-08-23` · **Tier:** correction of
a prior characterization + extended exact verification · **Discipline:** scope-(a); no fit; nothing
wired; no `c_k`; L2 unchanged. **Epic:** `qou-x631`; gap `qou-k5r5`.

## Two results

### 1. `M₁ > 0` exact for `60 < n ≤ 67`
The exact `Fraction` covariance gives `κ_n > κ = 128/(225π²)` (hence `M₁ = κ_n·n^{5/2} > 0`) for
**every `13 ≤ n ≤ 67`** — extending the previous `n ≤ 60`. The crossing stays at `n₀ = 13`; the gap
`κ_n − κ` is positive and declining slowly (`≈ 0.001317` at n=65). No sign of recrossing.

### 2. The correction's order is UNDETERMINED — edge (`n^{-2/3}`) vs bulk (`n^{-1/2}`) cannot be ranked
The [prior audit](2026-08-22-covariance-kernel-M1-sign-attempt-wall.md) called the correction
edge-dominated; this session first over-corrected to "bulk-dominated". **Both are over-claims.** What
is defensible is a scaling estimate for the **edge (Tracy–Widom)** contribution:

- **Edge contribution.** The Tracy–Widom edge enters `Σh` through `λ₁² = 4n + 4n^{2/3}χ + …`
  (`χ = TW`, `O(1)`), so `δ(Σh)_edge ~ n^{2/3}χ`. It enters `ω₃ = Σc²` through the extreme content
  `≈ λ₁ ≈ 2√n`: `∂Σc²/∂λ₁ ≈ (2√n)² = 4n`, so `δ(ω₃)_edge ~ 4n·n^{1/6}χ = 4n^{7/6}χ`. Both driven by the
  *same* `χ`, hence `Cov_edge ~ n^{2/3}·n^{7/6} = n^{11/6}`, i.e. **relative order `n^{-2/3}`** vs the
  leader `κn^{5/2}`.
- A bulk second-order CLT correction would be relative order `~ n^{-1/2}`.

> **⚠ Honest walk-back — do NOT read this as "bulk-dominated".** An earlier draft concluded "since
> `−2/3 < −1/2` the edge is subleading, so the correction is bulk-dominated." **Withdrawn** — that
> assumed the bulk correction is exactly `n^{-1/2}`, which is *not* established. The measured effective
> exponent `β` of `κ_n − κ` at high `n` (well past the peak at `n≈32`) runs `β ≈ 0.25 → 0.36` over
> `n = 40 … 64` and is **still rising, not converged**; no test `(κ_n−κ)·n^{β}` for `β ∈ {1/2, 2/3, 1}`
> is flat. So the correction's asymptotic order is **genuinely undetermined at `n ≤ 67`**, and edge
> (`n^{-2/3}`) vs bulk (`n^{-1/2}`) **cannot be ranked**. Both this session's "bulk-dominated" and the
> prior session's "edge-sensitive" are **over-claims**. The only defensible statement is: *the edge
> contributes at relative order `n^{-2/3}` (valid scaling); which of edge/bulk dominates is unknown.*

## Honest limits on the coefficient (no over-claim)

Empirically `κ_n − κ > 0` throughout (exact, n≤67), and a **2-term** fit
`κ_n − κ = a₁n^{-1/2} + a₂n^{-1}` gives `a₁ ≈ 0.013–0.015 > 0` at the top pairs. **But the coefficient
is NOT numerically pinned:** a **3-term** fit (n=44,52,60) collapses `a₁` to `≈ 0.002` with large
`a₂ ≈ 0.15`, `a₃ ≈ −0.63` — the series is **deeply pre-asymptotic** at reachable `n` (recall
`κ_n − κ` only peaks at `n≈32`). So:

- **Defensible:** `M₁>0` exact to n≤67 (**and Lean-proved for `k ≤ 7`**, `m1_pos_of_le_seven`); the
  edge contributes at `n^{-2/3}`; `κ_n − κ > 0` empirically throughout.
- **NOT claimed:** the correction's exponent or coefficient, or which of edge/bulk dominates — all
  numerically unresolved at n≤67.

## Frontier (honestly scoped)

Prove `κ_n ≥ κ` for `n ≥ 13` — i.e. `κ_n − κ ≥ 0` asymptotically. This is a **second-order
Plancherel-fluctuation** statement whose relevant order (bulk `n^{-1/2}` vs edge `n^{-2/3}` vs a mix)
is **not determined** by the accessible data. The sign is empirically robust (exact to n≤67) but its
proof needs the genuine second-order asymptotics; both bulk and edge contribute at close orders and
neither is ruled out. Open.

## Lean

`M₁ > 0` for the finite base is now **machine-checked**: `m1_pos_of_le_seven`
(`0 < scaledCov k (Σ□ h) (Σ□ c²)` for `3 ≤ k ≤ 7`, `interval_cases k <;> decide`) in
[`YoungDiagramKernel.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/YoungDiagramKernel.lean),
verified `lean`-direct exit 0. The all-`n` statement is **not** Lean-provable (it is the open analytic
problem above); the even moments `threeM4_pos`/`M6_pos` remain the only *general-`n`* proved
positivity.

## Compute

- Extended exact verification + fits: [`wlambda_covariance_epic_M1_onesided_kappa_bound.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_onesided_kappa_bound.py),
  [`wlambda_covariance_epic_M1_secondorder_fit.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_secondorder_fit.py) (exit 0; exact `Fraction`; NO float64).

## Cross-references

- Prior "edge-sensitive" audit (CORRECTED by this one): [`2026-08-22-covariance-kernel-M1-sign-attempt-wall.md`](2026-08-22-covariance-kernel-M1-sign-attempt-wall.md)
- One-sided reframing: [`2026-08-22-covariance-kernel-M1-onesided-reframing.md`](2026-08-22-covariance-kernel-M1-onesided-reframing.md)
- κ derivation: [`2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md`](2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md)
- Gap bean `qou-k5r5`.
