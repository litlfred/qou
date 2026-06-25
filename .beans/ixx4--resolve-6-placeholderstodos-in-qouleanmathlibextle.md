---
# ixx4
title: Resolve 6 placeholders/TODOs in qou/lean/MathlibExt.lean
status: todo
type: task
created_at: 2026-06-22T02:25:51Z
updated_at: 2026-06-25T17:05:00Z
---


resweep 2026-06-23 (#2637): honest actionable ~0 drainable (claimed 6) — all six are intentional '-- TODO upstream:' Mathlib-port markers, not cosmetic cruft. See docs/audits/2026-06-23-placeholder-bean-resweep.md.

resweep 2026-06-24 (honest counter, PR hygiene): **uncited-sorry = 0 corpus-wide**; this title count is a raw grep and is badly inflated. Honest actionable count for this scope + the full per-bean table in docs/audits/2026-06-24-placeholder-bean-count-resweep.md. Remaining TODO/FIXME are intentional markers (-- TODO upstream: on proved lemmas, witness-deps, research notes), NOT actionable placeholders — do not "drain a count" by removing them. Re-title/close is owner-only.

resweep 2026-06-25 (count-actionable-placeholders.ts, #2796 session): 0 uncited / missing-proof sorries — every `sorry` in scope is §3b-cited (intentional conjecture) or `-- Ref:`-cited. Honest actionable = 6 `-- TODO upstream:` annotations (claimed 6) on ALREADY-PROVED MathlibExt lemmas — these mark 'could be contributed to Mathlib', not missing proofs. Not mechanical drainage; recommend close or re-scope to 'upstream to Mathlib'.
