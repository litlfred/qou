# Covariance-kernel epic (`qou-x631`) — M₁>0 `qou-k5r5`: the pointwise route's error budget was understated 2.943× — a unit error of mine, and the shortfall factor should not be quoted at all

**Date:** 2026-09-03 · **Branch:** `claude/m1-k5r5-rigorous-C-2026-09-03` · **PR:** #6528 ·
**Tier:** correction of merged content (PR #6438), verdict unchanged · **Epic:** `qou-x631`; gap `qou-k5r5`.

## What survives, stated first

PR #6438's **structural negative stands and is untouched.** A *pointwise* uniform Bessel remainder
`|J − S| ≤ ε` cannot pin the variance constant, because

> `U/V = Σw|S| / (½Σw S²)` **grows without bound in θ** — measured 42.8, 45.7, 53.9, 70.7, 91.9 at
> `θ = 64, 78, 128, 256, 512`.

`S(k) ~ sin(πρk)/(πk)` decays like `1/k` while `S²` decays like `1/k²`, so `U` carries roughly an
extra power of the band width. No pointwise bound, **however sharp its constant**, controls `V_A`
uniformly in `θ`. The oscillatory cancellation (summation by parts / stationary phase) is
**essential, not a refinement**, and that argument never used the arithmetic below.

## The unit error

#6438 closes with:

> At θ = 78 the measured `U/V = 45.65` gives, for a pointwise remainder `ε = K·θ^{-1/2}`, a relative
> error on `V_A` of about `K·5.17`. Keeping that below `m_∞ = 0.3002` forces **`K < 0.058`**, whereas
> the leading Debye/Olver remainder coefficient is `O(1)`: the pointwise route misses the required
> constant by **~17×**.

The last step compares a **relative error on `V_A`** against `m_∞`, an **absolute margin**. Those are
different objects and the conversion was dropped. The margin is
`m = ρ_P − σ_D/σ_A` with `σ_D/σ_A = √(V_D/V_A)`, so a relative perturbation `δ_A` on `V_A` scales the
ratio by `√(1−δ_A) ≈ 1 − δ_A/2` and therefore moves the **margin** by

> `|Δm| = σ_ratio,∞ · δ_A / 2 = 0.679609581 · δ_A / 2 = 0.3398·δ_A` — **not** by `δ_A`.

Admissible relative error on `V_A` is thus `m_∞ / 0.3398 = 0.8834`, not `0.3002`. **The merged
threshold is 2.943× too strict.**

## Recomputed ([`…_pointwise_shortfall_recomputed.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_pointwise_shortfall_recomputed.py), exit 0, 0.9 s, NO float64)

The probe reuses #6438's own `U_and_V` by explicit file path, so the two are computing the same
kernel sums.

| θ | `U/V` | rel-err on `V_A` per `K` | `K_adm` (`V_A` alone) | `K_adm` (split with `V_D`) |
|---|---|---|---|---|
| 64 | 42.7462 | 5.34327 | 0.16533 | 0.082666 |
| **78** | **45.5868** | **5.16169** | **0.17115** | **0.085574** |
| 128 | 53.7259 | 4.74874 | 0.18603 | 0.093015 |
| 256 | 70.4983 | 4.40614 | 0.20049 | 0.10025 |

**The eps-multiplier reproduces #6438's 5.17 (measured 5.16169).** That agreement is the check that
this locates the exact defect rather than recomputing a different quantity — the two probes agree on
everything up to the threshold conversion, and diverge only there: `K_adm = 0.17115` against the
merged `0.058`.

Dividing by a Debye/Olver leading coefficient of `O(1) ≈ 1` would turn this into "~5.8× short"
(`V_A` carrying the whole budget) or "~11.7×" (split evenly with `V_D`), against the `~17×` on
record — **but see below: that division is not legitimate, and none of those three factors should be
quoted.** The defensible output of this probe is `K_admissible` itself.

θ = 78 is the right place to evaluate this: it is the largest `n` the exact `Fraction` table reaches,
so it is exactly where the asymptotic must take over from exhaustive verification.

## Why the budget matters even though the verdict doesn't move

The recorded `K < 0.058` understates the error budget the margin allows by 2.943×. That matters
because the budget is what any future bound — pointwise or not — has to fit inside: an argument
rejected for exceeding `0.058` may sit comfortably under `0.17115`. It does **not** revive the
pointwise route, whose failure is structural and independent of any constant.

What it does *not* license is reading "the route is only 5.8× short instead of 17×". Per the next
section, the denominator in that comparison is not a constant at all.

## What this does NOT settle — and it is sharper than "the `O(1)` is imprecise"

`O(1)` for the Debye/Olver remainder coefficient is not a pinned number anywhere in this corpus. But
[`…_bulk_kernel_rate_probe.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_bulk_kernel_rate_probe.py)
has already measured something stronger: the pointwise error `|J(x,x+k;θ) − S(k,a)|` **does not decay
cleanly at all** — its log-log slope **scatters over `b ≈ [−2, +2]`** across `r`, `k` and `θ`, because
the integer `x` quantises the local density `a = x/√θ` (and `S` is sensitive to `a`), and because the
sub-leading term oscillates.

**So there is no clean pointwise constant `K` to compare against: the ratio is not merely imprecise,
it is ill-defined.**

That does not weaken this correction; it relocates it. What is measured here is `K_admissible` — the
error budget the margin actually allows — which *is* well-defined and was computed 2.943× too small.
Both `~5.8×` and `~17×` divide that budget by an object the corpus says is not a constant.

**Quote `K_admissible = 0.17115` at θ = 78. Do not quote a shortfall factor at all** — and say the
pointwise route fails for the *structural* reason (`U/V` unbounded), which is exactly why correcting
the factor changes no verdict.

## Blast radius — every site

| site | status | disposition |
|---|---|---|
| [`…_pointwise_bound_insufficiency.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_pointwise_bound_insufficiency.py) docstring | merged #6438 | correction block inserted |
| same, printed `RESULT` line | merged #6438 | **rewritten** — it printed `~17×` on every run |
| [`…_deep_tail_rigorous_majorant.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_deep_tail_rigorous_majorant.py) printed note | merged #6438 | rewritten |
| [`…-deep-tail-rigorous-need-lit-localised.md`](2026-09-03-covariance-kernel-M1-k5r5-deep-tail-rigorous-need-lit-localised.md) | merged #6438 | correction block appended |
| [`…-p2-trace-split-refuted.md`](2026-09-03-covariance-kernel-M1-k5r5-p2-trace-split-refuted.md) route inventory | merged #6500 | corrected inline |
| [`…-weight-bug-retraction-retracted.md`](2026-09-03-covariance-kernel-M1-k5r5-weight-bug-retraction-retracted.md) blast table | merged #6469 | struck + corrected |
| beans `qou-k5r5`, `qou-tvok` | — | corrected by append |

Probes are fixed **at the producer** because they print the claim on every run; audit docs are
annotated rather than rewritten, per the convention that they are dated records of what was believed.

## The second unit error in two days, and they are the same error

This is the same failure mode as the `C ≤ 23.4` retraction earlier today (PR #6500): **a quantity
measured for one object, compared against a threshold belonging to another, with the conversion
between them dropped.** There, a `θ^{-1}` rate for `V_A`'s remainder was used as a premise about the
margin `m(n)`. Here, a relative error on `V_A` was compared against an absolute margin. Both times the
arithmetic *within* each object was correct, which is what let both survive review.

Practical guard for this arc: `V_A`, `σ_A`, `σ_D/σ_A` and `m` are four different objects, and moving
between them costs a factor — `δ(σ_A) = δ(V_A)/2`, and `Δm = σ_ratio·δ(σ_A/σ_D-ratio)`. Write the
conversion down before comparing anything to `m_∞`.

## Status of `qou-k5r5`

Gap **OPEN**, unchanged in kind. The remaining step is a **rigorous** `C ≤ 2.6681` in
`|m(n) − m_∞| ≤ C·n^{-1/2}` (against an empirical envelope of 0.0580 — 46× headroom, PR #6500), and
it must come from the oscillatory cancellation rather than from any pointwise magnitude bound.

## Cross-references

- The corrected claim's origin: PR #6438 / [`…-deep-tail-rigorous-need-lit-localised.md`](2026-09-03-covariance-kernel-M1-k5r5-deep-tail-rigorous-need-lit-localised.md)
- The sibling unit error: PR #6500 / [`…-margin-envelope-retraction.md`](2026-09-03-covariance-kernel-M1-k5r5-margin-envelope-retraction.md)
- The requirement and the headroom: `…_constant_C_landscape.py`, `…_margin_envelope_exponent.py`
- Epic `qou-x631`; gap `qou-k5r5`.
