# Covariance-kernel epic (`qou-x631`) — M₁>0 `qou-tvok`: P2 refuted — the EM-able side of the trace split carries no `θ²` term

**Date:** 2026-09-03 · **Branch:** `claude/m1-k5r5-p2-trace-split-orders-2026-09-03` · **PR:** #6500 ·
**Tier:** honest negative on a route this session itself proposed, with an independent positive
cross-check landed alongside it · **Epic:** `qou-x631`; gap `qou-k5r5`, child `qou-tvok`.

## What was proposed, and what it turns out to be

PR #6472 established that `TV(g″)` is ill-posed as stated — there is no *local* variance density —
and exhibited two well-posed replacements. **P2** was the one that looked cheap:

> **(P2) the trace split.** For a projection kernel (`K² = K`),
> `V_A = Σ_x g(x)²K(x,x) − Σ_{x≠y} g(x)g(y)K(x,y)² =: A − B`.
> The first term is a clean 1-D sum with a smooth integrand `g²ρ`, directly EM-able. Measure whether
> its own remainder carries `c₁`, or whether the cancellation against `B` does.

Executed here over `θ = 250 … 16000`
([`…_p2_trace_split_orders.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_p2_trace_split_orders.py),
exact descent-DPP kernel, `mpmath.mpf` at dps 40, exit 0, 8.5 s wall). **P2 does not work.** The
reasons are two and they are independent, and the second was not anticipated.

## The positive result first: the continuum reference for `A` is *verified*

This matters for how the negative should be read. `A ~ α·θ^{5/2}`; two-level Richardson on
`A/θ^{5/2}` gives `α = 0.429421692`. Independently, in the bulk `x = 2√θ·u` the discrete Bessel
kernel has diagonal `K(x,x) → ρ(u) = arccos(u)/π`, so `Kdiag → ρ(1−ρ)`, which **vanishes at both
edges** (`ρ → 1` at `u = −1`, `ρ → 0` at `u = +1`) — that is why `A` converges at all, given
`g(x)² ~ x⁴/4` grows. With `g² ≈ 4θ²u⁴` and `dx = 2√θ du`:

> `α = 8·∫_{−1}^{1} u⁴ ρ(u)(1−ρ(u)) du = 0.429421692`

| | level-1 Richardson | level-2 Richardson |
|---|---|---|
| `A/θ^{5/2}` | 0.429527086 … 0.429424984 | 0.429421672, 686, 691, 691, **692** |
| continuum integral | — | **0.429421692** |

**Relative difference 3.3e−10.** So the continuum integral that an Euler–Maclaurin argument for `A`
would be *defined against* is confirmed by computation rather than assumed. **The refutation below is
therefore about the split itself, not about a missing input** — which is what separates a negative
result from a stall.

## Reason (a) — `c₁ = a₁ − b₁`, so one side is never enough

Write `A = a_{5/2}θ^{5/2} + a₂θ² + a₁θ + …` and likewise `B = b_{5/2}θ^{5/2} + b₂θ² + b₁θ + …`. Then
the measured `c₁ ≈ −0.0678` is the **difference** `a₁ − b₁`. EM applied to `A` yields `a₁` alone;
obtaining `b₁` requires the **double** sum `B`, which is not a 1-D sum and is not EM-able by any tool
in the corpus. The split **partitions** the problem; it does not reduce it.

This much I expected. The second reason is worse and I did not.

## Reason (b) — `A` carries no `θ²` term at all

Because `α` is pinned independently to 10 digits by the cross-check above, the presence of a `θ²`
term in `A` is testable **directly** rather than inferred from a convergence trend:
`(A/θ^{5/2} − α)·√θ` tends to `a₂` if `a₂ ≠ 0`, and to 0 otherwise.

| θ | 250 | 500 | 1000 | 2000 | 4000 | 8000 | 16000 |
|---|---|---|---|---|---|---|---|
| `(f−α)·√θ` | 0.027455 | 0.020592 | 0.015394 | 0.011474 | 0.008530 | 0.006326 | **0.004681** |
| ratio to previous | — | 1.3333 | 1.3377 | 1.3416 | 1.3452 | 1.3484 | **1.3513** |

The column falls monotonically toward 0 **and the per-doubling ratio rises toward `√2 = 1.414`** —
the signature of a clean `θ^{-1/2}` decay to zero. A nonzero `a₂` would make the column **plateau**
at `a₂` and drive the ratio down toward 1; both diagnostics go the other way.

Stated as a bound rather than an assertion, since that is what is measured:

> **`|a₂| ≤ 0.00468`** — the last entry, itself an over-estimate since the column is still falling —
> against `V`'s `θ²` coefficient `8/π² = 0.8105694691`. So `A` supplies at most **0.578 %** of it.

**The entire leading `θ²` of `V` comes from `−B`.** The "clean, EM-able" side does not hold even `V`'s
*leading* coefficient, let alone the `θ^{-1}` correction P2 was meant to extract. The structure of
interest lives on the side EM cannot reach.

The weaker trend test agrees: successive-difference exponents on `A/θ^{5/2}` run
0.90965 / 0.91499 / 0.91974 / 0.92397 / 0.92779 — **rising toward 1**, whereas a nonzero `a₂` would
force them **down toward 0.5**.

## Supporting measurements

| θ | `A` | `B` | `V = A−B` | `A/θ^{5/2}` | `V/θ²` | `A/V` |
|---|---|---|---|---|---|---|
| 250 | 426075.49 | 375431.02 | 50644.470 | 0.4311581 | 0.810311526 | 8.4131 |
| 1000 | 13594899.9 | 12784396.8 | 810503.05 | 0.4299085 | 0.810503047 | 16.773 |
| 4000 | 434680676 | 421711835 | 12968841.1 | 0.4295566 | 0.810552569 | 33.517 |
| 16000 | 1.3907e10 | 1.3699e10 | 207504697 | 0.4294587 | 0.810565223 | 67.018 |

- **Cancellation depth.** `A` and `B` are each `~θ^{5/2}` with **equal** leading coefficients
  (`V` has no `θ^{5/2}` term), so `A/V ~ (α/(8/π²))·√θ`. Predicted coefficient **0.5297778**;
  measured `(A/V)/√θ` runs 0.5320893 → **0.5298262** at θ=16000. Five digits. This is what leaves `V`
  two half-orders smaller than either side, and it is why the split is well-conditioned rather than
  catastrophic.
- **How deep the target sits inside `A`.** `|c₁|·θ / A` runs 3.978e−5 → **7.801e−8**, with measured
  exponent **1.4999** against 3/2. So `c₁` lives at relative `θ^{-3/2}` inside `A` but at `θ^{-1}`
  inside `V`: reading it off `A` demands **half an order more** relative accuracy than reading it off
  `V` directly. Even setting reasons (a) and (b) aside, P2 would have been the harder route.

## What is *not* claimed

- **The split stands.** Exact (verified to `~1e−36` in #6472), well-conditioned, and now carrying a
  verified continuum reference for `A`. Refuted is the hope of **localising `c₁` on it**.
- **`P1` is untouched.** The mode sum `V_A = Σ_{k odd} Â_k²/k` is already a 1-D sum in `k` with a
  smooth summand; if the finite-θ correction is an EM remainder *in `k`*, that summand **is** the `g`
  whose `TV(g″)` #6469 asked for. It needs the finite-θ deformation of `Â_k`, which this probe does
  not address. `P1` is now the live candidate.
- **Nothing about the rate or the constant changes.** `θ^{-1}`, `c₁ ≈ −0.0678`. All unchanged.

  > **🛑 CORRECTED 2026-09-03 (PR #6500).** The sentence above is **wrong** and is retracted. The `θ^{-1}` rate is `V_A`'s, **not the (CS) margin's** — the margin `m(n) = ρ_P − σ_D/σ_A` is a ratio of square roots of variances plus a correlation, and no one has propagated the one rate into the other. What is **proved** (PR #5929) is `|m(n) − m_∞| ≤ C·n^{-1/2}`, so `N₀ = (C/m_∞)²` — *squared* — and the requirement is `C ≤ m_∞·√79 = 2.6681`. That is **the** requirement under the bound in hand, not "a conservative reading" of it. The route is nonetheless in better shape than either number suggested: the empirical envelope over `n ≥ 13` is `C_emp = 0.0580`, a **46× headroom** under the already-proved shape. See [`…-margin-envelope-retraction.md`](2026-09-03-covariance-kernel-M1-k5r5-margin-envelope-retraction.md).

## Status of `qou-k5r5`

Gap **OPEN**. The route inventory after this PR: the pointwise-Bessel route is refuted (`U/V` grows
without bound, ~17× short at θ=78, PR #6438); `TV(g″)` as originally posed is ill-posed (no local
density, `c(ρ) = +∞`, PR #6472); P2 is refuted here. **P1 is the remaining exhibited candidate**, and
the entire residual gap is still one finite-`n` constant.

## Cross-references

- The split and the two candidates: PR #6472 / [`…-tv-gpp-is-ill-posed.md`](2026-09-03-covariance-kernel-M1-k5r5-tv-gpp-is-ill-posed.md)
- The `TV(g″) ≈ 3.25` target and the `θ^{-1}` rate: PR #6469 / [`…-weight-bug-retraction-retracted.md`](2026-09-03-covariance-kernel-M1-k5r5-weight-bug-retraction-retracted.md)
- Pointwise-route refutation + far-tail majorant: PR #6438 / [`…-deep-tail-rigorous-need-lit-localised.md`](2026-09-03-covariance-kernel-M1-k5r5-deep-tail-rigorous-need-lit-localised.md)
- Epic `qou-x631`; gap `qou-k5r5`; child `qou-tvok`.
