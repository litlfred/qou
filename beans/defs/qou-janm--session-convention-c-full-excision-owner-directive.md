---
# qou-janm
title: 'Session: convention-C full excision (owner directive 2026-08-29)'
status: in-progress
type: milestone
priority: normal
created_at: 2026-08-29T07:36:26Z
updated_at: 2026-09-08T07:45:33Z
---

PR #5972, branch claude/convention-c-full-excision-2026-08-29. NOT merged; readiness reported.

DONE
- scripts/convention-c-value-audit.py — value-based detector (evaluates, does not
  shape-match). 90 confirmed C bindings in computations/, 21 of them reported in
  NO bucket by the shape audit. Taxonomy row 16.
- 5 sites migrated with per-field deltas (crossing signature 0.227044 confirmed
  on 3 of them).
- 5 sites registered blocked_on_rederivation with measurements; validator PASS.
- 3 content/ sites: 1 migrated, 2 annotated.
- AGENTS.md: all six convention-C figures re-measured and corrected.
- Beans qou-t9r1 / qou-pmkh / qou-961o / qou-uc1n carry what remains.

NOT DONE, deliberately
- 8 unannounced C sites in computations/ (qou-t9r1) — each needs its own
  baseline-from-git, re-run and field report; two of them (markov_trace_weights_wenzl,
  lw2_c2) may be C-PREMISED rather than merely C-spelled and must be checked
  before swapping.
- The markovZ rename (qou-961o) — 3 file-local renames, each needing lean-direct
  verification at ~1m43s per file.
- qa-sweep / pipeline render on the 3 content blocks — folio-assistant/ not cloned,
  disk at 5.3G. Stated in the commit rather than skipped silently.

## 2026-09-08: canonical ledger for the convention-C excision family is qou-wgta (the P0 excision tracker; owner-ruling milestone qou-cdx1, S2 science blocker qou-cds2); see docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 2 / §7.3 C3. Nine trackers, previously linked only cds2↔8iru and htsi→t9r1, now all point there.
