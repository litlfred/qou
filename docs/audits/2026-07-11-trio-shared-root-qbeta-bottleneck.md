# Q_β / m_n / Δ_pn L2 trio: shared-root consistent; the bottleneck is Q_β (not the α·|ΔΦ| residual)

**Date:** 2026-07-11
**Probe:** [`computations/probes/trio_shared_root_consistency_probe.py`](../../computations/probes/trio_shared_root_consistency_probe.py).
**Source:** `computations/per-observable-100x-status.witness.json` (Path C rows).

Confirms the "single shared root" of the three failing L2 observables
([`2026-05-30-l2-100x-status-3-failing-shared-root.md`](2026-05-30-l2-100x-status-3-failing-shared-root.md))
**quantitatively**, and — importantly — re-scopes where the residual actually
lives.

## Two different "Δ_pn" objects (do not conflate)

| object | formula | error |
|--------|---------|-------|
| **observations** (content block) | `Δm = α·|ΔΦ|` (traced-volume) | **0.63%** |
| **production** (dashboard, Path C) | `Δ_pn = m_n − m_p = Q_β + m_e` | **0.76 ppm** (756 ppb, 159× miss) |

The `α·|ΔΦ|` formula (the one whose EM-sign was pruned in
[`2026-07-11-np-splitting-L2-em-sign-prune.md`](2026-07-11-np-splitting-L2-em-sign-prune.md) /
`QOU.MassTheory.NeutronProtonEMSign`) is a **cruder standalone quark-level
estimate**, ~10⁴× less accurate than the production Path-C value. The EM-sign
result is correct **for that object**, but it is **not** the production trio
gap.

## Shared-root consistency (Path C) — confirmed to ~10⁻⁹ MeV

`m_n = m_p + Q_β + m_e`, `Δ_pn = Q_β + m_e`, `m_e` exact (CAL-1), so the
residuals `r(·) = pred − codata` must satisfy `r(Δ_pn) = r(Q_β)` and
`r(m_n) = r(m_p) + r(Q_β)`:

| residual | value (MeV) | err |
|----------|-------------|-----|
| `r(m_p)` | `+1.267×10⁻⁶` | 1.35 ppb |
| `r(Q_β)` | `+9.765×10⁻⁷` | **1248 ppb** |
| `r(m_n)` | `+2.245×10⁻⁶` | 2.39 ppb |
| `r(Δ_pn)` | `+9.772×10⁻⁷` | 756 ppb |

- `r(Δ_pn) − r(Q_β) = 6.9×10⁻¹⁰ MeV` ✓
- `r(m_n) − (r(m_p) + r(Q_β)) = 1.5×10⁻⁹ MeV` ✓

The trio is **algebraically consistent** with the single Path-C root (as it must
be — Path C builds them additively). No hidden per-observable term is needed to
reconcile them.

## The bottleneck is Q_β

`Q_β (+1248 ppb)` is the dominant residual; it drives `Δ_pn (756 ppb)` directly
(`Δ_pn = Q_β + m_e`) and, with `m_p (1.35 ppb)`, drives `m_n (2.39 ppb)`.
**Closing the trio ⇒ closing Q_β.**

Q_β's residual is the **c_k-truncation-order / Habiro-element** problem — a
deeply-documented open item with its own flip-flop history
([`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md),
[`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)). It is
**not** closed by an EM charge-structure scan on the `α·|ΔΦ|` formula, and this
audit does not attempt one — pointing a coupling fit at the wrong (observations-
level) residual would be content-free.

## Takeaway for future work

- The production L2 target for the trio is **Q_β**, at the **ppb** level — a
  research-grade (Subgoal) problem, not a quick scan.
- The traced-volume `α·|ΔΦ|` closed form (exact, ppQ-capable per
  [`2026-07-11-np-splitting-residual-not-q0-knob.md`](2026-07-11-np-splitting-residual-not-q0-knob.md))
  and its EM-sign prune are **correct but scoped to the observations block**,
  not the production trio gap.
