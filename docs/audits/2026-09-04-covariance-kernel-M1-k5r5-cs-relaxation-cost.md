# Covariance-kernel epic (`qou-x631`) — M₁>0 `qou-k5r5`: the Cauchy–Schwarz relaxation is cheap (≥78.6 % of the true margin) — but tightness is not tractability, and the machinery reaches `P > N`, not the margin

> **Withdrawn inference, corrected before merge (same branch, §Reach below).** This audit's first
> version was titled *"…so the margin route is the right one"* and concluded exactly that. **The
> measurement stands; the inference does not.** "The relaxation is tight" and "the resulting bound is
> tractable" are different claims, and only the first was measured. The Fulman identity is keyed to
> an **eigenfunction** of the up-down chain, and `A` is not one — so the identity reaches `P` and `N`
> but **not** `V_A`, which is the margin route's one remaining object. See §The reach.

**Date:** 2026-09-04 · **Branch:** `claude/m1-k5r5-cs-relaxation-cost-2026-09-04` ·
**Tier:** measurement + independent re-verification of a 2026-08-21 corpus reduction · **Epic:** `qou-x631`; gap `qou-k5r5`.

## Two routes, and the relationship nobody had priced

Two sufficient conditions for `M₁ > 0` coexist in this corpus, and PRs #6500 → #6602 sharpened one of
them without ever checking it against the other.

**Fulman reduction** ([`…-fulman-exchangeable-pair-reduction.md`](2026-08-21-covariance-kernel-M1-fulman-exchangeable-pair-reduction.md),
2026-08-21). With `ω₃ = Σc² − C(n,2) = W` an exact eigenfunction of the up-down chain on the Young
lattice, and the split identity `Σ□ h = Σ_u D(u)² + Σ□|c|` (i.e. `Σh = D + A`):

> `M₁ = Cov(Σh, W) = P − N`, with `P := Cov(A,W) ≥ 0` and `N := −Cov(D,W) ≥ 0`, **both signs manifest
> edge by edge.** So `M₁ > 0` is *exactly* `P > N` — necessary and sufficient.

**(CS) margin** (the route I have been sharpening). `m = ρ_P − √(V_D/V_A) > 0` with
`ρ_P = P/√(V_A·V_W)`. Multiplying through by `√(V_A·V_W)`, this is exactly `P > √(V_D·V_W)`. Since
Cauchy–Schwarz gives `N = |Cov(D,W)| ≤ √(V_D·V_W)`, **the margin is the CS relaxation of `P > N`** —
sufficient, not necessary, and it discards `N`'s per-edge sign structure entirely.

**So: what does that relaxation cost?** The whole question of whether four PRs of effort went to the
right place turns on it, and it is one exactly-computable number.

## Measured ([`…_cs_relaxation_cost.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_cs_relaxation_cost.py), exit 0, exact `Fraction` over every partition to n = 40, NO float64)

| n | `P` | `N` | `M₁ = P−N` | `√(V_D·V_W)` | `ρ_D` | surviving |
|---|---|---|---|---|---|---|
| 8 | 22.7111 | 12.8444 | 9.86667 | 15.3439 | 0.8371 | 0.7467 |
| 16 | 152.552 | 92.5494 | 60.0027 | 105.391 | 0.8782 | 0.7860 |
| 24 | 435.003 | 268.202 | 166.801 | 297.510 | 0.9015 | 0.8243 |
| 32 | 920.975 | 578.074 | 342.900 | 633.745 | 0.9122 | 0.8376 |
| 40 | 1622.90 | 1024.18 | 598.715 | 1112.83 | 0.9203 | 0.8519 |

where `ρ_D := N/√(V_D·V_W)` **is** the tightness of Cauchy–Schwarz on the `(D, W)` pair (1 = free),
and *surviving* `:= (P − √(V_D·V_W))/(P − N)` is the share of the true margin the relaxation still
certifies.

> **CS is cheap.** Over `n ≥ 16`: `ρ_D ∈ [0.8782, 0.9203]`, surviving fraction
> **∈ [0.786, 0.852]**. The relaxation costs at worst **1.27×**, and both quantities *increase* with
> `n` — so at `n ≥ 79` it should be cheaper still, which is the conservative direction for the
> extrapolation.

It was not obvious in advance: had `ρ_D` come out near 0.5, four PRs would have been paying a 2×
premium avoidable by working `P > N` directly.

*(This paragraph first continued "**the margin route is therefore the right target**". That does not
follow from a tightness measurement — see the next section, which withdraws it.)*

## The reach — tightness is not tractability, and only `W` is an eigenfunction

The Fulman identity is not a general covariance formula. It reads

> `Cov(f, g) = E_π[(f − f*)(g − g*)] / (2(1 − β))`, valid **when `J g = β g`**

— it computes the covariance of *any* `f` against an **eigenfunction** `g` of the up-down chain `J`.
The corpus's reduction takes `g = ω₃ = W`, which is why `P` and `N` come out as local per-edge sums.
`V_A = Cov(A, A)` would need **`A` itself** to be an eigenfunction.

