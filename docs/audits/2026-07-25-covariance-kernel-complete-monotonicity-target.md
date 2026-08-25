# Covariance-kernel epic (qou-x631) — attack A3: CM signature holds, but genuine CM is REFUTED

**Date:** 2026-07-25 · **Branch:** `claude/covariance-kernel-attack-a3-cumulants-2026-07-25` ·
**Tier:** structural test + route-elimination (60-dps) + literature intel · **Discipline:** scope-(a);
no fit; nothing wired; no `c_k`; L2 unchanged (2/7). **Epic:** `qou-x631`, attack `qou-4wl1` (A3).

> **Correction note.** An earlier version of this document proposed the complete monotonicity of
> `−g'` as a *target that would close everything*. The decisive moment/Hankel test (below) **refutes**
> genuine complete monotonicity. This document now records the honest result: the sign-alternation
> *signature* holds, but it is not sufficient, and the Bernstein route is eliminated.

## Setup

`g(θ) := E_{β=2+θ}[ω₃] = Σ_λ f^{2+θ}ω₃ / Σ_λ f^{2+θ}`, with `ω₃ = Σc² − C(n,2)`. Notation
(agent-confirmed against Ivanov–Olshanski / Śniady): **`ω₃ = p#₃ = Σ₃ = R₄ + R₂`, the 3-cycle central
character** (not `Σ₂`; `p#₂ = 2Σc` is the transposition). `g(0)=0`, `g(1)=` kernel,
`g'(0)=Cov_Planch(ln f, ω₃)`. Taylor coefficients `a_m := g^{(m)}(0)/m!` are the mixed Plancherel
cumulants `κ_{m+1}(ln f;…;ω₃)/m!`.

## Finding 1 — the sign-alternation signature holds (necessary, not sufficient)

`sign(a_m) = (−1)^m` **exactly for n = 8..17, to order m = 10** (60-dps); for n ≤ 7 the low orders
alternate but high orders deviate (small-n boundary). Also `Σ_{m≥2}|a_m| < |a_1|` for all n (absolute
domination — the Phase-7 transfer bound `|R| < |g'(0)|` in stronger form). This is the *necessary*
part of complete monotonicity of `−g'`.

## Finding 2 — genuine complete monotonicity is REFUTED (the decisive test)

Sign-alternation is **necessary but not sufficient** for CM. The actual criterion is the
Hausdorff/Stieltjes moment problem: `−g'` is completely monotone iff the would-be moments
`m_k := (k+1)!\,|a_{k+1}|` form a Stieltjes moment sequence, i.e. the Hankel matrices `H0=[m_{i+j}]`
and `H1=[m_{i+j+1}]` are both PSD (then `−g'(θ)=∫_0^∞ e^{−θs}dμ(s)` with `μ ≥ 0`).

They are **not**: the Hankel min-eigenvalues are negative for essentially all n, **robustly** at both
`3×3` (low-order, high-precision `a_1..a_6`) and `4×4` — PSD holds in only ~5/12 cases with no pattern
(borderline, and interleaved with clear failures like n=15). So **there is no positive Bernstein
measure `μ`**, `−g'` is **not** completely monotone, and the "one target closes everything via
Bernstein" route is **ELIMINATED** (route-elimination #10 across the epic).

## Net

The sign-alternation + absolute domination is a real but **weaker** structural fact that merely
re-expresses the Phase-7 transfer bound `|R| < |g'(0)|`; it does **not** provide the clean Bernstein
shortcut, and the two legs A2 (`g'(0)≤0`) and A3 (interval / all-θ) are **not** unified by a CM
property. The kernel remains open.

## Literature intel (paper-mining agent, validated numerically)

Mining Ivanov–Olshanski (`0304010`), Śniady (`0411647`), Biane (`0006111`):

- **Exact character-covariance engine.** IO Prop 5.1: `⟨p#_ρ⟩_Planch = n↓ʳ·δ_{ρ=(1ʳ)}`. With Śniady's
  product rule, any `Cov(p#_j, p#_k)` (`j,k≥2`) is a **finite signed connection-coefficient sum** —
  exact, no asymptotics. **Validated:** `Cov_Planch(Σc, ω₃) = 0` exactly (the transposition and
  3-cycle characters are exactly orthogonal — consistent with IO Thm 6.1 asymptotic independence,
  and here it is exact).
- **`ln f ∉ A`** (the algebra of polynomial functions on Young diagrams): there is **no** finite
  `Σ_μ`-expansion of the log-dimension — do not chase one. But `ln f = ½ ln M_n + ½ ln n!` with
  `M_n = dim²/n!`, so `Cov(ln f, ω₃) = ½ E[ω₃ ln M_n]` (the `ω₃`-weighted log-likelihood correlation).
  *(Validated exact; note this is an algebraic reframing, not new leverage — `ln M_n = 2 ln f − ln n!`
  and the constant drops since `E[ω₃]=0`.)*
- **Genus scaling** (Śniady): each handle costs `n⁻¹`; higher mixed cumulants are increasingly
  subleading (Gaussian-fluctuation regime). This is *consistent with* the sign-alternation of the
  low-order `a_m`, but — as Finding 2 shows — does **not** amount to genuine CM.

## Honesty

The signature is verified via signs to order 10; the CM refutation via the Hankel/moment PSD test at
60-dps. No proof of the kernel is claimed; this is an honest **negative** result (CM route eliminated)
plus validated literature machinery for the exact character covariances. The kernel stays an open §3b
conjecture; the Δ_λ growth chain stays Lean-proved modulo it.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_phase8_complete_monotonicity.py`](../../computations/deltalambda/wlambda_covariance_epic_phase8_complete_monotonicity.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-phase8-complete-monotonicity.witness.json`

## Cross-references

- Attack plan: bean `qou-v8t7` (A2 = `g'(0)≤0` endpoint, A3 = remainder/interval)
- Transfer bound (Phase 7): [`2026-07-24-covariance-kernel-effective-stein-step2-transfer-bound.md`](2026-07-24-covariance-kernel-effective-stein-step2-transfer-bound.md)
- Ivanov–Olshanski `0304010`, Śniady `0411647`, Biane `0006111` (in `library/`)
