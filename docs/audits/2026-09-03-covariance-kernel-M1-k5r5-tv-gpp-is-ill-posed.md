# Covariance-kernel epic (`qou-x631`) — M₁>0 `qou-tvok`: `TV(g″)` is ill-posed as stated — there is no local variance density

**Date:** 2026-09-03 · **Branch:** `claude/m1-k5r5-tv-gpp-2026-09-03` · **Tier:** honest negative on my
own framing + the well-posed reformulation, with its identity verified · **Discipline:** the target
number was not manufactured. **Epic:** `qou-x631`; gap `qou-k5r5`, child `qou-tvok`.

## What was asked, and why it cannot be answered as posed

PR #6469 set a **falsifiable target**: the corpus EM tool
`QOU.MathlibExt.abs_integral_sub_composite_le_osc` bounds `|∫ − composite| ≤ h³/12·(g″(a) − g″(b))`
with **no factor of `k`**, so on a bulk grid of spacing `h = 1/(2√θ)` a remainder `TV(g″)/(48θ)` would
reproduce the measured `θ⁻¹` rate, requiring `TV(g″) ≥ 48·|c₁| ≈ 3.25`.

**Computing that number requires knowing which `g`.** My `h`-scaling argument was **dimensional**: it
fixes the *rate* from the grid spacing but never exhibits the sum-to-integral pair whose integrand
gets differentiated twice. The corpus phrasing that invites one — *"the variance density is
`(g′(x))²·c(ρ(x))`"* ([rigorous-finite-n-bound](2026-08-29-covariance-kernel-M1-rigorous-finite-n-bound.md))
— would supply a **local** integrand. It does not exist.

## Two measurements ([`…_tv_gpp_wellposedness.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_tv_gpp_wellposedness.py), exit 0, NO float64)

**TEST 1 — the leading variance is a MODE functional, not a spatial integral.** The IO/Kerov CLT gives
`V_A = Σ_{k odd} Â_k²/k` with `Â_k = 8(−1)^{(k+1)/2}/(π(k²−4))`. Verified:

| K | 1 | 3 | 11 | 51 | 501 | 5001 |
|---|---|---|---|---|---|---|
| `Σ_{k odd ≤ K} Â_k²/k` | 0.72051 | 0.80697 | 0.81053 | 0.8105694 | 0.81056946913 | 0.8105694691387 |
| \|diff from `8/π²`\| | 9.0e−2 | 3.6e−3 | 4.0e−5 | 1.1e−7 | 1.3e−11 | **1.3e−15** |

This is an **H^{1/2}-type nonlocal** functional of the test function.

**TEST 2 — the candidate local density diverges.** Localising the exact projection formula
`V = ½Σ_{x≠y}(g(x)−g(y))²S(x−y;ρ)²` by `g(x)−g(y) ≈ g′(x)(x−y)` gives density `(g′)²·c(ρ)` with
`c(ρ) = Σ_{k≠0} k²S(k;ρ)²`. Since `S(k;ρ) = sin(πρk)/(πk)`, the summand is `sin²(πρk)/π²` — which does
**not decay**:

| ρ | K=10² | K=10³ | K=10⁴ | K=10⁵ | ratio |
|---|---|---|---|---|---|
| 0.25 / 0.50 / 0.75 | 10.132 | 101.32 | 1013.2 | 10132.0 | **10.0** |

Exactly linear growth, identical for every `ρ`. So **`c(ρ) = +∞`: no local density exists.** The
variance is nonlocal precisely because the sine kernel's `H^{1/2}` norm weights all separations; the
finite answer comes from `g(x)−g(y)` ceasing to grow like `g′(x)(x−y)` at large separation, which is a
**global** property of `g`.

## Consequence — and what I did not do

`TV(g″)` **cannot be computed, because there is no `g`.** The `θ⁻¹` rate stands (measured,
`c₁ ≈ −0.0678), and `h² = 1/(4θ)` scaling is *consistent* with an Euler–Maclaurin mechanism — but
**consistency is not identification**: many mechanisms give `θ⁻¹`. Choosing a plausible integrand and
checking its `TV` against 3.25 would be fitting a target, not deriving a constant, so it is not done.

This also scopes the target set in #6469: it presumed a `g` exists. The target is not *wrong* — the
EM bound may still apply to a **different** sum — but it is not yet attached to an object.

## The well-posed reformulation (TEST 3, verified)

For a projection kernel (`K² = K`, so `K(x,x) = Σ_y K(x,y)²`) the variance splits exactly:

> `V_A = Σ_x g(x)²K(x,x) − Σ_{x≠y} g(x)g(y)K(x,y)²`  =:  `A − B`

and the **first term is a clean 1-D sum with the smooth integrand `g²ρ` — directly EM-able.** Measured:

| θ | `A` | `A − B` | `½Σ(Δg)²K²` | \|diff\| | `A/(A−B)` |
|---|---|---|---|---|---|
| 64 | 14267.02 | 3316.1336 | 3316.1336 | 2.8e−37 | 4.302 |
| 100 | 43341.42 | 8098.6403 | 8098.6403 | 5.2e−36 | 5.352 |

The two forms agree to `~1e−36` at `dps=40` (confirming `K²=K`), and the cancellation is only
`O(√θ)`: `A/(A−B)` goes 4.302 → 5.352 as θ: 64 → 100, against `√(100/64) = 1.25` predicted vs
`5.352/4.302 = 1.244` observed. **So the split is numerically viable, not merely formal.**

## Status of `qou-tvok` / `qou-k5r5`

Gap **OPEN**. Unchanged and correct: rate `θ⁻¹`, `c₁ ≈ −0.0678`, closure needs only `C ≤ 23.4`.
Withdrawn: the implicit claim that `TV(g″)` is a computable quantity of the *local* variance density.
The next honest step is one of two exhibited pairs:

- **(P1) the mode sum.** `V_A = Σ_{k odd} Â_k²/k` is already a 1-D sum in `k` with a smooth summand. If
  the finite-θ correction is an EM remainder *in `k`*, that summand **is** `g` and `TV(g″)` follows.
  Needs the finite-θ deformation of `Â_k`.
- **(P2) the trace split.** Apply EM to `A = Σ_x g²K(x,x)` and measure whether its own remainder
  carries `c₁`, or whether the cancellation against `B` does. Verified exact and well-conditioned above.

## Cross-references

- Target set (now scoped): PR #6469 / [`…-weight-bug-retraction-retracted.md`](2026-09-03-covariance-kernel-M1-k5r5-weight-bug-retraction-retracted.md)
- Rate + `c₁`: `wlambda_covariance_epic_M1_tvok_remainder_rate.py`; bean `qou-tvok` STEP 2.
- Epic `qou-x631`; gap `qou-k5r5`.
