# Covariance-kernel epic (qou-x631) — effective-Stein, Step 2: the transfer-error bound

**Date:** 2026-07-24 · **Branch:** `claude/covariance-effective-stein-nqd-2026-07-24` · **Tier:**
bound (40-dps) · **Discipline:** scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged (2/7).
**Epic:** `qou-x631` (Phase 7). **Follows:** Step 1 (`…-effective-stein-step1-marginal.md`, #4170).

## The bound

Write `g(θ) := E_{β=2+θ}[ω₃] = Σ_λ f^{2+θ}ω₃ / Σ_λ f^{2+θ}` (with `ω₃ = Σc² − C(n,2)`). Because
`f^θ = e^{θ ln f}`, `g` is the **dimension-tilted mean** of `ω₃`, and its Taylor coefficients
`g^{(m)}(0)` are the **mixed Plancherel cumulants** `κ_{m+1}(ln f;…;ln f;ω₃)`. Three anchors:

- `g(0) = E_2[ω₃] = 0` (Plancherel content mean, exact);
- `g(1) = E_3[ω₃] = cov(n)/cubeSum(n)` — the **kernel**, up to a positive factor;
- `g'(0) = Cov_Planch(ln f, ω₃)` — the **Gaussian / linear main term**.

Taylor at `θ=1`: `g(1) = g'(0) + R`, `R := Σ_{m≥2} g^{(m)}(0)/m!` (the non-Gaussian remainder). Hence

> **`cov(n) ≤ 0`  ⇐  [ `g'(0) = Cov_Planch(ln f, ω₃) ≤ 0` ]  AND  [ `|R| < |g'(0)|` ]**

— the linear term dominates the remainder, so the sum keeps `g'(0)`'s (negative) sign.

## Result — the bound holds with margin (40 dps, `n ≤ 14`)

- `g'(0) < 0` for every `n` (the log-dimension is negatively correlated with the content-spread).
- Transfer ratio `r := g(1)/g'(0) ∈ (0.54, 0.87)`, so `|R|/|g'(0)| = |r − 1| ∈ (0.13, 0.46) < 1`.

The non-Gaussian correction is **at most ≈46 %** of the linear term — never enough to flip the sign.
This is the concrete quantitative statement the joint effective Berry–Esseen must certify.

## Route (negative quadrant dependence, NQD) — ELIMINATED

A clean sufficient condition would be that `(ln f, ω₃)` are **NQD** — the Hoeffding kernel
`H(s,t) = P(ln f>s, ω₃>t) − P(ln f>s)P(ω₃>t) ≤ 0` for all thresholds — which by Hoeffding's identity
`Cov(g(X),h(Y)) = ∫∫ g'h' H` would give `Cov(g(ln f), ω₃) ≤ 0` for **every** increasing `g` (the
kernel, the interval, and the whole `β≥2` family at once). It **fails**: `H(s,t) > 0` at some
thresholds, and the bad count grows with `n` (`n=4..14`: `1,1,5,5,10,20,46,50,91,142,171`; worst
`H ≈ +0.13`). So there is **no pointwise NQD certificate** — the sign is (again) a weighted-integral
cancellation. This is the 9th eliminated local/pointwise certificate across the epic.

## Honesty

The bound `|R| < |g'(0)|` and the main-term sign `g'(0) ≤ 0` are **verified numerically**, not proved.
Both are concrete analytic targets; the rigorous versions need **Plancherel-cumulant control of the
`g^{(m)}(0)`** (Kerov CLT gives their `n`-scaling), which is the open core of the effective-Stein
program. No proof of the kernel is claimed; the Δ_λ growth chain stays Lean-proved *modulo* the kernel.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_phase7_transfer_bound.py`](../../computations/deltalambda/wlambda_covariance_epic_phase7_transfer_bound.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-phase7-transfer-bound.witness.json`

## Cross-references

- Step 1 (marginal): [`2026-07-24-covariance-kernel-effective-stein-step1-marginal.md`](2026-07-24-covariance-kernel-effective-stein-step1-marginal.md) (#4170)
- Route-1 exchangeable pair + Dirichlet form: [`2026-07-24-covariance-kernel-route1-exchangeable-pair.md`](2026-07-24-covariance-kernel-route1-exchangeable-pair.md)
- Fulman (`math/0305423`); Ivanov–Olshanski (Kerov CLT, `math/0304010`)
