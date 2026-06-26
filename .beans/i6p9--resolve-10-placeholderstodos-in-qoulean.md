---
# i6p9
title: Resolve 10 placeholders/TODOs in qou/lean
status: todo
type: task
priority: normal
created_at: 2026-06-22T02:25:51Z
updated_at: 2026-06-26T03:10:18Z
---


resweep 2026-06-24 (honest counter, PR hygiene): **uncited-sorry = 0 corpus-wide**; this title count is a raw grep and is badly inflated. Honest actionable count for this scope + the full per-bean table in docs/audits/2026-06-24-placeholder-bean-count-resweep.md. Remaining TODO/FIXME are intentional markers (-- TODO upstream: on proved lemmas, witness-deps, research notes), NOT actionable placeholders — do not "drain a count" by removing them. Re-title/close is owner-only.

resweep 2026-06-25 (count-actionable-placeholders.ts, #2796 session): 0 uncited / missing-proof sorries — every `sorry` in scope is §3b-cited (intentional conjecture) or `-- Ref:`-cited. Honest actionable = 16 TODO/FIXME markers, 0 sorries, across the WHOLE QOU lean tree (content/.../lean/QOU) — overlaps sub-beans 95jh/b3pe/ixx4; markers are `-- TODO upstream:` / audit notes, not missing proofs.



[2026-06-26 grep-inflated] qou/lean whole-tree naive 757 → refined ~157 actionable (loose upper bound; excludes sorry-free; still over-counts §3b + comment-prose). Re-scope. Audit: docs/audits/2026-06-26-lean-placeholder-bean-grep-inflation.md
