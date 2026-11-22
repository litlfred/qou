---
# qou-xksw
title: SchurWeylMassDecomposition is inhabited by an empty instance
status: completed
type: task
priority: normal
tags:
    - lean
created_at: 2026-11-22T09:20:32Z
updated_at: 2026-11-22T21:17:12Z
parent: qou-uwyf
---

mass-theory/schur-weyl-mass-decomposition.lean: emptyDecomposition (partitions := [], markovTrace := 0) satisfies the class, so the class asserts nothing about the partitions of 3A. Add a completeness field (partitions enumerate Nat.Partition (3A)) or demote. The file's own comment already flags this as a structure refactor.

Record: docs/audits/2026-11-22-lean-audit-snapshot-gaps.md (§3). Epic qou-uwyf.


2026-11-22 (branch claude/honest-lean-descent-reidemeister-schurweyl-2026-11-22, commit 7441c63f7): class now sums over Finset.univ of Nat.Partition (3*A), with trace/weight/character as parameters (placeholder spechtCharacter = 0 would force trace 0, proved). card_partitions_three and exists_partition_with_long_row restate the two deleted axioms correctly. Decomposition itself for the Ocneanu trace is not proved (no Specht characters in Lean).

## 2026-11-22 — wave-2 drain (lean-devacuify), closed on main evidence
Session https://claude.ai/code/session_01Qmmkt5vgAD2YAm4VcqJgrF, main 3c4c98fcc.
Done on main: PR #8999 merged 2026-11-22T10:58Z. `mass-theory/schur-weyl-mass-decomposition.lean:76` `class SchurWeylMassDecomposition` now sums over `Finset.univ : Finset (Nat.Partition (3*A))`, so the empty instance no longer satisfies it (line 60 docstring). The decomposition for the Ocneanu trace itself is unproved (no Specht characters in Lean); that is M4 work (`qou-ltwg`), not this bean.
