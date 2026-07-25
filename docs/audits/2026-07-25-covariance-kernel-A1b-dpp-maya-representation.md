# Covariance-kernel epic (qou-x631) — DPP route: the Maya representation + depoissonization obstruction

**Date:** 2026-07-25 · **Branch:** `claude/covariance-kernel-dpp-maya-2026-07-25` · **Tier:**
exact structural bridge + obstruction localization · **Discipline:** scope-(a); no fit; nothing
wired; no `c_k`; L2 unchanged (2/7). **Epic:** `qou-x631`, attack `qou-g0n2` (A1b / DPP).

## Why this route

Every prior attack converged on the same missing tool: a determinantal / generating-function handle
on `ν_v = Cov_Planch(N_v, ω₃)` — the hook-count-vs-content-spread covariance — since the elementary
character / shifted-symmetric machinery is blind to the extra `dim` factor (the dim²→dim³ threshold)
and no sign-variation certificate certifies the A2 polynomial positivity. The **determinantal point
process** (DPP) structure of the Plancherel measure is that tool. This tranche sets it up and locates
its difficulty.

## The structural bridge (exact, verified n ≤ 10)

Encode `λ` by its **Maya diagram**: particle set `P(λ) = {λ_i − i : i ≥ 1} ⊂ ℤ` (vacuum
`{−1,−2,…}`), occupations `m_a = 1_{a∈P}`. Then two exact identities make the covariance a
**quadratic** DPP statistic:

| Claim | Identity | Meaning |
|---|---|---|
| 1 | `N_v = Σ_a (1 − m_a) m_{a+v}` | hook length = particle–hole distance; `N_v` is quadratic in `m` |
| 2 | `ω₃ = Σ_v v² N_v − n² − C(n,2)` | via `Σ_□ h² = Σ_□ c² + n²`; `ω₃` is also quadratic in `m` |

So `Cov(N_v, ω₃)` is the covariance of two quadratic occupation statistics. Under the **θ-poissonized
Plancherel** measure `P_θ(λ) = e^{−θ} θ^{|λ|} (dim λ / |λ|!)²`, the occupations `m_a` form a
determinantal point process with the **discrete-Bessel kernel** (Borodin–Okounkov–Olshanski,
[`math/9905032`](https://arxiv.org/abs/math/9905032)), so `Cov(N_v, N_w)` reduces by Wick to
kernel contractions.

## The obstruction — depoissonization is the real difficulty

The kernel condition that powers A2 is `Σ_v ν_v = 0`. It holds at **fixed `n`** because `Σ_v N_v = n`
is then a constant, so the `|λ|`-comovement is projected out. At the **poissonized** level `|λ|`
fluctuates and *dominates*: the same expression `Cov_θ(N_v, Σh²)` comes out **all positive**
(θ = 4: `+12.5, +10.0, …, +0.08`) — the opposite sign structure.

| level | object | `Σ_v(·)` | sign |
|---|---|---|---|
| fixed-`n` | `ν_v = Cov(N_v, Σh²) = Cov(N_v, ω₃)` | `0` | mixed (the A2 object) |
| poissonized | `Cov_θ(N_v, Σh²)` | `≠ 0` | **all positive** — `\|λ\|`-comovement dominates |

Hence the determinantal kernel must be **depoissonized** — conditioned on `|λ| = n`, equivalently
the `|λ|`-fluctuation contribution subtracted — before its sign reflects the fixed-`n` covariance.
That conditioning, **not** the kernel algebra, is where the DPP route's difficulty concentrates.

## Status / honesty

Establishes the exact structural bridge (Maya quadratic representation) and names the real
obstruction. It does **not** prove the kernel. It scopes the next attempt precisely:

> Compute the `|λ| = n`-conditioned discrete-Bessel kernel (or the steepest-descent depoissonization
> of `Cov_θ(N_v, N_w)` with the `|λ|`-mean-field subtracted), and read the sign of the resulting
> fixed-`n` covariance.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_A1b_dpp_maya_representation.py`](../../computations/deltalambda/wlambda_covariance_epic_A1b_dpp_maya_representation.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-A1b-dpp-maya-representation.witness.json`

## Cross-references

- A2 polynomial-positivity (the reduction this tool would prove): [`2026-07-25-covariance-kernel-A2-polynomial-positivity.md`](2026-07-25-covariance-kernel-A2-polynomial-positivity.md)
- dim²→dim³ threshold (why the elementary machinery fails): [`2026-07-25-covariance-kernel-A1-eliminated-dim-threshold.md`](2026-07-25-covariance-kernel-A1-eliminated-dim-threshold.md)
- Attack plan: bean `qou-v8t7`; DPP `qou-g0n2`. BOO `math/9905032`.