Measured ([`…_eigenfunction_reach.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_eigenfunction_reach.py),
exit 0, exact `Fraction`, `n = 3…12`, NO float64), quantified over the **family** — every
non-degenerate `n`, not any single one:

| statistic | eigenfunction at every n | consequence |
|---|---|---|
| `W` | **YES**, `β₃ = (n−2)/(n+1)` exactly | `Cov(·, W)` reachable ⟹ **`P` and `N` both reachable** |
| `A` | **NO** — at no non-degenerate `n` | `V_A = Cov(A,A)` **not** reachable by this identity |
| `D` | **NO** — constant (hence vacuously one) at `n = 3` only | `V_D` **not** reachable either |

**Positive control.** `W` is *known* to be an eigenfunction with `β₃ = (n−2)/(n+1)` (corpus,
2026-08-21, verified there to `n ≤ 13`). This probe's chain reproduces that **exactly** at every `n`,
and `J` is row-stochastic throughout — so a negative on `A` is a fact about `A`, not about the chain.

**Cross-check, from an independent direction.** #6627 found `V_W` an exact polynomial
`n(n−1)(n−2)/3` while `V_A`, `V_D` and `P` are not polynomial at all. That is the same boundary seen
from the other side: **the one object with a closed form is the one whose statistic is the
eigenfunction.** Two independent measurements, one split.

> **So the two routes are not symmetric in tractability.** `P > N` needs only covariances against
> `W` — both reachable, both local per-edge sums with manifest signs. The margin route needs `V_A`,
> which the named machinery does not reach and which #6627 showed has no polynomial closed form
> either. **#6651's tightness measurement stands; its inference that the margin route is the right
> target is withdrawn.**

**Scope — (a), not (b).** This says the *named identity* does not apply to `V_A`. It does **not**
exclude `V_A`: a spectral decomposition of `A` in the chain's eigenbasis, or a different chain for
which `A` is an eigenfunction, are both untested here. What it settles is where the roadmap's own
tool points.

### A quantifier bug in this probe, caught before commit

The first run reported *"D is an eigenfunction ⟹ `V_D` reachable"* on the strength of **n = 3
alone**, where `D ≡ 3` is **constant** — and a constant is trivially an eigenfunction of any
stochastic chain (`β = 1`), carrying no information. The summary used `any(n)` where reachability is
a claim about the **family**, so it needs `every(n)`, with constants excluded. Fixed to quantify over
non-degenerate `n` and to mark the constant case explicitly (`YES*` in the table). Same shape as the
`da-arity-conflation` class, and the second quantifier slip of this arc — #6602 had the mirror of it,
testing a family claim at a point.

## The corpus's reduction, independently re-verified

The probe does not assume the 2026-08-21 result it is pricing. `Σh` is computed **per cell** as an
explicit hook sum, never as `D + A`, and two assertions gate every number above:

| self-check | result |
|---|---|
| split identity `Σh == D + A` at **every partition**, `n ≤ 40` | **PASS** |
| Fulman reduction `Cov(Σh, W) == P − N` at **every n** | **PASS** |

If either had failed, the probe refuses to print a cost figure. Both pass, so the split identity and
the exchangeable-pair reduction are now confirmed from a second, independent computation.

## What this does not do

It prices the relaxation; it closes neither route. Both still need a rigorous finite-`n` argument —
`δ_A` for the margin, `P > N` for Fulman. The window ends at `n = 40` while the requirement is
`n ≥ 79`, so nothing here is a bound.

## Status of `qou-k5r5`

Gap **OPEN**. Two things are now known that were not, and they point in opposite directions:

- **The CS relaxation is cheap** — it forfeits at most ~21 % of the true margin, so the 40.5×
  headroom measured in #6576 is not being spent on a detour. Whichever route runs, this is not
  where the budget goes.
- **But the machinery reaches `P > N`, not the margin.** `V_A` is neither an eigenfunction covariance
  (this PR) nor a polynomial in `n` (#6627), while `P` and `N` are both exact local per-edge sums
  with manifest signs.

**So the recommended next target changes from `δ_A` to `P > N`** — the necessary-and-sufficient form,
whose two objects are the ones the roadmap's own tool can compute. `C ≤ m_∞√79 = 2.6681` remains the
requirement on the margin side if that route is taken anyway (empirical envelope 0.0580; `n ≤ 78`
certified exhaustively). That is a recommendation from a reach measurement, not a proof that the
margin route is dead — see the scope note above.

## Cross-references

- The sharper reduction being priced: [`…-fulman-exchangeable-pair-reduction.md`](2026-08-21-covariance-kernel-M1-fulman-exchangeable-pair-reduction.md)
- The route it validates: [`…-ratio-route-is-the-target.md`](2026-09-04-covariance-kernel-M1-k5r5-ratio-route-is-the-target.md) (#6576), [`…-ratio-is-a-constant-not-a-rate.md`](2026-09-04-covariance-kernel-M1-k5r5-ratio-is-a-constant-not-a-rate.md) (#6602)
- Why no closed form shortcuts it: [`…-variance-polynomiality.md`](2026-09-04-covariance-kernel-M1-k5r5-variance-polynomiality.md) (#6627)
- Epic `qou-x631`; gap `qou-k5r5`.
