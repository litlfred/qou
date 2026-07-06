# q-deformed Reeb-flow scale test: a huge q-enhancement, but not yet a forced number

**Date:** 2026-06-20
**Branch:** `claude/qbk2-qdeformed-scale-2026-06-20`
**Status:** Promising lead — SUGGESTIVE, **not** established. No fit, nothing wired.
**Bean:** [`qbk2`](../../.beans/qbk2--qbessel-2nd-kind-quadratic-action-binding-correction.md)
**Follows:** PR #2541 (Reeb-flow radial argument)
**Script:** [`computations/qbeta/qbessel_qdeformed_reeb_scale.py`](../../computations/qbeta/qbessel_qdeformed_reeb_scale.py) (`SCALE TEST COMPLETE`)

## The test

#2541 found the Reeb-flow correction is **forced + surviving** but ~25× small *at the
classical `q→1` first pass*. The owner's next step: does the substrate **q-deformation**
close the gap? This runs it in the correct **q-deformed convention**.

**Convention finding (why self-contained).** The Hahn–Exton `J_ν(x;q)` does **not** reduce
to classical `J_ν(x)` at fixed `x`: it carries a q-Gamma / `(1−q)^{−ν}` normalization and
`(q;q)_∞→0` as `q→1` (verified: `ν=2.5, x=1.3` gives `J(q=0.9)=−0.167` vs classical
`+0.091`). So #2541's classical proxy is a *different convention* — not directly
comparable. The real q-deformed propagator is the #2533 object
`G_q(w)=g₁(w)g₂(w)/D(w)`, `w=q·θ_λ²`, evaluated at the forced Reeb point.

## Result (deuteron) — and the critical-distance diagnostics

| Quantity | Value |
|----------|-------|
| `δ_q(q₀)` | **26.83** |
| `|δ_q| / (B(D)/m_e ≈ 4.35)` | **6.16** (vs #2541 classical **0.04**) |
| cross-anchor spread (q₀ vs q_μ) | 3.3% (stable) |
| **half-integer proxy swing (±0.5)** | **43%** ⚠ |
| **single-block domination** | **64%** — block `[1,1,1,1,1,1]`, dim 1, at `ν=−0.5` ⚠ |

## Honest verdict — SUGGESTIVE, NOT established

**The good (real) finding:** the q-deformation is a **huge effect** — it lifts the ratio
from #2541's classical **0.04×** into the **~6× ballpark**, a **~150× enhancement**. The
forced Reeb-flow correction, in the correct q-convention, is in the *same order of
magnitude* as the deuteron binding. That is a genuine, non-obvious result.

**The disqualifiers (why it is not yet a number):**

1. **Proxy-dependent (43% swing).** The `±0.5` half-integer offset — introduced only to
   dodge the integer Neumann resonance — is a residual **free choice**, and `δ_q` swings
   43% with it. #2536's obstruction-1 (an unforced knob) is creeping back at the order.
2. **Single-block-dominated (64%).** 64% of `δ_q` comes from one `dim=1` block at an
   **unphysical negative order `ν=−0.5`** (the proxy applied to the degenerate `ν=0` sign
   rep). That is an artifact, not a robust per-block sum.
3. **Missing ingredients:** real `y_λ` Markov weights, a definite bar-parity, and — the
   crux — the **genuine integer-order log-Neumann `Y_n`** (no `±0.5` proxy).

## What it takes to settle it (and the discipline guard)

The lead is worth pursuing because the q-enhancement is real and large. But establishing
it requires:

- **The proper integer-order log-Neumann** `Y_n(x;q)` via the `ν→n` limit — this removes
  the proxy swing and the unphysical negative-order artifact (both disqualifiers come
  from the proxy). This is the decisive next computation.
- **Real `y_λ` weights** and the `χ_λ` factor in the binding sum.
- **A declared bar-parity** (gate 2).

> **Critical-distance guard:** matching `B(D)` by *choosing* the offset sign or a prefactor
> would be a fit and fails the Δ_λ discipline. The number must come out of the forced
> integer-order log-Neumann + forced weights, or it is not a result. On this
> convention-correct first cut, the scale is **plausibly reachable but not yet reached**.

No fit; nothing wired; `c_k`/`Δ_λ` stay cal-anchored. Status: **promising lead, proxy-
limited** — the integer-order log-Neumann build is the gating next step.
