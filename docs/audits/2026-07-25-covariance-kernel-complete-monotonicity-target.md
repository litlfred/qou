# Covariance-kernel epic (qou-x631) — attack A3 refinement: the complete-monotonicity target

**Date:** 2026-07-25 · **Branch:** `claude/covariance-kernel-attack-a3-cumulants-2026-07-25` ·
**Tier:** structural discovery (60-dps) · **Discipline:** scope-(a); no fit; nothing wired; no `c_k`;
L2 unchanged (2/7). **Epic:** `qou-x631`, attack `qou-4wl1` (A3).

## The discovery

Executing attack A3 (bound the transfer remainder via the mixed-cumulant series), the Taylor
coefficients of the dimension-tilted mean revealed a clean, unifying structure.

With `g(θ) := E_{β=2+θ}[ω₃] = Σ_λ f^{2+θ}ω₃ / Σ_λ f^{2+θ}` (the exponentially-tilted mean of
`ω₃ = Σc² − C(n,2)`): `g(0)=0`, `g(1)=` kernel, `g'(0)=Cov_Planch(ln f,ω₃)`. Its Taylor coefficients
`a_m := g^{(m)}(0)/m!` are the mixed Plancherel cumulants `κ_{m+1}(ln f;…;ω₃)/m!`. Verified 60-dps:

> **`sign(a_m) = (−1)^m` exactly for `n = 8..17`, to order `m = 10`.**

This is the **complete-monotonicity signature** of `−g'(θ)` (its Taylor coefficients all `≥ 0`).
Also `Σ_{m≥2}|a_m| < |a_1|` for all n (absolute domination — stronger than the Phase-7 `|R|<|g'(0)|`).
For `n ≤ 7` the low orders still alternate but high orders (`m ≳ 5`) deviate — a small-n boundary
effect, and those n are covered by exact enumeration (`k ≤ 40`) anyway.

## Why it matters — one target closes everything

If `−g'(θ)` is **completely monotone** on `θ ∈ [0,∞)`, Bernstein's theorem gives a positive-measure
representation

> `−g'(θ) = ∫_0^∞ e^{−θ s}\,dμ(s)`,  `μ ≥ 0`,

so `g'(θ) ≤ 0` for **all** `θ ≥ 0`. Then immediately

- `g(1) = ∫_0^1 g'(θ)\,dθ ≤ 0` — the **kernel** `cov(k) ≤ 0`;
- `E_β[ω₃] = g(β−2) ≤ 0` for **all** `β ≥ 2` — the **whole β-family** (§Phase 3).

This **unifies** the two previously-separate legs: attack **A2** is exactly the `θ=0` endpoint
`g'(0) ≤ 0`, and attack **A3** is the all-`θ` statement — both are consequences of one property,
`−g'` completely monotone. It also names a concrete proof tool (a Hausdorff/Bernstein moment
representation), which none of the ~9 eliminated local certificates offered.

## The rigorous target (for a proof)

Prove `−g'(θ) = −\frac{d}{dβ}E_β[ω₃]\big|_{β=2+θ}` is completely monotone for `n ≥ n₀`, via the
tilted-mean / monotone-likelihood-ratio / moment structure of
`g(θ) = ⟨ω₃\, e^{θ\ln f}⟩ / ⟨e^{θ\ln f}⟩` (⟨·⟩ = Plancherel). A natural route: exhibit a positive
measure `μ` (a "spectral" decomposition of the dimension-tilted content-spread covariance), or show
the tilted family `Q_θ ∝ e^{θ\ln f}·P` has `E_{Q_θ}[ω₃]` with alternating θ-derivatives from an
association / MLR property of `(ln f, ω₃)`.

## Honesty

The `(−1)^m` pattern is verified via the **signs of Taylor coefficients to order 10** for `n=8..17`
— strong evidence, **not** a proof that `−g'` is exactly completely monotone (a finite exponential-sum
ratio is analytic; exact CM is an all-orders statement, and the small-n deviations show the property
is at best asymptotic in `n`). No proof of the kernel is claimed. This **sharpens and unifies** the
open target and supplies a proof tool; it does not close it.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_phase8_complete_monotonicity.py`](../../computations/deltalambda/wlambda_covariance_epic_phase8_complete_monotonicity.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-phase8-complete-monotonicity.witness.json`

## Cross-references

- Attack plan: bean `qou-v8t7` (A2 = θ=0 endpoint, A3 = this)
- Transfer-error bound (Phase 7): [`2026-07-24-covariance-kernel-effective-stein-step2-transfer-bound.md`](2026-07-24-covariance-kernel-effective-stein-step2-transfer-bound.md)
- Interval reduction (Phase 4): [`2026-07-24-covariance-kernel-interval-fkg-reframing.md`](2026-07-24-covariance-kernel-interval-fkg-reframing.md)
