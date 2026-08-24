---
# qou-a9fj
title: Integrate 406 commits of main drift into claude/mass-table-comprehensive-triage
status: todo
type: task
created_at: 2026-08-24T06:46:10Z
updated_at: 2026-08-24T06:46:10Z
---

Branch is 47 ahead / 406 behind origin/main (merge-base e556f8f38).

`git merge-tree` dry run: 16 conflicts.
- 14 generated witness JSON  -> resolve by RE-RUNNING the producer, never by hand-merging
  (a hand-merged witness carries a scriptHash matching neither parent)
- 1 modify/delete: computations/habiro/habiro-coefficients-extended.witness.json
  deleted on main, modified here -- must establish WHY main deleted it
- 1 real source file: computations/substrate/witness_constant_staleness.py

Also queued behind this merge: scripts/sync-qou-mass-vendor.py --apply
(run AFTER the merge so the vendored copies generate from post-merge sources).
