---
# qou-dg48
title: 'GAP: full from-source QOU build has never been run in CI — levels 3-16 unexamined'
status: todo
type: task
created_at: 2026-08-08T09:07:47Z
updated_at: 2026-08-08T09:07:47Z
---


## Finding

Nothing in CI ever builds the QOU Lean library from source. `build.yml` is
`workflow_dispatch`-only (Actions billing, owner directive 2026-06-30) and
there is no `lean_ci.yml` in the tree, so feature branches routinely show zero
check runs. The `lake-cache/qou-*` olean payload is a **snapshot** (seeded
2026-07-02), not a build — restoring it proves nothing about current source.

The consequence, measured: a full from-source build launched 2026-08-08 found
**88 failing modules by level 2 of 17** (1280/1606 modules built). These are
not new regressions; they are accumulated breakage that no gate was watching.
PR #4722 drained roughly 50 of them.

## What is still unexamined

Levels 3–16 of the topological build were never reached in that run. The true
red-file count for the library is **not yet known** and is > 88.

## Next honest step

Finish a full from-source build and publish the red list, then decide whether
to (a) restore a cheap CI gate that builds changed modules' cones from source,
or (b) run this sweep periodically. Note the cache trap recorded in
`qou-gdc1`: a red-file diagnosis made against the restored olean cache is
unsound, because a stale dep throws `Invalid field` / `Function expected`
errors indistinguishable from real upstream drift.
