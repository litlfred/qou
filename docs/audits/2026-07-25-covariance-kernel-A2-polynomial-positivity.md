# Covariance-kernel epic (qou-x631) — A2 advance: the polynomial-positivity reduction

> **⛔ CORRECTED 2026-07-25 — the central claim of this note is FALSE for n ≥ 29.** The pointwise
> target `R(x) ≥ 0 on (0,1)` (⟺ `Cov_Planch(H_s,ω₃) ≤ 0 ∀s>0`) was verified here only to `n ≤ 15`;
> pushing the exact computation further shows it FIRST FAILS at `n = 29` (`R` gains a root in `(0,1)`
> at `n = 30`). The "A2 ⟺ R≥0" equivalence was wrong — only `R≥0 ⟹ A2`, now with a false premise —
> so the polynomial-positivity target **cannot** prove A2. The **kernel and A2 themselves survive**
> (exact, `k,n ≤ 40`); A2 holds by cancellation in the full Frullani integral. The three
> route-eliminations below (ν single-crossing, cumulative `S_v≤0`, `R` nonneg-coeffs) remain correct.
> Full correction: [`2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md`](2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md).

**Date:** 2026-07-25 · **Branch:** `claude/covariance-kernel-A2-push-2026-07-25` · **Tier:**
exact reduction + 3 route-eliminations · **Discipline:** scope-(a); no fit; nothing wired; no `c_k`;
L2 unchanged (2/7). **Epic:** `qou-x631`, attack `qou-ogrk` (A2).

## Summary

The A2 leg — `Cov_Planch(ln f^λ, ω₃) ≤ 0`, the leading term of the kernel — reduces **exactly** to a
concrete **polynomial-positivity** statement, and three natural "easy proof" certificates are shown to
**fail**. This is the cleanest form of the log-covariance leg to date, and it tells the next attempt
precisely which approaches will not work.

## The reduction (rigorous)

Write `ν_v := Cov_Planch(N_v, ω₃)` for the hook-covariance signed measure (`N_v = #{cells with hook
length v}`, `ω₃ = Σ_□ c(□)² − C(n,2)`), and define the **hook-covariance generating polynomial**

> `P(x) := Σ_{v≥1} ν_v x^v`.

1. **Hook-length formula.** `ln f^λ = ln n! − Σ_□ ln h`, so `Cov(ln f, ω₃) = −Σ_v ln(v)·ν_v`.
2. **Laplace transform.** `Cov(H_s, ω₃) = Σ_v e^{−sv} ν_v = P(e^{−s})`, with `H_s = Σ_□ e^{−s h}`.
3. **Boundary zeros.** `P(0) = 0` (no constant term) and `P(1) = Σ_v ν_v = Cov(n, ω₃) = 0`
   (`Σ N_v = n`, a constant).
4. **Interval form.** With `x = e^{−s} ∈ (0,1)` for `s ∈ (0,∞)`:
   `Cov(H_s, ω₃) ≤ 0 ∀s>0  ⟺  P(x) ≤ 0 on (0,1)`.
5. **Factorization.** `P(0)=P(1)=0` forces `P(x) = x(x−1)·R(x)`, `deg R = n−2`. On `(0,1)`, `x>0` and
   `x−1<0`, so `x(x−1) < 0`, hence
   > **`P(x) ≤ 0 on (0,1)   ⟺   R(x) ≥ 0 on (0,1)`.**
6. **Frullani** (`ln v = ∫_0^∞ (e^{−s}−e^{−vs})/s\,ds`, using `Σν_v = 0`) gives
   `Cov(ln f, ω₃) = ∫_0^∞ (1/s)\,Cov(H_s, ω₃)\,ds`, so
   > **A2 `(Cov_Planch(ln f, ω₃) ≤ 0)`  ⟸  `R(x) ≥ 0 on (0,1)`.**

## What is verified (n ≤ 15, exact `Fraction`)

- **`R(x) ≥ 0` on `(0,1)`**, and in fact **R has no positive real root at all** — `R > 0` on `[0,∞)`,
  with every real root **negative**. So the reduced target holds with room to spare.
- **Moment tower** `M_k := Σ_v v^k ν_v = Cov_Planch(Σ_□ h^k, ω₃)`:
  `M_0 = 0`, `M_2 = |C₃| = n(n−1)(n−2)/3` (via the classical identity `Σ_□ h² = Σ_□ c² + n²`), and
  `M_1..M_8 > 0`.

## Three "easy proof" routes — each has a counterexample (none is a general proof)

The negativity of `Cov(H_s, ω₃)` is a **genuine polynomial-positivity fact**, not a total-positivity /
sign-variation phenomenon at the hook-strata level:

| # | Certificate (would prove A2 if it held ∀n) | Status | First counterexample |
|---|---|---|---|
| (a) | `ν_v` single-signed-crossing (`−` then `+`) ⇒ Karlin variation-diminishing ⇒ `Σ w(v)ν_v ≤ 0` for decreasing `w` | **FALSE for every `n ≥ 6`** | `ν` oscillates: 5 sign changes at `n=6`, up to 7 by `n=14` |
| (b) | cumulative `S_v = Σ_{u≤v} ν_u ≤ 0 ∀v` ⇒ (Abel summation) `Σ e^{−sv}ν_v ≤ 0` | **has a counterexample** | `n=6`: `S_2 = +1 > 0` |
| (c) | `R` has all-nonnegative coefficients ⇒ `R > 0` on `(0,∞)` trivially | **has a counterexample** | `n=6`: coeff signs `+ − + + +` |

(b) and (c) do hold for some `n` (e.g. `n = 7, 9`), which is exactly why they are seductive — but each
fails for infinitely many `n` (the even ones), so neither is a valid general proof. (a) fails for
**every** `n ≥ 6`.

## Status / honesty

This **sharpens** A2 by an exact reduction plus three route-eliminations. It does **not** prove the
kernel. The remaining open sub-problem is now a sharp, concrete polynomial statement:

> **Prove that the degree-`(n−2)` hook-covariance quotient polynomial `R(x)` has no root on the
> nonnegative real axis (equivalently, `R > 0` on `[0,∞)`) for all `n`.**

Because `R` does not have nonnegative coefficients, this is a nontrivial dominance among a few negative
low-order coefficients — the positivity is real, but there is no free lunch. The likely tools are
Hurwitz/root-location or a Plancherel-specific identity for `R`'s coefficients, **not** a
variation-diminishing argument on the hook strata (routes (a)/(b) are closed).

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_A2_polynomial_positivity.py`](../../computations/deltalambda/wlambda_covariance_epic_A2_polynomial_positivity.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-A2-polynomial-positivity.witness.json`

## Cross-references

- A2 hook/Frullani reduction (the prior step): [`2026-07-25-covariance-kernel-A2-hook-reduction.md`](2026-07-25-covariance-kernel-A2-hook-reduction.md)
- The dim²→dim³ synthesis (A1/A5): [`2026-07-25-covariance-kernel-A1-eliminated-dim-threshold.md`](2026-07-25-covariance-kernel-A1-eliminated-dim-threshold.md)
- Attack plan: bean `qou-v8t7`; A2 `qou-ogrk`
