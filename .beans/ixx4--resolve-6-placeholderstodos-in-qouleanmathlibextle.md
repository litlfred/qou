---
# ixx4
title: 'CLOSED (misclassified): MathlibExt.lean — 0 actionable; 6 `-- TODO upstream:` markers on proved lemmas'
status: completed
type: task
priority: normal
created_at: 2026-06-22T02:25:51Z
updated_at: 2026-06-26T15:30:00Z
---


resweep 2026-06-23 (#2637): honest actionable ~0 drainable (claimed 6) — all six are intentional '-- TODO upstream:' Mathlib-port markers, not cosmetic cruft. See docs/audits/2026-06-23-placeholder-bean-resweep.md.

resweep 2026-06-24 (honest counter, PR hygiene): **uncited-sorry = 0 corpus-wide**; this title count is a raw grep and is badly inflated. Honest actionable count for this scope + the full per-bean table in docs/audits/2026-06-24-placeholder-bean-count-resweep.md. Remaining TODO/FIXME are intentional markers (-- TODO upstream: on proved lemmas, witness-deps, research notes), NOT actionable placeholders — do not "drain a count" by removing them. Re-title/close is owner-only.

resweep 2026-06-25 (count-actionable-placeholders.ts, #2796 session): 0 uncited / missing-proof sorries — every `sorry` in scope is §3b-cited (intentional conjecture) or `-- Ref:`-cited. Honest actionable = 6 `-- TODO upstream:` annotations (claimed 6) on ALREADY-PROVED MathlibExt lemmas — these mark 'could be contributed to Mathlib', not missing proofs. Not mechanical drainage; recommend close or re-scope to 'upstream to Mathlib'.



[2026-06-26 MISCLASSIFIED] MathlibExt.lean has 0 sorry; the 6 'TODOs' are '-- TODO upstream:' markers on PROVED sorry-free lemmas (Mathlib-upstreaming candidates, not in-repo placeholders). Recommend CLOSE or re-scope as upstream-contribution tracking. Audit: docs/audits/2026-06-26-lean-placeholder-bean-grep-inflation.md

[2026-06-26 CLOSED — owner-authorized, rsseq-even-part session] 0 actionable confirmed (4 consecutive resweeps + lean-direct vs lake-cache/qou-v4-24-0). The 6 markers are Mathlib-upstreaming candidates on already-proved sorry-free lemmas, not in-repo work. If upstreaming is desired, open a fresh `upstream-to-mathlib` bean rather than reopening this grep-inflated placeholder count.
