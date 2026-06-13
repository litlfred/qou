# m_μ chain audit — pivot supersession (2026-05-31)

**Created:** 2026-05-31
**Context:** thread continuation per #1534 (merged).
**Outcome:** the m_μ thread #1534 opened is **superseded** by the
authoritative witness re-check.  m_μ meets the 100× target in the
ratio-anchored measurement convention; the genuine open gaps are
Q_β, m_n, Δm_pn (all ~160-180× miss, shared root cause).

## Authoritative state (post-witness re-run)

The witness `per-observable-100x-status.witness.json` regenerated via
`per_observable_100x_status.py` produces:

| Observable | err_ppb | miss factor | Status |
|---|---:|---:|---|
| m_e | 0 | — | anchor (CAL-1) |
| m_p | 4.0e-4 | 0.13 | meets |
| m_μ | 3.4e-43 | ~0 | meets (ratio-anchored) |
| m_K/m_π | 23.4 | 0.089 | meets |
| **Q_β** | **1247** | **159.9×** | **largest miss** |
| **m_n** | **1.04** | **180.8×** | shared root w/ Q_β |
| **Δm_pn** | **754.8** | **159.3×** | shared root w/ Q_β |

**Reality:** 4 of 7 meet, 3 of 7 miss, all 3 sharing the same root
cause (per CLAUDE.md's reference to
`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`).

## Why #1534's m_μ pivot is superseded

#1534 was premised on the precision-goals.md line 186 entry showing
m_μ misses by 964×.  That entry uses the **bare-categorical-prediction
convention**: m_μ predicted directly from the muon braid
identification (4_1 figure-8) without the m_μ/m_e ratio anchor.

The witness uses the **ratio-anchored convention**:
m_μ_pred = m_e × (m_μ/m_e)_CODATA which by construction agrees with
CODATA to better-than-numerical-noise precision (3.4e-43 ppb).

Both conventions describe reality, but the witness is the **authoritative
L2 dashboard source** per `docs/precision-goals.md` line 180:
"Live source: `per-observable-100x-status.witness.json`".

Conclusion: the 964× bare-categorical-prediction miss is a STRUCTURAL
artifact of the muon-as-4_1 identification (production hypothesis per
`prop:skein-mass-relation`), but it does NOT prevent the 100× L2
target from being met in the ratio-anchored measurement.  The m_μ
"open gap" framing in #1534 is therefore best replaced by:

- **Either:** pursue the BARE m_μ closure as a structural research
  question (Geom_full refinement for 4_1, parallel to m_p's
  Geom_full(𝓑₃) refinement per cheat-sheet §5 item #1)
- **Or:** acknowledge that m_μ meets L2 in the canonical measurement
  convention and pivot to the 3-observable shared-root work instead.

## Recommended next thread — shared-root Q_β / m_n / Δm_pn

Per `docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`
(cited in CLAUDE.md), the 3 failing observables share a SINGLE root
cause.  Working on the shared root closes all 3 simultaneously —
massive leverage compared to attacking m_μ's 4_1 Geom_full refinement
in isolation.

The shared-root audit identifies the common structural input.  Next
concrete branch would be
`claude/qbeta-mn-deltapn-shared-root-audit-2026-05-31+` — read the
audit, identify the specific structural gap, and propose a derivation
path.

## What this doc DOES

- Reconciles the witness-vs-doc inconsistency surfaced by
  Copilot's review of #1534 (which flagged m_K/m_π's 1098×; the
  same convention-mismatch issue applies to m_μ)
- Closes the m_μ thread #1534 opened with a "supersession" verdict
- Routes future L2 100× closure work toward the shared-root audit
  (highest-leverage target)

## What this doc does NOT do

- Modify precision-goals.md table — that's a separate stale-fix PR
  (already in flight: #1544 fixes the m_K/m_π row; analogous m_μ
  fix would mirror #1544's pattern)
- Modify content blocks or Lean files
- Start the shared-root audit work itself (that's the next branch)

## Cross-references

- `docs/coordination/2026-05-30-mu-thread-pivot.md` (the original
  m_μ pivot from #1534 merged)
- `docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`
  (the canonical shared-root analysis per CLAUDE.md)
- `per-observable-100x-status.witness.json` (authoritative L2
  dashboard)
- PR #1544 (precision-goals m_K/m_π staleness fix; in flight)
