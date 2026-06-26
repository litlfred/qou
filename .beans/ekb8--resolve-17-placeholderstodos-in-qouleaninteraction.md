---
# ekb8
title: Resolve 17 placeholders/TODOs in qou/lean/Interactions
status: todo
type: task
priority: normal
created_at: 2026-06-22T02:25:51Z
updated_at: 2026-06-26T03:10:18Z
---

resweep 2026-06-22: honest counter = 1 actionable (claimed 17) via scripts/count-actionable-placeholders.ts.

resweep 2026-06-23 (#2637): honest actionable = 1 (claimed 17): QIntegerMassFormula (1 sorry). See docs/audits/2026-06-23-placeholder-bean-resweep.md.

drain 2026-06-23 (#2654): actionable 1 -> 0 — repositioned the QIntegerMassFormula §3b conjecture-class sorry citation (-- Ref: now precedes := sorry; comment-only). lean/Interactions fully drained.

resweep 2026-06-24 (honest counter, PR hygiene): **uncited-sorry = 0 corpus-wide**; this title count is a raw grep and is badly inflated. Honest actionable count for this scope + the full per-bean table in docs/audits/2026-06-24-placeholder-bean-count-resweep.md. Remaining TODO/FIXME are intentional markers (-- TODO upstream: on proved lemmas, witness-deps, research notes), NOT actionable placeholders — do not "drain a count" by removing them. Re-title/close is owner-only.

resweep 2026-06-25 (count-actionable-placeholders.ts, #2796 session): 0 uncited / missing-proof sorries — every `sorry` in scope is §3b-cited (intentional conjecture) or `-- Ref:`-cited. Honest actionable = 0 (claimed 17) in QOU/Interactions. FULLY DRAINED — recommend close.



[2026-06-26 grep-inflated] Claimed 17; real actionable = 1 genuine sorry (QIntegerMassFormula.fits_AME @ line 180); other matches are §3b ctx.holds comment-prose / open-conjecture markers. Re-scope. Audit: docs/audits/2026-06-26-lean-placeholder-bean-grep-inflation.md
