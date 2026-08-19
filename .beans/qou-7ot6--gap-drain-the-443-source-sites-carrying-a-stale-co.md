---
# qou-7ot6
title: 'GAP: drain the 443 source sites carrying a stale CODATA edition'
status: todo
type: task
created_at: 2026-08-19T13:05:24Z
updated_at: 2026-08-19T13:05:24Z
---


## Context

Found by [`codata_corpus_literal_scan.py`](../computations/codata_corpus_literal_scan.py)
(PR #5302). The full site list is in
`computations/codata-corpus-vintage-scan.witness.json`; the analysis is
[`docs/audits/2026-08-19-codata-edition-straddle-corpus-sweep.md`](../docs/audits/2026-08-19-codata-edition-straddle-corpus-sweep.md).

**443 SOURCE sites** (`.py`/`.lean`/`.ts`) hand-type a CODATA constant from an
earlier adjustment — full-length, not truncated, so `codata_truncation_audit`
cannot see them. Each is 3–4.5 σ from the committed 2022 table.

## What the drain is

Not a find-and-replace. For each site:

1. Replace the literal with an import from the canonical registry
   (`codata_2022_source` / `codata_constants`), which is already correct.
2. **Re-run the producer** and regenerate its witness.
3. Report which numbers moved.

## What it is NOT

- **Never edit a committed witness to match the table.** A witness records
  what a producer actually computed. `RECORD` sites (1526) are history; the
  fix is at the producer.
- Not an idle-pass sweep. Re-running 443 producers is a large announced
  tranche with its own scope.

## Two outliers to triage separately

- `3727.379378` (m_α, 18 sites) — 9.068 ppb, **28.2 σ**. Two editions back.
- `137.035944` (1/α, 18 sites) — 402.6 ppb, **2630 σ**. Not any CODATA
  edition; something else is happening at those sites.

## Scope

(a), scope-limited. No physical conclusion moves — offsets are ~1.3–1.5 ppb,
an order of magnitude under the μ–p tension. The value is that the corpus
stops disagreeing with itself.
