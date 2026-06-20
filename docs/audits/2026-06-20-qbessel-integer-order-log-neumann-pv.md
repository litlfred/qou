# Integer-order log-Neumann (proxy-free): #2545's 6× deflates, but a real ~1× signal survives

**Date:** 2026-06-20
**Branch:** `claude/qbk2-log-neumann-limit-2026-06-20`
**Status:** Proxy-free integer-order test — encouraging but NOT established. No fit, nothing wired.
**Bean:** [`qbk2`](../../.beans/qbk2--qbessel-2nd-kind-quadratic-action-binding-correction.md)
**Follows:** PR #2545 (q-deformed scale, proxy-limited)
**Script:** [`computations/qbeta/qbessel_integer_order_log_neumann_pv.py`](../../computations/qbeta/qbessel_integer_order_log_neumann_pv.py) (`INTEGER-ORDER TEST COMPLETE`)

## What #2545 left open

#2545 found `|δ_q|/(B(D)/m_e) = 6.16` but flagged it as **proxy-limited**: the
`ν = dim−1 ± 0.5` offset (to dodge the integer Neumann resonance) gave a **43% swing**
and **64% single-block domination**. The gating next step was the **genuine integer
order** — no `±0.5` proxy. This runs it.

## Finding 1 — `G_q` is singular at *every* forced integer order

The q-deformed coincidence propagator `G_q(w;ν) = g₁g₂/D` is **not finite** at the
physically-forced order `ν = dim_λ−1`:

- **`ν ≥ 1` (dim ≥ 2): a simple pole.** The Neumann resonance `(q^k−q^ν)→0` at `k=ν`
  makes `g₂` diverge; numerically `G_q(n−ε) ≈ +c/ε`, `G_q(n+ε) ≈ −c/ε` (antisymmetric).
- **`ν = 0` (dim = 1): a confluent double-root.** The two indicial roots `ρ=0` and
  `ρ=−ν=0` **coincide** ⇒ Casoratian `D→0` ⇒ `G_q→∞` — a *different*, worse singularity
  that the principal value does **not** regularize.

**So #2545's `ν±0.5` was sampling the tail of these singularities 0.5 away — its `6×`
was largely the pole, not a physical binding-scale match.** This deflates #2545.

## Finding 2 — the proxy-free PV signal on the `dim ≥ 2` blocks is real and on-scale

For `ν ≥ 1` the pole is antisymmetric, so its unique proxy-free finite part is the
**principal value** `PV[G_q](w;n) = ½[G_q(n−ε)+G_q(n+ε)]`, which **converges** (e.g.
`ν=4` block: `0.066011 → 0.065992 → 0.065992` as `ε: 10⁻²→10⁻⁴`). Summing the forced
PV correction over the `dim ≥ 2` blocks:

| Quantity | Value |
|----------|-------|
| `δ_PV` (dim ≥ 2) | **5.52** |
| `|δ_PV| / (B(D)/m_e ≈ 4.35)` | **1.27** (on scale) |
| cross-anchor spread (q₀ vs q_μ) | **0.76%** (stable) |
| single-block domination | **31.6%** (not dominated) |

This is **proxy-free, on-scale (~1×), un-dominated, and cross-anchor stable** — genuinely
better evidence than #2545's pole-artifact `6×`.

## Honest status — NOT established; two open constructions

Encouraging, but **not** a result yet, because:

1. **The `dim = 1` confluent blocks are unsolved.** At `ν=0` the indicial roots coincide;
   the PV does not regularize the confluent degeneracy (the blocks blow up, e.g. `[1⁶]`
   grows without bound as `ε→0`). A **clean total is impossible** until the `ν=0`
   **confluent log solution** is constructed — a genuine, separate q-special-function task.
2. **PV ≠ rigorous `Y_n` (yet).** The principal value is the finite part of a simple
   pole; whether it equals the q-analog of the genuine log-Neumann coincidence propagator
   `(πx/2)J_n Y_n` needs the **L'Hôpital `ν→n` construction** to justify. The `~1.27`
   could shift under the rigorous object.

## Net

- #2545's headline `6×` was **a resonance-pole artifact** — correctly flagged there as
  proxy-limited, now confirmed.
- The proxy-free `dim ≥ 2` correction is **`~1.27×` the deuteron binding, un-dominated,
  cross-anchor stable** — a real, encouraging signal for the gapped blocks.
- **Two constructions gate any claim:** the `ν=0` confluent log solution (for a clean
  total) and the rigorous `Y_n` (to validate the PV). Until both, this is a **promising,
  partially-computed lead**, not a wireable result.

**Critical-distance note:** the `~1.27` must be treated as provisional — it is a
PV-regularized partial sum, and matching `B(D)` by choosing the regularization or
omitting the confluent blocks would be a fit. No fit; nothing wired; `c_k`/`Δ_λ`
cal-anchored. The Reeb-flow argument (forced, surviving) stands; the scale is
**plausible but not yet honestly closed**.
