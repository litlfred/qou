---
# qou-5v24
title: 'lean-direct-cone.sh and lean-axiom-guard.py disagree on freshness: verify-then-commit deadlocks the documented compose'
status: todo
type: task
priority: normal
created_at: 2026-08-26T07:08:18Z
updated_at: 2026-08-26T07:26:16Z
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

MITIGATED 2026-08-26 (rides on PR #5822). Not yet fully fixed -- the two notions are still different, this just makes the documented path terminate.

  * scripts/lean_cone_build.py gains -B/--force, which makes fresh() always return
    False. Its docstring now states the mtime-vs-commit-time divergence and the
    exact reproduction.
  * scripts/lean-axiom-guard.py's failure message now EMITS the working command:
      scripts/lean-direct-cone.sh --force <the stale modules>
    and explains why --force is needed. Following the old message literally is
    what looped.

Demonstrated end to end on a live instance (QOU.Machinery.MarkovCosetLift, built
then committed):
  without --force:  'done: up-to-date=2 in 0s' -> guard still rc=2   (deadlock)
  with    --force:  'done: ok=2 in 4s'         -> guard rc=0         (resolved)

STILL OPEN: unifying the freshness notion so --force is unnecessary. The candidates
in the original note stand; the guard's commit-time rule is deliberate (a fresh
clone stamps every source with checkout time, so raw mtime would flag everything),
so the fix is probably to teach the REBUILDER the same rule rather than to weaken
the guard.
