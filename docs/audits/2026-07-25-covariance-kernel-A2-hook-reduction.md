# Covariance-kernel epic (qou-x631) — A2 advance: the hook / Frullani reduction

**Date:** 2026-07-25 · **Branch:** `claude/covariance-kernel-A2-hook-strat-2026-07-25` · **Tier:**
exact reduction (30-dps) · **Discipline:** scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged
(2/7). **Epic:** `qou-x631`, attack `qou-ogrk` (A2).

## Target

A2 is the leading term of the kernel: prove `Cov_Planch(ln f^λ, ω₃) ≤ 0`, with `ω₃ = Σ_□c(□)² −
C(n,2)` (numerically `< 0` for all `n`). The dim²→dim³ synthesis pinned the obstruction: `ln f = ln
dim λ` is not a shifted-symmetric function, so the exact character-covariance engine does not reach it.
This note reduces it to a much cleaner one-parameter statement.

## Step 1 — hook-stratification and the classical identity `Σh² = Σc² + n²`

By the hook-length formula `ln f = ln(n!) − Σ_□ ln h(□)`, so `Cov(ln f, ω₃) = −Cov(Σ_□ ln h, ω₃)`.
Stratify by hook length: with `N_v(λ) = #{□ : h(□)=v}` and the **signed measure**
`ν_v := Cov_Planch(N_v, ω₃)`,

> `Cov(Σ_□ ln h, ω₃) = Σ_{v≥1} ln(v)·ν_v`.

Its moments are exact and clean:

- `Σ_v ν_v = Cov_Planch(Σ_v N_v, ω₃) = Cov(n, ω₃) = 0`  (`Σ N_v = n`, constant);
- `Σ_v v²·ν_v = Cov_Planch(Σ_□ h², ω₃) = Var_Planch(ω₃) = n(n−1)(n−2)/3 > 0`,

using the **classical identity `Σ_□ h(□)² = Σ_□ c(□)² + n²`** (verified for every `λ ⊢ n`): then
`Cov(Σh², ω₃) = Cov(Σc², ω₃) = Cov(ω₃, ω₃) = Var(ω₃) = |C₃|`. *(Both moment values verified exactly,
`n ≤ 8`.)*

## Step 2 — Frullani integral representation

Frullani's `ln v = ∫_0^∞ (e^{−s} − e^{−vs})/s\,ds`, together with `Σ_v ν_v = 0`, gives the **exact**
representation (verified to high precision, `n ≤ 10`):

> **`Cov_Planch(ln f, ω₃) = ∫_0^∞ \frac{1}{s}\,Cov_Planch(H_s, ω₃)\,ds`,   `H_s(λ) := Σ_□ e^{−s·h(□)}`**

— `H_s = Σ_□ q^{h(□)}` (`q = e^{−s} ∈ (0,1)`), the **hook-length exponential sum**.

## The reduction

Hence **A2 follows from the pointwise sign**

> **`Cov_Planch(H_s, ω₃) ≤ 0`  for all `s > 0`.**

Verified: `Cov(H_s, ω₃) < 0` **strictly** on the interior `s ∈ (0,∞)` (→ 0 at both endpoints), fine
grid, all `n ≤ 13`. This replaces the transcendental `ln`-covariance by a **one-parameter family of
covariances of a positive, analytic hook statistic** — a far cleaner target, and one where the exact
value `Cov(H_s, ω₃) = Σ_v q^v ν_v` is the generating function (Laplace transform) of the hook-covariance
signed measure `ν` with the two moment constraints above (`Σν_v = 0`, `Σv²ν_v = |C₃|`).

## Status / honesty

This **sharpens** A2 by an exact, verified reduction — the cleanest form of the log-covariance leg to
date. It does **not** prove the kernel. The remaining open sub-problem, `Cov_Planch(H_s, ω₃) ≤ 0
∀s>0`, is still hard: `H_s`, like `ln f`, is a **hook functional outside the shifted-symmetric algebra
`A`** (the dim²→dim³ obstruction persists — the reduction trades `log` for `exp`, both hook-based). But
it is a single positive analytic statistic with two exact moment constraints, which is a materially
better starting point than the raw `ln`-covariance.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_A2_hook_reduction.py`](../../computations/deltalambda/wlambda_covariance_epic_A2_hook_reduction.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-A2-hook-reduction.witness.json`

## Cross-references

- The dim²→dim³ synthesis (A1/A5): [`2026-07-25-covariance-kernel-A1-eliminated-dim-threshold.md`](2026-07-25-covariance-kernel-A1-eliminated-dim-threshold.md)
- Attack plan: bean `qou-v8t7`; A2 `qou-ogrk`
