# Δ_pn L2 residual: formalize-first prune — the missing term is the EM self-energy (sign fixed)

**Date:** 2026-07-11
**Depends on:**
[`2026-07-11-np-splitting-residual-not-q0-knob.md`](2026-07-11-np-splitting-residual-not-q0-knob.md)
(the 0.63% residual is structural, not a q₀ knob).
**Lean:** [`QOU.MassTheory.NeutronProtonEMSign`](../../content/quantum-observable-universe/lean/QOU/MassTheory/NeutronProtonEMSign.lean) (sorry-free, over ℚ).

> **Scope note (2026-07-11).** This prune addresses the **observations-level**
> `Δm = α·|ΔΦ|` traced-volume formula (0.63% error). The **production** Δ_pn
> (dashboard Path C, `Q_β + m_e`) is far more accurate (0.76 ppm) and its L2 gap
> is **Q_β-driven**, not this EM residual — see
> [`2026-07-11-trio-shared-root-qbeta-bottleneck.md`](2026-07-11-trio-shared-root-qbeta-bottleneck.md).
> The EM-sign result below is correct for the `α·|ΔΦ|` object; it is *not* the
> production trio gap.

Per the **formalize-first** discipline (AGENTS.md), before scanning candidate
closures for the Δ_pn residual, prove the invariant the missing term must
satisfy. Result: the correction is the **electromagnetic self-energy**, and its
**sign is fixed parameter-free** by the quark charge structure.

## The provable invariant (sign)

The pairwise Coulomb charge-structure factor `Σ_{i<j} q_i q_j`
(`q_u = 2/3`, `q_d = -1/3`):

| ordering | `Σ q_i q_j` |
|----------|-------------|
| proton `uud` | `0` |
| neutron `udd` | `-1/3` |
| **gap** `Σqq(p) − Σqq(n)` | **`+1/3 > 0`** |

So the proton carries the **larger** Coulomb self-energy ⇒ EM makes the proton
heavier ⇒ the EM correction to `Δm = m_n − m_p` is **negative**
(`em_correction_neg`, conditional on `δ = -k·gap`, `k > 0` — the standard
self-energy sign). The leading traced-volume piece **over**-predicts `Δm`
(residual `< 0`), so the EM term has **exactly the right sign** to close it.

This is the classic result (proton "should" be heavier from EM; the down–up
quark-mass excess overcompensates) — here derived as a parameter-free sign
constraint from the charge assignments alone.

## What it prunes

- **Rules out** a charge-blind `ℏ_q`-tower correction as the missing term: any
  closure must be **charge-odd** (source `Σqq(p) − Σqq(n) ≠ 0`) and must
  **reduce** `Δm`. A pure q-deformation of `|ΔΦ|` cannot supply the
  charge-structure dependence.
- **Magnitude is order-consistent but not decisive.** `|r − 1| = 0.634%`,
  `α_EM = 0.730%`, so `(r−1)/α_EM ≈ −0.87` — EM-order. But `ℏ_q² = 0.982%` is
  the same size, so *magnitude alone* does not separate EM from a q-term; the
  **sign + charge-structure** is the discriminator, not the size.

## Trio linkage (why this matters beyond Δ_pn)

Δ_pn, `m_n`, and `Q_β` are the three failing L2 observables sharing a single
root ([`2026-05-30-l2-100x-status-3-failing-shared-root.md`](2026-05-30-l2-100x-status-3-failing-shared-root.md)).
They all reduce to the **same `Δm` correction**:

```
m_n = m_p + Δm            Q_β(n→p) = Δm − m_e
```

so a single EM charge-structure correction to `Δm` moves all three coherently.
The formalize-first sign result therefore constrains the whole trio, not just
Δ_pn.

## Scope (honest)

This **prunes and constrains**; it does **not** close L2. The EM coupling `k` is
not derived from the 13 categorical drivers, so **nothing is wired into
production** (anti-laundering rule). The productive next step is to derive the
categorical form of the EM self-energy (the framework already carries a
categorical `α_EM = [2]_q·(1 − h²α)`, PR #1511) and check whether
`−k·(1/3)` at that `k` reproduces the `−0.634%` residual — a *charge-odd*
scan, now that the sign and charge-structure are fixed.
