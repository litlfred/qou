# Covariance-kernel epic (`qou-x631`) — M₁>0 sub-result (2) reframed to a ONE-SIDED bound

**Date:** 2026-08-22 · **Branch:** `claude/m1-effective-clt-project-2026-08-22` · **Tier:** exact
reframing (sharpens sub-result (2); supersedes the "explicit `C`" framing) · **Discipline:**
scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged. **Epic:** `qou-x631`; gap `qou-k5r5`.

## Result

The effective-CLT workplan posed sub-result (2) as: prove `M₁(n) ≥ κ·n^{5/2} − C·n²` with an
**explicit** `C` (`κ = 128/(225π²)`, `M₁ = Cov(T,ω₃)` after sub-result (1)). Exact computation shows a
**cleaner one-sided structure** that removes `C` entirely.

With `κ_n := M₁(n)/n^{5/2}` (exact `Fraction`, compared to `κ` at 60 dps):

> **`κ_n < κ` for `n ≤ 12`;  `κ_n > κ` for every `13 ≤ n ≤ 46`.** Crossing at **`n₀ = 13`**.
> The gap `κ_n − κ` is positive throughout `[13,46]`, peaking `≈ 0.001556` at `n=32`, then declining
> gently (`≈ 0.001472` at `n=46`) — far from recrossing 0.

Hence the proof structure:

> **`M₁(n) > 0` for all `n` ⟸ (a) exact `M₁(n) > 0` for `n ≤ 12`  ∧  (b) `κ_n ≥ κ` for all `n ≥ 13`.**

Part (a) is done (exact `Fraction`: `M₁ = 2/3, 4/3, 8/3, 14/3, 7, 148/15, 2437/180, …` all `> 0`,
`n ≤ 12`). Part (b) is the **sole remaining analytic task**, and it is now **one-sided**:

> `Cov(T, ω₃) ≥ κ·n^{5/2}` for `n ≥ 13`  ⟺  the correction `Cov(T,ω₃) − κn^{5/2} ≥ 0`.

## Why this is the right target (and easier than `C`)

- **No explicit constant needed.** The two-sided `M₁ ≥ κn^{5/2} − Cn²` required bounding *all* lower
  terms with a computable `C`. The one-sided form needs only the **sign** of the leading correction:
  that `κ_n → κ` **from above** for `n ≥ 13`. A sign is a far weaker demand on the second-order
  Kerov-CLT analysis than an explicit constant.
- **`κ` is proved** (IO Chebyshev-mode integral, `= 128/(225π²)`), and `κ_n → κ` is proved (the CLT).
  What is open is only the *one-sided* rate: the correction does not dip below 0 for `n ≥ 13`.
- **Finite base `n₀ = 13` is pinned exactly**, so the "for all `n ≥ 13`" tail is the only asymptotic
  content; everything below is the exact check (a).

## Honest status of part (b)

Verified `κ_n > κ` exactly for `13 ≤ n ≤ 46`. **Not proved for all `n`.** Closing it needs the sign of
the second-order correction to `Cov(T,ω₃)` — a genuine (if now one-sided) second-order Kerov-CLT /
Fulman-second-moment computation. Two honest sub-questions remain:

1. **Asymptotic sign:** show the leading correction to `Cov(T,ω₃)` beyond `κn^{5/2}` is `≥ 0`
   (so `κ_n → κ` from above), giving `κ_n ≥ κ` for `n ≥ N₀`.
2. **No dip in the window:** confirm `κ_n ≥ κ` on `13 ≤ n < N₀` (exact check; have it to 46).

Together with (a) these would give `M₁>0` for all `n`. The gap `qou-k5r5` stays **OPEN**, but its
remaining content is now precisely (b1): the *sign* of one correction term.

## Compute

- Probe: [`wlambda_covariance_epic_M1_onesided_kappa_bound.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_onesided_kappa_bound.py)
  (exit 0; exact `Fraction` `κ_n`, compared to `128/(225π²)` at 60 dps; crossing `n₀=13`).

## Cross-references

- Workplan: [`2026-08-22-M1-effective-CLT-project.md`](../workplans/2026-08-22-M1-effective-CLT-project.md)
- Sub-result (1) (`Λ*` orthogonality): [`2026-08-22-covariance-kernel-M1-lambda-star-orthogonality.md`](2026-08-22-covariance-kernel-M1-lambda-star-orthogonality.md)
- κ derivation: [`2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md`](2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md)
- Gap bean `qou-k5r5`.
