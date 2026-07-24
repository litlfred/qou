# Covariance-kernel epic (qou-x631) — effective-Stein program, Step 1: the ω₃ marginal

**Date:** 2026-07-24 · **Branch:** `claude/covariance-effective-stein-2026-07-24` · **Tier:**
Stein-method ingredients (exact chain + float moments) · **Discipline:** scope-(a); no fit; nothing
wired; no `c_k`; L2 unchanged (2/7). **Epic:** `qou-x631` (Phase 6).

## Context

The kernel `Cov_Planch(f, ω₃) ≤ 0` is closable (multi-session) only via a **joint effective
Berry–Esseen** bound on `(ln f, ω₃)` — controlling the transfer-factor error in
`Cov(f,ω₃) = Cov(e^{ln f}, ω₃) ≈ E[f]·Cov(ln f, ω₃)` below the negative main term (Route 1). This note
is **Step 1**: the *marginal* Stein ingredients for the 3-cycle content-spread `ω₃`, the direct k=3
analogue of Fulman's k=2 (transposition) computation (`math/0305423`, which is marginal-only).

## Setup

On the Plancherel-reversible down-up chain (Phase 5), `ω₃ = Σc² − C(n,2)` is an eigenfunction:
`E[ω₃(λ*)|λ] = (1−τ₃)ω₃(λ)`, `τ₃ = 3/n`. Normalise `W := ω₃/σ`, `σ² := Var_P(ω₃)`. Then
`E[W*|W] = (1−τ₃)W`, and Stein's exchangeable-pair Berry–Esseen bound (Fulman Thm 1.3) is
`|P(W≤x)−Φ(x)| ≤ c₁·A(n) + c₂·B(n)`, with dimensionless ingredients

- `A(n) := (1/τ₃)·√Var_P( E[(W*−W)² | λ] )` — fluctuation of the conditional variance,
- `B(n) := √( E_P|W*−W|³ / τ₃ )` — third-moment term.

## Results (verified `n ≤ 12`)

- **Exact variance:** `Var_P(ω₃) = n(n−1)(n−2)/3` — the number of 3-cycles in `S_n` (the size of the
  conjugacy class). Clean, and the expected form for a central-character variance.
- **Eigenfunction identity:** `E_P[(W*−W)²] = 2τ₃` exactly (all n), with `E_P[W]=0`, `Var_P(W)=1`.
- **Decay rates (tail log-log slope):** `A(n) ~ n^{−0.33}`, `B(n) ~ n^{−0.29}` — so the marginal CLT
  rate for the 3-cycle content-spread is `~ n^{−0.3}`, comparable to Fulman's `n^{−1/4}` for the
  transposition. The Stein machinery transfers cleanly to k=3.

## Scope / honesty

This is the **marginal** CLT ingredient — a **stepping stone**, not a bound on the kernel. The kernel
is the **joint** covariance `Cov(f, ω₃)`, and closing it needs the joint effective Berry–Esseen on
`(ln f, ω₃)` (Step 2+), which is **open** and **not in the literature** (Fulman gives only the marginal
transposition CLT; Ivanov–Olshanski give joint *asymptotic* Gaussianity but with no effective
constants). Step 1 establishes the k=3 marginal machinery and its rate; the joint bound is the
multi-session core.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_phase6_marginal_stein.py`](../../computations/deltalambda/wlambda_covariance_epic_phase6_marginal_stein.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-phase6-marginal-stein.witness.json`

## Cross-references

- Route-1 exchangeable pair + Dirichlet form: [`2026-07-24-covariance-kernel-route1-exchangeable-pair.md`](2026-07-24-covariance-kernel-route1-exchangeable-pair.md)
- Fulman, *Stein's Method and Plancherel Measure* (`math/0305423`, TAMS 2005)
