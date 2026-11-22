---
# qou-xksw
title: SchurWeylMassDecomposition is inhabited by an empty instance
status: in-progress
type: task
priority: normal
tags:
    - lean
created_at: 2026-11-22T09:20:32Z
updated_at: 2026-11-22T09:51:31Z
parent: qou-uwyf
---

mass-theory/schur-weyl-mass-decomposition.lean: emptyDecomposition (partitions := [], markovTrace := 0) satisfies the class, so the class asserts nothing about the partitions of 3A. Add a completeness field (partitions enumerate Nat.Partition (3A)) or demote. The file's own comment already flags this as a structure refactor.

Record: docs/audits/2026-11-22-lean-audit-snapshot-gaps.md (§3). Epic qou-uwyf.


2026-11-22 (branch claude/honest-lean-descent-reidemeister-schurweyl-2026-11-22, commit 7441c63f7): class now sums over Finset.univ of Nat.Partition (3*A), with trace/weight/character as parameters (placeholder spechtCharacter = 0 would force trace 0, proved). card_partitions_three and exists_partition_with_long_row restate the two deleted axioms correctly. Decomposition itself for the Ocneanu trace is not proved (no Specht characters in Lean).
