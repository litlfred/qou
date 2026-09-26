---
# i6p9
title: 'CLOSED (misclassified, duplicate-of-subbeans): qou/lean whole-tree — 0 distinct actionable'
status: completed
type: task
priority: normal
created_at: 2026-06-22T02:25:51Z
updated_at: 2026-06-26T15:30:00Z
---


resweep 2026-06-24 (honest counter, PR hygiene): **uncited-sorry = 0 corpus-wide**; this title count is a raw grep and is badly inflated. Honest actionable count for this scope + the full per-bean table in docs/audits/2026-06-24-placeholder-bean-count-resweep.md. Remaining TODO/FIXME are intentional markers (-- TODO upstream: on proved lemmas, witness-deps, research notes), NOT actionable placeholders — do not "drain a count" by removing them. Re-title/close is owner-only.

resweep 2026-06-25 (count-actionable-placeholders.ts, #2796 session): 0 uncited / missing-proof sorries — every `sorry` in scope is §3b-cited (intentional conjecture) or `-- Ref:`-cited. Honest actionable = 16 TODO/FIXME markers, 0 sorries, across the WHOLE QOU lean tree (content/.../lean/QOU) — overlaps sub-beans 95jh/b3pe/ixx4; markers are `-- TODO upstream:` / audit notes, not missing proofs.



[2026-06-26 grep-inflated] qou/lean whole-tree naive 757 → refined ~157 actionable (loose upper bound; excludes sorry-free; still over-counts §3b + comment-prose). Re-scope. Audit: docs/audits/2026-06-26-lean-placeholder-bean-grep-inflation.md

[2026-06-26 CLOSED — owner-authorized, rsseq-even-part session] This is a whole-tree grep that DUPLICATES the per-dir sub-beans (95jh/b3pe/ekb8/ixx4). The "10" are §3b comment-prose (`-- The Lean encoding below is a 'theorem … := by sorry' placeholder`), not real sorries — 0 distinct actionable. Closing as duplicate; track any real residual via the per-dir beans (95jh/b3pe), which are themselves re-scoped to §3b-excluded counts.
