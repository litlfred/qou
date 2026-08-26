---
# qou-5v24
title: 'lean-direct-cone.sh and lean-axiom-guard.py disagree on freshness: verify-then-commit deadlocks the documented compose'
status: todo
type: task
priority: normal
created_at: 2026-08-26T07:08:18Z
updated_at: 2026-08-26T07:20:14Z
---

Reproduced 2026-08-26 while merging PR #5820.

The two tools use DIFFERENT CLOCKS for 'is this olean current':
  * scripts/lean_cone_build.py  -- olean mtime vs source MTIME
  * scripts/lean-axiom-guard.py -- olean mtime vs _effective_source_time, which
    for a CLEAN file is the COMMIT TIME of the last commit touching it.

Measured instance (QOU.HeckeAlgebra.MarkovTrace):
  source mtime  06:45:09
  olean mtime   06:45:12   -> rebuilder: up-to-date, SKIP
  commit time   06:47:15   -> guard: STALE, refuse (rc=2)

So the compose documented in the guard's own docstring,
  bash scripts/lean-direct-cone.sh $(python3 scripts/lean-axiom-guard.py --print-modules)
  python3 scripts/lean-axiom-guard.py
DEADLOCKS: the rebuilder will not rebuild and the guard will not report. Neither
is wrong on its own terms.

Trigger is the NATURAL workflow order: verify, then commit. Building before
committing always leaves commit time > olean mtime. It does not reproduce if you
commit first and build after.

Workaround used: delete the one olean, then rerun lean-direct-cone.sh. 4s.

Candidate fixes, not yet chosen:
  * give lean_cone_build.py a --force/-B flag (smallest);
  * have the guard treat a clean file whose CONTENT is unchanged since the olean
    as fresh -- i.e. compare content, not times. Note the guard's
    _effective_source_time docstring explains carefully why raw mtime is wrong
    (clone stamps everything), so the commit-time rule is deliberate; the corner
    is specifically clean-file-committed-after-build.
  * make the rebuilder use the guard's _effective_source_time so the two agree.

Hit a THIRD time, 2026-08-26, same session. Raising priority: this is not a one-off, it fires whenever the natural verify-then-commit order is used, which is every time.
