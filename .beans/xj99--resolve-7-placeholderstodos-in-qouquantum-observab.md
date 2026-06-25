---
# xj99
title: Resolve 7 placeholders/TODOs in qou/quantum-observable-universes
status: todo
type: task
priority: normal
created_at: 2026-06-22T02:25:52Z
updated_at: 2026-06-25T17:05:00Z
---

Audit (amazing-mendel): claimed 7 -> honest counter 4 -> 1 after fixes. Resolved 2 stale 'TODO bib lookup' notes in pawlowski-leitner-inner-product.lean (key pawlowski-leitner-rep DOES resolve in references.ts; residual = title verification, bib-human-review owner-gated, references.ts:1442). Gated remainder NOT drained: q-resolvent.lean (documented True:=trivial pending q-shuffle Hopf infra, cited kassel1995); fiber-adjoint-involution.lean (vacuous ∃,True:=sorry) -> vacuity-audit axis. Left open.

resweep 2026-06-22: honest counter = 1 actionable (claimed 7) via scripts/count-actionable-placeholders.ts.

resweep 2026-06-23 (#2637): honest actionable = 1 (claimed 7): q-resolvent (1 sorry). See docs/audits/2026-06-23-placeholder-bean-resweep.md.

drain 2026-06-23 (#2654): actionable 1 -> 0 — de-vacuified QResolvent.first_identity (was `def : True := trivial`, a §1a dodge) into the real element-level first-resolvent identity + cited sorry. quantum-observable-universes fully drained.

resweep 2026-06-24 (honest counter, PR hygiene): **uncited-sorry = 0 corpus-wide**; this title count is a raw grep and is badly inflated. Honest actionable count for this scope + the full per-bean table in docs/audits/2026-06-24-placeholder-bean-count-resweep.md. Remaining TODO/FIXME are intentional markers (-- TODO upstream: on proved lemmas, witness-deps, research notes), NOT actionable placeholders — do not "drain a count" by removing them. Re-title/close is owner-only.

resweep 2026-06-25 (count-actionable-placeholders.ts, #2796 session): 0 uncited / missing-proof sorries — every `sorry` in scope is §3b-cited (intentional conjecture) or `-- Ref:`-cited. Honest actionable = 0 (claimed 7) in quantum-observable-universes. FULLY DRAINED — recommend close.
