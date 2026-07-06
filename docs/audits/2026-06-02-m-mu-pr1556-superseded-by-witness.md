## m_μ disposition: PR #1556 is superseded by the live witness

**Date:** 2026-06-02
**Branch:** `claude/m-mu-supersession-audit-2026-06-02`
**Scope:** L2 100× dashboard, m_μ row convention dispute
**Verdict:** PR #1556's premise is inverted by today's witness; recommend close.

### Background

PR [#1556](https://github.com/litlfred/qou/pull/1556) (opened 2026-05-31) argues:

1. `precision-goals.md` line 186 was stale, using a *bare-categorical*
   convention to report m_μ at 964× miss.
2. The "authoritative witness"
   (`per-observable-100x-status.witness.json`) uses a *ratio-anchored*
   convention (`m_μ_pred = m_e × (m_μ/m_e)_CODATA`) which gives
   `err_ppb ≈ 3.4e-43` — i.e. m_μ meets L2.
3. Future closure work should pivot to the shared-root Q_β / m_n /
   Δm_pn trio rather than m_μ in isolation.

### Current witness state (commit `653abf11` — refreshed today)

| field | value |
|---|---|
| `obs` | `m_mu` |
| `pred_MeV` | 105.658397811 |
| `codata_MeV` | 105.658375649 |
| `err_ppb` | 209.8 |
| `target_100x_ppb` | 0.2177 |
| `miss_factor` | 963.6 |
| `beats_100x_experimental` | **false** |

The witness's own `sigma_source` field carries an **explicit anti-#1556
note**:

> "The PREDICTION (`pred_MeV`) is the INDEPENDENT categorical value
> `m_μ = m_e · Vol(4_1) / ℏ_q²` from the Borromean witness — post the
> 2026-05-29 q₀ re-pin it is a genuine 9.5σ PREDICTION, NOT
> ratio-derived. The ~210 ppb pred-vs-codata gap (963.6× the 100×
> target) is the real μ-p tension; m_μ does NOT meet L2.
> Do not read 'ratio-derived' as 'm_μ trivially meets'
> (the error PR #1556 made)."

I.e. the witness has been deliberately updated since PR #1556 was
opened to (a) clarify that `pred_MeV` is the bare-categorical Borromean
prediction not the ratio-derived value, and (b) cite #1556 by number
as the prior misread.

### Reconciliation with `precision-goals.md`

[`docs/precision-goals.md` line 186](https://github.com/litlfred/qou/blob/claude/m-mu-supersession-audit-2026-06-02/docs/precision-goals.md#L186)
matches the witness exactly:

```
| m_μ | prediction | 21.8 ppb | **0.22 ppb** | 210 ppb | **misses ~964×** (9.5σ μ-p tension) |
```

`precision-goals.md` and the witness are in convention agreement on
the bare-categorical Borromean prediction; both say `misses ~964×`.

### Reconciliation with `AGENTS.md` STATUS block

[`AGENTS.md`](https://github.com/litlfred/qou/blob/claude/m-mu-supersession-audit-2026-06-02/AGENTS.md)
§Precision goals also matches:

> 3/7 met (m_p, m_e, m_K/m_π) — … the 4 missing observables (m_μ, Q_β,
> m_n, Δ_pn) … note **m_μ misses by 963.6× post-re-pin** …

All three sources — witness, precision-goals.md, AGENTS.md — agree:
m_μ is at 209.8 ppb / 963.6× miss, and does NOT meet L2.

### What about the shared-root pivot recommendation?

PR #1556's secondary recommendation — "future closure work should
pivot to the shared-root Q_β / m_n / Δm_pn trio rather than m_μ in
isolation" — was independently absorbed:

- [`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`](https://github.com/litlfred/qou/blob/claude/m-mu-supersession-audit-2026-06-02/docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md)
  is the canonical shared-root analysis.
- AGENTS.md cites it directly: "the Q_β/m_n/Δ_pn trio share a single
  root cause".
- The Q_β arm has a live keystone probe at
  [PR #1713](https://github.com/litlfred/qou/pull/1713) (Q_β Habiro
  element categorical ID, opened 2026-06-02).

m_μ is a separate L2 miss (independent μ-p VolDensity tension, not the
Q_β chain). The shared-root pivot does NOT replace m_μ — it runs
alongside.

### Verdict

PR #1556's main claim (m_μ meets L2 in the ratio-anchored convention,
witness convention is ratio-anchored) is **inverted by the live
witness**: the witness explicitly uses the bare-categorical
convention and names #1556 as a misread.

PR #1556's secondary recommendation (shared-root pivot for Q_β / m_n /
Δm_pn) is **already adopted** via the cited shared-root audit and the
live Q_β Habiro probe at PR #1713.

**Recommendation: owner closes PR #1556 as superseded.** No code or
content changes are required as part of the closure; this audit doc
captures the supersession verdict for posterity.

### Cross-refs

- Witness: [`computations/per-observable-100x-status.witness.json`](https://github.com/litlfred/qou/blob/claude/m-mu-supersession-audit-2026-06-02/computations/per-observable-100x-status.witness.json)
- Precision goals: [`docs/precision-goals.md`](https://github.com/litlfred/qou/blob/claude/m-mu-supersession-audit-2026-06-02/docs/precision-goals.md)
- AGENTS.md §Precision goals: [`AGENTS.md`](https://github.com/litlfred/qou/blob/claude/m-mu-supersession-audit-2026-06-02/AGENTS.md)
- Shared-root audit: [`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`](https://github.com/litlfred/qou/blob/claude/m-mu-supersession-audit-2026-06-02/docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md)
- Q_β re-pin staleness audit: [`docs/audits/2026-05-30-q0-repin-stale-witness-audit.md`](https://github.com/litlfred/qou/blob/claude/m-mu-supersession-audit-2026-06-02/docs/audits/2026-05-30-q0-repin-stale-witness-audit.md)
- Original m_μ pivot coord: [`docs/coordination/2026-05-30-mu-thread-pivot.md`](https://github.com/litlfred/qou/blob/claude/m-mu-supersession-audit-2026-06-02/docs/coordination/2026-05-30-mu-thread-pivot.md)
- Q_β Habiro keystone probe: PR [#1713](https://github.com/litlfred/qou/pull/1713)
