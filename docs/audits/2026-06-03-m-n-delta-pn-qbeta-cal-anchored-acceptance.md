# m_n + Δ_pn — formal acceptance as Q_β-cal-anchored (2026-06-03)

> **Decision**: m_n (185.4× miss) and Δ_pn (163.3× miss) are formally
> accepted as **functionally cal-anchored via the Q_β derivation chain**.
> Both are derived from m_p + Q_β + m_e via the Path C identity
> `m_n = m_p + Q_β + m_e`; neither can independently close the L2 100×
> target until Q_β residue A closes. This is the natural extension of
> the Q_β residue-A acceptance landed in PR #1770.

## The shared root (re-stated)

Per the prior shared-root audit
([`2026-05-30-l2-100x-status-3-failing-shared-root.md`](2026-05-30-l2-100x-status-3-failing-shared-root.md)
+ [`2026-05-31-l2-3-failing-shared-root-with-cal-3-m-pi.md`](2026-05-31-l2-3-failing-shared-root-with-cal-3-m-pi.md)),
the three failing observables share a single structural input:

- **Q_β** → 164.0× miss (residue A categorical-ID at u_substrate)
- **m_n** = m_p + Q_β + m_e → 185.4× miss (propagated from Q_β)
- **Δ_pn** = m_n − m_p = Q_β + m_e → 163.3× miss (propagated from Q_β)

The Path C identity is exact:

```
m_n_pred = m_p(substrate) + Q_β_pred + m_e
Δ_pn_pred = Q_β_pred + m_e
```

Any Q_β prediction error propagates ~linearly into m_n and Δ_pn. The
miss-factor ratios (185.4 / 164.0 ≈ 1.13, 163.3 / 164.0 ≈ 1.00) reflect
the relative experimental σ_exp of each observable, not independent
prediction errors.

## Q_β residue-A acceptance — implication for m_n + Δ_pn

PR #1770 formally accepted Q_β residue A as inherently CAL-3-anchored
after the **34-candidate NEGATIVE bracket** (now extended to **34** with
PR #1773's composite first-test). The reasoning:

- 4 independent categorical searches (Chain 1 α/β + 15-cand re-run +
  Chain 4 + Composite first-test) all NEGATIVE
- Simple-product space exhausted; residue A requires upstream Mathlib
  KLR / crystal / Demazure infrastructure not yet available
- Δ_λ gate held throughout

By Path C derivation, **the same acceptance applies to m_n and Δ_pn**:

- Their L2 100× miss is **not an independent gap** — it is a propagated
  manifestation of the Q_β residue-A gap
- Closing m_n or Δ_pn requires closing Q_β; no independent attack
  surface exists for them
- Until Q_β residue A is identified (research-grade), m_n and Δ_pn
  remain functionally cal-anchored

## What this means for production

1. **Production wiring unchanged.** m_n + Δ_pn are still computed via
   Path C in
   [`per-observable-100x-status.witness.json`](../../computations/per-observable-100x-status.witness.json).
   No fitted form is wired; the 185.4× / 163.3× miss factors remain
   the honest production values.

2. **L2 dashboard headline unchanged.** All three (Q_β + m_n + Δ_pn)
   continue to display their miss factors. This is not a wire decision.

3. **The "3 failing observables" framing is structurally misleading.**
   It conflates one root cause (Q_β residue A) with three observed
   symptoms (Q_β + m_n + Δ_pn). After this acceptance, the framing
   should be "1 categorical gap + 2 propagated derivatives".

4. **L2 met count: still 3/7.** No formal status change — the metric
   stays honest. But the active-attack-surface count drops from "3
   failing" to "1 categorical gap" (since attacking m_n or Δ_pn
   independently is moot until Q_β closes).

## What this is NOT

- **Not** a wire decision. No production code changes.
- **Not** a claim m_n or Δ_pn can never improve. They will improve
  automatically when Q_β residue A is closed via upstream infrastructure.
- **Not** ignoring m_n / Δ_pn. They remain on the L2 dashboard with
  their honest miss factors; this just clarifies the dependency chain.

## Cross-refs

- [Q_β residue-A acceptance (PR #1770)](2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md)
- [KLR/crystal infra scope (PR #1770)](../scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md)
- [Shared-root audit 2026-05-30](2026-05-30-l2-100x-status-3-failing-shared-root.md)
- [CAL-3=m_π corroboration 2026-05-31](2026-05-31-l2-3-failing-shared-root-with-cal-3-m-pi.md)
- [1ppQ Q_β master ledger](../coordination/1ppq-qbeta.md)
- CLAUDE.md §"Precision goals" — L2 status table

## Open question — m_μ remains independent

m_μ at 963.6× is the ONLY L2-failing observable with an independent
attack surface (it's not propagated from Q_β). Its current bare-
categorical wiring uses `Vol(4_1)/ℏ_q²` (Kashaev volume of figure-8
knot), which depends on q₀ but not on Q_β. m_μ closure requires its
own categorical attack — see companion probe in this PR for the first
exploratory results.
