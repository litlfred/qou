# Covariance-kernel epic (`qou-x631`) — M₁>0 finite-n step: the exact (CS) margin, and the ONE open requirement

**Date:** 2026-08-28 · **Branch:** `claude/m1-finite-n-cs-closure-2026-08-28` · **Tier:** exact
finite-n characterization + honest statement of the single remaining requirement (a refuted
sub-hypothesis noted) · **Discipline:** scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged.
**Epic:** `qou-x631`; gap `qou-k5r5`.

## Where the arc stands after the leading-order derivation

PR #5901 **derived** the Cauchy–Schwarz sufficient condition at leading order — `σ_D/σ_A → 0.67961`,
`ρ_P → 0.97980`, **leading (CS) margin `→ 0.30019`** (rigorous modulo the published IO Kerov CLT, 52 %
scalar margin). That gives `M₁ > 0` for all `n ≥ N₀`. To close `M₁ > 0` for **all** n, the finite-n
(CS) margin `m(n) = ρ_P(n) − σ_D(n)/σ_A(n)` must stay positive.

## What the exact finite-n margin actually does

Exact (`Fraction` covariances/variances; mpmath for `sqrt`/display; NO float64;
`wlambda_covariance_epic_M1_finite_n_cs_margin.py`, exit 0):

> **`m(n) > 0` for every `4 ≤ n ≤ 40`**, minimum `m(4) = 0.20025`; and `m(n)` **oscillates around the
> derived leading value `0.30019` with decreasing amplitude** (peak `≈0.329` at n=9, dip `≈0.298` at
> n=14, peak `≈0.313` at n=21, …) — the same damped-oscillation finite-n signature as `κ_n`.

**A sub-hypothesis is refuted here (recorded, per honest-negative discipline).** An earlier framing
(bean note, and the #5901 audit's "Next") suggested `m(n)` "increases to the leading value from below",
so that exact-check-small-n + leading-order-large-n would trivially cover all n. **That is false:**
`m(n)` overshoots the limit (it is *above* `0.30019` for `7 ≤ n ≤ 12` and again `16 ≤ n ≤ 36…`) and
oscillates. The convergence is damped-oscillatory, not monotone. So the small-n/large-n split does
**not** trivially close the gap.

## The single remaining requirement (precise)

`m(n) > 0` for all n is what remains. It is **not** closeable by the exact table alone (infinitely many
n) nor by the qualitative leading order alone (the tail oscillates). It needs:

> an **effective / quantitative** bound on the IO Kerov-CLT variance asymptotics —
> `|σ_A²/n² − V_A| ≤ C·n^{−a}`, likewise for `σ_D²/n²` and `ρ_P` — with a rate `a > 0` and constant
> `C` explicit enough that the oscillation is trapped below the `0.30` leading margin for `n ≥ N₀`,
> and the finite window `4 ≤ n < N₀` closed by the exact table.

This is a **materially softer** requirement than the sign of the rate `κ_n − κ` (which every literature
tool failed): the leading margin is `0.30`, so a **crude** rate `a` suffices. But it is **not**
delivered by (i) Fulman's marginal Berry–Esseen (`arxiv-math-0305423` — a distributional bound on a
different statistic, ruled out in PR #5887), nor (ii) the qualitative IO CLT (a limit, no rate). An
effective second-order/variance bound for these specific non-`A` statistics (`Σ|c|`, `ΣD²`) is the one
open step.

## Honest status

- **Proved (modulo published IO CLT):** the leading-order (CS) condition, hence `M₁ > 0` for `n ≥ N₀`.
- **Verified exact:** `M₁ > 0` for `n ≤ 78` (Track B); `(CS)` margin `> 0` for `4 ≤ n ≤ 40`.
- **Open (the one step):** an effective variance/correlation bound closing the oscillatory tail. Gap
  `qou-k5r5` stays **OPEN** — but reduced to a single, well-posed, large-headroom analytic estimate.

## Compute

- [`wlambda_covariance_epic_M1_finite_n_cs_margin.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_finite_n_cs_margin.py)
  (exit 0; exact `Fraction`; mpmath only for `sqrt`/display; NO float64).

## Cross-references

- Leading-order (CS) derivation: [`2026-08-28-covariance-kernel-M1-io-leading-order-CS-derived.md`](2026-08-28-covariance-kernel-M1-io-leading-order-CS-derived.md)
- (CS) reduction: [`2026-08-28-covariance-kernel-M1-cauchy-schwarz-margin-reduction.md`](2026-08-28-covariance-kernel-M1-cauchy-schwarz-margin-reduction.md)
- Fulman ruled out: [`2026-08-28-covariance-kernel-M1-fulman-stein-finite-n.md`](2026-08-28-covariance-kernel-M1-fulman-stein-finite-n.md)
- Gap bean `qou-k5r5`.
