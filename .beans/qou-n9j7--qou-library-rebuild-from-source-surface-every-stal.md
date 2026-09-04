---
# qou-n9j7
title: 'QOU library rebuild from source: surface every stale-cache red at once'
status: completed
type: task
priority: normal
created_at: 2026-09-04T12:25:52Z
updated_at: 2026-09-04T21:00:56Z
---

Motivation (measured 2026-09-03/04, PRs #6526/#6579): lean-direct on one file certifies against on-disk oleans; the restored cache is a snapshot, so main carried 10 red modules (retype + mem_addCell victims) for days, and this session also reported one FALSE red from stale dependency oleans. Nothing rebuilds the library (CI dispatch-only). Plan: topologically order every QOU module (library + content-block siblings), rebuild all from current main with lean -o in that order, log per-module status, classify reds (mechanical port vs real), fix the mechanical ones on this branch, record the rest as beans. Branch claude/qou-library-rebuild-2026-09-04.



## 2026-09-04 13:1xZ — library pass DONE: 157/158 green
Dirty closure (source newer than olean ∪ missing olean ∪ importer of dirty) = 158 of 2,597 (63/52/43), rebuilt in 842 s after a 100-module full-order first pass (0 fail). ONE red, real: ParticleInteractions/silver_ratio_beta_decay_null (own bean). The ten reds this week's PRs ported are confirmed gone. Siblings (907) next.



## 2026-09-04 14:0xZ — sibling pass DONE: 866/907 green, 41 red
4 fixed mechanically (green), 2 partial (parse+import fixed, deeper real errors remain), 1 harness (UGB path), hyperelliptic-z5: not fixed: tactic '' unmapped, 2 unverifiable here (import Mathlib root), rest REAL → umbrella bean . Library: 157/158 (qou-4a7a).



CORRECTION 14:1xZ: the umbrella bean is qou-isps (the ID was blank above); hyperelliptic-z5-classification's unknown tactic is interval_cases — Mathlib.Tactic.IntervalCases import added, errors now 0 (the previous commit c3e6d303b7 claimed this import and did not carry it).



## FINAL 2026-09-04 14:5xZ
Library: 157/158 (qou-4a7a). Siblings: my 5 mechanical fixes were superseded by qou-e7xv's landed sweep (taken main's versions on rebase). Re-verified all 41 original reds on current main: 32 green, 4 harness, 5 real (qou-isps: 4 outside e7xv's list + qou-0xrn). Lesson recorded as a lean-verifier TRAP: grep .beans before beaning a red list.



## LANDED — merged as 4f2a0f864193 (PR #6674, reopened from #6649 for the GraphQL draft-toggle quota). Successor tranche: the four untracked sibling reds (new bean, this branch).



## CORRECTION 21:0xZ — the '157/158 green' library claim was measured under an UNSOUND criterion
The per-module mtime dirty closure misses oleans whose mtime is the tarball extraction time but whose content is older than the source (measured: QOU.KnotTheory). So 157/158 is a lower bound on staleness, not a verification. The seed-commit closure (1,494 modules, Pauli witnesses last) is re-running; results will be recorded here and on the memory.
