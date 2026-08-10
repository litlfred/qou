---
# qou-py7e
title: 'GAP: lake-cache/qou-v4-24-0-new olean set is incomplete (missing Mathlib.Algebra.Module.LinearMap.Polynomial)'
status: todo
type: task
created_at: 2026-08-10T15:19:39Z
updated_at: 2026-08-10T15:19:39Z
---


Found while re-verifying PR #4913 (2026-08-10, branch
`claude/stalled-prs-wrap-up-uja5th`).

`content/.../QOU/MathlibExt/EndBaseChange.lean` imports
`Mathlib.Algebra.Module.LinearMap.Polynomial` directly. That olean is **absent**
from the restored set, so `lean`-direct fails with

    error: object file '.../Mathlib/Algebra/Module/LinearMap/Polynomial.olean'
    of module Mathlib.Algebra.Module.LinearMap.Polynomial does not exist

which is a **cache gap, not a defect in the file**. Confirmed the import is not
gratuitous: deleting it leaves `Algebra.TensorProduct.basis` and
`LinearMap.toMatrix_baseChange` unknown and the proof with unsolved goals.

Mathlib *sources* are not in the cache either (`.lake/packages/mathlib/Mathlib/`
does not exist), so the missing module cannot be rebuilt locally — restoring the
cache does not make you able to fill its own holes.

Consequences for other agents:

- Read `does not exist` on a **Mathlib** module as a cache gap. Do not report
  the file under test as failing to compile.
- The H4 cone is missing from this same cache branch (see `qou-x64l`), so this
  is not an isolated hole.

Next step: re-seed the cache branch from a build that includes the missing
modules, or record the covered module set alongside the tarball so a restoring
agent can tell up front what is not in it.
