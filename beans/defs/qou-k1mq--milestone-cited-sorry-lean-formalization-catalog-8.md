---
# qou-k1mq
title: 'MILESTONE: Cited-sorry Lean formalization catalog (80 sorries / 69 files)'
status: completed
type: milestone
priority: normal
tags:
    - lean
    - cited-sorry
    - catalog
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:00Z
updated_at: 2026-10-04T15:15:12Z
---

Catalog of every real (cited) `sorry` in the Lean corpus (`content/**/lean/`, `tools/**`), with a per-sorry plan to prove it in Lean + a literature link.

**80 real cited sorries across 69 files.** 0 uncited (no review failures). 0 unresolved citation keys (all 14 external keys resolve in `content/schema/references.ts`; `[manuscript]` is the internal chapter/section convention).

Tractability: **4 tractable-in-Mathlib-today (T)**, **43 repo-infra-dependent (P)**, **33 infra-blocked / open-conjecture (B)**.

Durable index: `docs/coordination/cited-sorry-formalization-catalog.md`.

NOTE: distinct from the sibling `citation-conjecture-lean-formalization` set (instance-LESS conjecture classes, no sorry). The 20 §3b conjecture-INSTANCE sorries here (`instance : Conj := sorry`) partially overlap that theme but carry an actual sorry + `-- Ref:`.

CATALOGUING task only — no sorry was proved, removed, or modified.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] catalog said 80 real sorries/69 files (2026-08-01); main 2026-10-03 has 15 real sorry terms in 6 files (3 in content siblings, 1 Fred2005, 2 in scratch/computations). Children re-sorted: sorry gon
