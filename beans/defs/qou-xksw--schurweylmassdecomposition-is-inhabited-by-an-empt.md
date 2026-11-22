---
# qou-xksw
title: SchurWeylMassDecomposition is inhabited by an empty instance
status: todo
type: task
priority: normal
tags:
    - lean
created_at: 2026-11-22T09:20:32Z
updated_at: 2026-11-22T09:20:32Z
parent: qou-uwyf
---

mass-theory/schur-weyl-mass-decomposition.lean: emptyDecomposition (partitions := [], markovTrace := 0) satisfies the class, so the class asserts nothing about the partitions of 3A. Add a completeness field (partitions enumerate Nat.Partition (3A)) or demote. The file's own comment already flags this as a structure refactor.

Record: docs/audits/2026-11-22-lean-audit-snapshot-gaps.md (§3). Epic qou-uwyf.
